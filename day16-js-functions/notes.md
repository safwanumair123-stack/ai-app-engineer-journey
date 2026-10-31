# Day 16 — JavaScript Functions and Cleaner App Logic

## Completed
- Created a Day 16 copy of the practice app.
- Updated the browser tab title and visible heading to Day 16.
- Reviewed the large submit-handler function from earlier days.
- Split repeated work into named JavaScript functions.
- Added clearFieldErrors() to remove error messages and aria-invalid.
- Added validateForm() to check the title and content fields.
- Added clearResults() to clear status, raw JSON, and results.
- Added buildPayload() to create the data sent to the API.
- Added displaySuccess() to show the readable result and raw JSON.
- Added displayError() to show request or network errors.
- Updated the submit and Clear handlers to use these functions.
- Tested empty fields, spaces-only fields, successful submission,
  and clearing.

## Checks passed
- Empty fields show individual error messages and red borders.
- Spaces-only fields show the same validation behaviour.
- Successful submission returns HTTP status 201.
- Readable result and raw JSON display correctly.
- Clear removes inputs, errors, status, results, and raw JSON.

## Key learning
Functions are named, reusable blocks of JavaScript code.

They can receive values as parameters and return a result.

Splitting a large function into smaller functions makes code easier
to read, test, and change.

Refactoring means improving the structure of code without changing
its external behaviour.