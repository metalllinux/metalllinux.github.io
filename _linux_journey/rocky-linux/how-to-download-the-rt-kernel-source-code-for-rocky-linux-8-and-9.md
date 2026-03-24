---
title: "How to Download the RT Kernel Source Code for Rocky Linux 8 and 9"
category: "rocky-linux"
tags: ["rocky-linux", "download", "kernel", "source", "code"]
---

# How to Download the RT Kernel Source Code for Rocky Linux 8 and 9

### Rocky Linux 9

* I made sure the `dnf-plugins-core` package was installed.
```
sudo dnf install -y dnf-plugins-core
```
* Enabled the RT Kernel repository:
```
sudo dnf config-manager --set-enabled rt
```
* Installed the RT Kernel:
```
sudo dnf install -y kernel-rt
```
* Downloaded the RT Kernel source code:
```
dnf download --source kernel-rt
```
* Installed the `rpm-build` package:
```
sudo dnf install -y rpm-build
```
* Extracted the source RPM:
```
rpm -ivh kernel-rt*.src.rpm
```

### Rocky Linux 8

* The above method does not work, you need to go directly to https://download.rockylinux.org/pub/rocky/8.10/RT/source/tree/Packages/k/ and then run `rpm -ivh kernel-rt*.src.rpm` from there.
