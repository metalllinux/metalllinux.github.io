---
title: "Python Script To Remove Any Lines That Have White"
category: "general-linux"
tags: ["python", "script", "remove", "any", "lines"]
---

````
with open('<file_with_two_columns_here>', 'r') as file:
    lines = file.readlines()

with open('<output_file>', 'w') as file:
    for line in lines:
        columns = line.strip().split()
        if len(columns) > 1 and columns[1].strip():
            file.write(line)
```