---
title: "Define the time format present in the logs"
category: "general-linux"
tags: ["python", "code", "check", "time", "between"]
---

from datetime import datetime

# Define the time format present in the logs
time_format = "%Y-%m-%d %H:%M:%S.%f"

# Suppose these are your two log lines
log_line1 = "2023-12-10 14:57:58.501"
log_line2 = "2023-12-10 14:59:58.501"

# Convert the log lines to datetime objects
time1 = datetime.strptime(log_line1, time_format)
time2 = datetime.strptime(log_line2, time_format)

# Calculate the time difference
time_difference = time2 - time1

print(f"The time difference is {time_difference}")

Then run the above code with `python <name>.py`