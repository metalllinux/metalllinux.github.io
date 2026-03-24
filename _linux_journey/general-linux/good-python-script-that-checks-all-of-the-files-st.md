---
title: "Directory to search"
category: "general-linux"
tags: ["good", "python", "script", "checks", "all"]
---

```
import os

# Directory to search
directory = '.'

# Loop through each file in the directory
for filename in os.listdir(directory):
    if filename.startswith('dnf'):
        # Open the file
        with open(os.path.join(directory, filename), 'r') as file:
            # Loop through each line in the file
            for line_num, line in enumerate(file, start=1):
                # Check if the line contains the word "error"
                if 'error' in line.lower():
                    # Print the filename and the line with the word "error"
                    print(f'File: {filename}, Line {line_num}: {line.strip()}')
```