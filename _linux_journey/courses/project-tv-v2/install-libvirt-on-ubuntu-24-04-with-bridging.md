---
title: "Install Libvirt On Ubuntu 24.04 With Bridging"
category: "project-tv-v2"
tags: ["project-tv-v2", "install", "libvirt", "ubuntu", "bridging"]
---

* Check that KVM is available:
```
sudo apt install -y cpu-checker
sudo kvm-ok
```
* Install required packages:
```
sudo apt install -y qemu-kvm libvirt-daemon-system libvirt-clients virt-manager
```
* Add the user to the right groups:
```
sudo adduser $USER libvirt
sudo adduser $USER kvm
```
* The `libvirtd` `systemd` service should already be running.
* Set up the Netplan configuration:
```
cat << "EOF" | sudo tee /etc/netplan/01-netcfg.yaml
network:
  version: 2
  renderer: networkd
  ethernets:
    enp3s0:
      dhcp4: no
  bridges:
    br0:
      interfaces: [enp3s0]
      addresses: [192.168.1.107/24]
      gateway4: 192.168.1.1
      nameservers:
        addresses: [8.8.8.8, 8.8.4.4]
      parameters:
        stp: false
        forward-delay: 0
EOF
```
* Apply the configuration:
```
sudo netplan apply
```
* Create a directory for the `libvirt` network definition files to live in:
```
mkdir ~/libvirt_network_definition_files
```
* Then create the network definition file:
```
cat << "EOF" | tee ~/libvirt_network_definition_files/br0-network.xml
<network>
  <name>br0-network</name>
  <forward mode='bridge'/>
  <bridge name='br0'/>
</network>
EOF
```
* Define and start the network in `libvirt`:
```
sudo virsh net-define ~/libvirt_network_definition_files/br0-network.xml
sudo virsh net-start br0-network
sudo virsh net-autostart br0-network
```
* Select the `br0-network` when creating a VM.
* Reboot:
```
reboot
```
* Create the ISOs directory:
```
mkdir ~/isos
```
* Change into the `isos` directory:
```
cd isos
```
* Download the latest Rocky Linux Gnome ISO:
```
wget https://dl.rockylinux.org/pub/rocky/9/live/x86_64/Rocky-9-Workstation-x86_64-latest.iso
```