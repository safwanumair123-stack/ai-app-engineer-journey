# Day 52 — Add Customer Phone Number with Validation

## What I learned

- How to add a phone number field to an enquiry.
- How to validate a phone number using a simple rule.
- How to display a phone number in the enquiry list and details page.
- How to edit a phone number.
- How to include a phone number in a CSV export.

## What I built

I added a customer phone number field to the Enquiry Tracker.

The user must enter a phone number when creating an enquiry. The application checks that the phone number contains only acceptable characters and is within a reasonable length. The phone number can also be edited later from the individual enquiry page.

## New skill

I learned how to validate contact information before saving it to a business record.

## Testing

I tested five scenarios:

1. Created an enquiry with a valid phone number.
2. Tried to create an enquiry without a phone number.
3. Tried to create an enquiry with an invalid phone number.
4. Edited the phone number and saved the changes.
5. Downloaded the CSV file and confirmed the phone number appeared in the correct column.

All five tests passed.