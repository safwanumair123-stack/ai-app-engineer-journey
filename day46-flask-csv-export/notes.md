# Day 46 — Add CSV Export

## What I learned

- How to export JSON data to CSV.
- How to use Python’s built-in csv module.
- How to send a downloadable file from Flask.
- How to export all enquiry records in one click.
- How to keep the export separate from the JSON data storage.

## What I built

I added a CSV export feature to the Enquiry Tracker.

The user can click a link to download all enquiries as a CSV file. The CSV file includes the reference number, customer name, enquiry type, priority, status, created date, enquiry details, next action, and notes.

The original JSON data remains unchanged.

## New skill

I learned how to convert JSON data into a downloadable CSV file using Python and Flask.

## Testing

I tested five scenarios:

1. Created three enquiries and confirmed they appeared in the enquiry list.
2. Clicked the CSV export link.
3. Opened the downloaded CSV file in Excel.
4. Checked that all enquiry fields appeared correctly.
5. Added a note to one enquiry and confirmed the note appeared in the CSV export.

All five tests passed.