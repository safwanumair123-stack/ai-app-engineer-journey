# Day 65 — Full Project Review and Consolidation

## What I learned

- How to review a growing application systematically.
- How to test core workflows after many changes.
- How to identify missing documentation or unclear features.
- How to prepare a project for a portfolio or demo.
- How to create a clear project review record.

## What I reviewed

I reviewed the Enquiry Tracker web application built during Days 30–64.

The application has developed from a simple enquiry register into a practical small-business workflow tool. It now supports enquiry creation, assignment, status tracking, follow-up dates, overdue detection, search, filters, sorting, notes, estimated value tracking, dashboard reporting, controlled status changes, deletion, and CSV export.

## Core workflow reviewed

I reviewed the complete enquiry workflow:

1. Create an enquiry.
2. Assign an owner.
3. Set a priority.
4. Set a next action.
5. Add a follow-up date.
6. Track the enquiry status.
7. Add timestamped notes.
8. Review overdue follow-ups.
9. Close or reopen an enquiry.
10. Delete an enquiry when required.
11. Export the enquiry register to CSV.

## Features reviewed

I reviewed the following feature groups:

- Enquiry creation and validation
- Unique reference numbers and timestamps
- Customer email and phone number validation
- Duplicate customer contact prevention
- Enquiry editing
- Enquiry assignment
- Enquiry status tracking
- Enquiry priority tracking
- Enquiry source tracking
- Enquiry type tracking
- Follow-up dates
- Overdue follow-up detection
- Search by customer name and enquiry type
- Filters by status, priority, assigned person, and source
- Sorting by follow-up date
- Timestamped notes
- Dashboard reporting
- Estimated value tracking
- Total, average, and highest estimated value
- Top three highest-value enquiries
- Value by status, priority, enquiry type, assigned person, and source
- Close and reopen actions with confirmation
- Deletion with confirmation
- CSV export

## Testing approach

I tested the application through the main user journeys rather than only checking individual features.

I tested:

- Creating a valid enquiry.
- Creating an enquiry with missing or invalid information.
- Creating duplicate customer contact records.
- Editing an enquiry.
- Adding a note.
- Changing an enquiry status.
- Closing and reopening an enquiry.
- Deleting an enquiry.
- Searching and filtering enquiries.
- Sorting enquiries by follow-up date.
- Reviewing dashboard metrics.
- Exporting enquiries to CSV.

## Documentation review

I reviewed the README to ensure it explains:

- The purpose of the application.
- The main features.
- How to run the application.
- The main routes.
- The dashboard metrics.
- The approved enquiry types, priorities, statuses, and sources.
- The current limitations.

I also reviewed the notes to ensure they explain what was learned, what was built, and how the work was tested.

## Current limitations

The application currently uses a local JSON file for storage.

This is suitable for learning and local testing, but a production-ready version would need:

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

## Testing

I tested five scenarios:

1. Created a valid enquiry and confirmed it appeared in the list.
2. Edited the enquiry and confirmed the changes were saved.
3. Added a note and confirmed it appeared with a timestamp.
4. Closed and reopened the enquiry and confirmed the status changed correctly.
5. Exported the enquiry register to CSV and confirmed the data was included.

All five tests passed.