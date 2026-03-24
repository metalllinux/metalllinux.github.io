---
title: "Function to read a list of RPM packages from a file"
category: "rocky-linux"
tags: ["rocky-linux", "good", "python", "script", "compare"]
---

```
# Function to read a list of RPM packages from a file
def read_package_list(file_path):
    packages = {}
    with open(file_path, 'r') as file:
        for line in file:
            package_name = line.strip()  # Get the entire line (package name with version)
            packages[package_name] = package_name  # Store the entire line (package name + version)
    return packages

# Function to compare the lists and find common packages with the same version
def compare_packages(system_a_packages, system_b_packages, system_a_name, system_b_name):
    common_packages = {}

    for pkg_a, version_a in system_a_packages.items():
        if pkg_a in system_b_packages:
            version_b = system_b_packages[pkg_a]
            if version_a == version_b:
                common_packages[pkg_a] = version_a

    # Display the results
    if common_packages:
        print(f"Packages with the same version between {system_a_name} and {system_b_name}:")
        for package, version in common_packages.items():
            print(f"{package}: {version}")
    else:
        print(f"No common packages with the same version between {system_a_name} and {system_b_name}.")

# Define custom names for the systems
system_a_name = "System A"
system_b_name = "System B"

# File paths to your package lists (replace with actual file paths)
file_path_a = '<FILE1_HERE>'
file_path_b = '<FILE2_HERE>'

# Read the package lists from files
system_a_packages = read_package_list(file_path_a)
system_b_packages = read_package_list(file_path_b)

# Compare the two systems
compare_packages(system_a_packages, system_b_packages, system_a_name, system_b_name)
```