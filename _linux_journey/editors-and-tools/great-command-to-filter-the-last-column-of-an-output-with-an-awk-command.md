---
title: "Great Command to Filter by the Last Column with an awk Command"
category: "editors-and-tools"
tags: ["editors-and-tools", "great", "command", "filter", "last"]
---

# Great Command to Filter by the Last Column with an awk Command

Example for a SAR report:

awk -F' ' '$NF == "0.0%" {print}' <FILE>

