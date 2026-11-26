# Day 68 — Add Basic Roles and Permissions

This project adds basic roles and permissions to the Enquiry Tracker web application.

## Purpose

The Enquiry Tracker helps a small or micro-business organise customer enquiries, assign responsibility, track follow-ups, prioritise opportunities, and export records for reporting.

## Roles

The application now supports two roles:

- Admin
- User

The first user who registers becomes an Admin. Every later user becomes a regular User.

Admin users can access an admin-only dashboard. The dashboard shows all registered users and all enquiries created by every user.

Regular users can access only their own enquiries.

## Database

The application uses SQLite and creates a local database file called:

enquiry_register.db

The database contains two tables:

### users

- id
- full_name
- email
- password_hash
- role
- created_at

### enquiries

- id
- reference_number
- user_id
- customer_name
- customer_email
- customer_phone
- enquiry_type
- priority
- status
- assigned_to
- enquiry_source
- estimated_value
- created_at
- follow_up_date
- enquiry_details
- next_action
- notes

## Features

- Creates user accounts.
- Hashes passwords before saving them.
- Requires a valid email address.
- Requires a password of at least eight characters.
- Confirms that the password and confirmation password match.
- Prevents duplicate user email addresses.
- Assigns the Admin role to the first registered user.
- Assigns the User role to every later registered user.
- Logs users in with a valid email address and password.
- Stores the user role in the browser session.
- Protects all enquiry routes with login.
- Protects the admin dashboard with both login and the Admin role.
- Redirects unauthenticated users to the login page.
- Shows the Admin dashboard link only to Admin users.
- Allows Admin users to view all registered users.
- Allows Admin users to view all enquiries from every user.
- Prevents regular users from accessing the admin dashboard.
- Allows each regular user to see only their own enquiries.
- Allows each regular user to create, edit, close, reopen, and delete only their own enquiries.
- Logs users out and clears their session.
- Creates new enquiry records.
- Assigns a unique reference number to each enquiry.
- Captures the current date and time.
- Saves enquiries to a SQLite database.
- Requires a valid customer email address.
- Requires a valid customer phone number.
- Prevents duplicate customer email addresses.
- Prevents duplicate customer phone numbers.
- Requires a non-negative estimated value.
- Validates the estimated value.
- Edits the estimated value.
- Calculates the total estimated value in the dashboard.
- Calculates the average estimated value in the dashboard.
- Identifies the enquiry with the highest estimated value.
- Displays the highest-value enquiry in the dashboard.
- Identifies the top three highest-value enquiries.
- Displays the top three highest-value enquiries in ranked order.
- Calculates estimated value by enquiry status.
- Calculates estimated value by assigned person.
- Calculates estimated value by enquiry source.
- Calculates estimated value by priority.
- Calculates estimated value by enquiry type.
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
- Includes the estimated value in the CSV export.
- Uses a .gitignore rule to keep changing local database test data out of GitHub.

## How to run

Open a terminal inside the day68-flask-roles-permissions folder and run:

py app.py

Then open:

http://127.0.0.1:5001/

## Main routes

- /register — Creates a new user account
- /login — Logs a user in
- /logout — Logs a user out
- / — Enquiry list, dashboard, and create-enquiry form
- /admin — Admin-only dashboard
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

## Security note

This is a learning application. For production use, the secret key should be stored securely in an environment variable, and additional security measures should be added.

## Current limitations

This application uses a local SQLite database and does not yet include automated tests, deployment, or AI features.

## Next phase

The next phase is to add automated tests, improved error handling, deployment, and focused AI features with human approval.