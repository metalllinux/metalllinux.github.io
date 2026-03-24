---
title: "File name"
category: "kernel-and-system-internals"
tags: ["kernel-and-system-internals", "useful", "python", "application", "sort"]
---

```
import re

# File name
input_file = "input.txt"
output_file = "sorted_output.txt"

def extract_timestamp(line):
    """
    Extracts the numeric value of the timestamp from a line.
    """
    match = re.search(r"<(\d+\.\d+)>$", line)
    return float(match.group(1)) if match else 0

def sort_lines_by_timestamp(file_name):
    """
    Reads a file, sorts its lines by the timestamp at the end of each line,
    and writes the sorted lines to a new file.
    """
    with open(file_name, "r") as f:
        lines = f.readlines()
    
    # Sort lines by extracted timestamp in descending order
    sorted_lines = sorted(lines, key=extract_timestamp, reverse=True)
    
    # Write sorted lines to output file
    with open(output_file, "w") as f:
        f.writelines(sorted_lines)

if __name__ == "__main__":
    sort_lines_by_timestamp(input_file)
```
* The `strace` output has to contain lines that look like this:
```
11:13:44.597126 wait4(22322, [{WIFEXITED(s) && WEXITSTATUS(s) == 0}], 0, NULL) = 22322 <0.000057>
```