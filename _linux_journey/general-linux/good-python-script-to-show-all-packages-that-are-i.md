---
title: "Custom system names"
category: "general-linux"
tags: ["good", "python", "script", "show", "all"]
---

```
import re

# Custom system names
system_a_name = "Custom System A"
system_b_name = "Custom System B"

def parse_rpm_list(file_path):
    rpm_dict = {}
    # Updated regular expression to capture the full package name, version, and architecture
    rpm_pattern = re.compile(r'^(?P<name>[a-zA-Z0-9\-\.]+)-(?P<version>[\S]+)-(?P<arch>[a-zA-Z0-9\+\.]+)$')
    
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            match = rpm_pattern.match(line)
            if match:
                package_name = match.group('name')
                version = match.group('version')
                arch = match.group('arch')
                # Use the full package name with architecture and version as key
                rpm_dict[f'{package_name}-{version}-{arch}'] = f'{package_name}-{version}-{arch}'
    return rpm_dict

def compare_rpm_lists(system_a_file, system_b_file):
    # Parse the RPM lists from files
    system_a_rpm_dict = parse_rpm_list(system_a_file)
    system_b_rpm_dict = parse_rpm_list(system_b_file)

    # Create sets of the package names with architecture
    system_a_packages = set(system_a_rpm_dict.keys())
    system_b_packages = set(system_b_rpm_dict.keys())
    
    # Print the title header
    print("*** Package Version Comparison Overview ***\n")
    
    # Compare versions only for common packages
    common_packages = system_a_packages.intersection(system_b_packages)
    
    for package in common_packages:
        system_a_full_name = system_a_rpm_dict[package]
        system_b_full_name = system_b_rpm_dict[package]
        
        if system_a_full_name != system_b_full_name:
            print(f"Version difference for {package}: {system_a_full_name} vs {system_b_full_name}")
    
    # Print packages only in System A
    unique_to_a = system_a_packages - system_b_packages
    print(f"\nPackages present in {system_a_name} but not in {system_b_name}:")
    for package in unique_to_a:
        full_name = system_a_rpm_dict[package]
        print(f"{full_name}")
    
    # Print packages only in System B
    unique_to_b = system_b_packages - system_a_packages
    print(f"\nPackages present in {system_b_name} but not in {system_a_name}:")
    for package in unique_to_b:
        full_name = system_b_rpm_dict[package]
        print(f"{full_name}")

# Example usage:
system_a_file = 'FILE1_HERE'  # Path to the RPM list for System A
system_b_file = 'FILE2_HERE'  # Path to the RPM list for System B

compare_rpm_lists(system_a_file, system_b_file)
```