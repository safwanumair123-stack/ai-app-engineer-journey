# Day 65 — Enquiry Tracker Project Review

This project is a review and consolidation version of the Enquiry Tracker web application built during Days 30–64 of the AI Applications Engineering journey.

The Enquiry Tracker helps a small or micro-business organise customer enquiries, assign responsibility, track follow-ups, prioritise opportunities, and export records for reporting.

## Purpose

The purpose of this project is to build a practical, understandable enquiry-management workflow.

Instead of relying on scattered WhatsApp messages, emails, spreadsheets, or memory, a business can use one structured system to see:

- What enquiries have arrived.
- Who is responsible for each enquiry.
- What the next action is.
- When follow-up is due.
- Which enquiries are overdue.
- Which enquiries are high priority.
- Where potential business value is coming from.
- Which enquiries need attention first.

## Core workflow

The application supports this workflow:

1. Capture the customer enquiry.
2. Assign an owner.
3. Set a priority.
4. Set the next action.
5. Record updates and conversations.
6. Track the status and follow-up date.
7. Review outstanding and overdue enquiries.
8. Close or reopen an enquiry when required.
9. Export the enquiry register for reporting.

## Features

### Enquiry records

- Creates new enquiry records.
- Assigns a unique reference number to each enquiry.
- Captures the current date and time.
- Saves enquiries to a JSON file.
- Captures customer name, email, phone number, enquiry type, priority, status, assigned person, source, estimated value, follow-up date, enquiry details, and next action.
- Requires a valid customer email address.
- Requires a valid customer phone number.
- Prevents duplicate customer email addresses.
- Prevents duplicate customer phone numbers.
- Allows an enquiry to keep its own email address when editing.
- Allows an enquiry to keep its own phone number when editing.

### Enquiry management

- Edits enquiry details.
- Updates enquiry status.
- Updates enquiry priority.
- Updates the next action.
- Edits the customer name.
- Edits the enquiry type.
- Edits the enquiry source.
- Edits the estimated value.
- Edits the follow-up date.
- Adds timestamped notes to an enquiry.
- Displays notes in reverse chronological order.
- Closes an enquiry with one click after confirmation.
- Reopens a closed enquiry with one click after confirmation.
- Deletes an enquiry after confirmation.
- Preserves all other enquiries after deletion.

### Follow-up management

- Adds a follow-up date to each enquiry.
- Validates the follow-up date.
- Edits the follow-up date.
- Identifies overdue follow-ups.
- Displays the overdue follow-up count in the dashboard.
- Filters enquiries to show only overdue follow-ups.
- Sorts enquiries by follow-up date, earliest first.

### Search and filters

- Searches enquiries by customer name.
- Searches enquiries by enquiry type.
- Filters enquiries by status.
- Filters enquiries by priority.
- Filters enquiries by assigned person.
- Filters enquiries by enquiry source.
- Filters enquiries to show only overdue follow-ups.
- Sorts enquiries by follow-up date.

### Dashboard reporting

- Displays total enquiries.
- Displays overdue follow-ups.
- Displays enquiries by status.
- Displays enquiries by priority.
- Displays enquiries by type.
- Displays enquiries by source.
- Calculates total estimated value.
- Calculates average estimated value.
- Identifies the highest-value enquiry.
- Identifies the top three highest-value enquiries.
- Calculates estimated value by status.
- Calculates estimated value by priority.
- Calculates estimated value by enquiry type.
- Calculates estimated value by assigned person.
- Calculates estimated value by enquiry source.

### Data export

- Exports all enquiries to a downloadable CSV file.
- Includes customer details, enquiry details, status, assignment, source, estimated value, follow-up date, and notes in the export.
- Uses a .gitignore rule to keep changing local JSON test data out of GitHub.

## How to run

Open a terminal inside the day65-flask-project-review folder and run:

py app.py

Then open:

http://127.0.0.1:5001/

## Main routes

- / — Enquiry list, dashboard, and create-enquiry form
- /create-enquiry — Creates a new enquiry
- /enquiry/<reference_number> — Displays one enquiry
- /edit-enquiry/<reference_number> — Edits one enquiry
- /close-enquiry/<reference_number> — Closes one enquiry
- /reopen-enquiry/<reference_number> — Reopens one enquiry
- /add-note/<reference_number> — Adds a timestamped note
- /delete-enquiry/<reference_number> — Deletes one enquiry
- /export-enquiries — Downloads all enquiries as CSV

## Dashboard metrics

- Total enquiries
- Overdue follow-ups
- Enquiries by status
- Enquiries by priority
- Enquiries by type
- Enquiries by source
- Total estimated value
- Average estimated value
- Highest estimated value
- Highest-value enquiry
- Top three highest-value enquiries
- Estimated value by status
- Estimated value by priority
- Estimated value by enquiry type
- Estimated value by assigned person
- Estimated value by source

## Approved enquiry types

- General enquiry
- Quotation
- Support
- Partnership

## Approved priorities

- Low
- Medium
- High

## Approved statuses

- New
- In progress
- Closed

## Approved enquiry sources

- Website
- WhatsApp
- Email
- Referral
- Phone call

## Project review

This version was reviewed after Days 30–64 of development.

The review confirmed that the application supports a complete local enquiry-management workflow:

- Create and validate an enquiry.
- Assign and prioritise an enquiry.
- Track status, follow-up date, notes, and estimated value.
- Search, filter, and sort enquiries.
- Review dashboard metrics.
- Close, reopen, or delete an enquiry with confirmation.
- Export the enquiry register to CSV.

## Current limitations

This is a learning and local-testing application.

It currently uses a local JSON file for storage and does not include user accounts, a database, automated tests, deployment, or AI features.

A production-ready version would need:

- A database.
- User accounts and login.
- Role-based access.
- Automated tests.
- Better error handling.
- Deployment to a live server.
- API integration.
- AI features with human approval and audit trails.

## Next phase

The next phase is to turn this working local application into a more complete, deployable business tool.

The priorities are:

- Move from JSON storage to a database.
- Add user accounts and basic roles.
- Add automated tests.
- Improve error handling.
- Deploy the application.
- Add one focused AI feature with human approval.
- Create a portfolio case study and demo.