# Day 14 — Form Errors and Usability

## Completed
- Created a Day 14 copy of the practice app.
- Updated the browser tab title and visible heading to Day 14.
- Added separate error-message elements for the title and content fields.
- Connected each error message to its field using aria-describedby.
- Added CSS variables and styles for error colours and invalid fields.
- Updated JavaScript to validate each field separately.
- Added novalidate to the form so the custom JavaScript validation
  controls the error messages.
- Removed the required attributes because JavaScript now handles
  empty-field validation.
- Fixed duplicate JavaScript variable declarations that prevented
  the script from running.
- Tested empty fields, spaces-only fields, successful submission,
  and clearing.

## Checks passed
- Empty fields show individual error messages.
- Spaces-only fields show individual error messages.
- Invalid fields show a red border and light red background.
- The status message asks the user to correct the highlighted fields.
- Successful submission still returns HTTP status 201.
- Readable result and raw JSON still display.
- Clear removes inputs, errors, red borders, status, and results.

## Key learning
Client-side validation gives users immediate feedback.

aria-describedby connects an error message to its related field.
aria-invalid="true" identifies a field that failed validation.

novalidate disables the browser’s automatic validation so custom
JavaScript validation can control the experience.

A JavaScript const variable can only be declared once with the same
name in the same scope. Duplicate declarations can stop the entire
script from working.

Client-side validation improves usability, but a real application
should also validate data on the server because browser-side
validation can be bypassed.