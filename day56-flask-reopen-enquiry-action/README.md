# Day 56 — Add Reopen Enquiry Quick Action

This project adds a reopen enquiry quick action to the Enquiry Tracker web application.

## Features

- Creates new enquiry records.
- Assigns a unique reference number to each enquiry.
- Captures the current date and time.
- Saves enquiries to a JSON file.
- Requires a valid customer email address.
- Requires a valid customer phone number.
- Prevents duplicate customer email addresses.
- Prevents duplicate customer phone numbers.
- Allows an enquiry to keep its own email address when editing.
- Allows an enquiry to keep its own phone number when editing.
- Adds a follow-up date to each enquiry.
- Validates the follow-up date.
- Edits the follow-up date.
- Identifies overdue follow-ups.
- Displays the overdue follow-up count in the dashboard.
- Filters enquiries to show only overdue follow-ups.
- Sorts enquiries by follow-up date, earliest first.
- Updates enquiry status.
- Closes an enquiry with one click after confirmation.
- Reopens a closed enquiry with one click after confirmation.
- Shows the Mark as closed button only for open enquiries.
- Shows the Reopen enquiry button only for closed enquiries.
- Updates enquiry priority.
- Updates the next action.
- Edits the customer name.
- Edits the enquiry type.
- Edits the priority.
- Edits the enquiry details.
- Edits the next action.
- Adds timestamped notes to an enquiry.
- Displays notes in reverse chronological order.
- Searches enquiries by customer name.
- Searches enquiries by enquiry type.
- Filters enquiries by status.
- Filters enquiries by priority.
- Displays a dashboard summary.
- Deletes an enquiry after confirmation.
- Preserves all other enquiries after deletion.
- Exports all enquiries to a downloadable CSV file.
- Includes the customer email address and phone number in the CSV export.
- Uses a .gitignore rule to keep changing local JSON test data out of GitHub.

## How to run

Open a terminal inside the day56-flask-reopen-enquiry-action folder and run:

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