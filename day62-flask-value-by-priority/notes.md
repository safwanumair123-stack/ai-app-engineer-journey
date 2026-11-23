# Day 62 — Add Enquiry Value by Priority

## What I learned

- How to group numeric values by priority.
- How to calculate a total value for each priority.
- How to display value-based prioritisation metrics.
- How to test grouped calculated values.
- How to connect dashboard metrics to workload decisions.

## What I built

I added enquiry value by priority to the Enquiry Tracker dashboard.

The dashboard now calculates the total estimated value for each priority: Low, Medium, and High. This helps a small business owner see where the most valuable work is concentrated and decide which enquiries need attention first.

## New skill

I learned how to calculate grouped business metrics by priority.

## Testing

I tested five scenarios:

1. Created enquiries with different priorities and estimated values.
2. Checked that the value for each priority was correct.
3. Changed an enquiry priority and checked that the value moved to the correct priority.
4. Deleted an enquiry and checked that its value was removed from the correct priority.
5. Deleted all enquiries and checked that all priority values returned to zero.

All five tests passed.