# Day 53 — Add Duplicate Email Check

## What I learned

- How to check whether an email address already exists.
- How to prevent duplicate customer records.
- How to display a clear duplicate-email error.
- How to protect data quality in a business application.
- How to test validation rules that depend on existing saved data.

## What I built

I added a duplicate email check to the Enquiry Tracker.

The application now prevents a new enquiry from being created if the customer email address has already been used. When editing an enquiry, the application allows the same enquiry to keep its existing email address but prevents it from using an email address that belongs to another enquiry.

## New skill

I learned how to protect data quality by preventing duplicate records.

## Testing

I tested five scenarios:

1. Created an enquiry with a valid email address.
2. Tried to create a second enquiry using the same email address.
3. Confirmed that the duplicate email error appeared.
4. Edited the first enquiry without changing its email address.
5. Tried to change the first enquiry’s email address to an email address used by another enquiry.

All five tests passed.