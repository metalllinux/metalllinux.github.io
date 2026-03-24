---
title: "Flirc Usb Setup Ubuntu 24.04"
category: "project-tv-v2"
tags: ["project-tv-v2", "flirc", "usb", "setup", "ubuntu"]
---

* Create the `appimages` directory:
```
mkdir ~/appimages
```
* Download from the "Linux Generic 64-bit Archive":
```
wget http://apt.flirc.tv/arch/x86_64/flirc.latest.x86_64.tar.gz
```
* Unzip the tarball:
```
tar -xf ./flirc.latest.x86_64.tar.gz
```
* Make the `binaries` directory:
```
mkdir -p /home/howard/binaries
```
* Move the `Flirc` binary to the directory:
```
mv ~/Flirc-3.27.16/Flirc ~/binaries/
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
* Install this package:
```
sudo apt install -y libhidapi-dev
```
* Reboot:
```
sudo reboot
```
* Advised to run the regular `Flirc` binary instead of the `appimage`.

###
Having the `udev` rules set up for the Flirc USB WILL NOT ALLOW THE SKIP 1S Remote Control to be detected by the Skip App!
###

* In the FLIRC configuration settings, go to `File` --> `Advanced` and un-toggle all built-in Profiles aside from `Flirc WMC Profile`. Do not touch the `Controllers` part. Then close the App.
###
THE USB PORT ALSO MATTERS, OTHERWISE YOU WILL RECEIVE PHANTOM INPUTS - UBUNTU 24.04
###