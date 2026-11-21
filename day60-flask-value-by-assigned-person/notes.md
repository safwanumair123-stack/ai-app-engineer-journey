# Day 60 — Add Enquiry Value by Assigned Person

## What I learned

- How to group numeric values by a person.
- How to calculate a total value for each assigned team member.
- How to display value-based team metrics.
- How to handle enquiries that have no assigned person.
- How to test grouped calculated values.

## What I built

I added enquiry value by assigned person to the Enquiry Tracker dashboard.

The dashboard now calculates the total estimated value assigned to each team member. If an enquiry has no assigned person, its value is grouped under Unassigned. This helps a small business owner see how much potential value is assigned to each person and identify workload or opportunity imbalances.

## New skill

I learned how to calculate grouped business metrics by team member.

## Testing

I tested five scenarios:

1. Created three enquiries assigned to different team members.
2. Checked that the value for each assigned person was correct.
3. Created an enquiry without assigning a person and checked that its value appeared under Unassigned.
4. Changed an enquiry assignment and checked that the value moved to the correct person.
5. Deleted an enquiry and checked that its value was removed from the correct person.

All five tests passed.