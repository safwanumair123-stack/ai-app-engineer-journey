# Day 42 — Add a Dashboard Summary to the Enquiry Tracker

## What I learned

- How to calculate summary totals in Flask.
- How to pass summary data to an HTML template.
- How to display dashboard cards.
- How to show key workload information at a glance.
- How to keep search and filters working alongside the dashboard.

## What I built

I added a dashboard summary to the Enquiry Tracker web interface.

The dashboard displays the total number of enquiries, enquiries by status, high-priority enquiries, enquiries by type, and enquiries by priority.

The dashboard appears at the top of the main page, giving the user an immediate view of the current workload.

## New skill

I learned how to calculate and display summary data in a Flask web application.

## Testing

I tested five scenarios:

1. Created the first enquiry and confirmed the dashboard showed one total enquiry.
2. Created a second enquiry and confirmed the dashboard updated correctly.
3. Updated an enquiry status and confirmed the status counts changed.
4. Used search and filters and confirmed the dashboard still showed the total workload.
5. Checked the dashboard on a smaller screen and confirmed the layout remained readable.

All five tests passed.

## Why this matters

A dashboard helps a user understand the overall workload at a glance. Instead of reading every enquiry, the user can quickly see what is new, in progress, closed, or high priority.