---
title: "Flirc Usb Setup"
category: "project-tv"
tags: ["project-tv", "flirc", "usb", "setup"]
---

* Download from the "Linux Generic 64-bit Archive":
```
wget http://apt.flirc.tv/arch/x86_64/flirc.latest.x86_64.tar.gz
```
Needed Dependencies: libhidapi-hidraw0 libqt5core5a libqt5network5 libqt5xml5  libqt5xmlpatterns5  libhid qt5-qtbase qt5-qtsvg hidapi
     cp the 99-flirc.rules rules to /etc/udev/rules.d/
     optionally copy flirc_util and flirc to /usr/local/bin/
* Copy the `Flirc` utilities over:
```
sudo cp ./flirc_util Flirc /usr/local/bin
```
* Set up the `udev` rules:
```
cat << "EOF" | sudo tee /etc/udev/rules.d/99-flirc.rules

# Flirc Devices

# Bootloader
SUBSYSTEM=="usb", ENV{DEVTYPE}=="usb_device", ATTR{idVendor}=="20a0", ATTR{idProduct}=="0000", MODE="0666"
SUBSYSTEM=="usb", ENV{DEVTYPE}=="usb_device", ATTR{idVendor}=="20a0", ATTR{idProduct}=="0002", MODE="0666"
SUBSYSTEM=="hidraw", ATTRS{idVendor}=="20a0", ATTRS{idProduct}=="0005", MODE="0666"

# Flirc Application
SUBSYSTEM=="usb", ENV{DEVTYPE}=="usb_device", ATTR{idVendor}=="20a0", ATTR{idProduct}=="0001", MODE="0666"
SUBSYSTEM=="usb", ENV{DEVTYPE}=="usb_device", ATTR{idVendor}=="20a0", ATTR{idProduct}=="0004", MODE="0666"
SUBSYSTEM=="hidraw", ATTRS{idVendor}=="20a0", ATTRS{idProduct}=="0006", MODE="0666"
EOF
```
* Reboot the machine:
```
sudo reboot
```
* Run the flirc appimage.

###
Having the `udev` rules set up for the Flirc USB WILL NOT ALLOW THE SKIP 1S Remote Control to be detected by the Skip App!
###