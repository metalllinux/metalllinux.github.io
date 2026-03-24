---
title: "Read the values from the first file"
category: "general-linux"
tags: ["python", "script", "check", "fixed", "cves"]
---

```
# Read the values from the first file
with open('<list_of_cves_fixed>', 'r') as f1:
    values = [line.strip() for line in f1]

# Read the lines from the second file and check for matches
with open('<list_of_cves_to_check_against>', 'r') as f2:
    for line in f2:
        line = line.strip()
        if line in values:
            print("Yes")
        else:
            print("No")
```