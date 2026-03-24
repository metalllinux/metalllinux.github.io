---
title: "Open and read the SAR file"
category: "kernel-and-system-internals"
tags: ["kernel-and-system-internals", "python", "script", "checks", "through"]
---

```
def parse_and_sort_sar_file(file_path):
    try:
        # Open and read the SAR file
        with open(file_path, "r") as file:
            lines = file.readlines()
        
        # Search for the headers line and data start index
        headers = None
        data_start_index = 0
        for i, line in enumerate(lines):
            if "%idle" in line.lower():
                headers = line.strip().split()
                data_start_index = i + 1
                break

        if headers is None:
            print("Error: '%idle' column not found in the file!")
            return []

        # Identify the index of the '%idle' column
        idle_index = headers.index("%idle")

        # Collect all rows with relevant data
        rows = []
        for line in lines[data_start_index:]:
            values = line.strip().split()
            try:
                idle_value = float(values[idle_index])
                rows.append(values)  # Add the entire row to the list
            except (ValueError, IndexError):
                continue

        # Sort rows by the '%idle' column in ascending order
        sorted_rows = sorted(rows, key=lambda x: float(x[idle_index]))

        return headers, sorted_rows

    except FileNotFoundError:
        print(f"Error: File not found at path '{file_path}'. Please check the file path.")
        return [], []
    except Exception as e:
        print(f"An error occurred: {e}")
        return [], []


# Path to your SAR file
sar_file_path = "<SAR_FILE_HERE>"

# Parse and sort the SAR file
headers, sorted_rows = parse_and_sort_sar_file(sar_file_path)

if sorted_rows:
    # Display headers and sorted rows
    print("Headers:", headers)
    print("Sorted data:")
    for row in sorted_rows:
        print(" ".join(row))
else:
    print("No valid data rows found.")
```