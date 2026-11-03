# Day 24 — Python dictionaries and enquiry records

import random

approved_enquiry_types = [
    "General enquiry",
    "Quotation",
    "Support",
    "Partnership"
]

priority_levels = [
    "Low",
    "Medium",
    "High"
]

enquiry_statuses = [
    "New",
    "In review",
    "Approved",
    "Closed"
]

print("Welcome to the enquiry record practice app.")
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
else:
    enquiry_type = input("Enter an enquiry type: ")
    clean_enquiry_type = enquiry_type.strip()

    if clean_enquiry_type == "":
        print("Enquiry type is required.")
    else:
        matching_type = None

        for approved_type in approved_enquiry_types:
            if clean_enquiry_type.lower() == approved_type.lower():
                matching_type = approved_type
                break

        if matching_type is None:
            print("Invalid enquiry type.")
            print("Please choose one of the approved enquiry types.")
        else:
            reference_number = f"ENQ-{random.randint(1000, 9999)}"

            enquiry = {
                "reference_number": reference_number,
                "customer_name": clean_name,
                "enquiry_type": matching_type,
                "priority": "Medium",
                "status": "New"
            }

            print("")
            print("Enquiry record created")
            print("")
            print(f"Reference number: {enquiry['reference_number']}")
            print(f"Customer: {enquiry['customer_name']}")
            print(f"Enquiry type: {enquiry['enquiry_type']}")
            print(f"Priority: {enquiry['priority']}")
            print(f"Status: {enquiry['status']}")
            print("")

            enquiry["status"] = "In review"

            print("Status updated")
            print(f"Reference number: {enquiry['reference_number']}")
            print(f"Customer: {enquiry['customer_name']}")
            print(f"Enquiry type: {enquiry['enquiry_type']}")
            print(f"Priority: {enquiry['priority']}")
            print(f"Status: {enquiry['status']}")