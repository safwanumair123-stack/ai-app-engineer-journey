# Day 44 — Add Enquiry Editing

## What I learned

- How to create an edit route in Flask.
- How to update multiple fields in one enquiry record.
- How to keep the reference number unchanged during editing.
- How to validate edited enquiry data.
- How to save updated data back to a JSON file.

## What I built

I added an enquiry editing feature to the Enquiry Tracker.

The user can open an enquiry and edit the customer name, enquiry type, priority, enquiry details, and next action. The reference number remains the same so the enquiry can still be identified correctly.

After saving, the application displays a success message and shows the updated information.

## New skill

I learned how to update an existing record in a JSON list without creating a new record.

## Testing

I tested five scenarios:

1. Created an enquiry and opened its details page.
2. Changed the customer name and saved the changes.
3. Changed the enquiry type and saved the changes.
4. Changed the priority and saved the changes.
5. Checked that the reference number remained unchanged after editing.

All five tests passed.