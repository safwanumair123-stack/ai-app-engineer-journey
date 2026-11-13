# Day 36 — Enquiry Tracker Interface Plan

## Product purpose

The Enquiry Tracker helps a small business capture customer enquiries, assign priorities, track progress, and follow up without losing important information.

The goal is to turn scattered messages and manual notes into a simple, visible workflow.

## Target user

The primary user is a small or micro-business owner, administrator, or team member who handles customer enquiries, quotation requests, support requests, or supplier requests.

This person may not be technical. They need a simple interface that makes it clear what needs to be done next.

## User problem

Customer enquiries may arrive through WhatsApp, email, phone calls, social media, or face-to-face conversations.

Without a shared system, important details can be missed:

- Who submitted the enquiry?
- What do they need?
- When did they contact the business?
- Who is responsible for following up?
- What is the current status?
- What is the next action?

## Product promise

Every enquiry should have:

- A clear record.
- A reference number.
- A timestamp.
- A customer name.
- An enquiry type.
- A priority level.
- A status.
- A next action.

## Core user jobs

The user should be able to:

1. Create a new enquiry.
2. See a list of enquiries.
3. Search for an enquiry.
4. Open an enquiry.
5. Update an enquiry status.
6. Change an enquiry priority.
7. Add a next action.
8. View a summary report.
9. Export or view enquiry data.

## Main screens

### Screen 1: Dashboard

The dashboard gives the user an immediate overview.

It should show:

- Total enquiries.
- New enquiries.
- Enquiries in progress.
- Closed enquiries.
- High-priority enquiries.
- Recent enquiries.

The dashboard should help the user answer one question:

**What needs attention today?**

### Screen 2: Enquiry list

The enquiry list shows all enquiries in a simple table or list.

Each enquiry should show:

- Reference number.
- Customer name.
- Enquiry type.
- Priority.
- Status.
- Created date and time.
- Next action.

The user should be able to filter by:

- Status.
- Priority.
- Enquiry type.
- Customer name.

### Screen 3: Create enquiry

The create-enquiry screen should be simple and clear.

It should include:

- Customer name.
- Enquiry type.
- Priority.
- Notes or enquiry details.
- Next action.

The system should automatically create:

- Reference number.
- Created date and time.
- Initial status: New.

### Screen 4: Enquiry details

The enquiry details screen shows one complete enquiry.

It should display:

- Reference number.
- Customer name.
- Enquiry type.
- Priority.
- Status.
- Created date and time.
- Enquiry details.
- Next action.
- Status history.

The user should be able to:

- Update the status.
- Change the priority.
- Add or update the next action.
- Add an internal note.

### Screen 5: Search and filters

The search screen should help the user find an enquiry quickly.

The user should be able to search by:

- Reference number.
- Customer name.
- Enquiry type.
- Status.
- Priority.

### Screen 6: Summary report

The summary report should show the overall workload.

It should display:

- Total enquiries.
- Enquiries by status.
- Enquiries by priority.
- Enquiries by type.
- High-priority enquiries that are still open.

## User flow

1. The user opens the dashboard.
2. The user sees how many enquiries need attention.
3. The user opens the enquiry list.
4. The user creates a new enquiry or opens an existing enquiry.
5. The user updates the status, priority, or next action.
6. The user saves the change.
7. The system updates the record and shows a confirmation message.
8. The user returns to the dashboard or enquiry list.

## Input validation

The system should prevent incomplete or invalid records.

Required fields:

- Customer name.
- Enquiry type.
- Priority.

Optional fields:

- Enquiry details.
- Next action.
- Internal notes.

Validation rules:

- Customer name cannot be empty.
- Enquiry type must be selected from approved options.
- Priority must be selected from approved options.
- Status must be selected from approved options.
- Reference number should be generated automatically.
- Created date and time should be generated automatically.

## Feedback and confirmation

After saving, the user should see a clear confirmation message.

Examples:

- “Enquiry created successfully.”
- “Status updated successfully.”
- “Priority updated successfully.”
- “Next action saved successfully.”

If something goes wrong, the user should see a clear message explaining what happened and what to do next.

## Human approval and traceability

The first version will not automatically send messages to customers.

AI may later help draft a response, classify an enquiry, or suggest a next action.

However, the user must review and approve anything customer-facing.

The system should record:

- What AI suggested.
- What the user changed.
- What the user approved.
- When the action happened.
- Who approved it.

## First version scope

The first version should include:

- Dashboard.
- Enquiry list.
- Create enquiry.
- Enquiry details.
- Status updates.
- Priority updates.
- Search and filters.
- Summary report.

The first version should not include:

- Automatic customer emails.
- Automatic WhatsApp messages.
- Automatic quotations.
- Complex user accounts.
- Multi-user permissions.
- Payment processing.

## Success measures

The tool is successful if it helps the user:

- Capture every enquiry in one place.
- Find an enquiry quickly.
- Know what needs attention.
- Avoid missed follow-ups.
- See the current status of work.
- Make better decisions about priorities.