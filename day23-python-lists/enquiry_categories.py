# Day 23 — Python lists and enquiry categories

approved_enquiry_types = [
    "General enquiry",
    "Quotation",
    "Support",
    "Partnership"
]

print("Welcome to the enquiry category practice app.")
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
            print("")
            print("Enquiry received")
            print(f"Customer: {clean_name}")
            print(f"Enquiry type: {matching_type}")
            print(
                f"Hello {clean_name}, thank you for your "
                f"{matching_type.lower()} enquiry."
            )