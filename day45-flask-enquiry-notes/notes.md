# Day 45 — Add Enquiry Notes with Timestamps

## What I learned

- How to store multiple notes inside one enquiry record.
- How to add a timestamp to each note.
- How to display notes in reverse chronological order.
- How to keep enquiry details separate from activity notes.
- How to validate that a note is not empty.

## What I built

I added an enquiry notes feature to the Enquiry Tracker.

The user can open an enquiry and add a note. Each note is saved with the current date and time. Notes appear in reverse chronological order, so the newest note appears first.

This creates a simple activity history for each enquiry.

## New skill

I learned how to store a list of related records inside one JSON enquiry record.

## Testing

I tested five scenarios:

1. Created an enquiry and opened its details page.
2. Added a first note and confirmed it appeared with a timestamp.
3. Added a second note and confirmed it appeared above the first note.
4. Tried to add an empty note and confirmed the validation message appeared.
5. Edited the enquiry details and confirmed the notes remained unchanged.

All five tests passed.