# Day 28 — Search Enquiry Records

## What I learned

- How to read all records from a CSV file.
- How to search records by customer name.
- How to search records by enquiry type.
- How to display matching results clearly.
- How to handle searches that find no records.

## What the script does

The script gives the user three options: create a new enquiry, update an enquiry status, or search enquiries.

When searching, the user can choose to search by customer name or enquiry type. The script reads the CSV file, compares the search text with each record, and displays all matching results.

The search is case-insensitive and supports partial matches. For example, searching for “ahmed” can find “Ahmed Traders”.

## New skill

I learned how to search CSV records and display matching results without changing the original data.

## Testing

I tested five scenarios:

1. Created the first enquiry and confirmed the CSV file and header row were created.
2. Created a second enquiry and confirmed it was appended without overwriting the first record.
3. Searched by customer name and found the matching enquiry.
4. Searched by enquiry type and found the matching enquiry.
5. Searched for a customer that does not exist and confirmed the script displayed “No matching enquiries found.”

All five tests passed.

## Why this matters

Search makes an enquiry register more useful because users can quickly find relevant records without reading the entire file.