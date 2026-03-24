---
title: "How To Setup A Rocky Linux Box For Centos Vmcore C"
category: "rocky-linux"
tags: ["rocky-linux", "setup", "rocky", "linux", "box"]
---

```
dnf upgrade -y
dnf install -y kexec-tools
dnf install -y crash
wget http://mirror.facebook.net/centos-debuginfo/7/x86_64/kernel-debuginfo-common-x86_64-3.10.0-1160.119.1.el7.x86_64.rpm
wget http://mirror.facebook.net/centos-debuginfo/7/x86_64/kernel-debuginfo-3.10.0-1160.119.1.el7.x86_64.rpm
dnf localinstall -y ./kernel-debuginfo-common-x86_64-3.10.0-1160.119.1.el7.x86_64.rpm
dnf localinstall -y ./kernel-debuginfo-3.10.0-1160.119.1.el7.x86_64.rpm
/usr/sbin/makedumpfile -R ./vmcore < ./vmcore.flat
crash /usr/lib/debug/lib/modules/3.10.0-1160.119.1.el7.x86_64/vmlinux ./vmcore
```