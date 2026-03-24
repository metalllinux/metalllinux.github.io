---
title: "Steps for Installing NVIDIA Drivers from RPMFusion on Rocky Linux"
category: "rocky-linux"
tags: ["rocky-linux", "steps", "installing", "nvidia", "drivers"]
---

# Steps for Installing NVIDIA Drivers from RPMFusion on Rocky Linux

sudo dnf install --nogpgcheck https://dl.fedoraproject.org/pub/epel/epel-release-latest-$(rpm -E %rhel).noarch.rpm

sudo dnf install --nogpgcheck https://mirrors.rpmfusion.org/free/el/rpmfusion-free-release-$(rpm -E %rhel).noarch.rpm https://mirrors.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-$(rpm -E %rhel).noarch.rpm

sudo /usr/bin/crb enable

sudo dnf install akmod-nvidia

sudo akmods --force

sudo grubby --args="nouveau.modeset=0 rd.driver.blacklist=nouveau" --update-kernel=ALL

Reboot
