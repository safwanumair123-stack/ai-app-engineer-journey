# Day 71 — Prepare the Enquiry Tracker for Deployment

## What I learned

- How to prepare a Flask application for deployment.
- How to create a requirements.txt file.
- How to use environment variables for sensitive settings.
- How to configure a Flask application to use a deployment port.
- How to run a Flask application on 0.0.0.0.
- How to disable debug mode for deployment.
- How to keep local database files out of GitHub.

## What I built

I prepared the Enquiry Tracker web application for deployment.

I added a requirements.txt file that lists Flask and Werkzeug. I updated app.py so the secret key, database file location, and port can be set using environment variables. I also configured the application to run on 0.0.0.0 and disabled debug mode, which makes it safer for deployment.

The application still supports user accounts, roles, enquiry creation, editing, notes, deletion, search, filters, sorting, value metrics, CSV export, and friendly error handling.

## New skill

I learned how to prepare a Flask application for deployment.

## Testing

I tested the application in Google Chrome.

All 5 Day 71 tests passed.