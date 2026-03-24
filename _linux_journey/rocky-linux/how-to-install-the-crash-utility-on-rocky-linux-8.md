---
title: "How To Install The Crash Utility On Rocky Linux 8."
category: "rocky-linux"
tags: ["rocky-linux", "install", "crash", "utility", "rocky"]
---

```
sudo dnf install -y kexec-tools
sudo dnf localinstall -y ./kernel-rt-debuginfo-common-x86_64-4.18.0-372.32.1.rt7.189.el8_6.x86_64.rpm
sudo dnf localinstall -y ./kernel-rt-debuginfo-4.18.0-372.32.1.rt7.189.el8_6.x86_64.rpm
sudo dnf install -y crash
crash /usr/lib/debug/lib/modules/<version_of_debuginfo_package_installed>/vmlinux ./vmcore
```
