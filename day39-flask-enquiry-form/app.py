# Day 39 — Connect the enquiry form to Flask

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


@app.route("/")
def index():
    enquiries = load_enquiries()

    return render_template(
        "index.html",
        enquiries=enquiries,
        approved_enquiry_types=APPROVED_ENQUIRY_TYPES,
        approved_priorities=APPROVED_PRIORITIES,
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
            approved_enquiry_types=APPROVED_ENQUIRY_TYPES,
            approved_priorities=APPROVED_PRIORITIES,
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
        approved_enquiry_types=APPROVED_ENQUIRY_TYPES,
        approved_priorities=APPROVED_PRIORITIES,
        message=message,
        message_type=message_type
    )


if __name__ == "__main__":
    app.run(debug=True)