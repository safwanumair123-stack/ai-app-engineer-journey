# Day 30 — Add Priority Levels to Enquiry Records

## What I learned

- How to add a new field to an existing CSV workflow.
- How to validate a priority selection.
- How to store priority consistently.
- How to count records by priority.
- How to expand a summary report without breaking existing features.

## What the script does

The script gives the user four options: create a new enquiry, update an enquiry status, search enquiries, or show a summary report.

When creating an enquiry, the user now chooses a priority level: Low, Medium, or High. The script validates the selected priority and saves it with the enquiry record.

The summary report now counts total enquiries, enquiries by status, enquiries by enquiry type, and enquiries by priority.

## New skill

I learned how to add a new field to an existing CSV workflow and update the summary report to include the new field.

## Testing

I tested five scenarios:

1. Created a high-priority enquiry and confirmed it was saved correctly.
2. Created a medium-priority enquiry and confirmed it was appended without overwriting the first record.
3. Created a low-priority enquiry and confirmed all three priority levels could be saved.
4. Entered an invalid priority choice and confirmed the script rejected it.
5. Displayed the summary report and confirmed the priority counts were correct.

All five tests passed.

## Why this matters

Priority levels make an enquiry register more useful for real-world triage. They help a small business understand which requests need attention first, rather than treating every enquiry with the same urgency.