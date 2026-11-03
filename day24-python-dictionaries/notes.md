# Day 24 — Python Dictionaries and Enquiry Records

## Completed
- Created a Day 24 copy of the Day 23 Python project.
- Renamed the Python file to enquiry_record.py.
- Reviewed approved enquiry types from Day 23.
- Added priority levels and enquiry statuses.
- Generated a simple enquiry reference number.
- Created an enquiry dictionary to store related details together.
- Stored reference number, customer name, enquiry type, priority,
  and status in one record.
- Displayed the complete enquiry record.
- Updated the enquiry status from New to In review.
- Displayed the updated enquiry record.
- Tested valid input, different capitalisation, invalid category,
  missing name, and missing enquiry type.

## Checks passed
- Valid enquiry creates a structured enquiry record.
- A reference number is generated for each enquiry.
- The enquiry type is displayed in its approved format.
- The initial status is New.
- The status updates to In review.
- Invalid enquiry types are rejected with a clear message.
- Missing customer name stops the script before asking for the
  enquiry type.
- Missing enquiry type shows a clear error message.

## Key learning
A dictionary stores related information as key-value pairs.

Dictionaries are useful when several values belong to one record,
such as a customer enquiry, order, service request, or invoice.

A reference number makes a record easier to identify and track.

Updating a dictionary value shows how an application can move a
record through a workflow, such as New to In review.

This is an early foundation for traceable business applications:
capture input, store it in a structured record, and record status
changes.