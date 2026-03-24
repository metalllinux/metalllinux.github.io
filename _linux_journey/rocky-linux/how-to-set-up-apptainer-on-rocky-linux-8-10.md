---
title: "How To Set Up Apptainer On Rocky Linux 8.10"
category: "rocky-linux"
tags: ["rocky-linux", "apptainer", "rocky", "linux"]
---

* Update all packages:
```
sudo dnf upgrade -y
```
* Install the EPEL repository:
```
sudo dnf install -y epel-release
```
* Install the `non-setuid` version of Apptainer:
```
sudo dnf install -y apptainer
```