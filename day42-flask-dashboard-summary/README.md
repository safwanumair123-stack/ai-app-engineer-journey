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

# Day 35 — Connect the Enquiry App to an External API

This project adds an external API integration to the enquiry application.

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
- Fetches sample API posts from JSONPlaceholder.
- Sends HTTP GET requests.
- Receives and parses JSON responses.
- Handles successful and failed API requests.
- Handles timeouts and connection errors.
- Uses a .gitignore rule to keep changing local JSON test data out of GitHub.

## How to run

Open a terminal inside the day35-python-api-data folder and run:

py enquiry_api.py

## API used

This project uses JSONPlaceholder:

https://jsonplaceholder.typicode.com/posts

## Menu options

1. Create a new enquiry
2. Update an enquiry status
3. Search enquiries
4. Show summary report
5. Show raw JSON data
6. Fetch sample API posts

## API request handling

The app checks the HTTP status code and handles:

- 200 Successful response
- 404 Not found
- Timeout
- Connection error
- General request error
- Invalid JSON response

# Day 36 — Plan the Enquiry Tracker Interface

This project plans the interface and user flow for an Enquiry Tracker for small and micro-businesses.

## Product purpose

The Enquiry Tracker helps a small business capture customer enquiries, assign priorities, track progress, and follow up without losing important information.

## Target user

The primary user is a small or micro-business owner, administrator, or team member who handles customer enquiries, quotation requests, support requests, or supplier requests.

## Main screens

- Dashboard
- Enquiry list
- Create enquiry
- Enquiry details
- Search and filters
- Summary report

## Core user jobs

- Create a new enquiry.
- See a list of enquiries.
- Search for an enquiry.
- Open an enquiry.
- Update an enquiry status.
- Change an enquiry priority.
- Add a next action.
- View a summary report.

## First version scope

The first version will include a dashboard, enquiry list, enquiry creation, enquiry details, status updates, priority updates, search and filters, and a summary report.

It will not include automatic customer emails, automatic WhatsApp messages, automatic quotations, complex user accounts, multi-user permissions, or payment processing.

## Human approval and traceability

AI may later help draft a response, classify an enquiry, or suggest a next action.

However, the user must review and approve anything customer-facing.

The system should record what AI suggested, what the user changed, what the user approved, when the action happened, and who approved it.
# Day 37 — Create the First Enquiry Tracker Interface

This project creates the first HTML interface for the Enquiry Tracker.

## Features

- Displays a clear page heading and product purpose.
- Includes a form to create a new enquiry.
- Includes fields for customer name, enquiry type, priority, enquiry details, and next action.
- Includes dropdown menus for enquiry type and priority.
- Includes Create enquiry and Clear form buttons.
- Includes a section for the enquiry list.
- Uses semantic HTML structure.
- Can be tested through a local server.

## How to run

Open a terminal inside the day37-html-enquiry-form folder and run:

py -m http.server 8000 --bind 127.0.0.1

Then open:

http://127.0.0.1:8000/

## Current limitation

The form does not save data yet.

The next step will be to connect the interface to Python logic so the enquiry can be saved and displayed.

# Day 38 — Style the Enquiry Tracker Interface

This project adds basic CSS styling to the Enquiry Tracker interface.

## Features

- Displays a clear page heading and product purpose.
- Includes a form to create a new enquiry.
- Includes fields for customer name, enquiry type, priority, enquiry details, and next action.
- Includes dropdown menus for enquiry type and priority.
- Includes Create enquiry and Clear form buttons.
- Includes a section for the enquiry list.
- Uses an external CSS file.
- Uses a clean, readable layout.
- Includes a mobile-friendly layout for smaller screens.
- Can be tested through a local server.

## How to run

Open a terminal inside the day38-css-enquiry-interface folder and run:

py -m http.server 8000 --bind 127.0.0.1

Then open:

http://127.0.0.1:8000/

## Current limitation

The form does not save data yet.

The next step will be to connect the interface to Python logic so the enquiry can be saved and displayed.

# Day 39 — Connect the Enquiry Form to Flask

This project connects the Enquiry Tracker HTML form to a Flask web application.

## Features

- Displays an enquiry form in the browser.
- Receives form data using Flask.
- Validates customer name, enquiry type, and priority.
- Displays success and error messages.
- Generates a reference number.
- Captures the created date and time.
- Saves enquiries to a JSON file.
- Displays saved enquiries on the page.
- Uses a .gitignore rule to keep changing local JSON test data out of GitHub.

## How to run

Open a terminal inside the day39-flask-enquiry-form folder and run:

py app.py

Then open:

http://127.0.0.1:5000/

## Project structure

day39-flask-enquiry-form
├── app.py
├── templates
│   └── index.html
├── static
│   └── styles.css
├── notes.md
└── README.md

## Validation rules

- Customer name is required.
- Enquiry type must be selected from approved options.
- Priority must be selected from approved options.
- Reference number is generated automatically.
- Created date and time are generated automatically.

## Approved enquiry types

- General enquiry
- Quotation
- Support
- Partnership

## Approved priorities

- Low
- Medium
- High
# Day 40 — View and Update Individual Enquiry Records

This project adds an enquiry details page to the Enquiry Tracker.

## Features

- Creates new enquiry records.
- Displays all saved enquiries.
- Opens an individual enquiry by reference number.
- Displays the full enquiry record.
- Updates enquiry status.
- Updates enquiry priority.
- Updates the next action.
- Saves updated records to JSON.
- Handles invalid reference numbers safely.
- Uses a .gitignore rule to keep changing local JSON test data out of GitHub.

## How to run

Open a terminal inside the day40-flask-enquiry-details folder and run:

py app.py

Then open:

http://127.0.0.1:5000/

## Main routes

- / — Enquiry list and create-enquiry form
- /create-enquiry — Creates a new enquiry
- /enquiry/<reference_number> — Displays one enquiry
- /update-enquiry/<reference_number> — Updates one enquiry

## Approved statuses

- New
- In progress
- Closed

## Approved priorities

- Low
- Medium
- High
# Day 41 — Add Search and Filters to the Enquiry Tracker

This project adds search and filter functionality to the Enquiry Tracker web application.

## Features

- Creates new enquiry records.
- Assigns a unique reference number to each enquiry.
- Captures the current date and time.
- Saves enquiries to a JSON file.
- Assigns a priority level to each enquiry.
- Updates enquiry status.
- Updates enquiry priority.
- Updates the next action.
- Searches enquiries by customer name.
- Searches enquiries by enquiry type.
- Filters enquiries by status.
- Filters enquiries by priority.
- Keeps search and filter values selected after applying filters.
- Displays matching results clearly.
- Handles searches with no results safely.
- Uses a .gitignore rule to keep changing local JSON test data out of GitHub.

## How to run

Open a terminal inside the day41-flask-search-filters folder and run:

py app.py

Then open:

http://127.0.0.1:5000/

## Search options

- Customer name
- Enquiry type

## Filter options

- Status
- Priority

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
# Day 41 — Add Search and Filters to the Enquiry Tracker

This project adds search and filter functionality to the Enquiry Tracker web application.

## Features

- Creates new enquiry records.
- Assigns a unique reference number to each enquiry.
- Captures the current date and time.
- Saves enquiries to a JSON file.
- Assigns a priority level to each enquiry.
- Updates enquiry status.
- Updates enquiry priority.
- Updates the next action.
- Searches enquiries by customer name.
- Searches enquiries by enquiry type.
- Filters enquiries by status.
- Filters enquiries by priority.
- Keeps search and filter values selected after applying filters.
- Displays matching results clearly.
- Handles searches with no results safely.
- Uses a .gitignore rule to keep changing local JSON test data out of GitHub.

## How to run

Open a terminal inside the day41-flask-search-filters folder and run:

py app.py

Then open:

http://127.0.0.1:5000/

## Search options

- Customer name
- Enquiry type

## Filter options

- Status
- Priority

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

# Day 42 — Add a Dashboard Summary to the Enquiry Tracker

This project adds a dashboard summary to the Enquiry Tracker web application.

## Features

- Creates new enquiry records.
- Assigns a unique reference number to each enquiry.
- Captures the current date and time.
- Saves enquiries to a JSON file.
- Assigns a priority level to each enquiry.
- Updates enquiry status.
- Updates enquiry priority.
- Updates the next action.
- Searches enquiries by customer name.
- Searches enquiries by enquiry type.
- Filters enquiries by status.
- Filters enquiries by priority.
- Displays a dashboard summary.
- Shows total enquiries.
- Shows enquiries by status.
- Shows enquiries by priority.
- Shows enquiries by enquiry type.
- Handles searches with no results safely.
- Uses a .gitignore rule to keep changing local JSON test data out of GitHub.

## How to run

Open a terminal inside the day42-flask-dashboard-summary folder and run:

py app.py

Then open:

http://127.0.0.1:5000/

## Dashboard summary

The dashboard shows:

- Total enquiries
- New enquiries
- In-progress enquiries
- Closed enquiries
- High-priority enquiries
- Enquiries by type
- Enquiries by priority

## Search options

- Customer name
- Enquiry type

## Filter options

- Status
- Priority

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

# Day 42 — Add a Dashboard Summary to the Enquiry Tracker

This project adds a dashboard summary to the Enquiry Tracker web application.

## Features

- Creates new enquiry records.
- Assigns a unique reference number to each enquiry.
- Captures the current date and time.
- Saves enquiries to a JSON file.
- Assigns a priority level to each enquiry.
- Updates enquiry status.
- Updates enquiry priority.
- Updates the next action.
- Searches enquiries by customer name.
- Searches enquiries by enquiry type.
- Filters enquiries by status.
- Filters enquiries by priority.
- Displays a dashboard summary.
- Shows total enquiries.
- Shows enquiries by status.
- Shows enquiries by priority.
- Shows enquiries by enquiry type.
- Handles searches with no results safely.
- Uses a .gitignore rule to keep changing local JSON test data out of GitHub.

## How to run

Open a terminal inside the day42-flask-dashboard-summary folder and run:

py app.py

Then open:

http://127.0.0.1:5000/

## Dashboard summary

The dashboard shows:

- Total enquiries
- New enquiries
- In-progress enquiries
- Closed enquiries
- High-priority enquiries
- Enquiries by type
- Enquiries by priority

## Search options

- Customer name
- Enquiry type

## Filter options

- Status
- Priority

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