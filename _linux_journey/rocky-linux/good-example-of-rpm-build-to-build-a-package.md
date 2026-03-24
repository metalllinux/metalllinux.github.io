---
title: "Good Example Of Rpm Build To Build A Package"
category: "rocky-linux"
tags: ["rocky-linux", "good", "example", "rpm", "build"]
---

* Install `rpm-build`:
```
sudo dnf install -y rpm-build
```
* Build the `libhid` RPM:
```
rpmbuild --rebuild ./libhid-0.2.17-49.fc41.src.rpm
```