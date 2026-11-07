# Day 27 — Update Enquiry Status

## What I learned

- How to read records from a CSV file.
- How to find a record using its reference number.
- How to update a specific field in a record.
- How to rewrite a CSV file with updated data.
- How to preserve the rest of the register while changing one row.

## What the script does

The script gives the user two options: create a new enquiry or update an existing enquiry status.

When creating an enquiry, the script asks for a customer name and enquiry type. It validates the enquiry type, creates a reference number, captures the current timestamp, and saves the record to enquiry_register.csv.

When updating an enquiry, the script asks for a reference number. It reads the CSV file, finds the matching record, asks for a new status, and rewrites the CSV file with the updated status.

## New skill

I learned how to read CSV records, search for a record using a unique reference number, update its status, and save the updated register.

## Testing

I tested five scenarios:

1. Created the first enquiry and confirmed the CSV file and header row were created.
2. Created a second enquiry and confirmed it was appended without overwriting the first record.
3. Updated the first enquiry status to In progress.
4. Updated the second enquiry status to Closed.
5. Entered an invalid reference number and confirmed the script rejected it.

All five tests passed.

## Why this matters

Status updates make an enquiry register more useful for real business workflows. They allow a team to track progress from a new enquiry through to completion.