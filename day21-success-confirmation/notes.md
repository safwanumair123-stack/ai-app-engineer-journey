# Day 21 — Success Confirmation

## Completed
- Created a Day 21 copy of the practice app.
- Updated the browser tab title and visible heading to Day 21.
- Added a green success confirmation section after a successful
  submission.
- Added a "Start another post" button inside the confirmation.
- Added resetFormForNextPost() to reset the form consistently.
- Made both Clear and Start another post use the same reset function.
- Updated clearResults() to hide the success confirmation.
- Added the success confirmation to accessible live-region behaviour.
- Included the Start another post button in the loading-state checks.
- Kept validation, API requests, spinner, character counter, and
  loading safeguards from earlier days.
- Tested empty fields, successful submission, Start another post,
  and Clear form and result.

## Checks passed
- Empty fields show validation errors without showing success.
- Successful submission returns HTTP status 201.
- Green success confirmation appears after success.
- Result section and raw JSON appear after success.
- Start another post clears inputs, counter, errors, status,
  confirmation, result, and raw JSON.
- Focus returns to the title field after resetting.
- Clear form and result uses the same reset behaviour.
- Loading safeguards continue to work during a request.

## Key learning
A success message should confirm what happened and offer a clear
next action.

A reusable reset function prevents different buttons from resetting
the app in slightly different ways.

role="status" and aria-live="polite" help screen readers announce
important confirmation messages.

Consistent reset behaviour makes an application easier to understand
and use.