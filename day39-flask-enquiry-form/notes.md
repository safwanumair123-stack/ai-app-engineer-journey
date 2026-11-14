# Day 39 — Connect the Enquiry Form to Flask

## What I learned

- What Flask is.
- How to create a basic web application.
- How to connect an HTML form to Python.
- How to receive form data.
- How to validate input.
- How to save data to JSON.
- How to display a confirmation message.

## What I built

I created a Flask web application for the Enquiry Tracker.

The HTML form now sends data to Flask. Flask validates the customer name, enquiry type, and priority. If the data is valid, Flask creates an enquiry record, saves it to a JSON file, and displays a success message.

If the data is invalid, Flask displays an error message and does not save the enquiry.

## New skill

I learned how to use Flask to connect an HTML form to Python and save form data to a JSON file.

## Testing

I tested five scenarios:

1. Opened the web page and confirmed Flask served the interface.
2. Created a valid enquiry and confirmed it was saved and displayed.
3. Submitted an enquiry without a customer name and confirmed the error message appeared.
4. Submitted an enquiry without selecting an enquiry type and confirmed the error message appeared.
5. Submitted an enquiry without selecting a priority and confirmed the error message appeared.

All five tests passed.

## Why this matters

Connecting a user interface to backend logic is an important step in building a practical web application. It allows a business user to submit information through a browser and see the result immediately.