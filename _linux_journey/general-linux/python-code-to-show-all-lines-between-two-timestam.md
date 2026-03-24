---
title: "Define the default year and the start and end times for the range"
category: "general-linux"
tags: ["python", "code", "show", "all", "lines"]
---

```
from datetime import datetime

# Define the default year and the start and end times for the range
default_year = "2025"
start_time = datetime.strptime(f"{default_year} Jan 16 14:22:00", "%Y %b %d %H:%M:%S")
end_time = datetime.strptime(f"{default_year} Jan 16 22:58:59", "%Y %b %d %H:%M:%S")

# Function to parse the timestamp from a log line
def extract_timestamp(line):
    try:
        # Assuming the timestamp is at the beginning of each line (first 15 characters)
        timestamp_str = line[:15]  # First 15 characters represent the timestamp
        # Add the default year to the timestamp for parsing
        timestamp_str_with_year = f"{default_year} {timestamp_str}"
        return datetime.strptime(timestamp_str_with_year, "%Y %b %d %H:%M:%S")
    except ValueError:
        return None

# Path to the log file
log_file_path = "messages"  # Update this to your log file path

# Read the log file and filter lines based on the timestamp
with open(log_file_path, 'r') as file:
    for line in file:
        timestamp = extract_timestamp(line)
        if timestamp and start_time <= timestamp <= end_time:
            print(line.strip())  # Print the line if it's within the time range
```