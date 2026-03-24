---
title: "Nvidia Gtx 1060 Setup On Rocky Linux 9.X"
category: "rocky-linux"
tags: ["rocky-linux", "nvidia", "gtx", "setup", "rocky"]
---

* Download the latest `.run` installer from Nvidia's site: https://www.nvidia.com/en-us/drivers/details/237928/
* Install `gcc`:
```
sudo dnf install -y gcc
```
* Install the `kernel-devel` package:
```
sudo dnf install -y kernel-devel-$(uname -r)
```
* Run the `.run` installer:
```
sudo sh NVIDIA-Linux-x86_64-$DRIVER_VERSION.run
```
* Allow the installer to blacklist the `nouveau` drivers.
* `reboot`
* Run the installer again.
* Install the 32-bit drivers.

NEW VERSION
### Host Config
* Find the `device-slot` and `vendor-id` information:
```
lspci -Dnn | grep -i NVIDIA
```
* Place the `device-id` and `vendor-id` into the `CMDLINE_LINUX` area.
*  Add the following parameters to your `grub` kernel cmdline parameters:
```
sudo tee /etc/default/grub <<EOF
GRUB_TIMEOUT=5
GRUB_DISTRIBUTOR="$(sed 's, release .*$,,g' /etc/system-release)"
GRUB_DEFAULT=saved
GRUB_DISABLE_SUBMENU=true
GRUB_TERMINAL_OUTPUT="console"
GRUB_CMDLINE_LINUX="crashkernel=1G-4G:192M,4G-64G:256M,64G-:512M resume=/dev/mapper/rl-swap rd.lvm.lv=rl/root rd.lvm.lv=rl/swap rhgb quiet amd_iommu=on iommu=pt pci-stub.ids=10de:1c03,10de:10f1"
GRUB_DISABLE_RECOVERY="true"
GRUB_ENABLE_BLSCFG=true
EOF
```
* Update `grub`:
```
sudo grub2-mkconfig -o /etc/grub2.cfg
```
* Blacklist the `nouveau` drivers:
```
sudo tee /etc/modprobe.d/blacklist.conf <<EOF
blacklist nouveau
EOF
```
* Add the EPEL repo:
```
sudo dnf install epel-release -y
```
```
curver="rhel$(rpm -E %rhel)"
```
```
sudo wget -O /etc/yum.repos.d/cuda-$curver.repo \
  http://developer.download.nvidia.com/compute/cuda/repos/$curver/$(uname -i)/cuda-$curver.repo
```
* Enable the CRB repo:
```
sudo crb enable
```
* Update with `dnf`:
```
sudo dnf update -y
```
* Reboot:
```
sudo reboot
```
* Install the Nvidia driver:
```
sudo dnf module install nvidia-driver:latest-dkms -y
```
* Reboot:
```
sudo reboot
```