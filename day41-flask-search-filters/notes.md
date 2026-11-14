# Day 41 — Add Search and Filters to the Enquiry Tracker

## What I learned

- How to read search and filter values from a web form.
- How to filter a list of records in Flask.
- How to keep filters active after a search.
- How to display matching results clearly.
- How to handle searches with no results.

## What I built

I added search and filter functionality to the Enquiry Tracker web interface.

The user can search enquiries by customer name or enquiry type. The user can also filter enquiries by status and priority.

The search and filter values remain selected after the user applies the filters. This makes it easier to refine or repeat a search.

## New skill

I learned how to use Flask request arguments to filter records and return matching results to a web interface.

## Testing

I tested five scenarios:

1. Created two enquiries and confirmed both appeared in the enquiry list.
2. Searched by customer name and confirmed only the matching enquiry appeared.
3. Searched by enquiry type and confirmed only the matching enquiry appeared.
4. Filtered by status and priority and confirmed only matching enquiries appeared.
5. Searched for a customer that does not exist and confirmed the app displayed “No matching enquiries found.”

All five tests passed.

## Why this matters

Search and filters make an enquiry tracker more useful for real business workflows. They help a user quickly find relevant records without reading through every enquiry.