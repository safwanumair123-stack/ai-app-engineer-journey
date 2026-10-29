# Day 12 — CSS Variables

## Completed
- Created a Day 12 copy of the practice app.
- Updated the browser tab title and visible heading to Day 12.
- Added CSS custom properties at the top of styles.css.
- Defined reusable values for text colour, border colour,
  background colours, spacing, and font family.
- Replaced repeated CSS values with var() references.
- Tested the app through the local development server.
- Confirmed that the appearance remained the same as Day 11.
- Confirmed that submission, response display, and clearing
  still worked.

## CSS variables added
- --main-text-color
- --border-color
- --page-background
- --code-background
- --main-spacing
- --small-spacing
- --main-font

## Checks passed
- The page appearance remained unchanged.
- Successful submission still worked.
- Readable result and raw JSON still displayed.
- Clear form and result still worked.

## Key learning
CSS custom properties store reusable values.

They are defined with two hyphens, for example:
--main-text-color: #1f2937;

They are used with var(), for example:
color: var(--main-text-color);

Using variables makes future design changes easier because a value
can be updated in one place.