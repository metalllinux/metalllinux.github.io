---
title: "Changing a Password and Adding an ssh Key to an Image Using Debian 13 and Lorax"
category: "networking"
tags: ["networking", "changing", "password", "adding", "ssh"]
---

# Changing a Password and Adding an ssh Key to an Image Using Debian 13 and Lorax

Debian 13 Baremetal Machine Setup
 

    Added my user to the sudoers file with the root account:

 

usermod -aG sudo howard

 

    Updated all packages:

 

sudo apt update
sudo apt upgrade -y

 

    Installed KVM, libvirt and other related packages:

 

sudo apt install -y qemu-kvm libvirt-daemon-system libvirt-clients \
    bridge-utils virt-manager virt-viewer libguestfs-tools \
    virtinst virt-top

 

    Added my user to the libvirt group:

 

sudo usermod -aG libvirt $USER

 

    Also added my user to the kvm group (needed for Debian):

 

sudo usermod -aG kvm $USER

 

    Applied group changes:

 

newgrp libvirt

 

    Ensured libvirtd was started:

 

sudo systemctl enable --now libvirtd
sudo systemctl enable --now virtlogd

 

    Set up a Virtual Bridge for KVM:

 

    Checked my currently available devices:

 

sudo nmcli connection show
NAME                UUID                                  TYPE      DEVICE 
Wired connection 1  4bd9954c-d273-4119-9955-908fb1fa4415  ethernet  enp2s0

 

    Ran the following BASH script to configure the bridge interface and networking:

 

cat << "EOF" | tee ~/br0_setup.sh
#!/bin/bash

# Clean up any existing connections for enp2s0
sudo nmcli connection delete "Wired connection 1" 2>/dev/null || true
sudo nmcli connection delete virbr0 2>/dev/null || true
sudo nmcli connection delete br0 2>/dev/null || true
sudo nmcli connection delete bridge-slave-enp2s0 2>/dev/null || true

# Create the bridge
sudo nmcli connection add type bridge autoconnect yes \
    con-name br0 ifname br0

# Configure IP
sudo nmcli connection modify br0 \
    ipv4.addresses 192.168.1.160/24 \
    ipv4.method manual \
    ipv4.gateway 192.168.1.1 \
    ipv4.dns 192.168.1.1

# Add the physical interface as a bridge slave
sudo nmcli connection add type bridge-slave autoconnect yes \
    con-name bridge-slave-enp2s0 ifname enp2s0 master br0

# Bring up the bridge
sudo nmcli connection up br0

# Verify
echo "Current connections:"
nmcli connection show
echo ""
echo "Bridge details:"
bridge link show
EOF

 

    Ran the BASH script:

 

sudo sh ~/br0_setup.sh

 

    Created the QEMU Bridge Access:

 

    Generated the directory:

 

sudo mkdir -p /etc/qemu

 

    Allowed bridge access:

 

echo "allow all" | sudo tee /etc/qemu/bridge.conf

 

    Set the appropriate permissions:

 

sudo chmod 644 /etc/qemu/bridge.conf

 

    Restarted libvirtd:

 

sudo systemctl restart libvirtd

 

    Created a default storage pool for my images:

 

sudo mkdir -p /var/lib/libvirt/images

 

    Configured permissions of the images directory to have my user manage them:

 

sudo chown -R $USER:libvirt /var/lib/libvirt/images

 
Testing - chroot Image Modification Method
 

    Installed the squashfs-tools package:

sudo apt update && sudo apt install -y squashfs-tools

 

    Installed the syslinux package:

 

sudo apt install -y syslinux syslinux-utils isolinux

 

    Installed the genisoimage package (optional - used for ISO volume validation):

 

sudo apt install -y genisoimage

 

    Made sure xorriso was installed for ISO creation:

 

sudo apt install -y xorriso

 

    Transferred the rocky-86-1.15-v20250716_iso_rocky-86-1.15-v20250716.iso ISO to the Debian 13 baremetal node.

 

sudo apt install rsync -y
rsync -AvP ./rocky-86-1.15-v20250716_iso_rocky-86-1.15-v20250716.iso howard@192.168.1.160:~/

 

    Confirmed the ISO Volume id from the original ISO (optional):

 

howard@debian:~$ isoinfo -d -i rocky-86-1.15-v20250716_iso_rocky-86-1.15-v20250716.iso | grep "Volume id"
Volume id: rocky86lts

 

    Created a mount point and working directory:

mkdir -p ~/temp/mnt_iso ~/temp/custom_iso

 

    Mounted the ISO:

howard@debian:~$ sudo mount -o loop rocky-86-1.15-v20250716_iso_rocky-86-1.15-v20250716.iso ~/temp/mnt_iso
mount: /home/howard/temp/mnt_iso: WARNING: source write-protected, mounted read-only.

 

    Copied all files from the ISO to the working directory:

sudo rsync -aH --progress ~/temp/mnt_iso/ ~/temp/custom_iso/

 

    Created a directory to modify the rootfs.img inside the squashfs structure:

mkdir -p ~/temp/rootfs-edit

 

    Extracted the original squashfs:

 

sudo unsquashfs -d ~/temp/squashfs-edit ~/temp/mnt_iso/LiveOS/squashfs.img

 

    Mounted the rootfs.img:

 

sudo mount -o loop ~/temp/squashfs-edit/LiveOS/rootfs.img ~/temp/rootfs-edit

 

    Set up the bind mounts:

 

sudo mount --bind /dev ~/temp/rootfs-edit/dev
sudo mount --bind /proc ~/temp/rootfs-edit/proc
sudo mount --bind /sys ~/temp/rootfs-edit/sys

 

    Unmounted the original ISO:

sudo umount ~/temp/mnt_iso

 

    I could then chroot into the filesystem:

sudo chroot ~/temp/rootfs-edit

 

    Made sure the .ssh directory was added and assign the appropriate permissions:

mkdir -p /root/.ssh
chmod 700 /root/.ssh

 

    Added my public key and also assigned the right permissions:

echo "<PUBLIC_KEY_HERE>" >> /root/.ssh/authorized_keys

chmod 600 /root/.ssh/authorized_keys

 

    Allowed public key authentication:

sed -i 's/^#PubkeyAuthentication yes/PubkeyAuthentication yes/' /etc/ssh/sshd_config

 

    Updated the root user's password to a new DISA-STIG compliant password:

passwd root

 

    For the /etc/rc.d/rc.local issue, I performed the following (rc.local comes from the SysV init days and is kept for legacy purposes. systemd has taken over and has its own methods for running startup commands now (services, timers and so on)):

 

systemctl disable rc-local.service

 

    Exited out the chroot:

exit

 

    Umounted all filesystems and the squashfs mount:

sudo umount ~/temp/rootfs-edit/dev
sudo umount ~/temp/rootfs-edit/proc
sudo umount ~/temp/rootfs-edit/sys
sudo umount ~/temp/rootfs-edit

 

    Changed into my temp directory:

 

cd ~/temp

 

    Rebuilt the squashfs.img:

 

sudo mksquashfs squashfs-edit custom_iso/LiveOS/squashfs.img \
  -noappend \
  -comp xz \
  -Xbcj x86 \
  -b 1M \
  -no-xattrs

 

    Changed into the custom ISO directory:

cd ~/temp/custom_iso

 

    Created a new ISO (keep in mind the volume flag of -V needs to be set as rocky86lts. The ISO can be named to anything you desire with the -o flag):

 

sudo xorriso -as mkisofs \
  -r -J -l \
  -V "rocky86lts" \
  -b isolinux/isolinux.bin \
  -c isolinux/boot.cat \
  -no-emul-boot \
  -boot-load-size 4 \
  -boot-info-table \
  -eltorito-alt-boot \
  -e images/efiboot.img \
  -no-emul-boot \
  -isohybrid-mbr /usr/lib/ISOLINUX/isohdpfx.bin \
  -o ~/temp/rocky86-custom-boot-generated-by-debian13-baremetal.iso .

 

    Ensured for my Debian 13 baremetal machine that ovmf support was available for UEFI to work in virt-manager:

 

sudo apt install -y ovmf qemu-system-x86

 

    To check if the OVMF files are present, run this command:

 

ls -la /usr/share/OVMF/

 

    Whilst still on the Debian 13 baremetal node, I started up virt-manager --> New VM --> Import existing disk image --> Added my temp ISO directory as a pool --> Selected the image I had created --> Set Rocky Linux 8 under Choose the operating system you are installing --> Checked Customise configuration before install, selected the XML tab and replaced the os block of my VM's XML with the following and hit Apply:

 

<os>
  <type arch="x86_64" machine="q35">hvm</type>
  <loader readonly="yes" type="pflash">/usr/share/OVMF/OVMF_CODE_4M.fd</loader>
  <nvram template="/usr/share/OVMF/OVMF_VARS_4M.fd">/var/lib/libvirt/qemu/nvram/rocky8_VARS.fd</nvram>
  <boot dev="hd"/>
</os>

 

    The above XML is just standard UEFI without secure boot.

 

    I then clicked Begin Installation and once booted could log in as root and with my DISA STIG password (please see the attached screenshot).

 

    I could also successfully ssh into the VM with:

 

ssh -i <path_to_my_private_key> root@<IP>
