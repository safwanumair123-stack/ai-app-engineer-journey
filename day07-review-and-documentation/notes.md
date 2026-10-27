# Day 6 — Clear Form and Results

## Completed
- Added a "Clear form and result" button.
- Used type="button" so it does not submit the form.
- Connected the button to a JavaScript click event listener.
- Added code to clear both inputs, the status message,
  the readable result, and the raw JSON.
- Returned the cursor to the title input after clearing.
- Added a guard to prevent clearing while a request is sending.

## Tests completed
- Submitted a practice post successfully.
- Clicked Clear and confirmed the inputs and results disappeared.
- Checked the Network panel: existing requests remained,
  but clicking Clear did not add another request.

## Key learning
Clearing the webpage is different from clearing the browser's
network history. Existing request entries remain visible even
after the form and results have been cleared.

Today I made targeted changes to existing HTML and JavaScript
rather than replacing the entire application.