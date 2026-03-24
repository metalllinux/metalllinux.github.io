---
title: "What is KABI"
category: "general-linux"
tags: ["kabi"]
---

# What is KABI

KABI stands for **Kernel Application Binary Interface** in the Linux context. It refers to the binary interface between the Linux kernel and kernel modules (drivers, filesystem modules, etc.).

The KABI defines:

1. **Data structure layouts** - How structures used by the kernel are organised in memory
2. **Function signatures** - The calling conventions and parameters for kernel functions
3. **Symbol exports** - Which kernel symbols (functions, variables) are available to modules
4. **System call interfaces** - How modules interact with core kernel services

## Why KABI Matters

KABI stability is particularly important for enterprise Linux distributions because:

- **Binary compatibility** - Kernel modules compiled for one kernel version can work with other versions that maintain the same KABI
- **Third-party drivers** - Hardware vendors can distribute pre-compiled drivers that work across kernel updates
- **Reduced maintenance** - System administrators don't need to recompile out-of-tree modules after every kernel update

## KABI Management Approaches

Different distributions handle KABI differently:

- **Enterprise distributions** (RHEL, SLES) maintain strict KABI stability within major releases, using techniques like:
  - Symbol versioning
  - Padding structures for future expansion
  - Careful backporting that preserves interfaces
  
- **Community distributions** (Fedora, Ubuntu non-LTS) typically allow KABI changes between kernel updates, prioritising new features and improvements

The trade-off is between stability (important for production systems) and the ability to incorporate upstream kernel improvements that might require interface changes.

