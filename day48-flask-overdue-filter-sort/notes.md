# Day 48 — Add Overdue Filter and Follow-Up Date Sorting

## What I learned

- How to filter enquiries by overdue status.
- How to sort enquiries by follow-up date.
- How to handle enquiries with no follow-up date.
- How to combine filters and sorting in one view.
- How to make an operations dashboard more useful.

## What I built

I added overdue filtering and follow-up date sorting to the Enquiry Tracker.

The user can choose to show only overdue enquiries. The user can also sort the enquiry list by follow-up date, with the earliest follow-up date appearing first. Enquiries without a follow-up date appear after enquiries with a date.

## New skill

I learned how to sort a list of records by date and combine sorting with filtering.

## Testing

I tested five scenarios:

1. Created three enquiries with different follow-up dates.
2. Applied the overdue-only filter.
3. Confirmed that only overdue enquiries appeared.
4. Applied follow-up date sorting.
5. Confirmed that enquiries appeared from the earliest follow-up date to the latest.

All five tests passed.