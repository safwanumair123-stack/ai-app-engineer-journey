# Day 25 — Save Enquiry Records to a CSV File

## Completed
- Created a Day 25 copy of the Day 24 Python project.
- Renamed the Python file to enquiry_register.py.
- Imported Python's built-in csv and os modules.
- Defined a CSV filename and column headers.
- Kept approved enquiry types from Day 23.
- Collected and validated customer name and enquiry type.
- Created an enquiry dictionary for each valid enquiry.
- Checked whether the CSV file already exists.
- Wrote the header row only when creating a new CSV file.
- Appended each valid enquiry as a new CSV row.
- Displayed the saved enquiry details and CSV filename.
- Tested first enquiry, second enquiry, different capitalisation,
  invalid category, and missing customer name.

## Checks passed
- First valid enquiry creates enquiry_register.csv.
- The CSV contains the correct header row and enquiry row.
- Additional valid enquiries are appended as new rows.
- Existing rows are not replaced when new enquiries are added.
- SUPPORT is saved as the approved category Support.
- Invalid enquiry types do not create a CSV row.
- Missing customer name does not create a CSV row.

## Key learning
A CSV file stores tabular data as rows and columns.

The csv module helps Python read and write structured CSV data.

Opening a file in append mode adds new data without replacing
existing data.

A CSV register is a simple form of traceability: it keeps a record
of what was submitted, when it can be reviewed, and how it can be
used later.

This is an early foundation for enquiry logs, service registers,
quote trackers, and AI-assisted workflow records.