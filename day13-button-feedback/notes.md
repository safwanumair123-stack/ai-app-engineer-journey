# Day 13 — Button Feedback and Hierarchy

## Completed
- Created a Day 13 copy of the practice app.
- Updated the browser tab title and visible heading to Day 13.
- Added CSS variables for primary and secondary button colours.
- Styled the submit button as the primary action.
- Styled the Clear button as the secondary action.
- Added hover feedback for both buttons.
- Fixed a malformed CSS rule that prevented the button styles
  from applying.
- Tested the app through the local development server.
- Confirmed that submission and clearing still worked.

## Checks passed
- Send practice post is dark with white text.
- Clear form and result is light with dark text.
- Hover feedback works for both buttons.
- Successful submission still works.
- Clear form and result still works.

## Key learning
Visual hierarchy helps users understand which action is primary.

CSS variables can store button colours and make future changes easier.

A CSS rule must open with { and close with }.
An unclosed rule can prevent later rules from working correctly.

:hover provides visual feedback when a pointer moves over an element,
but it should not be the only way to communicate important information
because touch devices may not support hover.