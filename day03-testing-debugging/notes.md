# Day 3 — Testing and Debugging

## Tests completed
- Empty fields: browser blocked submission.
- Spaces-only input: JavaScript displayed the validation message.
- Internet disconnected: app displayed "Error: Failed to fetch".
- Internet reconnected: request succeeded with HTTP status 201.

## What I learned
- HTML and JavaScript provide different input checks.
- Error handling gives the user feedback when a request fails.
- The app can recover and submit again after a network failure.
- Testing should include unsuccessful situations, not only success.