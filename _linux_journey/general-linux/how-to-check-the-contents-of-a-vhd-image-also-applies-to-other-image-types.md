---
title: "How to Check the Contents of a VHD Image - Applies to Other Image Types"
category: "general-linux"
tags: ["check", "contents", "vhd", "image", "also"]
---

# How to Check the Contents of a VHD Image - Applies to Other Image Types

Here's the complete set of steps for Solution 1 to inspect the kernel version in your VHD image:

## Complete Steps for Solution 1

### Step 1: Convert VHD to raw format
```bash
# Convert the VHD to raw format
qemu-img convert -f vpc -O raw CIQ-Rocky-9.4LTS-x86_64-Confidential-20250421.vhd CIQ-Rocky-9.4LTS-x86_64-Confidential-20250421.raw
```

### Step 2: Detach any existing loop device (if applicable)
```bash
# Check if loop0 is already in use
sudo losetup -l

# If /dev/loop0 is in use, detach it
sudo losetup -d /dev/loop0
```

### Step 3: Create loop device with partition support
```bash
# Attach the raw image with partition scanning enabled (-P flag)
sudo losetup -f -P CIQ-Rocky-9.4LTS-x86_64-Confidential-20250421.raw

# Verify which loop device was assigned (usually loop0)
sudo losetup -l

# Verify partition devices were created
ls -la /dev/loop0*
```

### Step 4: Create mount point and mount the root partition
```bash
# Create mount directory
sudo mkdir -p /mnt/CIQ-Rocky-9.4LTS-x86_64-Confidential-20250421

# Mount the root partition (partition 2)
sudo mount /dev/loop0p2 /mnt/CIQ-Rocky-9.4LTS-x86_64-Confidential-20250421
```

### Step 5: Check the kernel version
```bash
# List kernel files in /boot
ls -la /mnt/CIQ-Rocky-9.4LTS-x86_64-Confidential-20250421/boot/vmlinuz-*

# List kernel modules directories
ls -la /mnt/CIQ-Rocky-9.4LTS-x86_64-Confidential-20250421/lib/modules/

# Check kernel packages in the RPM database
sudo rpm --root=/mnt/CIQ-Rocky-9.4LTS-x86_64-Confidential-20250421 -qa | grep kernel

# Check default boot entry if needed
cat /mnt/CIQ-Rocky-9.4LTS-x86_64-Confidential-20250421/boot/grub2/grubenv | grep saved_entry
```

### Step 6: Clean up
```bash
# Unmount the filesystem
sudo umount /mnt/CIQ-Rocky-9.4LTS-x86_64-Confidential-20250421

# Detach the loop device
sudo losetup -d /dev/loop0

# Optional: Remove the raw file if you don't need it anymore
# rm CIQ-Rocky-9.4LTS-x86_64-Confidential-20250421.raw
```

The kernel version will be visible in the filenames under `/boot/vmlinuz-*` and in the directory names under `/lib/modules/`. For Rocky Linux 9.4, you should typically see a 5.14.0 kernel series with a specific build number.

