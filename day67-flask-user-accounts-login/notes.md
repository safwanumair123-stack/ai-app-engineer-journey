# Day 67 — Add User Accounts and Login

## What I learned

- How to store user accounts securely.
- How to hash passwords.
- How to create a registration page.
- How to create a login page.
- How to use browser sessions.
- How to protect application routes.
- How to log users out.

## What I built

I added user accounts and login to the Enquiry Tracker.

The application now has a users table in the SQLite database. Users can create an account with their full name, email address, and password. Passwords are hashed before they are saved, so the application does not store plain-text passwords.

Users can log in with their email address and password. After logging in, they can access the Enquiry Tracker. Each user can only see and manage their own enquiries.

The application now has a Log out link. When a user logs out, their session is cleared and they are returned to the login page.

## New skill

I learned how to add authentication and route protection to a web application.

## Testing

I tested five scenarios:

1. Created a new user account.
2. Logged in with the correct email address and password.
3. Tried to access the enquiry list without logging in.
4. Created an enquiry while logged in and confirmed it was linked to my account.
5. Logged out and confirmed that I could no longer access the enquiry list.

All five tests passed.