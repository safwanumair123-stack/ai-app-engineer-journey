# Day 10 — Accessibility

## Completed
- Created a Day 10 copy of the practice app.
- Updated the browser tab title and visible heading to Day 10.
- Reviewed the form labels and input connections.
- Confirmed that the title label is connected to the title input.
- Confirmed that the content label is connected to the content textarea.
- Reviewed the status message element.
- Confirmed that role="status" already provides polite live-region
  behaviour for status updates.
- Tested successful submission, clearing, and spaces-only validation.
- Confirmed that the app still works after the accessibility review.

## Checks passed
- Form labels are correctly associated with their inputs.
- The status element uses role="status".
- Successful submission still works.
- Clear still works.
- Spaces-only validation still works.

## Key learning
Accessibility should be reviewed before adding extra code.

A label’s for attribute must exactly match the related input’s id.
The status role helps assistive technology announce dynamic updates.

If an accessibility feature already exists, it is better to verify it
than to add duplicate attributes or unnecessary complexity.