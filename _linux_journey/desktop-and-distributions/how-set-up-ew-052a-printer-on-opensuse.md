---
title: "How Set Up Ew 052A Printer On Opensuse"
category: "desktop-and-distributions"
tags: ["desktop-and-distributions", "052a", "printer", "opensuse"]
---

* Install the rpm printer driver with `sudo zypper in DRIVER`.
* Find the IP of the printer.
* Open `Yast Printer` and add the IP of the printer manually (the default TCP port should be fine).
* After that, save the printer settings.