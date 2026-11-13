# Day 35 — Connect the Enquiry App to an External API

## What I learned

- What an API is.
- How HTTP requests work.
- How to send a GET request.
- How to receive and parse JSON.
- How to handle successful and failed requests.
- How to display API data in a readable format.

## What the script does

The script still provides the existing enquiry features: create a new enquiry, update an enquiry status, search enquiries, show a summary report, and display raw JSON data.

A new option was added to fetch sample API posts from JSONPlaceholder. The script sends a GET request, receives a JSON response, converts it into Python data, and displays the first three posts.

## New skill

I learned how to use the requests library to connect a Python application to an external API.

## Testing

I tested five scenarios:

1. Created the first enquiry and confirmed the local JSON file was created.
2. Fetched sample API posts and confirmed the app received and displayed JSON data.
3. Updated the first enquiry status and confirmed the local JSON file was updated.
4. Displayed the raw JSON data and confirmed the saved enquiry structure.
5. Disconnected the internet and confirmed the app displayed a safe API connection error.

All five tests passed.

## Why this matters

APIs allow applications to communicate with external services. Learning to send requests, receive JSON, and handle failures prepares the enquiry app for future integrations with AI services, CRMs, email tools, and automation platforms.