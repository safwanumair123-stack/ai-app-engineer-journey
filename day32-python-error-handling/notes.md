# Day 32 — Add Error Handling to the Enquiry App

## What I learned

- How to use try and except.
- How to handle missing files safely.
- How to handle invalid CSV data.
- How to prevent unexpected crashes.
- How to show clear, useful error messages.

## What the script does

The script still provides four options: create a new enquiry, update an enquiry status, search enquiries, or show a summary report.

The main improvement is that file operations are now protected with error handling. The app can respond safely if a file cannot be read, written, or accessed.

## Error handling added

- try and except around saving a new enquiry.
- try and except around reading the CSV register.
- try and except around updating and rewriting the CSV register.
- PermissionError handling.
- UnicodeDecodeError handling.
- OSError handling.

## New skill

I learned how to use try and except to handle file errors and prevent an application from crashing unexpectedly.

## Testing

I tested five scenarios:

1. Created an enquiry and confirmed the file was saved correctly.
2. Updated the enquiry status and confirmed the file was rewritten correctly.
3. Searched by customer name and confirmed the app could read the register safely.
4. Displayed the summary report and confirmed the app could process the register safely.
5. Deleted the CSV file and confirmed the app displayed a safe message instead of crashing.

All five tests passed.

## Why this matters

Error handling makes an application more reliable. Instead of crashing when something goes wrong, the app can explain the problem and guide the user toward a solution.