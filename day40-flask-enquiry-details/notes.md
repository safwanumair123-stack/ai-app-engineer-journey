# Day 40 — View and Update Individual Enquiry Records

## What I learned

- How to create a dynamic route in Flask.
- How to find one enquiry by reference number.
- How to display a single record on its own page.
- How to update a record from a web form.
- How to preserve the rest of the enquiry register while updating one record.

## What I built

I added an enquiry details page to the Enquiry Tracker.

The enquiry list now includes a link to view and update each enquiry. When the user opens an enquiry, Flask finds the record using its reference number and displays its full details.

The user can update the enquiry status, priority, and next action. Flask validates the status and priority, updates the record, saves the updated register, and displays a confirmation message.

## New skill

I learned how to create dynamic routes in Flask and update a single record from a web form.

## Testing

I tested five scenarios:

1. Created an enquiry and confirmed it appeared in the enquiry list.
2. Opened the enquiry details page and confirmed the full record was displayed.
3. Updated the enquiry status, priority, and next action.
4. Returned to the enquiry list and confirmed the updated record was still available.
5. Entered an invalid reference number and confirmed the app displayed a safe error message.

All five tests passed.

## Why this matters

Being able to view and update individual records makes an application more useful for real business workflows. It allows a user to track progress and keep enquiry information up to date.