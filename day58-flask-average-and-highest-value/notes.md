# Day 58 — Add Average and Highest Estimated Value

## What I learned

- How to calculate an average from numeric records.
- How to identify the highest-value enquiry.
- How to display calculated business metrics.
- How to handle a dashboard when there are no enquiries.
- How to test calculated values.

## What I built

I added two dashboard insights to the Enquiry Tracker.

The dashboard now calculates the average estimated value across all enquiries. It also identifies the enquiry with the highest estimated value and displays its reference number, customer name, estimated value, and a link to view the enquiry.

If there are no enquiries, the average estimated value is zero and the dashboard shows that no enquiries have been created yet.

## New skill

I learned how to calculate business metrics from stored records.

## Testing

I tested five scenarios:

1. Created three enquiries with different estimated values.
2. Checked that the total estimated value was correct.
3. Checked that the average estimated value was correct.
4. Checked that the highest-value enquiry was correct.
5. Deleted all enquiries and checked that the dashboard handled the empty state correctly.

All five tests passed.