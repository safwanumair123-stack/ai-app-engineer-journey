## Running through a local development server

From this folder, run:

```powershell
py -m http.server 8000 --bind 127.0.0.1
```

Then open:

```text
http://127.0.0.1:8000/
```

Press Ctrl+C in the terminal to stop the server.

## Day 9 responsive check

The app was tested at a 375-pixel width using Chrome DevTools.

The form, buttons, status message, readable result, and raw JSON
remained readable and usable. No additional CSS changes were needed.

## Day 10 accessibility review

The form labels are correctly associated with their inputs using
matching `for` and `id` values.

The status message uses `role="status"`, which provides polite
live-region behaviour for dynamic updates.

Successful submission, clearing, and spaces-only validation were
tested after the accessibility review. All checks passed.

## Day 11 CSS

This version adds an external stylesheet named `styles.css`.

The stylesheet is connected in `index.html` using:

```html
<link rel="stylesheet" href="styles.css">
```

It provides base styling for the page, form fields, buttons,
readable result, and raw JSON display.

The inline `white-space: pre-wrap;` rule was moved from the result
paragraph into the external stylesheet.

## Day 12 CSS variables

This version introduces CSS custom properties for repeated values.

The variables are defined in `:root` and used with `var()`.

They include colours, spacing values, and the main font family.
The visual appearance and app behaviour remain the same as Day 11.

## Day 13 button feedback

The submit button is styled as the primary action using a dark
background and white text.

The Clear button is styled as a secondary action using a light
background and dark text.

Both buttons include hover feedback. The app’s submission and
clearing behaviour remain unchanged.

## Day 14 form errors

This version adds field-level validation messages.

Each field has an associated error-message element connected using
`aria-describedby`. When validation fails, JavaScript sets
`aria-invalid="true"` on the field and CSS applies a red border and
light red background.

The form uses `novalidate` so the custom JavaScript validation
controls the user experience. Client-side validation improves
usability but does not replace server-side validation.

## Day 15 CSS review

The stylesheet was reviewed and organised into labelled sections:
design tokens, base styles, form styles, button styles, error
styles, and result styles.

No visual values or app behaviour were changed. The review confirmed
that validation, submission, response display, and clearing still work.

## Day 16 JavaScript functions

This version organises the JavaScript into smaller named functions.

The app behaviour remains the same as Day 15, but the submit and
Clear handlers are now shorter and easier to understand.

Functions include validation, error clearing, result clearing,
payload creation, success display, and error display.