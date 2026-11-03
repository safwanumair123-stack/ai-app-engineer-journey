# Day 22 — Python basics: enquiry greeting

print("Welcome to the enquiry greeting practice app.")

customer_name = input("Enter the customer name: ")
clean_name = customer_name.strip()

if clean_name == "":
    print("Customer name is required.")
else:
    enquiry_type = input("Enter the enquiry type: ")
    clean_enquiry_type = enquiry_type.strip()

    if clean_enquiry_type == "":
        print("Enquiry type is required.")
    else:
        print("")
        print("Enquiry received")
        print(f"Customer: {clean_name}")
        print(f"Enquiry type: {clean_enquiry_type}")
        print(f"Hello {clean_name}, thank you for your {clean_enquiry_type.lower()} enquiry.")