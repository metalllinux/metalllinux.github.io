---
title: "Ipxe Server On Rocky Linux 9.X Setup Steps"
category: "rocky-linux"
tags: ["rocky-linux", "ipxe", "server", "rocky", "linux"]
---

* Install a `dhcp` server:
```
sudo dnf install -y dhcp-server
```
* Edit the configurations of your DHCP server in `/etc/dhcp/dhcpd.conf`:
```
cat << "EOF" | sudo tee /etc/dhcp/dhcpd.conf
subnet 192.168.1.0 netmask 255.255.255.0 {
  range 192.168.1.240 192.168.1.250;
  option broadcast-address 192.168.1.255;
  option routers 192.168.1.1;
  filename "pxelinux.0";
  next-server 192.168.1.71;
}
EOF
```
* Install the `tftp` server:
```
sudo dnf install -y tftp-server
```
* Start and enable the `tftp` service:
```
sudo systemctl enable --now tftp
```
* Install the `syslinux` package, which contains the PXE bootloader:
```
sudo dnf install -y syslinux
```
* Copy boot files to the TFTP server directory:
```
sudo cp /usr/share/syslinux/pxelinux.0 /var/lib/tftpboot/
```
* Create a directory for your installation files:
```
sudo mkdir /var/lib/tftpboot/<distro_name_here>
```
* Mount the ISO image:
```
sudo mount -o loop /path/to/<your_ISO>.iso /mnt
```
* Copy the contents of the distro ISO to the `tftpboot` directory:
```
sudo cp /mnt/images/pxeboot/{vmlinuz,initrd.img} /var/lib/tftpboot/<distro_name_here>
```
* Create a configuration at `/var/lib/tftpboot/pxelinux.cfg`:
```
cat << "EOF" | sudo tee /var/lib/tftpboot/pxelinux.cfg
default menu.c32
prompt 0
timeout 300
ONTIMEOUT local
menu title PXE Boot Menu
label TEST
  kernel testiso/vmlinuz
  append initrd=testiso/initrd.img method=http://192.168.1.106/testiso/os/ devfs=nomount
EOF
```
* Restart the `dhcp` server:
```
sudo systemctl restart dhcpd
```
* Restart the `tftp` server:
```
sudo systemctl restart tftp
```
* Check that the configurations were correct:
```
sudo systemctl status dhcpd
sudo systemctl status tftp
```
* Unmount the ISO at `/mnt`:
```
sudo umount /mnt
```
* Edit this file on your host running `libvirt`:
```
/etc/libvirt/qemu.conf
```
* Uncomment this line:
```
#vnc_listen = "0.0.0.0"
```
* Restart `libvirt` with:
```
sudo systemctl restart libvirtd
```
* Then for testing, set up a local VM with `virt-install` and in particular set the graphics option as `vnc` (default port is `5900`):
```
virt-install --connect qemu:///system --name testvm --ram 4096 --vcpus 4 --network=bridge:virbr0 --pxe --osinfo detect=on,require=off --disk path=/home/myuser/images/testvm.qcow2,size=20 --graphics vnc
```
* Connect to the host that has the VM via its IP address and port `5900` like so: IP:PORT