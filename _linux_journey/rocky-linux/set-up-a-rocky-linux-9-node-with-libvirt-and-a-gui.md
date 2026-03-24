---
title: "Set Up A Rocky Linux 9 Node With Libvirt And A Gui"
category: "rocky-linux"
tags: ["rocky-linux", "rocky", "linux", "node", "libvirt"]
---

```
useradd -m libvirt-user
passwd libvirt-user
usermod -aG wheel libvirt-user
su - libvirt-user
sudo dnf upgrade -y
sudo dnf install -y qemu-kvm libvirt virt-manager virt-install
sudo dnf install -y epel-release
sudo dnf install -y bridge-utils virt-top libguestfs-tools bridge-utils virt-viewer
sudo systemctl enable --now libvirtd
sudo usermod -aG libvirt $USER
sudo newgrp libvirt
exit
sudo chown -R $USER:libvirt /var/lib/libvirt/
sudo dnf group install -y "Server with GUI"
sudo systemctl set-default graphical
sudo reboot
```