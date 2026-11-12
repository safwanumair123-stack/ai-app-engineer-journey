# Day 31 — Improve enquiry app using functions

import csv
import os
import random
from datetime import datetime

csv_file = "enquiry_register.csv"

csv_headers = [
    "reference_number",
    "customer_name",
    "enquiry_type",
    "priority",
    "status",
    "created_at"
]

approved_enquiry_types = [
    "General enquiry",
    "Quotation",
    "Support",
    "Partnership"
]

approved_statuses = [
    "New",
    "In progress",
    "Closed"
]

approved_priorities = [
    "Low",
    "Medium",
    "High"
]


def show_main_menu():
    print("Welcome to the enquiry functions practice app.")
    print("")
    print("Choose an option:")
    print("1. Create a new enquiry")
    print("2. Update an enquiry status")
    print("3. Search enquiries")
    print("4. Show summary report")
    print("")

    choice = input("Enter 1, 2, 3, or 4: ")
    return choice.strip()


def get_matching_option(user_input, approved_options):
    clean_input = user_input.strip().lower()

    for approved_option in approved_options:
        if clean_input == approved_option.lower():
            return approved_option

    return None


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

    customer_name = input("Enter the customer name: ")
    clean_name = customer_name.strip()

    if clean_name == "":
        print("Customer name is required.")
        return

    enquiry_type = input("Enter an enquiry type: ")
    matching_type = get_matching_option(
        enquiry_type,
        approved_enquiry_types
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

    priority_choice = input("Enter 1, 2, or 3: ")
    clean_priority_choice = priority_choice.strip()

    if clean_priority_choice == "1":
        priority = "Low"
    elif clean_priority_choice == "2":
        priority = "Medium"
    elif clean_priority_choice == "3":
        priority = "High"
    else:
        print("Invalid priority choice.")
        print("Please enter 1, 2, or 3.")
        return

    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    reference_number = f"ENQ-{random.randint(1000, 9999)}"

    enquiry = {
        "reference_number": reference_number,
        "customer_name": clean_name,
        "enquiry_type": matching_type,
        "priority": priority,
        "status": "New",
        "created_at": created_at
    }

    file_exists = os.path.exists(csv_file)

    with open(csv_file, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=csv_headers)

        if not file_exists:
            writer.writeheader()

        writer.writerow(enquiry)

    print("")
    print("Enquiry record created and saved")
    print("")
    print(f"Reference number: {enquiry['reference_number']}")
    print(f"Customer: {enquiry['customer_name']}")
    print(f"Enquiry type: {enquiry['enquiry_type']}")
    print(f"Priority: {enquiry['priority']}")
    print(f"Status: {enquiry['status']}")
    print(f"Created at: {enquiry['created_at']}")
    print("")
    print(f"Saved to: {csv_file}")


def load_enquiries():
    if not os.path.exists(csv_file):
        return None

    with open(csv_file, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def find_enquiry(enquiries, reference_number):
    clean_reference = reference_number.strip()

    for enquiry in enquiries:
        if enquiry["reference_number"] == clean_reference:
            return enquiry

    return None


def update_enquiry_status():
    print("")
    print("Update an enquiry status")
    print("")

    enquiries = load_enquiries()

    if enquiries is None:
        print("No enquiry register found.")
        print("Create an enquiry first by choosing option 1.")
        return

    reference_number = input("Enter the reference number: ")

    if reference_number.strip() == "":
        print("Reference number is required.")
        return

    matching_enquiry = find_enquiry(enquiries, reference_number)

    if matching_enquiry is None:
        print("No enquiry found with that reference number.")
        return

    print("")
    print("Enquiry found:")
    print(f"Reference number: {matching_enquiry['reference_number']}")
    print(f"Customer: {matching_enquiry['customer_name']}")
    print(f"Enquiry type: {matching_enquiry['enquiry_type']}")
    print(f"Current priority: {matching_enquiry['priority']}")
    print(f"Current status: {matching_enquiry['status']}")
    print("")
    print("Approved statuses:")
    print("1. New")
    print("2. In progress")
    print("3. Closed")
    print("")

    status_choice = input("Enter 1, 2, or 3: ")
    clean_status_choice = status_choice.strip()

    if clean_status_choice == "1":
        new_status = "New"
    elif clean_status_choice == "2":
        new_status = "In progress"
    elif clean_status_choice == "3":
        new_status = "Closed"
    else:
        print("Invalid status choice.")
        return

    matching_enquiry["status"] = new_status
    updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    matching_enquiry["created_at"] = updated_at

    with open(csv_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=csv_headers)
        writer.writeheader()

        for enquiry in enquiries:
            writer.writerow(enquiry)

    print("")
    print("Enquiry status updated and saved")
    print("")
    print(f"Reference number: {matching_enquiry['reference_number']}")
    print(f"Customer: {matching_enquiry['customer_name']}")
    print(f"New status: {matching_enquiry['status']}")
    print(f"Updated at: {matching_enquiry['created_at']}")


def search_enquiries():
    print("")
    print("Search enquiries")
    print("")
    print("Choose a search field:")
    print("1. Customer name")
    print("2. Enquiry type")
    print("")

    search_choice = input("Enter 1 or 2: ")
    clean_search_choice = search_choice.strip()

    if clean_search_choice not in ["1", "2"]:
        print("Invalid search choice.")
        print("Please enter 1 or 2.")
        return

    search_text = input("Enter the text to search for: ")
    clean_search_text = search_text.strip().lower()

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
        if clean_search_choice == "1":
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
        print(f"Reference number: {enquiry['reference_number']}")
        print(f"Customer: {enquiry['customer_name']}")
        print(f"Enquiry type: {enquiry['enquiry_type']}")
        print(f"Priority: {enquiry['priority']}")
        print(f"Status: {enquiry['status']}")
        print(f"Created at: {enquiry['created_at']}")
        print("-" * 40)


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

    total_enquiries = len(enquiries)

    status_counts = {
        "New": 0,
        "In progress": 0,
        "Closed": 0
    }

    type_counts = {
        "General enquiry": 0,
        "Quotation": 0,
        "Support": 0,
        "Partnership": 0
    }

    priority_counts = {
        "Low": 0,
        "Medium": 0,
        "High": 0
    }

    for enquiry in enquiries:
        status = enquiry["status"]
        enquiry_type = enquiry["enquiry_type"]
        priority = enquiry["priority"]

        if status in status_counts:
            status_counts[status] = status_counts[status] + 1

        if enquiry_type in type_counts:
            type_counts[enquiry_type] = type_counts[enquiry_type] + 1

        if priority in priority_counts:
            priority_counts[priority] = priority_counts[priority] + 1

    print(f"Total enquiries: {total_enquiries}")
    print("")
    print("Enquiries by status:")
    print(f"New: {status_counts['New']}")
    print(f"In progress: {status_counts['In progress']}")
    print(f"Closed: {status_counts['Closed']}")
    print("")
    print("Enquiries by type:")
    print(f"General enquiry: {type_counts['General enquiry']}")
    print(f"Quotation: {type_counts['Quotation']}")
    print(f"Support: {type_counts['Support']}")
    print(f"Partnership: {type_counts['Partnership']}")
    print("")
    print("Enquiries by priority:")
    print(f"Low: {priority_counts['Low']}")
    print(f"Medium: {priority_counts['Medium']}")
    print(f"High: {priority_counts['High']}")


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