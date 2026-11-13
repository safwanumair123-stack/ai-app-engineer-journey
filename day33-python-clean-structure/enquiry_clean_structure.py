# Day 33 — Improve the structure of the enquiry app

import csv
import os
import random
from datetime import datetime

# Configuration

CSV_FILE = "enquiry_register.csv"

CSV_HEADERS = [
    "reference_number",
    "customer_name",
    "enquiry_type",
    "priority",
    "status",
    "created_at"
]

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


# User interaction

def show_main_menu():
    print("Welcome to the enquiry clean structure practice app.")
    print("")
    print("Choose an option:")
    print("1. Create a new enquiry")
    print("2. Update an enquiry status")
    print("3. Search enquiries")
    print("4. Show summary report")
    print("")

    choice = input("Enter 1, 2, 3, or 4: ")
    return choice.strip()


def get_user_input(prompt):
    user_input = input(prompt)
    return user_input.strip()


def display_enquiry(enquiry):
    print(f"Reference number: {enquiry['reference_number']}")
    print(f"Customer: {enquiry['customer_name']}")
    print(f"Enquiry type: {enquiry['enquiry_type']}")
    print(f"Priority: {enquiry['priority']}")
    print(f"Status: {enquiry['status']}")
    print(f"Created at: {enquiry['created_at']}")


# Data logic

def get_matching_option(user_input, approved_options):
    clean_input = user_input.strip().lower()

    for approved_option in approved_options:
        if clean_input == approved_option.lower():
            return approved_option

    return None


def load_enquiries():
    if not os.path.exists(CSV_FILE):
        return None

    try:
        with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return list(reader)

    except PermissionError:
        print("Could not read the enquiry register.")
        print("The file may be open in another program.")
        return None

    except UnicodeDecodeError:
        print("Could not read the enquiry register.")
        print("The file appears to have an encoding problem.")
        return None

    except OSError:
        print("Could not read the enquiry register.")
        print("There was a problem accessing the file.")
        return None


def save_enquiry(enquiry):
    try:
        file_exists = os.path.exists(CSV_FILE)

        with open(CSV_FILE, "a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=CSV_HEADERS)

            if not file_exists:
                writer.writeheader()

            writer.writerow(enquiry)

        return True

    except PermissionError:
        print("Could not save the enquiry.")
        print("The file may be open in another program.")
        print("Close the file and try again.")
        return False

    except OSError:
        print("Could not save the enquiry.")
        print("There was a problem accessing the file.")
        return False


def save_all_enquiries(enquiries):
    try:
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=CSV_HEADERS)
            writer.writeheader()

            for enquiry in enquiries:
                writer.writerow(enquiry)

        return True

    except PermissionError:
        print("Could not save the updated enquiry.")
        print("The file may be open in another program.")
        print("Close the file and try again.")
        return False

    except OSError:
        print("Could not save the updated enquiry.")
        print("There was a problem accessing the file.")
        return False


def find_enquiry(enquiries, reference_number):
    clean_reference = reference_number.strip()

    for enquiry in enquiries:
        if enquiry["reference_number"] == clean_reference:
            return enquiry

    return None


def create_enquiry_record(customer_name, enquiry_type, priority):
    created_at = datetime.now().strftime(TIMESTAMP_FORMAT)
    reference_number = f"ENQ-{random.randint(1000, 9999)}"

    return {
        "reference_number": reference_number,
        "customer_name": customer_name,
        "enquiry_type": enquiry_type,
        "priority": priority,
        "status": "New",
        "created_at": created_at
    }


# Main features

def create_enquiry():
    print("")
    print("Create a new enquiry")
    print("")
    print("Approved enquiry types:")
    print("1. General enquiry")
    print("2. Quotation")
    print("3. Support")
    print("4. Partnership")
    print("")

    customer_name = get_user_input("Enter the customer name: ")

    if customer_name == "":
        print("Customer name is required.")
        return

    enquiry_type = get_user_input("Enter an enquiry type: ")
    matching_type = get_matching_option(
        enquiry_type,
        APPROVED_ENQUIRY_TYPES
    )

    if matching_type is None:
        print("Invalid enquiry type.")
        print("Please choose one of the approved enquiry types.")
        return

    print("")
    print("Approved priorities:")
    print("1. Low")
    print("2. Medium")
    print("3. High")
    print("")

    priority_choice = get_user_input("Enter 1, 2, or 3: ")

    if priority_choice == "1":
        priority = "Low"
    elif priority_choice == "2":
        priority = "Medium"
    elif priority_choice == "3":
        priority = "High"
    else:
        print("Invalid priority choice.")
        print("Please enter 1, 2, or 3.")
        return

    enquiry = create_enquiry_record(
        customer_name,
        matching_type,
        priority
    )

    saved_successfully = save_enquiry(enquiry)

    if saved_successfully:
        print("")
        print("Enquiry record created and saved")
        print("")
        display_enquiry(enquiry)
        print("")
        print(f"Saved to: {CSV_FILE}")


def update_enquiry_status():
    print("")
    print("Update an enquiry status")
    print("")

    enquiries = load_enquiries()

    if enquiries is None:
        print("No enquiry register found.")
        print("Create an enquiry first by choosing option 1.")
        return

    reference_number = get_user_input("Enter the reference number: ")

    if reference_number == "":
        print("Reference number is required.")
        return

    matching_enquiry = find_enquiry(enquiries, reference_number)

    if matching_enquiry is None:
        print("No enquiry found with that reference number.")
        return

    print("")
    print("Enquiry found:")
    display_enquiry(matching_enquiry)
    print("")
    print("Approved statuses:")
    print("1. New")
    print("2. In progress")
    print("3. Closed")
    print("")

    status_choice = get_user_input("Enter 1, 2, or 3: ")

    if status_choice == "1":
        new_status = "New"
    elif status_choice == "2":
        new_status = "In progress"
    elif status_choice == "3":
        new_status = "Closed"
    else:
        print("Invalid status choice.")
        return

    matching_enquiry["status"] = new_status
    matching_enquiry["created_at"] = datetime.now().strftime(TIMESTAMP_FORMAT)

    saved_successfully = save_all_enquiries(enquiries)

    if saved_successfully:
        print("")
        print("Enquiry status updated and saved")
        print("")
        display_enquiry(matching_enquiry)


def search_enquiries():
    print("")
    print("Search enquiries")
    print("")
    print("Choose a search field:")
    print("1. Customer name")
    print("2. Enquiry type")
    print("")

    search_choice = get_user_input("Enter 1 or 2: ")

    if search_choice not in ["1", "2"]:
        print("Invalid search choice.")
        print("Please enter 1 or 2.")
        return

    search_text = get_user_input("Enter the text to search for: ")
    clean_search_text = search_text.lower()

    if clean_search_text == "":
        print("Search text is required.")
        return

    enquiries = load_enquiries()

    if enquiries is None:
        print("No enquiry register found.")
        print("Create an enquiry first by choosing option 1.")
        return

    matching_enquiries = []

    for enquiry in enquiries:
        if search_choice == "1":
            if clean_search_text in enquiry["customer_name"].lower():
                matching_enquiries.append(enquiry)
        else:
            if clean_search_text in enquiry["enquiry_type"].lower():
                matching_enquiries.append(enquiry)

    if len(matching_enquiries) == 0:
        print("No matching enquiries found.")
        return

    print("")
    print(f"{len(matching_enquiries)} matching enquiry record(s) found:")
    print("")

    for enquiry in matching_enquiries:
        display_enquiry(enquiry)
        print("-" * 40)


def count_records(enquiries, field_name, approved_options):
    counts = {}

    for approved_option in approved_options:
        counts[approved_option] = 0

    for enquiry in enquiries:
        value = enquiry[field_name]

        if value in counts:
            counts[value] = counts[value] + 1

    return counts


def show_summary_report():
    print("")
    print("Enquiry summary report")
    print("")

    enquiries = load_enquiries()

    if enquiries is None:
        print("No enquiry register found.")
        print("Create an enquiry first by choosing option 1.")
        return

    if len(enquiries) == 0:
        print("No enquiry records found.")
        return

    status_counts = count_records(
        enquiries,
        "status",
        APPROVED_STATUSES
    )

    type_counts = count_records(
        enquiries,
        "enquiry_type",
        APPROVED_ENQUIRY_TYPES
    )

    priority_counts = count_records(
        enquiries,
        "priority",
        APPROVED_PRIORITIES
    )

    print(f"Total enquiries: {len(enquiries)}")
    print("")
    print("Enquiries by status:")

    for status, count in status_counts.items():
        print(f"{status}: {count}")

    print("")
    print("Enquiries by type:")

    for enquiry_type, count in type_counts.items():
        print(f"{enquiry_type}: {count}")

    print("")
    print("Enquiries by priority:")

    for priority, count in priority_counts.items():
        print(f"{priority}: {count}")


# Application entry point

def main():
    choice = show_main_menu()

    if choice == "1":
        create_enquiry()
    elif choice == "2":
        update_enquiry_status()
    elif choice == "3":
        search_enquiries()
    elif choice == "4":
        show_summary_report()
    else:
        print("Invalid choice.")
        print("Please enter 1, 2, 3, or 4.")


main()