---
title: "Kde Plasma Setup Ubuntu 24.04"
category: "project-tv-v2"
tags: ["project-tv-v2", "kde", "plasma", "setup", "ubuntu"]
---

* Update all package repositories:
```
sudo apt update
```
* Install the full desktop environment:
```
sudo apt install -y kde-full
```
* For a minimal set of KDE applications, install:
```
sudo apt install -y kde-standard
```
* Choose `sddm` at the prompt.
* `reboot`