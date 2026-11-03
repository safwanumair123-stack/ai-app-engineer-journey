# Day 23 — Python Lists and Enquiry Categories

## Completed
- Created a Day 23 copy of the Day 22 Python project.
- Renamed the Python file to enquiry_categories.py.
- Added a list of approved enquiry types.
- Displayed the approved enquiry types to the user.
- Used a for loop to check the entered enquiry type.
- Made the comparison case-insensitive using .lower().
- Returned the correctly formatted approved enquiry type.
- Added a clear invalid enquiry type message.
- Kept validation for missing customer name and missing enquiry type.
- Tested valid input, different capitalisation, invalid category,
  missing name, and missing enquiry type.

## Checks passed
- Valid enquiry types are accepted.
- QUOTATION, Quotation, and quotation all match the approved
  Quotation category.
- Invalid enquiry types are rejected with a clear message.
- Missing customer name stops the script before asking for the
  enquiry type.
- Missing enquiry type shows a clear error message.

## Key learning
A list stores multiple related values in one variable.

A for loop can check each item in a list.

Case-insensitive comparison makes input validation more forgiving
without accepting unapproved categories.

Using approved categories keeps business data consistent, which is
important for reporting, automation, and traceability.