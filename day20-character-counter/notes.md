# Day 20 — Character Counter

## Completed
- Created a Day 20 copy of the practice app.
- Updated the browser tab title and visible heading to Day 20.
- Added a live character counter below the post-content field.
- Added maxlength="200" to prevent more than 200 characters.
- Added updateCharacterCounter() to count characters as the user types.
- Added an input event listener to update the counter while typing.
- Added a warning state at 160 characters or more.
- Added a limit state when the field reaches exactly 200 characters.
- Added aria-live="polite" so screen readers can announce counter
  changes politely.
- Updated the Clear handler to reset the counter after clearing.
- Called updateCharacterCounter() when the page loads.
- Kept the loading safeguards from Day 19.

## Checks passed
- Initial counter shows 0 / 200 characters.
- Counter updates live while typing.
- Counter becomes orange and bold at 160 characters or more.
- Counter becomes red and bold at 200 characters.
- The textarea prevents typing beyond 200 characters.
- Clear resets the counter to 0 / 200 characters.
- Warning and limit colours disappear after clearing.
- Submit, Clear, spinner, and loading safeguards continue to work.

## Key learning
A character counter gives users immediate feedback while they type.

maxlength prevents users from entering more characters than allowed.

The input event fires whenever the value of a text field changes,
making it useful for live validation and live counters.

aria-live="polite" helps assistive technology announce important
changes without interrupting the user.