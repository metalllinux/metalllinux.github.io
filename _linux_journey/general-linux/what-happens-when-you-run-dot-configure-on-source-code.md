---
title: "What Happens When you Run ./configure on Source Code"
category: "general-linux"
tags: ["happens", "when", "you", "run", "dot"]
---

# What Happens When you Run ./configure on Source Code

When you run `./configure` on Linux to build a program from source, it's executing a shell script that prepares the build environment for compilation. Here's what it does:

## Main Functions

**System Detection**: The configure script examines your system to determine:
- Operating system type and version
- CPU architecture
- Available system libraries and their versions
- Compiler presence and capabilities (gcc, g++, etc.)
- Build tools like make, ar, and ld

**Dependency Checking**: It verifies that all required dependencies are present:
- Checks for necessary libraries (like libxml2, openssl, etc.)
- Confirms required header files exist
- Tests that dependencies meet minimum version requirements
- Identifies optional features that can be enabled based on what's available

**Build Customisation**: The script processes various options you can pass to customise the build:
- `--prefix=/path` to set the installation directory
- `--enable-feature` or `--disable-feature` flags
- `--with-library` or `--without-library` options
- Optimisation and debugging flags

**File Generation**: Based on its findings, configure generates several important files:
- **Makefile**: The primary build instructions that `make` will use
- **config.h**: A C header file containing system-specific definitions and feature flags
- **config.log**: A detailed log of all tests performed
- **config.status**: A script that can recreate the current configuration

## The Process Flow

The configure script typically works by compiling and running small test programs to verify functionality. For example, it might compile a tiny program that uses a specific library function to confirm that library is working correctly on your system.

If everything checks out, you'll see a summary of what was configured and can proceed with `make` to actually compile the program. If something is missing, configure will usually stop and tell you what's needed.

This system, part of the GNU Autotools suite (autoconf/automake), allows the same source code to be built on many different Unix-like systems by adapting to each system's specific characteristics.

