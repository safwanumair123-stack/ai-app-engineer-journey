# Day 70 — Improve Error Handling and User Messages

## What I learned

- How to add friendly error pages to a Flask application.
- How to handle missing pages using a 404 error handler.
- How to handle unexpected server errors using a 500 error handler.
- How to show clear validation messages to users.
- How to keep the application working when database errors occur.
- How to make dropdown options appear correctly in the dashboard.
- How to display the correct user name and role after logging in.
- How to show all users and all enquiries in the Admin dashboard.

## What I built

I improved the error handling and user messages in the Enquiry Tracker web application.

The application now shows a friendly Page not found error page when a user visits an address that does not exist. It also shows a friendly error page if an unexpected server error occurs.

I improved validation messages for invalid customer email addresses and invalid customer phone numbers. I also added clear messages for successful actions, such as creating an account, logging in, creating an enquiry, updating an enquiry, adding a note, closing an enquiry, reopening an enquiry, and deleting an enquiry.

I fixed the dashboard so that the enquiry type, priority, and source dropdowns display their correct options. I also made sure that newly created accounts appear in the Admin dashboard and that newly created enquiries appear in the enquiry list.

## New skill

I learned how to improve error handling and user messages in a web application.

## Testing

I tested the application in Google Chrome.

All 10 Day 70 tests passed.