# Day 17 — Submit Button Loading State

## Completed
- Created a Day 17 copy of the practice app.
- Updated the browser tab title and visible heading to Day 17.
- Added a loading state for the submit button.
- Added setSubmitButtonLoading() to control the button state.
- Changed the button text to "Sending..." during a request.
- Disabled the submit button while a request is running.
- Added aria-busy="true" during loading for accessibility.
- Restored the original button text and enabled state afterwards.
- Used a finally block so the button is restored after success
  or failure.
- Prevented duplicate submissions by checking whether the submit
  button is already disabled.
- Added CSS styling for the disabled submit button.
- Tested empty fields, successful submission, duplicate clicks,
  and clearing.

## Checks passed
- Empty fields show validation errors without changing the button
  to a loading state.
- Successful submission changes the button to "Sending...".
- The button is disabled while the request is running.
- The button returns to "Send practice post" after completion.
- Repeated clicks during loading do not send extra requests.
- Clear removes inputs, errors, status, result, and raw JSON.

## Key learning
A loading state gives users feedback while the app waits for a
network request.

Disabling a submit button during a request prevents accidental
duplicate submissions.

The finally block runs after either success or failure, so it is
useful for restoring UI state.

aria-busy helps assistive technology understand that an element is
currently busy.