---
title: "Enable Handbrake In Opensuse"
category: "desktop-and-distributions"
tags: ["desktop-and-distributions", "enable", "handbrake", "opensuse"]
---

Tumbleweed:

sudo zypper addrepo -cfp 90 'https://ftp.gwdg.de/pub/linux/misc/packman/suse/openSUSE_Tumbleweed/' packman

Leap:

sudo zypper addrepo -cfp 90 'https://ftp.gwdg.de/pub/linux/misc/packman/suse/openSUSE_Leap_$releasever/' packman

Then, install the desired codecs by first refreshing your local repository database and allowing vendor change for the required packages (consider reading Vendor change). The vendor change step will switch already installed packages to the ones provided by Packman. For example, PipeWire from Packman is compiled with aptX support.

sudo zypper refresh
sudo zypper dist-upgrade --from packman --allow-vendor-change

Then you can install with `handbrake-gtk`