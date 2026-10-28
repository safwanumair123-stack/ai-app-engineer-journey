# Day 8 — Local Web Server

## Completed
- Created a Day 8 copy of the practice app.
- Confirmed Python 3.14.4 was installed.
- Started a local development server using:
  py -m http.server 8000 --bind 127.0.0.1
- Opened the app at:
  http://127.0.0.1:8000/
- Confirmed the form submission and Clear button still worked.
- Viewed index.html, styles.css, and script.js through the server.
- Stopped the server using Ctrl+C.
- Confirmed the app was no longer reachable after stopping it.

## Key learning
Opening a file directly uses a file path beginning with file:///.

Running a local development server uses an HTTP address beginning
with http://127.0.0.1:8000/.

The local server serves the files in the folder where it was started.
It is useful for development and testing, but it is not a production
hosting solution.