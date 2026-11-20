# Day 59 — Add Enquiry Value by Status

## What I learned

- How to group numeric values by a status field.
- How to calculate a total value for each status.
- How to display value-based dashboard metrics.
- How to test calculated grouped totals.
- How to connect dashboard metrics to a practical sales pipeline.

## What I built

I added enquiry value by status to the Enquiry Tracker dashboard.

The dashboard now shows the total estimated value for each enquiry status: New, In progress, and Closed. This helps a small business owner see not only how many enquiries are in each status, but also how much potential value is sitting in each stage of the pipeline.

## New skill

I learned how to calculate grouped business metrics from stored records.

## Testing

I tested five scenarios:

1. Created three enquiries with different estimated values and statuses.
2. Checked that the value for each status was correct.
3. Changed an enquiry status and checked that the value moved to the correct status.
4. Deleted an enquiry and checked that its value was removed from the correct status.
5. Deleted all enquiries and checked that all status values returned to zero.

All five tests passed.