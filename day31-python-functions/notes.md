# Day 31 — Improve the Enquiry App Using Functions

## What I learned

- How to create functions.
- How to pass information into functions.
- How to return results from functions.
- How to reduce repeated code.
- How to organise a longer script into clear sections.
- How to improve code without changing how the app behaves.

## What the script does

The script still provides four options: create a new enquiry, update an enquiry status, search enquiries, or show a summary report.

The main improvement is that the code is now organised into functions. Each major task has its own function, making the script easier to read, maintain, and extend.

## Functions created

- show_main_menu()
- get_matching_option()
- create_enquiry()
- load_enquiries()
- find_enquiry()
- update_enquiry_status()
- search_enquiries()
- show_summary_report()
- main()

## New skill

I learned how to use functions to organise a Python application and avoid repeating the same logic.

## Testing

I tested five scenarios:

1. Created an enquiry and confirmed the create function worked.
2. Updated the enquiry status and confirmed the load and find functions worked.
3. Searched by customer name and confirmed the search function worked.
4. Displayed the summary report and confirmed the summary function worked.
5. Entered an invalid menu choice and confirmed the app handled it safely.

All five tests passed.

## Why this matters

Functions make code easier to understand, maintain, and extend. Instead of one long script, each part of the application now has a clear responsibility.