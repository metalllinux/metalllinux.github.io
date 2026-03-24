---
title: "Virt Install Commands"
category: "virtualisation"
tags: ["virtualisation", "virt", "install", "commands"]
---

Debian 11

virt-install --virt-type kvm --name debian-bullseye-amd64 --cdrom ~/Downloads/debian-11.7.0-amd64-netinst.iso --disk path=/mnt/remeltindtdrinc/vms/debian_11.qcow2,format=qcow2,size=10 --memory 4096 --vcpus 2 --os-variant debian11

Alma Linux 9

virt-install --virt-type kvm --name almalinux9-2 --cdrom /mnt/meaddle/linux_isos/AlmaLinux-9.2-x86_64/AlmaLinux-9.2-x86_64-dvd.iso --disk path=/mnt/remeltindtdrinc/vms/almalinux9-2.qcow2,format=qcow2,size=15 --memory 4096 --vcpus 2 --os-variant almalinux9

Rocky 9

virt-install --virt-type kvm --name rocky9 --cdrom ~/vms/Rocky-9.3-x86_64-dvd.iso --disk path=~/vms/rocky9.qcow2,format=qcow2,size=20 --memory 4096 --vcpus 2 --os-variant rocky9