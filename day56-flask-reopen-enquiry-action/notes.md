# Day 56 — Add Reopen Enquiry Quick Action

## What I learned

- How to create the opposite of a close action.
- How to reopen a closed enquiry.
- How to ask for confirmation before changing a status.
- How to show the reopen button only for closed enquiries.
- How to keep the close and reopen actions separate.

## What I built

I added a reopen enquiry quick action to the Enquiry Tracker.

When an enquiry is closed, the user can reopen it with one click. Before the enquiry is reopened, the browser asks for confirmation. After confirmation, the enquiry status changes to In progress and the user returns to the enquiry list.

The Reopen enquiry button appears only when the enquiry status is Closed. The Mark as closed button appears only when the enquiry is not closed.

## New skill

I learned how to create opposite actions while keeping the interface clear and controlled.

## Testing

I tested five scenarios:

1. Created an enquiry and closed it.
2. Opened the closed enquiry and confirmed the Reopen enquiry button appeared.
3. Clicked Reopen enquiry and confirmed the confirmation message appeared.
4. Confirmed the action and checked that the enquiry status changed to In progress.
5. Opened the reopened enquiry and confirmed that the Mark as closed button appeared again.

All five tests passed.