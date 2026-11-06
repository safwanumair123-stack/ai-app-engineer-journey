# Day 26 — Add Timestamps to Enquiry Records

## What I learned

- How to import Python’s datetime module.
- How to capture the current date and time.
- How to format timestamps consistently.
- How to add a timestamp to a CSV record.
- How timestamps improve traceability in business workflows.

## What the script does

The script asks for a customer name and enquiry type. It validates the enquiry type against approved categories and creates an enquiry record with a reference number, customer name, enquiry type, priority, status, and timestamp.

The script saves each record to enquiry_register.csv. The CSV file and header row are created on first use. Later records are appended, so earlier enquiry data is preserved.

## New skill

I learned to use datetime.now() to capture the current date and time and format it as YYYY-MM-DD HH:MM:SS.

## Testing

I tested five scenarios:

1. First enquiry created the CSV file and header row.
2. Second enquiry was appended without overwriting the first record.
3. Different capitalisation was converted to the approved enquiry type.
4. Invalid enquiry type was rejected and not saved.
5. Missing customer name was rejected and not saved.

All five tests passed.

## Why this matters

Timestamps make enquiry records more useful for follow-up, reporting, and auditing. They show not only what was submitted but also when it was submitted.