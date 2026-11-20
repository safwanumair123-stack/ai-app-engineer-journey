# Day 57 — Add Estimated Value and Total Value

## What I learned

- How to add a numeric business field.
- How to validate a positive number.
- How to display an estimated value.
- How to calculate a total estimated value.
- How to include the value in a CSV export.

## What I built

I added an estimated value field to the Enquiry Tracker.

The user must enter a non-negative number when creating an enquiry. The application validates the value and displays it in the enquiry list and individual enquiry page. The dashboard calculates and displays the total estimated value of all enquiries.

## New skill

I learned how to work with numeric business data and calculate a total value.

## Testing

I tested five scenarios:

1. Created an enquiry with a valid estimated value.
2. Tried to create an enquiry without an estimated value.
3. Tried to create an enquiry with a negative estimated value.
4. Edited the estimated value and saved the changes.
5. Checked that the dashboard total estimated value updated correctly.

All five tests passed.