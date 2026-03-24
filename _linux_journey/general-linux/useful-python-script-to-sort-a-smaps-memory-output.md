---
title: "!/usr/bin/env python3"
category: "general-linux"
tags: ["useful", "python", "script", "sort", "smaps"]
---

```
#!/usr/bin/env python3
import argparse
import re
import sys

def parse_smaps(filepath):
    """
    Parse the smaps file into blocks.
    Each mapping block starts with a header line (memory range + permission info)
    and is followed by lines in the format "Field: value unit".
    Returns a list of dictionaries with 'header' and field keys.
    """
    blocks = []
    current = None

    # A header line typically begins with an address range (hexadecimal numbers).
    header_pattern = re.compile(r'^[0-9a-fA-F]+-[0-9a-fA-F]+\s')
    # This pattern matches lines like "Size:                184 kB"
    value_pattern = re.compile(r'^(\S+):\s+(\d+)\s*(\S*)')

    try:
        with open(filepath, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    # Blank lines separate blocks.
                    if current is not None:
                        blocks.append(current)
                        current = None
                    continue

                if header_pattern.match(line):
                    # Start of a new mapping block.
                    if current is not None:
                        blocks.append(current)
                    current = {"header": line}
                else:
                    m = value_pattern.match(line)
                    if m:
                        field = m.group(1).rstrip(':')
                        val_str = m.group(2)
                        # We ignore the unit (usually 'kB') since the numeric value suffices.
                        try:
                            value = int(val_str)
                        except ValueError:
                            value = val_str
                        current[field] = value
                    else:
                        # For non-numeric fields (like VmFlags)
                        if ':' in line and current is not None:
                            parts = line.split(":", 1)
                            field = parts[0].strip()
                            value = parts[1].strip()
                            current[field] = value
        if current is not None:
            blocks.append(current)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        sys.exit(1)
    return blocks

def print_blocks(blocks, keys_to_print):
    """
    Print the blocks in a simple table that includes the mapping header and selected statistics.
    """
    # Build the header row. We include "Mapping" (the header column) plus the provided keys.
    headers = ["Mapping"] + keys_to_print

    # Determine column widths dynamically.
    col_widths = {header: len(header) for header in headers}
    for block in blocks:
        mapping_text = block.get("header", "")
        col_widths["Mapping"] = max(col_widths["Mapping"], len(mapping_text))
        for key in keys_to_print:
            val = str(block.get(key, ""))
            col_widths[key] = max(col_widths[key], len(val))

    # Print header row.
    header_line = " | ".join(header.ljust(col_widths[header]) for header in headers)
    separator = "-+-".join('-' * col_widths[header] for header in headers)
    print(header_line)
    print(separator)
    
    # Print each mapping block.
    for block in blocks:
        row = [block.get("header", "").ljust(col_widths["Mapping"])]
        for key in keys_to_print:
            row.append(str(block.get(key, "")).ljust(col_widths[key]))
        print(" | ".join(row))

def main():
    # Define allowed sort fields.
    allowed_fields = [
        "Size", "KernelPageSize", "MMUPageSize", "Rss", "Pss", "Pss_Dirty",
        "Shared_Clean", "Shared_Dirty", "Private_Clean", "Private_Dirty", "Referenced",
        "Anonymous", "LazyFree", "AnonHugePages", "ShmemPmdMapped", "FilePmdMapped",
        "Shared_Hugetlb", "Private_Hugetlb", "Swap", "SwapPss", "Locked",
        "THPeligible", "VmFlags"
    ]

    parser = argparse.ArgumentParser(
        description="Sort mappings from a smaps file by a given memory field."
    )
    # Provide a default file name of smaps.txt.
    parser.add_argument(
        "file", nargs="?", default="smaps.txt",
        help="Path to the smaps file (default: smaps.txt in the current directory)"
    )
    parser.add_argument(
        "--sort-field", type=str, required=True,
        help="Field to sort by. One of: " + ", ".join(allowed_fields)
    )
    parser.add_argument(
        "--order", type=str, choices=["asc", "desc"], default="asc",
        help="Sort order: 'asc' for ascending or 'desc' for descending (default is asc)"
    )
    args = parser.parse_args()

    if args.sort_field not in allowed_fields:
        print(f"Error: Invalid sort field '{args.sort_field}'.", file=sys.stderr)
        print("Allowed fields are:", ", ".join(allowed_fields), file=sys.stderr)
        sys.exit(1)

    blocks = parse_smaps(args.file)
    if not blocks:
        print("No mapping blocks found in the file.", file=sys.stderr)
        sys.exit(1)

    # Define a sorting key function.
    def sort_key(block):
        # Get the chosen field. Use a default value if it's missing.
        value = block.get(args.sort_field, 0)
        # Attempt numeric conversion; if not applicable (e.g., for VmFlags), return as string.
        try:
            return int(value)
        except (ValueError, TypeError):
            return str(value)

    reverse_order = (args.order == "desc")
    sorted_blocks = sorted(blocks, key=sort_key, reverse=reverse_order)

    # Only print the mapping header and the selected sort field.
    print_blocks(sorted_blocks, [args.sort_field])

if __name__ == "__main__":
    main()
```
* Example usage:
```
python3 sort_smaps.py bad-smaps.txt --sort-field Rss --order asc 
```