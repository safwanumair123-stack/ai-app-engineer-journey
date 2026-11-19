# Day 55 — Add Close Enquiry Quick Action

## What I learned

- How to create a focused business action.
- How to update one field without editing the whole record.
- How to ask for confirmation before changing an enquiry status.
- How to return to the enquiry list after completing an action.
- How to make an application easier to use for repetitive operational tasks.

## What I built

I added a Mark as closed quick action to the Enquiry Tracker.

The user can open an enquiry and close it with one click. Before the enquiry is closed, the browser asks for confirmation. After confirmation, the enquiry status changes to Closed and the user returns to the enquiry list.

The Mark as closed button does not appear if the enquiry is already closed.

## New skill

I learned how to create a focused action that improves usability for repetitive operational tasks.

## Testing

I tested five scenarios:

1. Created an enquiry and opened its details page.
2. Confirmed that the Mark as closed button appeared.
3. Clicked Mark as closed and confirmed the confirmation message appeared.
4. Confirmed the action and checked that the enquiry status changed to Closed.
5. Opened the closed enquiry and confirmed that the Mark as closed button no longer appeared.

All five tests passed.