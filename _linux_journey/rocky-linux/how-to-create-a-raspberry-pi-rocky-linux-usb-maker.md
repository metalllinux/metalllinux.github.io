---
title: "How to Creat a Raspberry Pi Rocky Linux USB Maker"
category: "rocky-linux"
tags: ["rocky-linux", "create", "raspberry", "rocky", "linux"]
---

# How to Creat a Raspberry Pi Rocky Linux USB Maker

* Download the Rocky Linux Raspberry Pi image.

* Run `unxz` on the compressed file to extract the `raw` image 

* Use `dd` to flash the Rocky Linux Raspberry Piimage to a MicroSD card.

* Boot up the Raspberry Pi and login. The default credentials are:

Username: `rocky`
Password: `rockylinux`

* Expand the filesystem so that it uses the full capacity of your microsd card.

* Install the `cloud-utils-growpart` package:

```
sudo dnf install -y cloud-utils-growpart
```

* Find the partition information with:

```
df -T /
```

* Grow the partition size using the following command:

```
sudo growpart /dev/<OUTPUT_FROM_DF_-T>
```

* Resize the filesystem:

```
sudo resize2fs /dev/<OUTPUT_FROM_DF_-T>
```

* Confirm with `df -h /` that the filesystem has expanded in size.

* Upgrade all of your packages with `sudo dnf upgrade -y`.

* Reboot the system by running `sudo reboot`.

* Install the packages required for the user-facing CLI application:

```
sudo dnf install -y python3-pyudev util-linux parted dosfstools
```

* Create required directories:

```
mkdir ~/scripts ~/isos
```

* Either use `wget` or `rsync` to place the Rocky Linux 9.6 and Rocky Linux 10 DVD ISOs into the `~/isos` directory. A recommended command is `rsync -AvP` from a PC via Ethernet to the Pi also connected via Ethernet for reliable delivery of the images.

* If you choose the `rsync` route, you will need to make sure that `rsync` is installed on the Raspberry Pi as well with:

```
sudo dnf install -y rsync
```

* Python script to create the USB memory stick. Write it to the `~/scripts` directory.

```
cat << "EOF" | tee /home/rocky/scripts/rocky-linux-usb-creator.py
#!/usr/bin/env python3

import os
import subprocess
import time
import sys
import csv
from datetime import datetime
import shutil
import pyudev
import logging

ISO_DIR = "/home/rocky/isos"
LOGFILE = "/tmp/rocky_usb_creator.log"
HISTORY_FILE = "/home/rocky/usb_creator_log.csv"

ISOS = {
    "1": ("Rocky Linux 9.6", "Rocky-9.6-x86_64-dvd.iso"),
    "2": ("Rocky Linux 10", "Rocky-10.0-x86_64-dvd1.iso"),
}

logging.basicConfig(filename=LOGFILE, level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')


def welcome():
    print("\n" + "="*60)
    print("     Welcome to the Rocky Linux USB Creator     ")
    print("="*60 + "\n")


def choose_iso():
    print("Choose the version to write:")
    for key, (name, _) in ISOS.items():
        print(f"  {key}. {name}")
    choice = input("\nEnter number: ").strip()
    return ISOS.get(choice)


def wait_for_usb():
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by(subsystem='block')

    print("\nPlease insert your USB drive...")

    for device in iter(monitor.poll, None):
        if device.action == 'add' and device.get('ID_BUS') == 'usb' and device.get('DEVTYPE') == 'disk':
            time.sleep(2)  # settle
            print(f"Detected USB device at {device.device_node}")
            return device.device_node

def write_iso(iso_path, device):
    print(f"Writing ISO to {device}...\nThis may take a few minutes.")
    try:
        subprocess.run(["dd", f"if={iso_path}", f"of={device}", "bs=4M", "status=progress", "oflag=sync"], check=True)
        print("Write completed.")
    except subprocess.CalledProcessError:
        raise RuntimeError("ISO write failed")


def verify_image(iso_path, device):
    print("Verifying written image...")
    try:
        result = subprocess.run(["cmp", "-n", "1048576", iso_path, device], stdout=subprocess.DEVNULL)
        if result.returncode == 0:
            print("Verification successful.")
        else:
            raise RuntimeError("Verification mismatch.")
    except Exception as e:
        raise RuntimeError(f"Verification failed: {e}")


def log_event(os_name):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    exists = os.path.isfile(HISTORY_FILE)
    with open(HISTORY_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if not exists:
            writer.writerow(["DateTime", "Version"])
        writer.writerow([now, os_name])


def reset_prompt():
    input("\nUSB creation complete. Please remove the USB drive and press Enter to return to main menu...")


def main():
    while True:
        os.system("clear")
        welcome()

        try:
            selection = choose_iso()
            if not selection:
                print("Invalid selection.")
                time.sleep(1)
                continue

            os_name, iso_filename = selection
            iso_path = os.path.join(ISO_DIR, iso_filename)
            if not os.path.exists(iso_path):
                raise FileNotFoundError(f"ISO not found at {iso_path}")

            device = wait_for_usb()
            write_iso(iso_path, device)
            verify_image(iso_path, device)
            log_event(os_name)
            reset_prompt()

        except Exception as e:
            logging.error(str(e))
            print(f"\nERROR: {e}")
            print(f"Check logs in {LOGFILE}")
            input("Press Enter to return to main menu...")

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("This script must be run as root.")
        sys.exit(1)
    main()
EOF
```

* Run the Python script with:

```
sudo sh ~/scripts/rocky-linux-usb-creator.py
```

* Creating a Rocky Linux 10 bootable USB stick will take 11 minutes.

* Creating a Rocky Linux 9.6 bootable USB stick will take 22 minutes.
