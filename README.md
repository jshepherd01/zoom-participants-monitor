# Zoom Participants Monitor
A simple tool for monitoring the number of participants in a zoom meeting.

## Usage
- Join the meeting from your browser (not from the app)
- Paste the contents of start.js into the javascript console and execute
- You should see logs appear in the console immediately, and whenever people join or leave the call
- After the call, but still on zoom.us, paste the contents of retrieve.js into the console and execute
- The console will output a list of numbers. If you see 'Copied to clipboard', carry on to the next step, otherwise you'll need to copy the list yourself.
- Run display.py, and paste the string from the last step as prompted
- A graph should appear on your screen showing the number of participants in the call against the time since you started monitoring
