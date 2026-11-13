# Day 33 — Improve the Structure of the Enquiry App

## What I learned

- How to use constants for values that should not change.
- How to separate configuration from application logic.
- How to organise related functions into clear sections.
- How to improve naming and comments.
- How to prepare a project for future growth.

## What the script does

The script still provides four options: create a new enquiry, update an enquiry status, search enquiries, or show a summary report.

The main improvement is that the code is now organised into clear sections. Configuration, user interaction, data logic, main features, and the application entry point are separated.

## Improvements made

- Moved important values into constants.
- Created a reusable get_user_input function.
- Created a reusable display_enquiry function.
- Created separate functions for loading and saving data.
- Created a reusable function for finding an enquiry.
- Created a reusable function for creating an enquiry record.
- Created a reusable count_records function for summary reporting.
- Added clear section comments.

## New skill

I learned how to organise a Python application into clear sections and reusable functions.

## Testing

I tested five scenarios:

1. Created an enquiry and confirmed the record was saved correctly.
2. Updated the enquiry status and confirmed the record was updated correctly.
3. Searched by customer name and confirmed the search function worked.
4. Displayed the summary report and confirmed the reusable counting function worked.
5. Deleted the CSV file and confirmed the app displayed a safe message.

All five tests passed.

## Why this matters

Clean structure makes an application easier to understand, maintain, test, and extend. It prepares the project for future improvements such as APIs, databases, user interfaces, and AI integration.