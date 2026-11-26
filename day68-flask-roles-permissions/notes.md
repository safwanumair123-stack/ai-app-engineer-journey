# Day 68 — Add Basic Roles and Permissions

## What I learned

- How to add a role to a user account.
- How to store permissions in a database.
- How to protect admin-only pages.
- How to show admin links only to admins.
- How to let admins view all users and enquiries.
- How to keep regular users limited to their own enquiries.

## What I built

I added basic roles and permissions to the Enquiry Tracker.

The users table now includes a role field. The first user who registers becomes an Admin. Every later user becomes a regular User.

Admin users can access an admin-only dashboard. The dashboard shows all registered users and all enquiries created by every user. Regular users cannot access the admin dashboard.

The enquiry list remains protected by login. Regular users can still create, view, edit, close, reopen, and delete only their own enquiries.

## New skill

I learned how to add roles and permissions to a web application.

## Testing

I tested five scenarios:

1. Registered the first user and confirmed the account was assigned the Admin role.
2. Registered a second user and confirmed the account was assigned the User role.
3. Logged in as the Admin and opened the admin dashboard.
4. Logged in as a regular User and confirmed the admin dashboard was not accessible.
5. Confirmed that the Admin dashboard showed all users and all enquiries.

All five tests passed.