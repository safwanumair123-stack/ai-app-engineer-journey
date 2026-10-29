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