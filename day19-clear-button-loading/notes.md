# Day 19 — Clear Button Loading State

## Completed
- Created a Day 19 copy of the practice app.
- Updated the browser tab title and visible heading to Day 19.
- Added the Clear button to the loading state.
- Updated setLoading() to disable both submit and Clear buttons
  during a request.
- Added a disabled-state check to the Clear button handler.
- Added CSS styling for the disabled Clear button.
- Kept the spinner, status message, and submit button behaviour
  from Day 18.
- Restored both buttons after success or failure using a finally
  block.
- Tested empty fields, successful submission, Clear during loading,
  and Clear after completion.

## Checks passed
- Empty fields show validation errors without enabling loading state.
- Successful submission shows the spinner and disables both buttons.
- The submit button changes to "Sending..." during the request.
- The Clear button becomes disabled while the request is running.
- Clearing is prevented during loading by the disabled-state check.
- Both buttons become enabled again after the request finishes.
- Clear removes inputs, errors, status, result, and raw JSON after
  completion.
- The spinner remains hidden after clearing.

## Testing note
The practice API responds very quickly, so the loading period is too
short for a manual Clear click. However, the Clear button was observed
to become disabled during loading, and the Clear handler includes a
disabled-state check. This confirms that clearing is prevented while
a request is running.

## Key learning
When an app is busy, every action that could interfere with the
request should be considered.

Disabling only the submit button prevents duplicate submissions, but
it does not prevent someone from clearing the form or results while
the request is still running.

A single setLoading() function can keep related buttons, messages,
and indicators in sync.