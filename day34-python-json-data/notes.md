# Day 34 — Work with JSON Data in the Enquiry App

## What I learned

- What JSON is.
- How Python dictionaries relate to JSON.
- How to save data as JSON.
- How to load data from JSON.
- How JSON differs from CSV.
- How to prepare an application for future API and AI integrations.

## What the script does

The script provides five options: create a new enquiry, update an enquiry status, search enquiries, show a summary report, or display the raw JSON data.

The script now saves enquiry records to enquiry_register.json instead of enquiry_register.csv. Each enquiry is stored as a JSON object inside a JSON array.

## New skill

I learned how to use Python’s json module to save and load structured data.

## Testing

I tested five scenarios:

1. Created the first enquiry and confirmed the JSON file was created.
2. Created a second enquiry and confirmed it was added without overwriting the first record.
3. Updated the first enquiry status and confirmed the JSON file was updated.
4. Displayed the raw JSON data and confirmed the structure was readable.
5. Displayed the summary report and confirmed the counts were correct.

All five tests passed.

## Why this matters

JSON is widely used by APIs, web applications, and AI services. Learning to work with JSON prepares the enquiry app for future integrations with external systems and AI tools.