# Day 54 — Add Duplicate Phone Number Check

## What I learned

- How to check whether a phone number already exists.
- How to prevent duplicate customer phone records.
- How to allow an enquiry to keep its own phone number when editing.
- How to display a clear duplicate-phone error.
- How to protect contact-data quality.

## What I built

I added duplicate phone number prevention to the Enquiry Tracker.

The application now prevents a new enquiry from being created if the customer phone number has already been used. When editing an enquiry, the application allows that enquiry to keep its existing phone number but prevents it from using a phone number that belongs to another enquiry.

## New skill

I learned how to protect contact-data quality by preventing duplicate phone numbers.

## Testing

I tested five scenarios:

1. Created an enquiry with a valid phone number.
2. Tried to create a second enquiry using the same phone number.
3. Confirmed that the duplicate phone error appeared.
4. Edited the first enquiry without changing its phone number.
5. Tried to change the first enquiry’s phone number to a phone number used by another enquiry.

All five tests passed.