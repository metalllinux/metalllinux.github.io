---
title: "Install Postmarketos To The Pinephone Pro"
category: "general-linux"
tags: ["install", "postmarketos", "pinephone", "pro"]
---

* Plug in the PinePhone to a computer.
* Hold the Volume Up button down.
* The charging LED will turn blue.
* Download the latest postmarketOS Edge release for Plasma Mobile: https://images.postmarketos.org/bpo/edge/pine64-pinephonepro/plasma-mobile/
* Extract the tarball:
```
unxz <name>.img.xz
```
* `dd` the image onto the PinePhone:
```
sudo dd if=<name>.img of=/dev/sda bs=1M oflag=direct,sync status=progress
```
* Hold down the Power Button for 5 seconds.
Default username: user
Default password: 147147
Switch to a TTY at any point by holding Volume Down and pressing the Power button 3 times.