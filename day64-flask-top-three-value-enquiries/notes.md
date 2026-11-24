# Day 64 — Add Top Three Highest-Value Enquiries

## What I learned

- How to identify the highest-value records.
- How to display more than one important opportunity.
- How to sort records by estimated value.
- How to handle an empty dashboard safely.
- How to test a ranked business metric.

## What I built

I added a Top three highest-value enquiries section to the Enquiry Tracker dashboard.

The dashboard now identifies and displays the three enquiries with the greatest estimated value. Each entry shows the customer name, estimated value, status, and a link to view the enquiry.

This helps a small business owner quickly identify the most important opportunities without reviewing every enquiry individually.

## New skill

I learned how to create a ranked business metric from stored records.

## Testing

I tested five scenarios:

1. Created four enquiries with different estimated values.
2. Checked that the top three highest-value enquiries appeared in the correct order.
3. Edited the highest-value enquiry and checked that the ranking updated.
4. Deleted an enquiry and checked that the ranking updated.
5. Deleted all enquiries and checked that the dashboard handled the empty state correctly.

All five tests passed.