# Day 63 — Add enquiry value by enquiry type

import csv
import io
import json
import os
import random
import re
from datetime import datetime

from flask import Flask, render_template, request, redirect, url_for, Response

app = Flask(__name__)

JSON_FILE = "enquiry_register.json"

APPROVED_ENQUIRY_TYPES = [
    "General enquiry",
    "Quotation",
    "Support",
    "Partnership"
]

APPROVED_STATUSES = [
    "New",
    "In progress",
    "Closed"
]

APPROVED_PRIORITIES = [
    "Low",
    "Medium",
    "High"
]

APPROVED_SOURCES = [
    "Website",
    "WhatsApp",
    "Email",
    "Referral",
    "Phone call"
]

TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"
DATE_FORMAT = "%Y-%m-%d"

EMAIL_PATTERN = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
PHONE_PATTERN = r"^[0-9+\-\s()]{7,20}$"

CSV_HEADERS = [
    "Reference number",
    "Customer name",
    "Customer email",
    "Customer phone",
    "Enquiry type",
    "Priority",
    "Status",
    "Assigned to",
    "Enquiry source",
    "Estimated value",
    "Created at",
    "Follow-up date",
    "Enquiry details",
    "Next action",
    "Notes"
]


def load_enquiries():
    if not os.path.exists(JSON_FILE):
        return []

    try:
        with open(JSON_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            return data

        return []

    except json.JSONDecodeError:
        return []

    except OSError:
        return []


def save_enquiries(enquiries):
    try:
        with open(JSON_FILE, "w", encoding="utf-8") as file:
            json.dump(enquiries, file, indent=2, ensure_ascii=False)

        return True

    except OSError:
        return False


def is_valid_email(email_address):
    return re.match(EMAIL_PATTERN, email_address) is not None


def is_valid_phone(phone_number):
    return re.match(PHONE_PATTERN, phone_number) is not None


def email_already_exists(enquiries, email_address, exclude_reference_number=None):
    for enquiry in enquiries:
        existing_email = enquiry.get("customer_email", "").strip().lower()

        if existing_email != email_address:
            continue

        if exclude_reference_number is not None:
            if enquiry["reference_number"] == exclude_reference_number:
                continue

        return True

    return False


def phone_already_exists(enquiries, phone_number, exclude_reference_number=None):
    for enquiry in enquiries:
        existing_phone = enquiry.get("customer_phone", "").strip()

        if existing_phone != phone_number:
            continue

        if exclude_reference_number is not None:
            if enquiry["reference_number"] == exclude_reference_number:
                continue

        return True

    return False


def find_enquiry(enquiries, reference_number):
    for enquiry in enquiries:
        if enquiry["reference_number"] == reference_number:
            return enquiry

    return None


def count_records(enquiries, field_name, approved_options):
    counts = {}

    for approved_option in approved_options:
        counts[approved_option] = 0

    for enquiry in enquiries:
        value = enquiry[field_name]

        if value in counts:
            counts[value] = counts[value] + 1

    return counts


def calculate_value_by_status(enquiries):
    value_by_status = {}

    for approved_status in APPROVED_STATUSES:
        value_by_status[approved_status] = 0

    for enquiry in enquiries:
        status = enquiry["status"]
        estimated_value = enquiry.get("estimated_value", 0)

        if status in value_by_status:
            if isinstance(estimated_value, (int, float)):
                value_by_status[status] = (
                    value_by_status[status] + estimated_value
                )

    return value_by_status


def calculate_value_by_assigned_person(enquiries):
    value_by_person = {}

    for enquiry in enquiries:
        assigned_to = enquiry.get("assigned_to", "").strip()

        if assigned_to == "":
            assigned_to = "Unassigned"

        estimated_value = enquiry.get("estimated_value", 0)

        if assigned_to not in value_by_person:
            value_by_person[assigned_to] = 0

        if isinstance(estimated_value, (int, float)):
            value_by_person[assigned_to] = (
                value_by_person[assigned_to] + estimated_value
            )

    return value_by_person


def calculate_value_by_source(enquiries):
    value_by_source = {}

    for approved_source in APPROVED_SOURCES:
        value_by_source[approved_source] = 0

    for enquiry in enquiries:
        enquiry_source = enquiry.get("enquiry_source", "")
        estimated_value = enquiry.get("estimated_value", 0)

        if enquiry_source in value_by_source:
            if isinstance(estimated_value, (int, float)):
                value_by_source[enquiry_source] = (
                    value_by_source[enquiry_source] + estimated_value
                )

    return value_by_source


def calculate_value_by_priority(enquiries):
    value_by_priority = {}

    for approved_priority in APPROVED_PRIORITIES:
        value_by_priority[approved_priority] = 0

    for enquiry in enquiries:
        priority = enquiry["priority"]
        estimated_value = enquiry.get("estimated_value", 0)

        if priority in value_by_priority:
            if isinstance(estimated_value, (int, float)):
                value_by_priority[priority] = (
                    value_by_priority[priority] + estimated_value
                )

    return value_by_priority


def calculate_value_by_enquiry_type(enquiries):
    value_by_enquiry_type = {}

    for approved_enquiry_type in APPROVED_ENQUIRY_TYPES:
        value_by_enquiry_type[approved_enquiry_type] = 0

    for enquiry in enquiries:
        enquiry_type = enquiry["enquiry_type"]
        estimated_value = enquiry.get("estimated_value", 0)

        if enquiry_type in value_by_enquiry_type:
            if isinstance(estimated_value, (int, float)):
                value_by_enquiry_type[enquiry_type] = (
                    value_by_enquiry_type[enquiry_type] + estimated_value
                )

    return value_by_enquiry_type


def is_overdue(enquiry):
    follow_up_date = enquiry.get("follow_up_date", "")

    if follow_up_date == "":
        return False

    if enquiry["status"] == "Closed":
        return False

    try:
        follow_up = datetime.strptime(
            follow_up_date,
            DATE_FORMAT
        )

        today = datetime.now()

        return follow_up.date() < today.date()

    except ValueError:
        return False


def create_dashboard_summary(enquiries):
    overdue_count = 0
    total_estimated_value = 0
    highest_value_enquiry = None

    for enquiry in enquiries:
        if is_overdue(enquiry):
            overdue_count = overdue_count + 1

        estimated_value = enquiry.get("estimated_value", 0)

        if isinstance(estimated_value, (int, float)):
            total_estimated_value = total_estimated_value + estimated_value

            if highest_value_enquiry is None:
                highest_value_enquiry = enquiry

            elif estimated_value > highest_value_enquiry.get("estimated_value", 0):
                highest_value_enquiry = enquiry

    if len(enquiries) > 0:
        average_estimated_value = total_estimated_value / len(enquiries)
    else:
        average_estimated_value = 0

    return {
        "total_enquiries": len(enquiries),
        "overdue_follow_ups": overdue_count,
        "total_estimated_value": total_estimated_value,
        "average_estimated_value": average_estimated_value,
        "highest_value_enquiry": highest_value_enquiry,
        "value_by_status": calculate_value_by_status(enquiries),
        "value_by_assigned_person": calculate_value_by_assigned_person(
            enquiries
        ),
        "value_by_source": calculate_value_by_source(enquiries),
        "value_by_priority": calculate_value_by_priority(enquiries),
        "value_by_enquiry_type": calculate_value_by_enquiry_type(enquiries),
        "status_counts": count_records(
            enquiries,
            "status",
            APPROVED_STATUSES
        ),
        "priority_counts": count_records(
            enquiries,
            "priority",
            APPROVED_PRIORITIES
        ),
        "type_counts": count_records(
            enquiries,
            "enquiry_type",
            APPROVED_ENQUIRY_TYPES
        ),
        "source_counts": count_records(
            enquiries,
            "enquiry_source",
            APPROVED_SOURCES
        )
    }


def sort_enquiries_by_follow_up_date(enquiries):
    enquiries_with_date = []
    enquiries_without_date = []

    for enquiry in enquiries:
        follow_up_date = enquiry.get("follow_up_date", "")

        if follow_up_date:
            try:
                follow_up = datetime.strptime(
                    follow_up_date,
                    DATE_FORMAT
                )

                enquiries_with_date.append(
                    (follow_up, enquiry)
                )

            except ValueError:
                enquiries_without_date.append(enquiry)

        else:
            enquiries_without_date.append(enquiry)

    enquiries_with_date.sort(
        key=lambda item: item[0]
    )

    sorted_enquiries = []

    for follow_up, enquiry in enquiries_with_date:
        sorted_enquiries.append(enquiry)

    for enquiry in enquiries_without_date:
        sorted_enquiries.append(enquiry)

    return sorted_enquiries


def filter_enquiries(
    enquiries,
    search_text,
    search_field,
    status_filter,
    priority_filter,
    overdue_only,
    assigned_to_filter,
    source_filter
):
    filtered_enquiries = enquiries

    if search_text:
        if search_field == "customer-name":
            filtered_enquiries = [
                enquiry for enquiry in filtered_enquiries
                if search_text in enquiry["customer_name"].lower()
            ]

        elif search_field == "enquiry-type":
            filtered_enquiries = [
                enquiry for enquiry in filtered_enquiries
                if search_text in enquiry["enquiry_type"].lower()
            ]

    if status_filter:
        filtered_enquiries = [
            enquiry for enquiry in filtered_enquiries
            if enquiry["status"] == status_filter
        ]

    if priority_filter:
        filtered_enquiries = [
            enquiry for enquiry in filtered_enquiries
            if enquiry["priority"] == priority_filter
        ]

    if overdue_only:
        filtered_enquiries = [
            enquiry for enquiry in filtered_enquiries
            if is_overdue(enquiry)
        ]

    if assigned_to_filter:
        filtered_enquiries = [
            enquiry for enquiry in filtered_enquiries
            if enquiry.get("assigned_to", "").lower()
            == assigned_to_filter.lower()
        ]

    if source_filter:
        filtered_enquiries = [
            enquiry for enquiry in filtered_enquiries
            if enquiry.get("enquiry_source", "") == source_filter
        ]

    return filtered_enquiries


def create_csv_file(enquiries):
    output = io.StringIO()

    csv_writer = csv.DictWriter(
        output,
        fieldnames=CSV_HEADERS
    )

    csv_writer.writeheader()

    for enquiry in enquiries:
        notes = enquiry.get("notes", [])

        note_text = ""

        for note in notes:
            if note_text:
                note_text = note_text + " | "

            note_text = note_text + note.get("note_text", "")

        csv_writer.writerow({
            "Reference number": enquiry["reference_number"],
            "Customer name": enquiry["customer_name"],
            "Customer email": enquiry.get("customer_email", ""),
            "Customer phone": enquiry.get("customer_phone", ""),
            "Enquiry type": enquiry["enquiry_type"],
            "Priority": enquiry["priority"],
            "Status": enquiry["status"],
            "Assigned to": enquiry.get("assigned_to", ""),
            "Enquiry source": enquiry.get("enquiry_source", ""),
            "Estimated value": enquiry.get("estimated_value", 0),
            "Created at": enquiry["created_at"],
            "Follow-up date": enquiry.get("follow_up_date", ""),
            "Enquiry details": enquiry.get("enquiry_details", ""),
            "Next action": enquiry.get("next_action", ""),
            "Notes": note_text
        })

    return output.getvalue()


@app.route("/")
def index():
    enquiries = load_enquiries()

    dashboard_summary = create_dashboard_summary(enquiries)

    search_text = request.args.get("search-text", "").strip().lower()
    search_field = request.args.get("search-field", "").strip()
    status_filter = request.args.get("status-filter", "").strip()
    priority_filter = request.args.get("priority-filter", "").strip()
    overdue_only = request.args.get("overdue-only", "").strip()
    assigned_to_filter = request.args.get("assigned-to-filter", "").strip()
    source_filter = request.args.get("source-filter", "").strip()
    sort_by_follow_up = request.args.get("sort-by-follow-up", "").strip()

    filtered_enquiries = filter_enquiries(
        enquiries,
        search_text,
        search_field,
        status_filter,
        priority_filter,
        overdue_only == "yes",
        assigned_to_filter,
        source_filter
    )

    if sort_by_follow_up == "yes":
        filtered_enquiries = sort_enquiries_by_follow_up_date(
            filtered_enquiries
        )

    assigned_names = []

    for enquiry in enquiries:
        assigned_to = enquiry.get("assigned_to", "").strip()

        if assigned_to and assigned_to not in assigned_names:
            assigned_names.append(assigned_to)

    assigned_names.sort()

    return render_template(
        "index.html",
        enquiries=filtered_enquiries,
        total_enquiries=len(enquiries),
        dashboard_summary=dashboard_summary,
        approved_enquiry_types=APPROVED_ENQUIRY_TYPES,
        approved_priorities=APPROVED_PRIORITIES,
        approved_statuses=APPROVED_STATUSES,
        approved_sources=APPROVED_SOURCES,
        assigned_names=assigned_names,
        search_text=search_text,
        search_field=search_field,
        status_filter=status_filter,
        priority_filter=priority_filter,
        overdue_only=overdue_only,
        assigned_to_filter=assigned_to_filter,
        source_filter=source_filter,
        sort_by_follow_up=sort_by_follow_up,
        message=None,
        message_type=None
    )


@app.route("/create-enquiry", methods=["POST"])
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
        errors.append("Customer email is required.")

    elif not is_valid_email(customer_email):
        errors.append("Please enter a valid customer email address.")

    if customer_phone == "":
        errors.append("Customer phone number is required.")

    elif not is_valid_phone(customer_phone):
        errors.append("Please enter a valid customer phone number.")

    if enquiry_type not in APPROVED_ENQUIRY_TYPES:
        errors.append("Please select a valid enquiry type.")

    if priority not in APPROVED_PRIORITIES:
        errors.append("Please select a valid priority.")

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
            errors.append("Please enter a valid estimated value.")
            estimated_value = 0

    if follow_up_date:
        try:
            datetime.strptime(
                follow_up_date,
                DATE_FORMAT
            )

        except ValueError:
            errors.append("Please enter a valid follow-up date.")

    enquiries = load_enquiries()

    if customer_email and is_valid_email(customer_email):
        if email_already_exists(enquiries, customer_email):
            errors.append(
                "An enquiry already exists with this customer email address."
            )

    if customer_phone and is_valid_phone(customer_phone):
        if phone_already_exists(enquiries, customer_phone):
            errors.append(
                "An enquiry already exists with this customer phone number."
            )

    if errors:
        dashboard_summary = create_dashboard_summary(enquiries)

        assigned_names = []

        for enquiry in enquiries:
            assigned_to_value = enquiry.get("assigned_to", "").strip()

            if assigned_to_value and assigned_to_value not in assigned_names:
                assigned_names.append(assigned_to_value)

        assigned_names.sort()

        return render_template(
            "index.html",
            enquiries=enquiries,
            total_enquiries=len(enquiries),
            dashboard_summary=dashboard_summary,
            approved_enquiry_types=APPROVED_ENQUIRY_TYPES,
            approved_priorities=APPROVED_PRIORITIES,
            approved_statuses=APPROVED_STATUSES,
            approved_sources=APPROVED_SOURCES,
            assigned_names=assigned_names,
            search_text="",
            search_field="",
            status_filter="",
            priority_filter="",
            overdue_only="",
            assigned_to_filter="",
            source_filter="",
            sort_by_follow_up="",
            message=errors,
            message_type="error"
        )

    created_at = datetime.now().strftime(TIMESTAMP_FORMAT)
    reference_number = f"ENQ-{random.randint(1000, 9999)}"

    enquiry = {
        "reference_number": reference_number,
        "customer_name": customer_name,
        "customer_email": customer_email,
        "customer_phone": customer_phone,
        "enquiry_type": enquiry_type,
        "priority": priority,
        "status": "New",
        "assigned_to": assigned_to,
        "enquiry_source": enquiry_source,
        "estimated_value": estimated_value,
        "created_at": created_at,
        "follow_up_date": follow_up_date,
        "enquiry_details": enquiry_details,
        "next_action": next_action,
        "notes": []
    }

    enquiries.append(enquiry)

    saved_successfully = save_enquiries(enquiries)

    if saved_successfully:
        message = f"Enquiry created successfully. Reference number: {reference_number}"
        message_type = "success"
    else:
        message = "Could not save the enquiry. Please try again."
        message_type = "error"

    enquiries = load_enquiries()
    dashboard_summary = create_dashboard_summary(enquiries)

    assigned_names = []

    for enquiry in enquiries:
        assigned_to_value = enquiry.get("assigned_to", "").strip()

        if assigned_to_value and assigned_to_value not in assigned_names:
            assigned_names.append(assigned_to_value)

    assigned_names.sort()

    return render_template(
        "index.html",
        enquiries=enquiries,
        total_enquiries=len(enquiries),
        dashboard_summary=dashboard_summary,
        approved_enquiry_types=APPROVED_ENQUIRY_TYPES,
        approved_priorities=APPROVED_PRIORITIES,
        approved_statuses=APPROVED_STATUSES,
        approved_sources=APPROVED_SOURCES,
        assigned_names=assigned_names,
        search_text="",
        search_field="",
        status_filter="",
        priority_filter="",
        overdue_only="",
        assigned_to_filter="",
        source_filter="",
        sort_by_follow_up="",
        message=message,
        message_type=message_type
    )


@app.route("/enquiry/<reference_number>")
def enquiry_details(reference_number):
    enquiries = load_enquiries()
    enquiry = find_enquiry(enquiries, reference_number)

    if enquiry is None:
        return render_template(
            "enquiry.html",
            enquiry=None,
            approved_enquiry_types=APPROVED_ENQUIRY_TYPES,
            approved_statuses=APPROVED_STATUSES,
            approved_priorities=APPROVED_PRIORITIES,
            approved_sources=APPROVED_SOURCES,
            notes=[],
            message="No enquiry found with that reference number.",
            message_type="error"
        )

    notes = enquiry.get("notes", [])
    notes = list(reversed(notes))

    return render_template(
        "enquiry.html",
        enquiry=enquiry,
        approved_enquiry_types=APPROVED_ENQUIRY_TYPES,
        approved_statuses=APPROVED_STATUSES,
        approved_priorities=APPROVED_PRIORITIES,
        approved_sources=APPROVED_SOURCES,
        notes=notes,
        message=None,
        message_type=None
    )


@app.route("/edit-enquiry/<reference_number>", methods=["POST"])
def edit_enquiry(reference_number):
    enquiries = load_enquiries()
    enquiry = find_enquiry(enquiries, reference_number)

    if enquiry is None:
        return render_template(
            "enquiry.html",
            enquiry=None,
            approved_enquiry_types=APPROVED_ENQUIRY_TYPES,
            approved_statuses=APPROVED_STATUSES,
            approved_priorities=APPROVED_PRIORITIES,
            approved_sources=APPROVED_SOURCES,
            notes=[],
            message="No enquiry found with that reference number.",
            message_type="error"
        )

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
        errors.append("Customer email is required.")

    elif not is_valid_email(customer_email):
        errors.append("Please enter a valid customer email address.")

    if customer_phone == "":
        errors.append("Customer phone number is required.")

    elif not is_valid_phone(customer_phone):
        errors.append("Please enter a valid customer phone number.")

    if enquiry_type not in APPROVED_ENQUIRY_TYPES:
        errors.append("Please select a valid enquiry type.")

    if priority not in APPROVED_PRIORITIES:
        errors.append("Please select a valid priority.")

    if status not in APPROVED_STATUSES:
        errors.append("Please select a valid status.")

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
            errors.append("Please enter a valid estimated value.")
            estimated_value = 0

    if follow_up_date:
        try:
            datetime.strptime(
                follow_up_date,
                DATE_FORMAT
            )

        except ValueError:
            errors.append("Please enter a valid follow-up date.")

    if customer_email and is_valid_email(customer_email):
        if email_already_exists(
            enquiries,
            customer_email,
            exclude_reference_number=reference_number
        ):
            errors.append(
                "Another enquiry already exists with this customer email address."
            )

    if customer_phone and is_valid_phone(customer_phone):
        if phone_already_exists(
            enquiries,
            customer_phone,
            exclude_reference_number=reference_number
        ):
            errors.append(
                "Another enquiry already exists with this customer phone number."
            )

    if errors:
        notes = enquiry.get("notes", [])
        notes = list(reversed(notes))

        return render_template(
            "enquiry.html",
            enquiry=enquiry,
            approved_enquiry_types=APPROVED_ENQUIRY_TYPES,
            approved_statuses=APPROVED_STATUSES,
            approved_priorities=APPROVED_PRIORITIES,
            approved_sources=APPROVED_SOURCES,
            notes=notes,
            message=errors,
            message_type="error"
        )

    enquiry["customer_name"] = customer_name
    enquiry["customer_email"] = customer_email
    enquiry["customer_phone"] = customer_phone
    enquiry["enquiry_type"] = enquiry_type
    enquiry["priority"] = priority
    enquiry["status"] = status
    enquiry["assigned_to"] = assigned_to
    enquiry["enquiry_source"] = enquiry_source
    enquiry["estimated_value"] = estimated_value
    enquiry["follow_up_date"] = follow_up_date
    enquiry["enquiry_details"] = enquiry_details
    enquiry["next_action"] = next_action
    enquiry["created_at"] = datetime.now().strftime(TIMESTAMP_FORMAT)

    saved_successfully = save_enquiries(enquiries)

    if saved_successfully:
        message = "Enquiry updated successfully."
        message_type = "success"
    else:
        message = "Could not save the enquiry. Please try again."
        message_type = "error"

    notes = enquiry.get("notes", [])
    notes = list(reversed(notes))

    return render_template(
        "enquiry.html",
        enquiry=enquiry,
        approved_enquiry_types=APPROVED_ENQUIRY_TYPES,
        approved_statuses=APPROVED_STATUSES,
        approved_priorities=APPROVED_PRIORITIES,
        approved_sources=APPROVED_SOURCES,
        notes=notes,
        message=message,
        message_type=message_type
    )


@app.route("/close-enquiry/<reference_number>", methods=["POST"])
def close_enquiry(reference_number):
    enquiries = load_enquiries()
    enquiry = find_enquiry(enquiries, reference_number)

    if enquiry is None:
        return redirect(url_for("index"))

    enquiry["status"] = "Closed"
    enquiry["created_at"] = datetime.now().strftime(TIMESTAMP_FORMAT)

    saved_successfully = save_enquiries(enquiries)

    if saved_successfully:
        message = f"Enquiry {reference_number} closed successfully."
        message_type = "success"
    else:
        message = "Could not close the enquiry. Please try again."
        message_type = "error"

    enquiries = load_enquiries()
    dashboard_summary = create_dashboard_summary(enquiries)

    search_text = request.args.get("search-text", "").strip().lower()
    search_field = request.args.get("search-field", "").strip()
    status_filter = request.args.get("status-filter", "").strip()
    priority_filter = request.args.get("priority-filter", "").strip()
    overdue_only = request.args.get("overdue-only", "").strip()
    assigned_to_filter = request.args.get("assigned-to-filter", "").strip()
    source_filter = request.args.get("source-filter", "").strip()
    sort_by_follow_up = request.args.get("sort-by-follow-up", "").strip()

    filtered_enquiries = filter_enquiries(
        enquiries,
        search_text,
        search_field,
        status_filter,
        priority_filter,
        overdue_only == "yes",
        assigned_to_filter,
        source_filter
    )

    if sort_by_follow_up == "yes":
        filtered_enquiries = sort_enquiries_by_follow_up_date(
            filtered_enquiries
        )

    assigned_names = []

    for enquiry in enquiries:
        assigned_to_value = enquiry.get("assigned_to", "").strip()

        if assigned_to_value and assigned_to_value not in assigned_names:
            assigned_names.append(assigned_to_value)

    assigned_names.sort()

    return render_template(
        "index.html",
        enquiries=filtered_enquiries,
        total_enquiries=len(enquiries),
        dashboard_summary=dashboard_summary,
        approved_enquiry_types=APPROVED_ENQUIRY_TYPES,
        approved_priorities=APPROVED_PRIORITIES,
        approved_statuses=APPROVED_STATUSES,
        approved_sources=APPROVED_SOURCES,
        assigned_names=assigned_names,
        search_text=search_text,
        search_field=search_field,
        status_filter=status_filter,
        priority_filter=priority_filter,
        overdue_only=overdue_only,
        assigned_to_filter=assigned_to_filter,
        source_filter=source_filter,
        sort_by_follow_up=sort_by_follow_up,
        message=message,
        message_type=message_type
    )


@app.route("/reopen-enquiry/<reference_number>", methods=["POST"])
def reopen_enquiry(reference_number):
    enquiries = load_enquiries()
    enquiry = find_enquiry(enquiries, reference_number)

    if enquiry is None:
        return redirect(url_for("index"))

    enquiry["status"] = "In progress"
    enquiry["created_at"] = datetime.now().strftime(TIMESTAMP_FORMAT)

    saved_successfully = save_enquiries(enquiries)

    if saved_successfully:
        message = f"Enquiry {reference_number} reopened successfully."
        message_type = "success"
    else:
        message = "Could not reopen the enquiry. Please try again."
        message_type = "error"

    enquiries = load_enquiries()
    dashboard_summary = create_dashboard_summary(enquiries)

    search_text = request.args.get("search-text", "").strip().lower()
    search_field = request.args.get("search-field", "").strip()
    status_filter = request.args.get("status-filter", "").strip()
    priority_filter = request.args.get("priority-filter", "").strip()
    overdue_only = request.args.get("overdue-only", "").strip()
    assigned_to_filter = request.args.get("assigned-to-filter", "").strip()
    source_filter = request.args.get("source-filter", "").strip()
    sort_by_follow_up = request.args.get("sort-by-follow-up", "").strip()

    filtered_enquiries = filter_enquiries(
        enquiries,
        search_text,
        search_field,
        status_filter,
        priority_filter,
        overdue_only == "yes",
        assigned_to_filter,
        source_filter
    )

    if sort_by_follow_up == "yes":
        filtered_enquiries = sort_enquiries_by_follow_up_date(
            filtered_enquiries
        )

    assigned_names = []

    for enquiry in enquiries:
        assigned_to_value = enquiry.get("assigned_to", "").strip()

        if assigned_to_value and assigned_to_value not in assigned_names:
            assigned_names.append(assigned_to_value)

    assigned_names.sort()

    return render_template(
        "index.html",
        enquiries=filtered_enquiries,
        total_enquiries=len(enquiries),
        dashboard_summary=dashboard_summary,
        approved_enquiry_types=APPROVED_ENQUIRY_TYPES,
        approved_priorities=APPROVED_PRIORITIES,
        approved_statuses=APPROVED_STATUSES,
        approved_sources=APPROVED_SOURCES,
        assigned_names=assigned_names,
        search_text=search_text,
        search_field=search_field,
        status_filter=status_filter,
        priority_filter=priority_filter,
        overdue_only=overdue_only,
        assigned_to_filter=assigned_to_filter,
        source_filter=source_filter,
        sort_by_follow_up=sort_by_follow_up,
        message=message,
        message_type=message_type
    )


@app.route("/add-note/<reference_number>", methods=["POST"])
def add_note(reference_number):
    enquiries = load_enquiries()
    enquiry = find_enquiry(enquiries, reference_number)

    if enquiry is None:
        return render_template(
            "enquiry.html",
            enquiry=None,
            approved_enquiry_types=APPROVED_ENQUIRY_TYPES,
            approved_statuses=APPROVED_STATUSES,
            approved_priorities=APPROVED_PRIORITIES,
            approved_sources=APPROVED_SOURCES,
            notes=[],
            message="No enquiry found with that reference number.",
            message_type="error"
        )

    note_text = request.form.get("note-text", "").strip()

    if note_text == "":
        notes = enquiry.get("notes", [])
        notes = list(reversed(notes))

        return render_template(
            "enquiry.html",
            enquiry=enquiry,
            approved_enquiry_types=APPROVED_ENQUIRY_TYPES,
            approved_statuses=APPROVED_STATUSES,
            approved_priorities=APPROVED_PRIORITIES,
            approved_sources=APPROVED_SOURCES,
            notes=notes,
            message="Note cannot be empty.",
            message_type="error"
        )

    if "notes" not in enquiry:
        enquiry["notes"] = []

    note = {
        "note_text": note_text,
        "created_at": datetime.now().strftime(TIMESTAMP_FORMAT)
    }

    enquiry["notes"].append(note)

    saved_successfully = save_enquiries(enquiries)

    if saved_successfully:
        message = "Note added successfully."
        message_type = "success"
    else:
        message = "Could not save the note. Please try again."
        message_type = "error"

    notes = enquiry.get("notes", [])
    notes = list(reversed(notes))

    return render_template(
        "enquiry.html",
        enquiry=enquiry,
        approved_enquiry_types=APPROVED_ENQUIRY_TYPES,
        approved_statuses=APPROVED_STATUSES,
        approved_priorities=APPROVED_PRIORITIES,
        approved_sources=APPROVED_SOURCES,
        notes=notes,
        message=message,
        message_type=message_type
    )


@app.route("/delete-enquiry/<reference_number>", methods=["POST"])
def delete_enquiry(reference_number):
    enquiries = load_enquiries()
    enquiry = find_enquiry(enquiries, reference_number)

    if enquiry is None:
        return redirect(url_for("index"))

    updated_enquiries = []

    for existing_enquiry in enquiries:
        if existing_enquiry["reference_number"] != reference_number:
            updated_enquiries.append(existing_enquiry)

    saved_successfully = save_enquiries(updated_enquiries)

    if saved_successfully:
        message = f"Enquiry {reference_number} deleted successfully."
        message_type = "success"
    else:
        message = "Could not delete the enquiry. Please try again."
        message_type = "error"

    enquiries = load_enquiries()
    dashboard_summary = create_dashboard_summary(enquiries)

    search_text = request.args.get("search-text", "").strip().lower()
    search_field = request.args.get("search-field", "").strip()
    status_filter = request.args.get("status-filter", "").strip()
    priority_filter = request.args.get("priority-filter", "").strip()
    overdue_only = request.args.get("overdue-only", "").strip()
    assigned_to_filter = request.args.get("assigned-to-filter", "").strip()
    source_filter = request.args.get("source-filter", "").strip()
    sort_by_follow_up = request.args.get("sort-by-follow-up", "").strip()

    filtered_enquiries = filter_enquiries(
        enquiries,
        search_text,
        search_field,
        status_filter,
        priority_filter,
        overdue_only == "yes",
        assigned_to_filter,
        source_filter
    )

    if sort_by_follow_up == "yes":
        filtered_enquiries = sort_enquiries_by_follow_up_date(
            filtered_enquiries
        )

    assigned_names = []

    for enquiry in enquiries:
        assigned_to_value = enquiry.get("assigned_to", "").strip()

        if assigned_to_value and assigned_to_value not in assigned_names:
            assigned_names.append(assigned_to_value)

    assigned_names.sort()

    return render_template(
        "index.html",
        enquiries=filtered_enquiries,
        total_enquiries=len(enquiries),
        dashboard_summary=dashboard_summary,
        approved_enquiry_types=APPROVED_ENQUIRY_TYPES,
        approved_priorities=APPROVED_PRIORITIES,
        approved_statuses=APPROVED_STATUSES,
        approved_sources=APPROVED_SOURCES,
        assigned_names=assigned_names,
        search_text=search_text,
        search_field=search_field,
        status_filter=status_filter,
        priority_filter=priority_filter,
        overdue_only=overdue_only,
        assigned_to_filter=assigned_to_filter,
        source_filter=source_filter,
        sort_by_follow_up=sort_by_follow_up,
        message=message,
        message_type=message_type
    )


@app.route("/export-enquiries")
def export_enquiries():
    enquiries = load_enquiries()

    csv_content = create_csv_file(enquiries)

    return Response(
        csv_content,
        mimetype="text/csv",
        headers={
            "Content-Disposition": "attachment; filename=enquiry_register.csv"
        }
    )


if __name__ == "__main__":
    app.run(debug=True, port=5001)