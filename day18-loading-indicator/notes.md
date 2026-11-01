# Day 18 — Loading Indicator

## Completed
- Created a Day 18 copy of the practice app.
- Updated the browser tab title and visible heading to Day 18.
- Added a CSS-only loading spinner beside the status message.
- Added a status-row container to align the spinner and status text.
- Added a setLoading() function to coordinate loading UI.
- Showed the spinner and "Sending..." status during a request.
- Disabled the submit button during a request.
- Added aria-busy="true" to the submit button during loading.
- Hid the spinner and restored the button after completion.
- Used a finally block so the loading state is cleared after
  success or failure.
- Prevented duplicate submissions by checking the disabled state.
- Tested empty fields, successful submission, duplicate clicks,
  and clearing.

## Checks passed
- Empty fields show validation errors without showing the spinner.
- Successful submission shows the spinner beside "Sending...".
- The submit button becomes disabled during the request.
- The spinner disappears after the request finishes.
- The status shows HTTP status 201 after success.
- Repeated clicks during loading do not send