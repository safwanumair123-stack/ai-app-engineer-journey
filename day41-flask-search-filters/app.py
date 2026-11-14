# Day 41 — Add search and filters to the Enquiry Tracker

import json
import os
import random
from datetime import datetime

from flask import Flask, render_template, request, redirect, url_for

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


def filter_enquiries(
    enquiries,
    search_text,
    search_field,
    status_filter,
    priority_filter
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

    return filtered_enquiries


@app.route("/")
def index():
    enquiries = load_enquiries()

    search_text = request.args.get("search-text", "").strip().lower()
    search_field = request.args.get("search-field", "").strip()
    status_filter = request.args.get("status-filter", "").strip()
    priority_filter = request.args.get("priority-filter", "").strip()

    filtered_enquiries = filter_enquiries(
        enquiries,
        search_text,
        search_field,
        status_filter,
        priority_filter
    )

    return render_template(
        "index.html",
        enquiries=filtered_enquiries,
        total_enquiries=len(enquiries),
        approved_enquiry_types=APPROVED_ENQUIRY_TYPES,
        approved_priorities=APPROVED_PRIORITIES,
        approved_statuses=APPROVED_STATUSES,
        search_text=search_text,
        search_field=search_field,
        status_filter=status_filter,
        priority_filter=priority_filter,
        message=None,
        message_type=None
    )


@app.route("/create-enquiry", methods=["POST"])
def create_enquiry():
    customer_name = request.form.get("customer-name", "").strip()
    enquiry_type = request.form.get("enquiry-type", "").strip()
    priority = request.form.get("priority", "").strip()
    enquiry_details = request.form.get("enquiry-details", "").strip()
    next_action = request.form.get("next-action", "").strip()

    errors = []

    if customer_name == "":
        errors.append("Customer name is required.")

    if enquiry_type not in APPROVED_ENQUIRY_TYPES:
        errors.append("Please select a valid enquiry type.")

    if priority not in APPROVED_PRIORITIES:
        errors.append("Please select a valid priority.")

    if errors:
        enquiries = load_enquiries()

        return render_template(
            "index.html",
            enquiries=enquiries,
            total_enquiries=len(enquiries),
            approved_enquiry_types=APPROVED_ENQUIRY_TYPES,
            approved_priorities=APPROVED_PRIORITIES,
            approved_statuses=APPROVED_STATUSES,
            search_text="",
            search_field="",
            status_filter="",
            priority_filter="",
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
        "enquiry_details": enquiry_details,
        "next_action": next_action
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

    return render_template(
        "index.html",
        enquiries=enquiries,
        total_enquiries=len(enquiries),
        approved_enquiry_types=APPROVED_ENQUIRY_TYPES,
        approved_priorities=APPROVED_PRIORITIES,
        approved_statuses=APPROVED_STATUSES,
        search_text="",
        search_field="",
        status_filter="",
        priority_filter="",
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
            approved_statuses=APPROVED_STATUSES,
            approved_priorities=APPROVED_PRIORITIES,
            message="No enquiry found with that reference number.",
            message_type="error"
        )

    return render_template(
        "enquiry.html",
        enquiry=enquiry,
        approved_statuses=APPROVED_STATUSES,
        approved_priorities=APPROVED_PRIORITIES,
        message=None,
        message_type=None
    )


@app.route("/update-enquiry/<reference_number>", methods=["POST"])
def update_enquiry(reference_number):
    enquiries = load_enquiries()
    enquiry = find_enquiry(enquiries, reference_number)

    if enquiry is None:
        return render_template(
            "enquiry.html",
            enquiry=None,
            approved_statuses=APPROVED_STATUSES,
            approved_priorities=APPROVED_PRIORITIES,
            message="No enquiry found with that reference number.",
            message_type="error"
        )

    new_status = request.form.get("status", "").strip()
    new_priority = request.form.get("priority", "").strip()
    new_next_action = request.form.get("next-action", "").strip()

    errors = []

    if new_status not in APPROVED_STATUSES:
        errors.append("Please select a valid status.")

    if new_priority not in APPROVED_PRIORITIES:
        errors.append("Please select a valid priority.")

    if errors:
        return render_template(
            "enquiry.html",
            enquiry=enquiry,
            approved_statuses=APPROVED_STATUSES,
            approved_priorities=APPROVED_PRIORITIES,
            message=errors,
            message_type="error"
        )

    enquiry["status"] = new_status
    enquiry["priority"] = new_priority
    enquiry["next_action"] = new_next_action
    enquiry["created_at"] = datetime.now().strftime(TIMESTAMP_FORMAT)

    saved_successfully = save_enquiries(enquiries)

    if saved_successfully:
        message = "Enquiry updated successfully."
        message_type = "success"
    else:
        message = "Could not save the enquiry. Please try again."
        message_type = "error"

    return render_template(
        "enquiry.html",
        enquiry=enquiry,
        approved_statuses=APPROVED_STATUSES,
        approved_priorities=APPROVED_PRIORITIES,
        message=message,
        message_type=message_type
    )


if __name__ == "__main__":
    app.run(debug=True)