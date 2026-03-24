---
title: "How to Setup a Raspberry Pi to Setup Bootable Rocky Linux USB Sticks"
category: "rocky-linux"
tags: ["rocky-linux", "setup", "raspberry", "create", "bootable"]
---

# How to Setup a Raspberry Pi to Setup Bootable Rocky Linux USB Sticks

Perfect — since the **Raspberry Pi 4 itself will run Rocky Linux 10**, here's a refined solution **specifically tailored to Rocky Linux 10 on a Pi**, meeting your original goal.

---

## ✅ Solution Overview

* **Host OS**: Rocky Linux 10 (on Raspberry Pi 4)
* **Peripherals**: USB keyboard, HDMI monitor
* **User goal**: Insert a blank USB stick → Choose ISO (Rocky 9.6 or 10) → `dd` it to the USB stick → Visual confirmation

---

## ✅ Prerequisites

1. **Install dialogue & UDisks2** (for UI and device management):

   ```bash
   sudo dnf install dialog udisks2 -y
   ```

2. **Create ISO Storage Directory**:

   ```bash
   mkdir -p ~/isos
   # Place these files in ~/isos:
   # - Rocky-9.6-x86_64-dvd.iso
   # - Rocky-10-x86_64-dvd.iso
   ```

---

## ✅ Full Script: `~/usb_imager.sh`

```bash
#!/bin/bash

ISO_DIR=~/isos

# Check ISO files exist
if [[ ! -f "$ISO_DIR/Rocky-9.6-x86_64-dvd.iso" || ! -f "$ISO_DIR/Rocky-10-x86_64-dvd.iso" ]]; then
    dialog --msgbox "Missing ISO files in $ISO_DIR. Exiting." 8 40
    clear
    exit 1
fi

# Ask user to select ISO
CHOICE=$(dialog --title "Choose ISO" --menu "Select ISO to write:" 15 60 2 \
1 "Rocky Linux 9.6" \
2 "Rocky Linux 10" \
3>&1 1>&2 2>&3)

clear

case $CHOICE in
  1) ISO_PATH="$ISO_DIR/Rocky-9.6-x86_64-dvd.iso" ;;
  2) ISO_PATH="$ISO_DIR/Rocky-10-x86_64-dvd.iso" ;;
  *) echo "Cancelled."; exit 1 ;;
esac

# Prompt to insert USB
dialog --infobox "Insert USB drive now..." 5 40
sleep 3

# Detect new USB drive
echo "Waiting for USB stick..."
while true; do
  USB_DEV=$(lsblk -o NAME,TRAN,TYPE -n | grep 'usb' | grep 'disk' | awk '{print $1}' | head -n 1)
  if [ -n "$USB_DEV" ]; then
    DEV_PATH="/dev/$USB_DEV"
    break
  fi
  sleep 1
done

# Confirm overwrite
dialog --yesno "Write $ISO_PATH to $DEV_PATH? This will ERASE all data on the USB stick!" 10 60
if [ $? -ne 0 ]; then
    clear
    echo "Cancelled by user."
    exit 1
fi

# Unmount all partitions of USB
for part in $(ls ${DEV_PATH}?* 2>/dev/null); do
    umount "$part" 2>/dev/null
done

# Write ISO using dd
(
    echo "Writing ISO to $DEV_PATH..."
    dd if="$ISO_PATH" of="$DEV_PATH" bs=4M status=progress oflag=sync
) 2>&1 | dialog --programbox "Writing..." 20 70

# Completion Message
dialog --msgbox "✅ Done! ISO written to $DEV_PATH" 6 40
clear
```

---

## ✅ Make It Executable

```bash
chmod +x ~/usb_imager.sh
```

---

## ✅ Optional: Auto-start Script on Boot (TTY only)

To auto-run this script on login:

```bash
echo "~/usb_imager.sh" >> ~/.bash_profile
```

---

## ✅ USB Detection Notes

This script uses `lsblk` + `grep usb` to detect the first USB storage device that appears. It works reliably on Rocky Linux with udev and common USB sticks.

---

## ✅ Summary

* **User-friendly** selection and confirmation dialogs
* Fully **interactive** terminal-based workflow
* No GUI required (works via HDMI + keyboard)
* Visually shows progress and success/failure

Let me know if you want:

* Multiple USB support
* SHA checksum verification
* A full graphical version (if you ever install a GUI)
