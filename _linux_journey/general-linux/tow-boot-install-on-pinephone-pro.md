---
title: "Tow Boot Install On Pinephone Pro"
category: "general-linux"
tags: ["tow", "boot", "install", "pinephone", "pro"]
---

* Check the latest releases: https://github.com/Tow-Boot/Tow-Boot/releases
* Extract the tarball:
```
tar -xvf pine64-pinephonePro-<version>.tar.xz
```
* Insert a microSD card.
* Run this command:
```
sudo dd if=spi.installer.img of=/dev/XXX bs=1M oflag=direct,sync status=progress
```
* Open the back cover.
* Use a pick. Hold down the RE button with the pick and awkwardly insert the power connector at the same time.
* The phone's status LED will go from red to yellow and vibrate two times.
* Select the `Install Tow-Boot to SPI` option.
* Press `Start install