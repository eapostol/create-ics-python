from datetime import datetime, timedelta
from ics import Calendar, Event

# Create a new calendar
calendar = Calendar()

# Define the events
events = [
    ("Check-in opens for PR119", datetime(2025, 4, 11, 9, 0)),
    ("Begin departure checklist", datetime(2025, 4, 13, 18, 0)),
    ("Leave for Pearson Airport", datetime(2025, 4, 13, 20, 0)),
    ("Check-in at Terminal 3", datetime(2025, 4, 13, 21, 30)),
    ("Boarding begins for PR119", datetime(2025, 4, 14, 0, 30)),
    ("Flight PR119 Departs", datetime(2025, 4, 14, 1, 35)),
]

# Add each event to the calendar
for title, start_time in events:
    event = Event()
    event.name = title
    event.begin = start_time
    event.duration = timedelta(minutes=30)
    calendar.events.add(event)

# Save to a .ics file
with open("Philippine_Airlines_PR119_Reminders-02.ics", "w") as f:
    f.writelines(calendar)

print("✅ Calendar file created: Philippine_Airlines_PR119_Reminders.ics")
