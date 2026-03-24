---
title: "Opensuse Initial Setup"
category: "desktop-and-distributions"
tags: ["desktop-and-distributions", "opensuse", "initial", "setup"]
---

   sudo zypper ar -cfp 90 https://ftp.fau.de/packman/suse/openSUSE_Tumbleweed/ packman
  sudo zypper refresh
  sudo zypper dist-upgrade --from packman --allow-vendor-change
