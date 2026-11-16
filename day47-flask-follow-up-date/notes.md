# Day 47 — Add Follow-Up Date and Overdue Tracking

## What I learned

- How to add a date field to an enquiry.
- How to validate a date entered by the user.
- How to display a follow-up date.
- How to edit a follow-up date.
- How to identify overdue follow-ups.
- How to show overdue follow-ups in the dashboard.

## What I built

I added a follow-up date feature to the Enquiry Tracker.

The user can add a follow-up date when creating an enquiry and edit it later. The application checks whether the follow-up date is valid. If the follow-up date has passed and the enquiry is not closed, the dashboard counts it as an overdue follow-up.

## New skill

I learned how to work with dates in Python and Flask and how to identify overdue records.

## Testing

I tested five scenarios:

1. Created an enquiry with a future follow-up date.
2. Created an enquiry with a past follow-up date.
3. Checked that the overdue follow-up count increased.
4. Edited the overdue follow-up date to a future date.
5. Confirmed that the overdue follow-up count decreased.

All five tests passed.