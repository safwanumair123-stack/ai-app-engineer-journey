# Day 43 — Add Enquiry Deletion with Confirmation

## What I learned

- How to create a delete route in Flask.
- How to remove one record from a JSON list.
- How to preserve all other records.
- How to ask for confirmation before deleting.
- How to return to the enquiry list after deletion.

## What I built

I added a delete feature to the Enquiry Tracker.

The user can open an enquiry and choose to delete it. Before deletion, the browser asks for confirmation. If the user confirms, Flask removes the enquiry from the JSON register and saves the updated list.

All other enquiries remain unchanged.

## New skill

I learned how to delete a single record from a JSON list while preserving the remaining records.

## Testing

I tested five scenarios:

1. Created two enquiries and confirmed both appeared in the enquiry list.
2. Opened the first enquiry and confirmed the delete button appeared.
3. Clicked delete and confirmed the confirmation message appeared.
4. Confirmed deletion and checked that the enquiry was removed from the list.
5. Checked that the second enquiry remained unchanged.

All five tests passed.

## Why this matters

Deletion needs to be handled carefully in business applications. Asking for confirmation helps prevent accidental loss of important records.