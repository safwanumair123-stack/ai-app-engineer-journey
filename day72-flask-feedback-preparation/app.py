# Day 71 — Prepare the Enquiry Tracker for deployment

import os

from flask import Flask, render_template, request, redirect, url_for, session, Response
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from datetime import datetime, date
import sqlite3
import csv
import io
import re

app = Flask(__name__)

app.secret_key = os.environ.get(
    "SECRET_KEY",
    "change-this-secret-key-before-deployment"
)

DATABASE_FILE = os.environ.get(
    "DATABASE_FILE",
    "enquiry_register.db"
)

APPROVED_ENQUIRY_TYPES = [
    "General enquiry",
    "Quotation",
    "Support",
    "Partnership"
]

APPROVED_PRIORITIES = [
    "Low",
    "Medium",
    "High"
]

APPROVED_SOURCES = [
    "Website",
    "Referral",
    "Social media",
    "Advertisement",
    "Other"
]

APPROVED_STATUSES = [
    "New",
    "In progress",
    "Closed"
]

CREATE_USERS_TABLE = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    role TEXT NOT NULL DEFAULT 'user',
    created_at TEXT NOT NULL
)
"""

CREATE_ENQUIRIES_TABLE = """
CREATE TABLE IF NOT EXISTS enquiries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    reference_number TEXT UNIQUE NOT NULL,
    user_id INTEGER NOT NULL,
    customer_name TEXT NOT NULL,
    customer_email TEXT NOT NULL,
    customer_phone TEXT NOT NULL,
    enquiry_type TEXT NOT NULL,
    priority TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'New',
    assigned_to TEXT NOT NULL,
    enquiry_source TEXT NOT NULL,
    estimated_value REAL NOT NULL DEFAULT 0,
    follow_up_date TEXT,
    enquiry_details TEXT,
    next_action TEXT,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id)
)
"""

CREATE_NOTES_TABLE = """
CREATE TABLE IF NOT EXISTS enquiry_notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    enquiry_id INTEGER NOT NULL,
    note_text TEXT NOT NULL,
    created_at TEXT NOT NULL,
    FOREIGN KEY (enquiry_id) REFERENCES enquiries (id)
)
"""

SELECT_USER_BY_EMAIL = """
SELECT * FROM users WHERE email = ?
"""

INSERT_USER = """
INSERT INTO users (full_name, email, password_hash, role, created_at)
VALUES (?, ?, ?, ?, ?)
"""

SELECT_USER_BY_ID = """
SELECT * FROM users WHERE id = ?
"""

SELECT_ALL_USERS = """
SELECT * FROM users ORDER BY created_at ASC
"""

SELECT_ENQUIRIES_BY_USER = """
SELECT * FROM enquiries WHERE user_id = ? ORDER BY created_at DESC
"""

SELECT_ALL_ENQUIRIES_WITH_OWNER = """
SELECT enquiries.*, users.full_name AS owner_name
FROM enquiries
JOIN users ON enquiries.user_id = users.id
ORDER BY enquiries.created_at DESC
"""

SELECT_ENQUIRY_BY_REFERENCE_AND_USER = """
SELECT * FROM enquiries WHERE reference_number = ? AND user_id = ?
"""

INSERT_ENQUIRY = """
INSERT INTO enquiries (
    reference_number,
    user_id,
    customer_name,
    customer_email,
    customer_phone,
    enquiry_type,
    priority,
    status,
    assigned_to,
    enquiry_source,
    estimated_value,
    follow_up_date,
    enquiry_details,
    next_action,
    created_at,
    updated_at
)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

UPDATE_ENQUIRY = """
UPDATE enquiries
SET customer_name = ?,
    customer_email = ?,
    customer_phone = ?,
    enquiry_type = ?,
    priority = ?,
    status = ?,
    assigned_to = ?,
    enquiry_source = ?,
    estimated_value = ?,
    follow_up_date = ?,
    enquiry_details = ?,
    next_action = ?,
    updated_at = ?
WHERE reference_number = ? AND user_id = ?
"""

DELETE_ENQUIRY = """
DELETE FROM enquiries WHERE reference_number = ? AND user_id = ?
"""

INSERT_NOTE = """
INSERT INTO enquiry_notes (enquiry_id, note_text, created_at)
VALUES (?, ?, ?)
"""

SELECT_NOTES_BY_ENQUIRY = """
SELECT * FROM enquiry_notes WHERE enquiry_id = ? ORDER BY created_at DESC
"""


def get_database_connection():
    connection = sqlite3.connect(DATABASE_FILE)

    connection.row_factory = sqlite3.Row

    return connection


def create_database_tables():
    connection = get_database_connection()

    connection.execute(CREATE_USERS_TABLE)
    connection.execute(CREATE_ENQUIRIES_TABLE)
    connection.execute(CREATE_NOTES_TABLE)

    connection.commit()
    connection.close()


def is_valid_email(email):
    email_pattern = r"^[^\s@]+@[^\s@]+\.[^\s@]+$"

    return re.match(email_pattern, email) is not None


def is_valid_phone_number(phone_number):
    cleaned_phone_number = re.sub(r"[\s\-\(\)]", "", phone_number)

    phone_pattern = r"^\+?\d{7,15}$"

    return re.match(phone_pattern, cleaned_phone_number) is not None


def is_valid_date(date_text):
    try:
        datetime.strptime(date_text, "%Y-%m-%d")

        return True

    except ValueError:
        return False


def set_message(message, message_type="success"):
    session["message"] = message
    session["message_type"] = message_type


def get_message():
    message = session.pop("message", "")
    message_type = session.pop("message_type", "success")

    return message, message_type


def login_required(view_function):
    @wraps(view_function)
    def protected_view(*args, **kwargs):
        if session.get("user_id") is None:
            set_message("Please log in to access the Enquiry Tracker.", "error")

            return redirect(url_for("login"))

        return view_function(*args, **kwargs)

    return protected_view


def admin_required(view_function):
    @wraps(view_function)
    def protected_view(*args, **kwargs):
        if session.get("user_id") is None:
            set_message("Please log in to access the Enquiry Tracker.", "error")


            return redirect(url_for("login"))


        if session.get("user_role") != "admin":
            return render_template(
                "admin-access-denied.html"
            ), 200


        return view_function(*args, **kwargs)


    return protected_view


def generate_reference_number():
    current_time = datetime.now()

    reference_number = "ENQ-" + current_time.strftime("%Y%m%d%H%M%S%f")

    return reference_number


def get_enquiry_metrics(enquiries):
    total_enquiries = len(enquiries)

    total_estimated_value = 0

    for enquiry in enquiries:
        total_estimated_value = total_estimated_value + enquiry["estimated_value"]

    if total_enquiries > 0:
        average_estimated_value = total_estimated_value / total_enquiries

    else:
        average_estimated_value = 0

    highest_value_enquiry = None

    for enquiry in enquiries:
        if highest_value_enquiry is None:
            highest_value_enquiry = enquiry

        elif enquiry["estimated_value"] > highest_value_enquiry["estimated_value"]:
            highest_value_enquiry = enquiry

    top_three_value_enquiries = sorted(
        enquiries,
        key=lambda enquiry: enquiry["estimated_value"],
        reverse=True
    )[:3]

    overdue_follow_ups = 0

    today = date.today()

    for enquiry in enquiries:
        if enquiry["follow_up_date"]:
            try:
                follow_up_date = datetime.strptime(
                    enquiry["follow_up_date"],
                    "%Y-%m-%d"
                ).date()

                if follow_up_date < today and enquiry["status"] != "Closed":
                    overdue_follow_ups = overdue_follow_ups + 1

            except ValueError:
                pass

    status_counts = {
        "New": 0,
        "In progress": 0,
        "Closed": 0
    }

    priority_counts = {
        "Low": 0,
        "Medium": 0,
        "High": 0
    }

    type_counts = {
        "General enquiry": 0,
        "Quotation": 0,
        "Support": 0,
        "Partnership": 0
    }

    value_by_status = {
        "New": 0,
        "In progress": 0,
        "Closed": 0
    }

    value_by_priority = {
        "Low": 0,
        "Medium": 0,
        "High": 0
    }

    value_by_enquiry_type = {}

    value_by_assigned_person = {}

    value_by_source = {}

    source_counts = {}

    for enquiry in enquiries:
        status = enquiry["status"]
        priority = enquiry["priority"]
        enquiry_type = enquiry["enquiry_type"]
        assigned_to = enquiry["assigned_to"]
        enquiry_source = enquiry["enquiry_source"]
        estimated_value = enquiry["estimated_value"]

        if status in status_counts:
            status_counts[status] = status_counts[status] + 1

        if priority in priority_counts:
            priority_counts[priority] = priority_counts[priority] + 1

        if enquiry_type in type_counts:
            type_counts[enquiry_type] = type_counts[enquiry_type] + 1

        if status in value_by_status:
            value_by_status[status] = value_by_status[status] + estimated_value

        if priority in value_by_priority:
            value_by_priority[priority] = value_by_priority[priority] + estimated_value

        value_by_enquiry_type[enquiry_type] = value_by_enquiry_type.get(enquiry_type, 0) + estimated_value

        value_by_assigned_person[assigned_to] = value_by_assigned_person.get(assigned_to, 0) + estimated_value

        value_by_source[enquiry_source] = value_by_source.get(enquiry_source, 0) + estimated_value

        source_counts[enquiry_source] = source_counts.get(enquiry_source, 0) + 1

    return {
        "total_enquiries": total_enquiries,
        "total_estimated_value": total_estimated_value,
        "average_estimated_value": average_estimated_value,
        "highest_value_enquiry": highest_value_enquiry,
        "top_three_value_enquiries": top_three_value_enquiries,
        "overdue_follow_ups": overdue_follow_ups,
        "status_counts": status_counts,
        "priority_counts": priority_counts,
        "type_counts": type_counts,
        "value_by_status": value_by_status,
        "value_by_priority": value_by_priority,
        "value_by_enquiry_type": value_by_enquiry_type,
        "value_by_assigned_person": value_by_assigned_person,
        "value_by_source": value_by_source,
        "source_counts": source_counts
    }


@app.errorhandler(404)
def page_not_found(error):
    return render_template(
        "error.html",
        error_title="Page not found",
        error_message="The page you requested could not be found."
    ), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template(
        "error.html",
        error_title="Something went wrong",
        error_message="An unexpected error occurred. Please try again."
    ), 500


@app.route("/register", methods=["GET", "POST"])
def register():
    message, message_type = get_message()

    if request.method == "POST":
        full_name = request.form.get("full-name", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        confirm_password = request.form.get("confirm-password", "")

        errors = []

        if full_name == "":
            errors.append("Full name is required.")

        if email == "":
            errors.append("Email address is required.")

        elif not is_valid_email(email):
            errors.append("Please enter a valid email address.")

        if password == "":
            errors.append("Password is required.")

        elif len(password) < 8:
            errors.append("Password must be at least 8 characters long.")

        if password != confirm_password:
            errors.append("Passwords do not match.")

        connection = get_database_connection()

        try:
            existing_user = connection.execute(
                SELECT_USER_BY_EMAIL,
                (email,)
            ).fetchone()

            if existing_user:
                errors.append("An account with this email address already exists.")

            if errors:
                connection.close()

                return render_template(
                    "register.html",
                    errors=errors,
                    full_name=full_name,
                    email=email,
                    message="",
                    message_type="success"
                )

            user_count = connection.execute(
                "SELECT COUNT(*) AS user_count FROM users"
            ).fetchone()

            if user_count["user_count"] == 0:
                role = "admin"

            else:
                role = "user"

            connection.execute(
                INSERT_USER,
                (
                    full_name,
                    email,
                    generate_password_hash(password),
                    role,
                    datetime.now().isoformat()
                )
            )

            connection.commit()
            connection.close()

            set_message("Account created successfully. Please log in.")

            return redirect(url_for("login"))

        except sqlite3.Error:
            connection.close()

            return render_template(
                "register.html",
                errors=["A database error occurred while creating your account. Please try again."],
                full_name=full_name,
                email=email,
                message="",
                message_type="success"
            )

    return render_template(
        "register.html",
        errors=[],
        full_name="",
        email="",
        message=message,
        message_type=message_type
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    message, message_type = get_message()

    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        errors = []

        if email == "":
            errors.append("Email address is required.")

        if password == "":
            errors.append("Password is required.")

        if errors:
            return render_template(
                "login.html",
                errors=errors,
                email=email,
                message="",
                message_type="success"
            )

        connection = get_database_connection()

        try:
            user = connection.execute(
                SELECT_USER_BY_EMAIL,
                (email,)
            ).fetchone()

            connection.close()

            if user is None or not check_password_hash(
                user["password_hash"],
                password
            ):
                return render_template(
                    "login.html",
                    errors=["Invalid email address or password."],
                    email=email,
                    message="",
                    message_type="success"
                )

            session["user_id"] = user["id"]
            session["user_name"] = user["full_name"]
            session["user_role"] = user["role"]

            set_message("Logged in successfully.")

            return redirect(url_for("index"))

        except sqlite3.Error:
            connection.close()

            return render_template(
                "login.html",
                errors=["A database error occurred while logging in. Please try again."],
                email=email,
                message="",
                message_type="success"
            )

    return render_template(
        "login.html",
        errors=[],
        email="",
        message=message,
        message_type=message_type
    )


@app.route("/logout")
def logout():
    session.clear()

    set_message("You have been logged out.")

    return redirect(url_for("login"))


@app.route("/")
@login_required
def index():
    connection = get_database_connection()

    try:
        enquiries = connection.execute(
            SELECT_ENQUIRIES_BY_USER,
            (session["user_id"],)
        ).fetchall()

        connection.close()

        search_text = request.args.get("search-text", "").strip().lower()
        search_field = request.args.get("search-field", "customer-name")
        status_filter = request.args.get("status-filter", "")
        priority_filter = request.args.get("priority-filter", "")
        assigned_to_filter = request.args.get("assigned-to-filter", "")
        source_filter = request.args.get("source-filter", "")
        overdue_only = request.args.get("overdue-only", "")
        sort_by_follow_up = request.args.get("sort-by-follow-up", "")

        filtered_enquiries = []

        for enquiry in enquiries:
            matches_search = True
            matches_status = True
            matches_priority = True
            matches_assigned_to = True
            matches_source = True
            matches_overdue = True

            if search_text:
                if search_field == "customer-name":
                    searchable_text = enquiry["customer_name"].lower()

                elif search_field == "enquiry-type":
                    searchable_text = enquiry["enquiry_type"].lower()

                else:
                    searchable_text = enquiry["customer_name"].lower()

                if search_text not in searchable_text:
                    matches_search = False

            if status_filter and enquiry["status"] != status_filter:
                matches_status = False

            if priority_filter and enquiry["priority"] != priority_filter:
                matches_priority = False

            if assigned_to_filter and enquiry["assigned_to"] != assigned_to_filter:
                matches_assigned_to = False

            if source_filter and enquiry["enquiry_source"] != source_filter:
                matches_source = False

            if overdue_only == "yes":
                is_overdue = False

                if enquiry["follow_up_date"]:
                    try:
                        follow_up_date = datetime.strptime(
                            enquiry["follow_up_date"],
                            "%Y-%m-%d"
                        ).date()

                        if follow_up_date < date.today() and enquiry["status"] != "Closed":
                            is_overdue = True

                    except ValueError:
                        is_overdue = False

                if not is_overdue:
                    matches_overdue = False

            if matches_search and matches_status and matches_priority and matches_assigned_to and matches_source and matches_overdue:
                filtered_enquiries.append(enquiry)

        if sort_by_follow_up == "yes":
            filtered_enquiries = sorted(
                filtered_enquiries,
                key=lambda enquiry: enquiry["follow_up_date"] or "9999-12-31"
            )

        assigned_names = []

        for enquiry in enquiries:
            assigned_name = enquiry["assigned_to"]

            if assigned_name and assigned_name not in assigned_names:
                assigned_names.append(assigned_name)

        dashboard_summary = get_enquiry_metrics(enquiries)

        message, message_type = get_message()

        return render_template(
            "index.html",
            enquiries=filtered_enquiries,
            total_enquiries=len(enquiries),
            dashboard_summary=dashboard_summary,
            approved_enquiry_types=APPROVED_ENQUIRY_TYPES,
            approved_priorities=APPROVED_PRIORITIES,
            approved_sources=APPROVED_SOURCES,
            approved_statuses=APPROVED_STATUSES,
            assigned_names=assigned_names,
            search_text=search_text,
            search_field=search_field,
            status_filter=status_filter,
            priority_filter=priority_filter,
            assigned_to_filter=assigned_to_filter,
            source_filter=source_filter,
            overdue_only=overdue_only,
            sort_by_follow_up=sort_by_follow_up,
            message=message,
            message_type=message_type
        )

    except sqlite3.Error:
        connection.close()

        set_message("A database error occurred while loading enquiries. Please try again.", "error")

        return redirect(url_for("index"))


@app.route("/admin")
@admin_required
def admin_dashboard():
    connection = get_database_connection()

    try:
        users = connection.execute(
            SELECT_ALL_USERS
        ).fetchall()

        enquiries = connection.execute(
            SELECT_ALL_ENQUIRIES_WITH_OWNER
        ).fetchall()

        connection.close()

        dashboard_summary = get_enquiry_metrics(enquiries)

        message, message_type = get_message()

        return render_template(
            "admin.html",
            users=users,
            enquiries=enquiries,
            dashboard_summary=dashboard_summary,
            message=message,
            message_type=message_type
        )

    except sqlite3.Error:
        connection.close()

        set_message("A database error occurred while loading the admin dashboard. Please try again.", "error")

        return redirect(url_for("index"))


@app.route("/create-enquiry", methods=["POST"])
@login_required
def create_enquiry():
    customer_name = request.form.get("customer-name", "").strip()
    customer_email = request.form.get("customer-email", "").strip().lower()
    customer_phone = request.form.get("customer-phone", "").strip()
    enquiry_type = request.form.get("enquiry-type", "").strip()
    priority = request.form.get("priority", "").strip()
    assigned_to = request.form.get("assigned-to", "").strip()
    enquiry_source = request.form.get("enquiry-source", "").strip()
    estimated_value = request.form.get("estimated-value", "").strip()
    follow_up_date = request.form.get("follow-up-date", "").strip()
    enquiry_details = request.form.get("enquiry-details", "").strip()
    next_action = request.form.get("next-action", "").strip()

    errors = []

    if customer_name == "":
        errors.append("Customer name is required.")

    if customer_email == "":
        errors.append("Customer email address is required.")

    elif not is_valid_email(customer_email):
        errors.append("Please enter a valid customer email address.")

    if customer_phone == "":
        errors.append("Customer phone number is required.")

    elif not is_valid_phone_number(customer_phone):
        errors.append("Please enter a valid customer phone number.")

    if enquiry_type not in APPROVED_ENQUIRY_TYPES:
        errors.append("Please select a valid enquiry type.")

    if priority not in APPROVED_PRIORITIES:
        errors.append("Please select a valid priority.")

    if assigned_to == "":
        errors.append("Assigned person is required.")

    if enquiry_source not in APPROVED_SOURCES:
        errors.append("Please select a valid enquiry source.")

    if estimated_value == "":
        errors.append("Estimated value is required.")

    else:
        try:
            estimated_value = float(estimated_value)

            if estimated_value < 0:
                errors.append("Estimated value cannot be negative.")

        except ValueError:
            errors.append("Estimated value must be a valid number.")

    if follow_up_date and not is_valid_date(follow_up_date):
        errors.append("Please enter a valid follow-up date.")

    if errors:
        set_message(errors, "error")

        return redirect(url_for("index"))

    connection = get_database_connection()

    try:
        duplicate_email = connection.execute(
            "SELECT id FROM enquiries WHERE customer_email = ? AND user_id = ?",
            (customer_email, session["user_id"])
        ).fetchone()

        duplicate_phone = connection.execute(
            "SELECT id FROM enquiries WHERE customer_phone = ? AND user_id = ?",
            (customer_phone, session["user_id"])
        ).fetchone()

        if duplicate_email:
            errors.append("An enquiry with this customer email address already exists.")

        if duplicate_phone:
            errors.append("An enquiry with this customer phone number already exists.")

        if errors:
            connection.close()

            set_message(errors, "error")

            return redirect(url_for("index"))

        reference_number = generate_reference_number()
        current_time = datetime.now().isoformat()

        connection.execute(
            INSERT_ENQUIRY,
            (
                reference_number,
                session["user_id"],
                customer_name,
                customer_email,
                customer_phone,
                enquiry_type,
                priority,
                "New",
                assigned_to,
                enquiry_source,
                estimated_value,
                follow_up_date,
                enquiry_details,
                next_action,
                current_time,
                current_time
            )
        )

        connection.commit()
        connection.close()

        set_message("Enquiry created successfully.")

        return redirect(url_for("index"))

    except sqlite3.Error:
        connection.close()

        set_message("A database error occurred while creating the enquiry. Please try again.", "error")

        return redirect(url_for("index"))


@app.route("/enquiry/<reference_number>")
@login_required
def enquiry_details(reference_number):
    connection = get_database_connection()

    try:
        enquiry = connection.execute(
            SELECT_ENQUIRY_BY_REFERENCE_AND_USER,
            (reference_number, session["user_id"])
        ).fetchone()

        if enquiry is None:
            connection.close()

            set_message("Enquiry not found.", "error")

            return redirect(url_for("index"))

        notes = connection.execute(
            SELECT_NOTES_BY_ENQUIRY,
            (enquiry["id"],)
        ).fetchall()

        connection.close()

        message, message_type = get_message()

        return render_template(
            "enquiry.html",
            enquiry=enquiry,
            notes=notes,
            message=message,
            message_type=message_type
        )

    except sqlite3.Error:
        connection.close()

        set_message("A database error occurred while loading the enquiry. Please try again.", "error")

        return redirect(url_for("index"))


@app.route("/edit-enquiry/<reference_number>", methods=["GET", "POST"])
@login_required
def edit_enquiry(reference_number):
    connection = get_database_connection()

    try:
        enquiry = connection.execute(
            SELECT_ENQUIRY_BY_REFERENCE_AND_USER,
            (reference_number, session["user_id"])
        ).fetchone()

        if enquiry is None:
            connection.close()

            set_message("Enquiry not found.", "error")

            return redirect(url_for("index"))

        if request.method == "POST":
            customer_name = request.form.get("customer-name", "").strip()
            customer_email = request.form.get("customer-email", "").strip().lower()
            customer_phone = request.form.get("customer-phone", "").strip()
            enquiry_type = request.form.get("enquiry-type", "").strip()
            priority = request.form.get("priority", "").strip()
            status = request.form.get("status", "").strip()
            assigned_to = request.form.get("assigned-to", "").strip()
            enquiry_source = request.form.get("enquiry-source", "").strip()
            estimated_value = request.form.get("estimated-value", "").strip()
            follow_up_date = request.form.get("follow-up-date", "").strip()
            enquiry_details = request.form.get("enquiry-details", "").strip()
            next_action = request.form.get("next-action", "").strip()

            errors = []

            if customer_name == "":
                errors.append("Customer name is required.")

            if customer_email == "":
                errors.append("Customer email address is required.")

            elif not is_valid_email(customer_email):
                errors.append("Please enter a valid customer email address.")

            if customer_phone == "":
                errors.append("Customer phone number is required.")

            elif not is_valid_phone_number(customer_phone):
                errors.append("Please enter a valid customer phone number.")

            if enquiry_type not in APPROVED_ENQUIRY_TYPES:
                errors.append("Please select a valid enquiry type.")

            if priority not in APPROVED_PRIORITIES:
                errors.append("Please select a valid priority.")

            if status not in APPROVED_STATUSES:
                errors.append("Please select a valid status.")

            if assigned_to == "":
                errors.append("Assigned person is required.")

            if enquiry_source not in APPROVED_SOURCES:
                errors.append("Please select a valid enquiry source.")

            if estimated_value == "":
                errors.append("Estimated value is required.")

            else:
                try:
                    estimated_value = float(estimated_value)

                    if estimated_value < 0:
                        errors.append("Estimated value cannot be negative.")

                except ValueError:
                    errors.append("Estimated value must be a valid number.")

            if follow_up_date and not is_valid_date(follow_up_date):
                errors.append("Please enter a valid follow-up date.")

            if errors:
                connection.close()

                set_message(errors, "error")

                return redirect(url_for("edit_enquiry", reference_number=reference_number))

            connection.execute(
                UPDATE_ENQUIRY,
                (
                    customer_name,
                    customer_email,
                    customer_phone,
                    enquiry_type,
                    priority,
                    status,
                    assigned_to,
                    enquiry_source,
                    estimated_value,
                    follow_up_date,
                    enquiry_details,
                    next_action,
                    datetime.now().isoformat(),
                    reference_number,
                    session["user_id"]
                )
            )

            connection.commit()
            connection.close()

            set_message("Enquiry updated successfully.")

            return redirect(url_for("enquiry_details", reference_number=reference_number))

        connection.close()

        message, message_type = get_message()

        return render_template(
            "enquiry.html",
            enquiry=enquiry,
            notes=[],
            edit_mode=True,
            approved_enquiry_types=APPROVED_ENQUIRY_TYPES,
            approved_priorities=APPROVED_PRIORITIES,
            approved_sources=APPROVED_SOURCES,
            approved_statuses=APPROVED_STATUSES,
            message=message,
            message_type=message_type
        )

    except sqlite3.Error:
        connection.close()

        set_message("A database error occurred while editing the enquiry. Please try again.", "error")

        return redirect(url_for("index"))


@app.route("/close-enquiry/<reference_number>", methods=["POST"])
@login_required
def close_enquiry(reference_number):
    connection = get_database_connection()

    try:
        enquiry = connection.execute(
            SELECT_ENQUIRY_BY_REFERENCE_AND_USER,
            (reference_number, session["user_id"])
        ).fetchone()

        if enquiry is None:
            connection.close()

            set_message("Enquiry not found.", "error")

            return redirect(url_for("index"))

        connection.execute(
            "UPDATE enquiries SET status = 'Closed', updated_at = ? WHERE reference_number = ? AND user_id = ?",
            (
                datetime.now().isoformat(),
                reference_number,
                session["user_id"]
            )
        )

        connection.commit()
        connection.close()

        set_message("Enquiry closed successfully.")

        return redirect(url_for("enquiry_details", reference_number=reference_number))

    except sqlite3.Error:
        connection.close()

        set_message("A database error occurred while closing the enquiry. Please try again.", "error")

        return redirect(url_for("index"))


@app.route("/reopen-enquiry/<reference_number>", methods=["POST"])
@login_required
def reopen_enquiry(reference_number):
    connection = get_database_connection()

    try:
        enquiry = connection.execute(
            SELECT_ENQUIRY_BY_REFERENCE_AND_USER,
            (reference_number, session["user_id"])
        ).fetchone()

        if enquiry is None:
            connection.close()

            set_message("Enquiry not found.", "error")

            return redirect(url_for("index"))

        connection.execute(
            "UPDATE enquiries SET status = 'New', updated_at = ? WHERE reference_number = ? AND user_id = ?",
            (
                datetime.now().isoformat(),
                reference_number,
                session["user_id"]
            )
        )

        connection.commit()
        connection.close()

        set_message("Enquiry reopened successfully.")

        return redirect(url_for("enquiry_details", reference_number=reference_number))

    except sqlite3.Error:
        connection.close()

        set_message("A database error occurred while reopening the enquiry. Please try again.", "error")

        return redirect(url_for("index"))


@app.route("/add-note/<reference_number>", methods=["POST"])
@login_required
def add_note(reference_number):
    note_text = request.form.get("note-text", "").strip()

    if note_text == "":
        set_message("Note text is required.", "error")

        return redirect(url_for("enquiry_details", reference_number=reference_number))

    connection = get_database_connection()

    try:
        enquiry = connection.execute(
            SELECT_ENQUIRY_BY_REFERENCE_AND_USER,
            (reference_number, session["user_id"])
        ).fetchone()

        if enquiry is None:
            connection.close()

            set_message("Enquiry not found.", "error")

            return redirect(url_for("index"))

        connection.execute(
            INSERT_NOTE,
            (
                enquiry["id"],
                note_text,
                datetime.now().isoformat()
            )
        )

        connection.commit()
        connection.close()

        set_message("Note added successfully.")

        return redirect(url_for("enquiry_details", reference_number=reference_number))

    except sqlite3.Error:
        connection.close()

        set_message("A database error occurred while adding the note. Please try again.", "error")

        return redirect(url_for("index"))


@app.route("/delete-enquiry/<reference_number>", methods=["POST"])
@login_required
def delete_enquiry(reference_number):
    connection = get_database_connection()

    try:
        enquiry = connection.execute(
            SELECT_ENQUIRY_BY_REFERENCE_AND_USER,
            (reference_number, session["user_id"])
        ).fetchone()

        if enquiry is None:
            connection.close()

            set_message("Enquiry not found.", "error")

            return redirect(url_for("index"))

        connection.execute(
            "DELETE FROM enquiry_notes WHERE enquiry_id = ?",
            (enquiry["id"],)
        )

        connection.execute(
            DELETE_ENQUIRY,
            (reference_number, session["user_id"])
        )

        connection.commit()
        connection.close()

        set_message("Enquiry " + reference_number + " deleted successfully.")

        return redirect(url_for("index"))

    except sqlite3.Error:
        connection.close()

        set_message("A database error occurred while deleting the enquiry. Please try again.", "error")

        return redirect(url_for("index"))


@app.route("/export-enquiries")
@login_required
def export_enquiries():
    connection = get_database_connection()

    try:
        enquiries = connection.execute(
            SELECT_ENQUIRIES_BY_USER,
            (session["user_id"],)
        ).fetchall()

        connection.close()

        output = io.StringIO()

        writer = csv.writer(output)

        writer.writerow([
            "Reference Number",
            "Customer Name",
            "Customer Email",
            "Customer Phone",
            "Enquiry Type",
            "Priority",
            "Status",
            "Assigned To",
            "Enquiry Source",
            "Estimated Value",
            "Follow-Up Date",
            "Enquiry Details",
            "Next Action",
            "Created At",
            "Updated At"
        ])

        for enquiry in enquiries:
            writer.writerow([
                enquiry["reference_number"],
                enquiry["customer_name"],
                enquiry["customer_email"],
                enquiry["customer_phone"],
                enquiry["enquiry_type"],
                enquiry["priority"],
                enquiry["status"],
                enquiry["assigned_to"],
                enquiry["enquiry_source"],
                enquiry["estimated_value"],
                enquiry["follow_up_date"],
                enquiry["enquiry_details"],
                enquiry["next_action"],
                enquiry["created_at"],
                enquiry["updated_at"]
            ])

        csv_data = output.getvalue()

        output.close()

        return Response(
            csv_data,
            mimetype="text/csv",
            headers={
                "Content-Disposition": "attachment; filename=enquiry_register.csv"
            }
        )

    except sqlite3.Error:
        connection.close()

        set_message("A database error occurred while exporting enquiries. Please try again.", "error")

        return redirect(url_for("index"))


if __name__ == "__main__":
    create_database_tables()

    port = int(os.environ.get("PORT", 5001))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )