---
title: "Setting Up Gpu Passthrough With Virt Manager And R"
category: "virtualisation"
tags: ["virtualisation", "setting", "gpu", "passthrough", "virt"]
---

* Enable `IOMMU` support in the BIOS.
* **Detach the GPU from the host machine**:
* Identify the `vendor-id` and `device-id`:
```
lspci -Dnn | grep -i NVIDIA
```
* You will observe an output such as this:
```
lspci -Dnn | grep -i NVIDIA
0000:05:00.0 VGA compatible controller [0300]: NVIDIA Corporation GP106 [GeForce GTX 1060 6GB] [10de:1c03] (rev a1)
0000:05:00.1 Audio device [0403]: NVIDIA Corporation GP106 High Definition Audio Controller [10de:10f1] (rev a1)
```
* Take both `vendor-id` and `device-id` from the VGA controller and Audio device and apply them to the kernel cmdline parameters like so:
```
sudo vim /etc/default/grub
```
* Then edit the line like so:
```
GRUB_CMDLINE_LINUX="crashkernel=1G-4G:192M,4G-64G:256M,64G-:512M resume=/dev/mapper/rl-swap rd.lvm.lv=rl/root rd.lvm.lv=rl/swap rhgb quiet pci-stub.ids=10de:1c03,10de:10f1"
```
* For Intel systems, you will need to add `intel_iommu=on`
* Regenerate the `grub` bootloader:
```
sudo grubby --args=pci-stub.ids=10de:1c03,10de:10f1 --update-kernel=/boot/vmlinuz-`uname -r`
```
* Ensure the Nouveau drivers are blacklisted:
```
sudo grubby --args=rdblacklist=nouveau --update-kernel=/boot/vmlinuz-`uname -r`
```
* Reboot the machine:
```
sudo reboot
```
* Confirm that the kernel cmdline parameters worked successfully:
```
cat /proc/cmdline
```
* Create a VM in `virt-manager`.
* Add the Graphics Card to the VM. Go to `Add Hardware` --> `PCI Host Device` --> Choose your Graphics Card.
* Hit `Finish`.
* Start the VM.
* Download the GPU driver:
```
wget https://uk.download.nvidia.com/XFree86/Linux-x86_64/550.142/NVIDIA-Linux-x86_64-550.142.run
```
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
* Check your GPU and driver are detected:
```
lspci -nnk
```