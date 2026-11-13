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

## Day 17 submit button loading state

This version adds a loading state to the submit button.

While a request is running, the button text changes to
"Sending...", the button is disabled, and aria-busy is set.

This prevents duplicate submissions and gives clearer feedback.

The button is restored after the request succeeds or fails.

# Day 18 — Loading Indicator

This practice app sends a POST request to a practice API.

While the request is running, a CSS spinner appears beside the
status message. The submit button changes to "Sending...", becomes
disabled, and uses aria-busy for accessibility.

This prevents duplicate submissions and gives clearer feedback
while the app waits for the response.

The spinner, button, and status message are restored after the
request succeeds or fails.

## Day 18 changes
- Added a CSS spinner beside the status message.
- Added a setLoading() function to coordinate loading UI.
- Showed the spinner and disabled the submit button during loading.
- Restored the UI after success or failure.
- Prevented duplicate submissions while a request was running.

# Day 19 — Clear Button Loading State

This practice app sends a POST request to a practice API.

While the request is running, both the submit button and the Clear
button are disabled.

The submit button changes to "Sending..." and shows a loading state.
The Clear button cannot clear the form, errors, status, spinner, or
results while the request is running.

This prevents users from interrupting a request or clearing results
before the response has arrived.

Both buttons are restored after the request succeeds or fails.

## Day 19 changes
- Disabled the Clear button during loading.
- Updated setLoading() to control both buttons.
- Added a disabled-state check to the Clear handler.
- Added styling for the disabled Clear button.
- Kept the spinner and submit-button loading state from Day 18.

# Day 20 — Character Counter

This practice app sends a POST request to a practice API.

The post-content field includes a live character counter and a
maximum limit of 200 characters.

As the user types, the counter updates immediately. At 160 characters
or more, the counter changes to a warning colour. At 200 characters,
it changes to a limit colour and the textarea prevents further input.

The Clear button resets the counter along with the form, errors,
status, spinner, and results.

## Day 20 changes
- Added a live character counter to the content field.
- Added a 200-character maximum using maxlength.
- Added warning and limit visual states.
- Added aria-live="polite" for accessible counter updates.
- Reset the counter when the form is cleared.
- Kept the loading safeguards from Day 19.

# Day 21 — Success Confirmation

This practice app sends a POST request to a practice API.

After a successful submission, the app shows a clear green
confirmation message and a "Start another post" button.

The confirmation tells the user that the request succeeded. The
button resets the form, character counter, errors, status, result,
and raw API response so the user can submit another post.

Both "Start another post" and "Clear form and result" use the same
reset function, keeping the behaviour consistent.

## Day 21 changes
- Added a success confirmation section after successful submission.
- Added a Start another post action.
- Added a reusable resetFormForNextPost() function.
- Made Clear and Start another post behave consistently.
- Added accessible live-region behaviour for the confirmation.
- Retained validation, API feedback, loading safeguards, spinner,
  and character counter from earlier days.

  # Day 22 — Python Basics: Enquiry Greeting

This is the first Python practice project in the 30-day learning
journey.

The script collects a customer name and enquiry type, removes extra
spaces, validates the input, and displays a structured enquiry
confirmation.

It demonstrates basic Python concepts:

- print()
- input()
- variables
- strings
- .strip()
- if, elif, and else
- f-strings

## How to run

```powershell
cd day22-python-basics
py enquiry_greeting.py
```

## Business relevance

This simple script demonstrates the core pattern behind many small
business automation tools:

1. Collect information.
2. Validate it.
3. Process it.
4. Produce a clear, useful result.

Later, this pattern can be extended into enquiry triage, quotation
requests, service-request logging, document extraction, and AI
assisted workflows.

# Day 23 — Python Lists and Enquiry Categories

This Python practice script collects a customer name and enquiry
type, then checks whether the enquiry type is approved.

It uses a list of approved enquiry categories and a for loop to
compare the user’s input with each approved option.

The comparison is case-insensitive, so “Quotation”, “QUOTATION”,
and “quotation” all match the approved “Quotation” category.

## Approved enquiry types

- General enquiry
- Quotation
- Support
- Partnership

## How to run

```powershell
cd day23-python-lists
py enquiry_categories.py
```

## Business relevance

Approved categories keep enquiry data consistent.

Consistent data is important for reporting, automation, follow-up,
and traceability. In a real business application, approved categories
could be stored in a database or configuration file rather than
directly in the script.

# Day 24 — Python Dictionaries and Enquiry Records

This Python practice script collects a customer name and enquiry
type, validates the enquiry type, and creates a structured enquiry
record.

The enquiry record stores:

- Reference number
- Customer name
- Enquiry type
- Priority
- Status

After creating the record, the script updates its status from
"New" to "In review" and displays the updated record.

## How to run

```powershell
cd day24-python-dictionaries
py enquiry_record.py
```

## Business relevance

A dictionary is a simple way to represent one business record.

In a real enquiry-management or AI-triage application, a record could
include customer details, enquiry category, priority, assigned owner,
status, timestamps, and an audit trail.

This project demonstrates the first step: collecting validated input
and storing it as a structured record.

# Day 25 — Save Enquiry Records to a CSV File

This Python practice script collects a customer name and enquiry
type, validates the input, and saves each valid enquiry to
enquiry_register.csv.

The CSV file contains:

- Reference number
- Customer name
- Enquiry type
- Priority
- Status

The first time the script runs, it creates the CSV file and writes
the header row. Every later valid enquiry is appended as a new row.

## How to run

```powershell
cd day25-python-csv-records
py enquiry_register.py
```

## Business relevance

A CSV enquiry register is a simple traceability record.

It can be opened in Excel, reviewed later, shared with a team, or
used as the starting point for reporting and automation.

In a real business application, the same idea could support an
enquiry log, service-request register, quotation tracker, or AI
triage workflow.

# Day 26 — Add Timestamps to Enquiry Records

This project extends the enquiry register by adding a timestamp to every enquiry record.

## Features

- Captures the current date and time for each enquiry.
- Adds a created_at column to the CSV register.
- Creates the CSV file and header row on first use.
- Appends new enquiry records without overwriting earlier records.
- Validates enquiry type against approved categories.
- Prevents invalid or incomplete input from being saved.
- Uses a .gitignore rule to keep changing local CSV test data out of GitHub.

## How to run

Open a terminal inside the day26-python-timestamps folder and run:

py enquiry_timestamp.py

## Approved enquiry types

- General enquiry
- Quotation
- Support
- Partnership

## Example CSV row

ENQ-1234,Ahmed Traders,Quotation,Medium,New,2026-11-05 22:20:45

# Day 27 — Update Enquiry Status

This project extends the enquiry register by adding a status update feature.

## Features

- Creates new enquiry records.
- Assigns a unique reference number to each enquiry.
- Captures the current date and time.
- Saves enquiries to a CSV register.
- Allows an enquiry status to be updated.
- Supports New, In progress, and Closed statuses.
- Finds records using their reference number.
- Preserves all other records when updating one enquiry.
- Prevents invalid reference numbers from being processed.
- Uses a .gitignore rule to keep changing local CSV test data out of GitHub.

## How to run

Open a terminal inside the day27-python-status-updates folder and run:

py enquiry_status.py

## Menu options

1. Create a new enquiry
2. Update an enquiry status

## Approved enquiry types

- General enquiry
- Quotation
- Support
- Partnership

## Approved statuses

- New
- In progress
- Closed

# Day 28 — Search Enquiry Records

This project extends the enquiry register by adding a search feature.

## Features

- Creates new enquiry records.
- Assigns a unique reference number to each enquiry.
- Captures the current date and time.
- Saves enquiries to a CSV register.
- Updates enquiry status.
- Searches enquiries by customer name.
- Searches enquiries by enquiry type.
- Supports case-insensitive and partial matching.
- Displays all matching records.
- Handles searches with no results safely.
- Uses a .gitignore rule to keep changing local CSV test data out of GitHub.

## How to run

Open a terminal inside the day28-python-search-records folder and run:

py enquiry_search.py

## Menu options

1. Create a new enquiry
2. Update an enquiry status
3. Search enquiries

## Search options

1. Customer name
2. Enquiry type

## Approved enquiry types

- General enquiry
- Quotation
- Support
- Partnership

## Approved statuses

- New
- In progress
- Closed

# Day 29 — Create an Enquiry Summary Report

This project extends the enquiry register by adding a summary report.

## Features

- Creates new enquiry records.
- Assigns a unique reference number to each enquiry.
- Captures the current date and time.
- Saves enquiries to a CSV register.
- Updates enquiry status.
- Searches enquiries by customer name.
- Searches enquiries by enquiry type.
- Displays a summary report.
- Counts total enquiries.
- Counts enquiries by status.
- Counts enquiries by enquiry type.
- Handles a missing CSV register safely.
- Uses a .gitignore rule to keep changing local CSV test data out of GitHub.

## How to run

Open a terminal inside the day29-python-summary-report folder and run:

py enquiry_summary.py

## Menu options

1. Create a new enquiry
2. Update an enquiry status
3. Search enquiries
4. Show summary report

## Approved enquiry types

- General enquiry
- Quotation
- Support
- Partnership

## Approved statuses

- New
- In progress
- Closed

# Day 30 — Add Priority Levels to Enquiry Records

This project extends the enquiry register by adding priority levels.

## Features

- Creates new enquiry records.
- Assigns a unique reference number to each enquiry.
- Captures the current date and time.
- Saves enquiries to a CSV register.
- Assigns a priority level to each enquiry.
- Supports Low, Medium, and High priorities.
- Updates enquiry status.
- Searches enquiries by customer name.
- Searches enquiries by enquiry type.
- Displays a summary report.
- Counts total enquiries.
- Counts enquiries by status.
- Counts enquiries by enquiry type.
- Counts enquiries by priority.
- Handles a missing CSV register safely.
- Uses a .gitignore rule to keep changing local CSV test data out of GitHub.

## How to run

Open a terminal inside the day30-python-priority-levels folder and run:

py enquiry_priority.py

## Menu options

1. Create a new enquiry
2. Update an enquiry status
3. Search enquiries
4. Show summary report

## Approved enquiry types

- General enquiry
- Quotation
- Support
- Partnership

## Approved priorities

- Low
- Medium
- High

## Approved statuses

- New
- In progress
- Closed

# Day 31 — Improve the Enquiry App Using Functions

This project improves the structure of the enquiry application by organising the code into functions.

## Features

- Creates new enquiry records.
- Assigns a unique reference number to each enquiry.
- Captures the current date and time.
- Saves enquiries to a CSV register.
- Assigns a priority level to each enquiry.
- Updates enquiry status.
- Searches enquiries by customer name.
- Searches enquiries by enquiry type.
- Displays a summary report.
- Uses functions to organise the code.
- Handles invalid menu choices safely.
- Uses a .gitignore rule to keep changing local CSV test data out of GitHub.

## How to run

Open a terminal inside the day31-python-functions folder and run:

py enquiry_functions.py

## Main functions

- show_main_menu()
- get_matching_option()
- create_enquiry()
- load_enquiries()
- find_enquiry()
- update_enquiry_status()
- search_enquiries()
- show_summary_report()
- main()

## Approved enquiry types

- General enquiry
- Quotation
- Support
- Partnership

## Approved priorities

- Low
- Medium
- High

## Approved statuses

- New
- In progress
- Closed

# Day 32 — Add Error Handling to the Enquiry App

This project improves the reliability of the enquiry application by adding error handling around file operations.

## Features

- Creates new enquiry records.
- Assigns a unique reference number to each enquiry.
- Captures the current date and time.
- Saves enquiries to a CSV register.
- Assigns a priority level to each enquiry.
- Updates enquiry status.
- Searches enquiries by customer name.
- Searches enquiries by enquiry type.
- Displays a summary report.
- Uses functions to organise the code.
- Handles missing files safely.
- Handles file permission errors.
- Handles file encoding errors.
- Handles general file-access errors.
- Uses a .gitignore rule to keep changing local CSV test data out of GitHub.

## How to run

Open a terminal inside the day32-python-error-handling folder and run:

py enquiry_error_handling.py

## Error handling

The app uses try and except to handle:

- PermissionError
- UnicodeDecodeError
- OSError

## Approved enquiry types

- General enquiry
- Quotation
- Support
- Partnership

## Approved priorities

- Low
- Medium
- High

## Approved statuses

- New
- In progress
- Closed

# Day 33 — Improve the Structure of the Enquiry App

This project improves the organisation of the enquiry application by separating configuration, user interaction, data logic, and main features.

## Features

- Creates new enquiry records.
- Assigns a unique reference number to each enquiry.
- Captures the current date and time.
- Saves enquiries to a CSV register.
- Assigns a priority level to each enquiry.
- Updates enquiry status.
- Searches enquiries by customer name.
- Searches enquiries by enquiry type.
- Displays a summary report.
- Uses constants for configuration.
- Uses reusable functions for input, display, saving, loading, finding, and counting.
- Handles missing files safely.
- Handles file permission errors.
- Handles file encoding errors.
- Handles general file-access errors.
- Uses a .gitignore rule to keep changing local CSV test data out of GitHub.

## How to run

Open a terminal inside the day33-python-clean-structure folder and run:

py enquiry_clean_structure.py

## Project structure

The script is organised into:

- Configuration
- User interaction
- Data logic
- Main features
- Application entry point

## Approved enquiry types

- General enquiry
- Quotation
- Support
- Partnership

## Approved priorities

- Low
- Medium
- High

## Approved statuses

- New
- In progress
- Closed

# Day 34 — Work with JSON Data in the Enquiry App

This project replaces CSV storage with JSON storage and adds a raw JSON viewer.

## Features

- Creates new enquiry records.
- Assigns a unique reference number to each enquiry.
- Captures the current date and time.
- Saves enquiries to a JSON file.
- Assigns a priority level to each enquiry.
- Updates enquiry status.
- Searches enquiries by customer name.
- Searches enquiries by enquiry type.
- Displays a summary report.
- Displays raw JSON data.
- Handles invalid JSON safely.
- Handles file permission errors.
- Handles general file-access errors.
- Uses a .gitignore rule to keep changing local JSON test data out of GitHub.

## How to run

Open a terminal inside the day34-python-json-data folder and run:

py enquiry_json.py

## Menu options

1. Create a new enquiry
2. Update an enquiry status
3. Search enquiries
4. Show summary report
5. Show raw JSON data

## JSON structure

Each enquiry is stored as a JSON object inside a JSON array.

Example:

[
  {
    "reference_number": "ENQ-1234",
    "customer_name": "Ahmed Traders",
    "enquiry_type": "Quotation",
    "priority": "Medium",
    "status": "New",
    "created_at": "2026-11-13 23:00:00"
  }
]

## Approved enquiry types

- General enquiry
- Quotation
- Support
- Partnership

## Approved priorities

- Low
- Medium
- High

## Approved statuses

- New
- In progress
- Closed