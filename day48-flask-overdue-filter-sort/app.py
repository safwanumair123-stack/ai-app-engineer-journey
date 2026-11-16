# Day 48 — Add overdue filter and follow-up date sorting

import csv
import io
import json
import os
import random
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

TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"
DATE_FORMAT = "%Y-%m-%d"

CSV_HEADERS = [
    "Reference number",
    "Customer name",
    "Enquiry type",
    "Priority",
    "Status",
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

    for enquiry in enquiries:
        if is_overdue(enquiry):
            overdue_count = overdue_count + 1

    return {
        "total_enquiries": len(enquiries),
        "overdue_follow_ups": overdue_count,
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
    overdue_only
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
            "Enquiry type": enquiry["enquiry_type"],
            "Priority": enquiry["priority"],
            "Status": enquiry["status"],
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
    sort_by_follow_up = request.args.get("sort-by-follow-up", "").strip()

    filtered_enquiries = filter_enquiries(
        enquiries,
        search_text,
        search_field,
        status_filter,
        priority_filter,
        overdue_only == "yes"
    )

    if sort_by_follow_up == "yes":
        filtered_enquiries = sort_enquiries_by_follow_up_date(
            filtered_enquiries
        )

    return render_template(
        "index.html",
        enquiries=filtered_enquiries,
        total_enquiries=len(enquiries),
        dashboard_summary=dashboard_summary,
        approved_enquiry_types=APPROVED_ENQUIRY_TYPES,
        approved_priorities=APPROVED_PRIORITIES,
        approved_statuses=APPROVED_STATUSES,
        search_text=search_text,
        search_field=search_field,
        status_filter=status_filter,
        priority_filter=priority_filter,
        overdue_only=overdue_only,
        sort_by_follow_up=sort_by_follow_up,
        message=None,
        message_type=None
    )


@app.route("/create-enquiry", methods=["POST"])
def create_enquiry():
    customer_name = request.form.get("customer-name", "").strip()
    enquiry_type = request.form.get("enquiry-type", "").strip()
    priority = request.form.get("priority", "").strip()
    follow_up_date = request.form.get("follow-up-date", "").strip()
    enquiry_details = request.form.get("enquiry-details", "").strip()
    next_action = request.form.get("next-action", "").strip()

    errors = []

    if customer_name == "":
        errors.append("Customer name is required.")

    if enquiry_type not in APPROVED_ENQUIRY_TYPES:
        errors.append("Please select a valid enquiry type.")

    if priority not in APPROVED_PRIORITIES:
        errors.append("Please select a valid priority.")

    if follow_up_date:
        try:
            datetime.strptime(
                follow_up_date,
                DATE_FORMAT
            )

        except ValueError:
            errors.append("Please enter a valid follow-up date.")

    if errors:
        enquiries = load_enquiries()
        dashboard_summary = create_dashboard_summary(enquiries)

        return render_template(
            "index.html",
            enquiries=enquiries,
            total_enquiries=len(enquiries),
            dashboard_summary=dashboard_summary,
            approved_enquiry_types=APPROVED_ENQUIRY_TYPES,
            approved_priorities=APPROVED_PRIORITIES,
            approved_statuses=APPROVED_STATUSES,
            search_text="",
            search_field="",
            status_filter="",
            priority_filter="",
            overdue_only="",
            sort_by_follow_up="",
            message=errors,
            message_type="error"
        )

    created_at = datetime.now().strftime(TIMESTAMP_FORMAT)
    reference_number = f"ENQ-{random.randint(1000, 9999)}"

    enquiry = {
        "reference_number": reference_number,
        "customer_name": customer_name,
        "enquiry_type": enquiry_type,
        "priority": priority,
        "status": "New",
        "created_at": created_at,
        "follow_up_date": follow_up_date,
        "enquiry_details": enquiry_details,
        "next_action": next_action,
        "notes": []
    }

    enquiries = load_enquiries()
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

    return render_template(
        "index.html",
        enquiries=enquiries,
        total_enquiries=len(enquiries),
        dashboard_summary=dashboard_summary,
        approved_enquiry_types=APPROVED_ENQUIRY_TYPES,
        approved_priorities=APPROVED_PRIORITIES,
        approved_statuses=APPROVED_STATUSES,
        search_text="",
        search_field="",
        status_filter="",
        priority_filter="",
        overdue_only="",
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
            notes=[],
            message="No enquiry found with that reference number.",
            message_type="error"
        )

    customer_name = request.form.get("customer-name", "").strip()
    enquiry_type = request.form.get("enquiry-type", "").strip()
    priority = request.form.get("priority", "").strip()
    status = request.form.get("status", "").strip()
    follow_up_date = request.form.get("follow-up-date", "").strip()
    enquiry_details = request.form.get("enquiry-details", "").strip()
    next_action = request.form.get("next-action", "").strip()

    errors = []

    if customer_name == "":
        errors.append("Customer name is required.")

    if enquiry_type not in APPROVED_ENQUIRY_TYPES:
        errors.append("Please select a valid enquiry type.")

    if priority not in APPROVED_PRIORITIES:
        errors.append("Please select a valid priority.")

    if status not in APPROVED_STATUSES:
        errors.append("Please select a valid status.")

    if follow_up_date:
        try:
            datetime.strptime(
                follow_up_date,
                DATE_FORMAT
            )

        except ValueError:
            errors.append("Please enter a valid follow-up date.")

    if errors:
        notes = enquiry.get("notes", [])
        notes = list(reversed(notes))

        return render_template(
            "enquiry.html",
            enquiry=enquiry,
            approved_enquiry_types=APPROVED_ENQUIRY_TYPES,
            approved_statuses=APPROVED_STATUSES,
            approved_priorities=APPROVED_PRIORITIES,
            notes=notes,
            message=errors,
            message_type="error"
        )

    enquiry["customer_name"] = customer_name
    enquiry["enquiry_type"] = enquiry_type
    enquiry["priority"] = priority
    enquiry["status"] = status
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
        notes=notes,
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
    sort_by_follow_up = request.args.get("sort-by-follow-up", "").strip()

    filtered_enquiries = filter_enquiries(
        enquiries,
        search_text,
        search_field,
        status_filter,
        priority_filter,
        overdue_only == "yes"
    )

    if sort_by_follow_up == "yes":
        filtered_enquiries = sort_enquiries_by_follow_up_date(
            filtered_enquiries
        )

    return render_template(
        "index.html",
        enquiries=filtered_enquiries,
        total_enquiries=len(enquiries),
        dashboard_summary=dashboard_summary,
        approved_enquiry_types=APPROVED_ENQUIRY_TYPES,
        approved_priorities=APPROVED_PRIORITIES,
        approved_statuses=APPROVED_STATUSES,
        search_text=search_text,
        search_field=search_field,
        status_filter=status_filter,
        priority_filter=priority_filter,
        overdue_only=overdue_only,
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