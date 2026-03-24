---
title: "What is the grub2-pc Package?"
category: "kernel-and-system-internals"
tags: ["kernel-and-system-internals", "grub2", "package"]
---

# What is the grub2-pc Package?

The `grub2-pc` package is the **GRUB 2 bootloader for PC/BIOS systems** in Debian-based Linux distributions (like Ubuntu, Debian, etc.).

## Key Details:

**What it contains:**
- GRUB 2 (GRand Unified Bootloader version 2) binaries and modules specifically compiled for traditional BIOS-based PCs
- The "pc" in the name refers to PC/BIOS platform, as opposed to UEFI systems
- Core bootloader files that get installed to the Master Boot Record (MBR) or partition boot record

**Purpose:**
- Manages the boot process on BIOS-based systems
- Presents the boot menu allowing you to choose between different operating systems or kernel versions
- Loads the Linux kernel and initial ramdisk into memory
- Handles boot parameters and configurations

**When it's used:**
- On older systems that use legacy BIOS (not UEFI)
- On newer systems where UEFI is disabled or running in legacy/CSM (Compatibility Support Module) mode
- In virtual machines that emulate BIOS systems

**Related packages:**
- `grub-efi-amd64`: The equivalent package for UEFI systems on 64-bit machines
- `grub-efi-ia32`: For 32-bit UEFI systems  
- `grub2-common`: Common files shared between different GRUB variants
- `grub-pc-bin`: Binary files for GRUB PC/BIOS version

**Important files it manages:**
- `/boot/grub/grub.cfg` - Main configuration file
- `/etc/default/grub` - User-editable configuration
- MBR bootloader code (first 440 bytes of the disk)

If you're on a UEFI system, you'd typically have `grub-efi-amd64` instead of `grub2-pc`. You can check which one you have with `dpkg -l | grep grub`.

