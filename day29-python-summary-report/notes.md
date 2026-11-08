# Day 29 — Create an Enquiry Summary Report

## What I learned

- How to count records in a CSV file.
- How to group records by status.
- How to group records by enquiry type.
- How to display a simple summary report.
- How to handle an empty or missing register safely.

## What the script does

The script gives the user four options: create a new enquiry, update an enquiry status, search enquiries, or show a summary report.

The summary report reads the CSV file and counts the total number of enquiries. It also counts enquiries by status and enquiry type.

The script displays totals for New, In progress, and Closed enquiries. It also displays totals for General enquiry, Quotation, Support, and Partnership enquiries.

## New skill

I learned how to count and group CSV records to create a simple summary report.

## Testing

I tested five scenarios:

1. Created the first enquiry and confirmed the CSV file and header row were created.
2. Created a second enquiry and confirmed it was appended without overwriting the first record.
3. Updated the first enquiry status to In progress.
4. Displayed the summary report and confirmed the counts were correct.
5. Deleted the CSV file and confirmed the script displayed a safe message when no register was found.

All five tests passed.

## Why this matters

Summary reports help users understand the overall workload at a glance. They show how many enquiries are new, in progress, or closed, and which enquiry types are most common.