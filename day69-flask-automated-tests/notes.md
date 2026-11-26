# Day 69 — Add Automated Tests

## What I learned

- How to create automated tests for a Flask application.
- How to test user registration and login.
- How to test protected routes.
- How to test enquiry creation and editing.
- How to test notes and deletion.
- How to test admin and regular user permissions.

## What I built

I added automated tests to the Enquiry Tracker web application.

The tests check that the first registered user becomes an Admin, later users become regular Users, users can log in, enquiry routes are protected, users can create enquiries, users can edit enquiries, users can add notes, users can delete enquiries, regular users cannot access the admin dashboard, and admins can access the admin dashboard.

The tests use a temporary SQLite database, so they do not affect the main application database.

## New skill

I learned how to add automated tests to a web application.

## Testing

I ran the automated test suite using pytest.

All tests passed.