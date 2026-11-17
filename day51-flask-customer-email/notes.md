# Day 51 — Add Customer Email with Validation

## What I learned

- How to add an email field to an enquiry.
- How to validate an email address in Flask.
- How to display an email address on the enquiry list and details page.
- How to edit an email address.
- How to include an email address in a CSV export.

## What I built

I added a customer email field to the Enquiry Tracker.

The user must enter a valid email address when creating an enquiry. The application checks that the email contains an @ symbol and a domain extension. The email address can also be edited later from the individual enquiry page.

## New skill

I learned how to validate user input before saving it to a business record.

## Testing

I tested five scenarios:

1. Created an enquiry with a valid email address.
2. Tried to create an enquiry without an email address.
3. Tried to create an enquiry with an invalid email address.
4. Edited the email address and saved the changes.
5. Downloaded the CSV file and confirmed the email address appeared in the correct column.

All five tests passed.