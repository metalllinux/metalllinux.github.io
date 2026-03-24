---
title: "Function to calculate the time difference between pairs of lines"
category: "general-linux"
tags: ["python", "code", "calculate", "time", "difference"]
---

```
from datetime import datetime
from dateutil import parser

# Function to calculate the time difference between pairs of lines
def calculate_time_difference(file_path):
    # Open the file and read lines
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # List to store the time differences
    time_differences = []

    # Iterate over the lines, two at a time
    for i in range(0, len(lines) - 1, 2):
        # Extract timestamps from consecutive lines (line i and line i+1)
        timestamp1 = lines[i].strip()
        timestamp2 = lines[i + 1].strip()

        # Parse the timestamps using the dateutil parser (handles the format)
        time1 = parser.isoparse(timestamp1)
        time2 = parser.isoparse(timestamp2)

        # Calculate the time difference
        time_diff = time2 - time1
        time_differences.append(time_diff)

    # Print or return the results
    for idx, diff in enumerate(time_differences):
        print(f"Time difference between line {2*idx+1} and {2*idx+2}: {diff}")

# Example usage
calculate_time_difference("temp3")
```