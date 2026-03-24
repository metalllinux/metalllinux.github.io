---
title: "Create a set to store the lines with a value in the second column"
category: "general-linux"
tags: ["python", "script", "remove", "any", "lines"]
---

```
with open('<input_file_with_two_columns_to_use>', 'r') as file:
    lines = file.readlines()

# Create a set to store the lines with a value in the second column
lines_to_delete = set()

# Iterate through the lines and identify the lines to delete
for line in lines:
    columns = line.strip().split()
    if len(columns) >= 2 and columns[1]:
        lines_to_delete.add(line.strip())

# Write the output to a new file, skipping the lines to be deleted
with open('<output_file>', 'w') as file:
    for line in lines:
        if line.strip() not in lines_to_delete:
            file.write(line)
```