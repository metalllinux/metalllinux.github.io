---
title: "Setting Up Libvirt On Rocky Linux 9"
category: "rocky-linux"
tags: ["rocky-linux", "setting", "libvirt", "rocky", "linux"]
---

```
sudo grep -e 'vmx' /proc/cpuinfo
sudo dnf install -y epel-release
sudo dnf install -y bridge-utils virt-top libguestfs-tools bridge-utils virt-viewer qemu-kvm libvirt virt-manager virt-install
sudo usermod -aG libvirt $USER
newgrp libvirt
sudo systemctl enable --now libvirtd
```
* Set up a bridge interface.
* Check the current interfaces.
```
sudo nmcli connection show
```
* Delete any existing `virbr0` interface.
```
sudo nmcli connection delete <INTERFACE_UUID_HERE>
```
* Delete the main Ethernet interface as well (you will lose your ssh connecton if you do this via ssh).
```
sudo nmcli connection delete <INTERFACE_UUID_HERE>
```
* Create the new bridge connection.
```
sudo nmcli connection add type bridge autoconnect yes con-name virbr0 ifname virbr0
sudo nmcli connection modify virbr0 ipv4.addresses 192.168.1.106/24 ipv4.method manual
sudo nmcli connection modify virbr0 ipv4.gateway 192.168.1.1
sudo nmcli connection modify virbr0 ipv4.dns 192.168.1.1
```
* Add the bridge slave. Make sure the Ethernet device selected is the main one that connects out to the Internet.
```
sudo nmcli connection add type bridge-slave autoconnect yes con-name enp1s0f1 ifname enp1s0f1 master virbr0
```
* Bring up the bridge connection.
```
sudo nmcli connection up virbr0
```
* Run the following script in `tmux` as a `root` or user with `sudo` privileges to do the above automatically:
```
#!/bin/bash
sudo nmcli connection delete eno1
sudo nmcli connection delete virbr0
sudo nmcli connection add type bridge autoconnect yes con-name virbr0 ifname virbr0
sudo nmcli connection modify virbr0 ipv4.addresses 192.168.1.105/24 ipv4.method manual
sudo nmcli connection modify virbr0 ipv4.gateway 192.168.1.1
sudo nmcli connection modify virbr0 ipv4.dns 192.168.1.1
sudo nmcli connection add type bridge-slave autoconnect yes con-name eno1 ifname eno1 master virbr0
sudo nmcli connection up virbr0
```
* Edit `/etc/qemu-kvm/bridge.conf`
* Add this line.
```
allow all
```
* Set the ownership of the `images` directory to your user.
```
sudo chown -R $USER:libvirt /var/lib/libvirt/
```
* Restart libvirtd.
```
sudo systemctl restart libvirtd
```
* Example `virt-install` that uses the new bridge.
```
virt-install --name ubuntu22.04 --ram=4096 --vcpus=3 --cpu host --hvm --disk path=~/vms/ubuntu22-04.qcow2,size=15 --cdrom ~/isos/ubuntu-22.04.5-live-server-amd64.iso --graphics none --console pty,target_type=serial --os-variant ubuntu22.04 --network bridge=virbr0,model=virtio --hvm --force --debug --boot kernel=mnt/casper/vmlinuz,initrd=mnt/casper/initrd,kernel_args="console=ttyS0"

```