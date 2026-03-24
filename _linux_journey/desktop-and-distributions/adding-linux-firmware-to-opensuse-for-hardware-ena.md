---
title: "Adding Linux Firmware To Opensuse For Hardware Ena"
category: "desktop-and-distributions"
tags: ["desktop-and-distributions", "adding", "linux", "firmware", "opensuse"]
---

git clone git://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git

sudo zypper in git

sudo chown -R root:root linux-firmware/

sudo cp -r /lib/firmware /lib/firmware.bak

sudo mv linux-firmware /lib/firmware

sudo reboot

