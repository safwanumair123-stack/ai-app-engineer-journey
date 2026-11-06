# Day 26 — Add timestamps to enquiry records

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

print("Welcome to the enquiry timestamp practice app.")
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
            created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            reference_number = f"ENQ-{random.randint(1000, 9999)}"

            enquiry = {
                "reference_number": reference_number,
                "customer_name": clean_name,
                "enquiry_type": matching_type,
                "priority": "Medium",
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