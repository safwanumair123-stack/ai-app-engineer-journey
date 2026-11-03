# Day 22 — Python Basics: Enquiry Greeting

## Completed
- Created the Day 22 Python project folder.
- Created enquiry_greeting.py.
- Used print() to display messages in the terminal.
- Used input() to collect customer name and enquiry type.
- Used variables to store user input.
- Used .strip() to remove extra spaces from input.
- Used if, elif, and else to validate input.
- Used f-strings to display personalised output.
- Fixed the validation order so a missing customer name is checked
  before asking for the enquiry type.
- Tested valid input, missing name, missing enquiry type, and
  extra spaces.

## Checks passed
- Valid input displays a structured enquiry confirmation.
- Missing customer name immediately shows:
  "Customer name is required."
- Missing enquiry type shows:
  "Enquiry type is required."
- Extra spaces are removed before displaying the result.
- The script does not ask for the enquiry type if the customer
  name is missing.

## Key learning
Python programs can collect input, validate it, and produce a
useful response.

input() pauses the program and waits for the user to type a value.

.strip() removes unnecessary spaces from the beginning and end of
a text value.

Validation should happen as close as possible to the point where
the user provides the input.

This is the same principle used in web forms: check each field at
the right time and give clear feedback.