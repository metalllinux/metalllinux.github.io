---
title: "Example awk Command to Check Timestamps of messages Files"
category: "editors-and-tools"
tags: ["editors-and-tools", "example", "awk", "command", "check"]
---

# Example awk Command to Check Timestamps of messages Files
```
awk '$1 == "Jul" && $2 == "31" && $3 >= "10:20:00" && $3 <= "10:22:59"' your_log_file.log
```
