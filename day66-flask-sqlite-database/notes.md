# Day 66 — Move Enquiry Tracker to SQLite Database

## What I learned

- How to use SQLite with Python.
- How to create a database table.
- How to save enquiry records to a database.
- How to read enquiry records from a database.
- How to update and delete database records.
- How to keep the existing application features working.

## What I built

I moved the Enquiry Tracker from a local JSON file to a SQLite database.

The application now creates a database file called enquiry_register.db and stores each enquiry in a structured database table. The table includes the reference number, customer details, enquiry type, priority, status, assigned person, source, estimated value, timestamps, follow-up date, enquiry details, next action, and notes.

The application can now create, read, update, and delete enquiry records directly in the SQLite database.

## New skill

I learned how to use a database as the data layer for a web application.

## Testing

I tested five scenarios:

1. Created a valid enquiry and confirmed it was saved in the SQLite database.
2. Restarted the application and confirmed the enquiry was still available.
3. Edited the enquiry and confirmed the database record was updated.
4. Added a note and confirmed the note was saved in the database.
5. Deleted the enquiry and confirmed it was removed from the database.

All five tests passed.