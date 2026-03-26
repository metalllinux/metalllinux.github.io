---
title: "Testing - ISO Method - Performed on a Rocky Linux 10 System"
category: "rocky-linux"
tags: ["rocky-linux", "edit", "root", "password", "iso"]
---

### Testing - ISO Method - Performed on a Rocky Linux 10 System

* Installed the `squashfs-tools` package:
```
sudo dnf install -y squashfs-tools
```

* Installed the `syslinux` package:

```
sudo dnf install -y syslinux
```

* Installed the `genisoimage` package (optional - used for ISO volume validation):

```
sudo dnf install -y genisoimage
```

* Confirmed the ISO `Volume id` from the original ISO (optional):

```
isoinfo -d -i rocky-86-1.15-v20250716_iso_rocky-86-1.15-v20250716.iso | grep "Volume id"
Volume id: rocky86lts
```

* Downloaded the `rocky-86-1.15-v20250716` ISO image.

* Created a mount point and working directory:
```
mkdir -p ~/temp/mnt_iso ~/temp/custom_iso
```

* Mounted the ISO:
```
sudo mount -o loop rocky-86-1.15-v20250716_iso_rocky-86-1.15-v20250716.iso ~/temp/mnt_iso
```

* Copied all files from the ISO to the working directory:
```
sudo rsync -aH --progress ~/temp/mnt_iso/ ~/temp/custom_iso/
```

* Created a directory to modify the `rootfs.img` inside the `squashfs` structure:
```
mkdir -p ~/temp/rootfs-edit
```

* Extracted the original `squashfs`:

```
sudo unsquashfs -d ~/temp/squashfs-edit ~/temp/mnt_iso/LiveOS/squashfs.img
```

* Mounted the `rootfs.img`:

```
sudo mount -o loop ~/temp/squashfs-edit/LiveOS/rootfs.img ~/temp/rootfs-edit
```

* Set up the bind mounts:

```
sudo mount --bind /dev ~/temp/rootfs-edit/dev
sudo mount --bind /proc ~/temp/rootfs-edit/proc
sudo mount --bind /sys ~/temp/rootfs-edit/sys
```

* Unmounted the original ISO:
```
sudo umount ~/temp/mnt_iso
```

* I could then `chroot` into the filesystem:
```
sudo chroot ~/temp/rootfs-edit
```

* Added the `.ssh`  directory and assign the appropriate permissions:
```
mkdir -p /root/.ssh
chmod 700 /root/.ssh
```

* Added my public key and also assigned the right permissions:
```
echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCOZfq6DVBBBEN3dkAMu9vRPfRLiZgNMN+95U+Yvs7KeASnr5r1Urk6tdUBifY5GEjc1O1agh/1FtoOUAV+90fFzXDQVs11RIn1A4xc31jIXO9kEND+luGQueekh8p6tbtQ+TVAoOyMKOjrveRQmuGPk1qbL7FWktOOmB5XeAapT71DzeoqFD+qKLvCA/jEHiAP0ewVc/ugq8dnzscTQMODShjRzt0KqHrnZcHxatRyw1JPJ700mPWDAB9ntdOKsPt89lMKRLU9A4ac6b2sGJZ4QDFwUTBVd07m+qnmmoqDe6rGDmbwrtAb9/eI5oZsjXgtc6n95J5ffp+AQ2gx80mXb4hIipqKkegdwE4Z/0FFEWuayqBRhnLVzajJ2KfY1Op9IE7JiFqIqjvP1b7aBWvXbVZWVUbpQzz/9izQ+kGdl2LhTvEilMeHTUlPrC3Ge+4NCZZX2s0GACpgE/t8/7TzxnH+3YlKKCJceQhxDspu+meKRrxpP2edQZUuXzfW+QySUNrT1nOUp91Z1hTXkYEL9SRoN3BPqgsqGX/lZuGs4qrHvhcfm34ToxjJfPVTkctkvuQkFfF7jPEkxWzx6uFw/vn86WfjlbkOm9P6iigWEMBtP5uoLD/KJWsQTQKqlldItAMr/PzV7n0A573z5snoO1yYLzqriy9Zy3FRNO93lw== myuser@ciq-rocky-linux10" >> /root/.ssh/authorized_keys

chmod 600 /root/.ssh/authorized_keys
```

* Allowed public key authentication:
```
sed -i 's/^#PubkeyAuthentication yes/PubkeyAuthentication yes/' /etc/ssh/sshd_config
```

* Updated the `root` user's password to a new DISA-STIG compliant password:
```
passwd root
```

* Exited out the `chroot`:
```
exit
```

* Umounted all filesystems and the `squashfs` mount:
```
sudo umount ~/temp/rootfs-edit/dev
sudo umount ~/temp/rootfs-edit/proc
sudo umount ~/temp/rootfs-edit/sys
sudo umount ~/temp/rootfs-edit
```

* Changed into my `temp` directory:

```
cd ~/temp
```

* Rebuilt the `squashfs.img`:

```
sudo mksquashfs squashfs-edit custom_iso/LiveOS/squashfs.img \
  -noappend \
  -comp xz \
  -Xbcj x86 \
  -b 1M \
  -no-xattrs
```

* Changed into the custom ISO directory:
```
cd ~/temp/custom_iso
```

* Created a new ISO (keep in mind the volume flag of `-V` needs to be set as `rocky86lts`. The ISO can be named to anything you desire with the `-o` flag):
```
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
  -isohybrid-mbr /usr/share/syslinux/isohdpfx.bin \
  -o ~/temp/rocky86-custom-boot.iso .
```

* I moved the newly created ISO to my ISOs directory pool for `virt-manager` to see.

* Then under `virt-manager`, I went to `New VM` --> `Import existing disk image`, allocated resources to the VM and could start the VM without issue.

* I was able to log into the `root` account with my DISA-STIG password and also `ssh` into the machine as well.

### Next Steps

I observed you are using an Ubuntu VM and to make sure I do my due diligence, I will also provide instructions on how to go through the above steps on Ubuntu as well.

Kind Regards,
myuser

Hi Ping,

Please find the full steps for an Ubuntu Server 25.04 VM below. These are the same that I listed before, but with the appropriate Ubuntu commands added in:

### Testing - ISO Method - Performed on an Ubuntu 25.04 Server VM

* Installed the `squashfs-tools` package:
```
sudo apt update && sudo apt install -y squashfs-tools
```

* Installed the `syslinux` package:

```
sudo apt install -y syslinux syslinux-utils isolinux
```

* Installed the `genisoimage` package (optional - used for ISO volume validation):

```
sudo apt install -y genisoimage
```

* Installed `xorriso` for ISO creation:

```
sudo apt install -y xorriso
```

* Transferred the `rocky-86-1.15-v20250716_iso_rocky-86-1.15-v20250716.iso` ISO to the Ubuntu VM.

* Confirmed the ISO `Volume id` from the original ISO (optional):

```
isoinfo -d -i rocky-86-1.15-v20250716_iso_rocky-86-1.15-v20250716.iso | grep "Volume id"
Volume id: rocky86lts
```

* Created a mount point and working directory:
```
mkdir -p ~/temp/mnt_iso ~/temp/custom_iso
```

* Mounted the ISO:
```
sudo mount -o loop rocky-86-1.15-v20250716_iso_rocky-86-1.15-v20250716.iso ~/temp/mnt_iso
```

* Copied all files from the ISO to the working directory:
```
sudo rsync -aH --progress ~/temp/mnt_iso/ ~/temp/custom_iso/
```

* Created a directory to modify the `rootfs.img` inside the `squashfs` structure:
```
mkdir -p ~/temp/rootfs-edit
```

* Extracted the original `squashfs`:

```
sudo unsquashfs -d ~/temp/squashfs-edit ~/temp/mnt_iso/LiveOS/squashfs.img
```

* Mounted the `rootfs.img`:

```
sudo mount -o loop ~/temp/squashfs-edit/LiveOS/rootfs.img ~/temp/rootfs-edit
```

* Set up the bind mounts:

```
sudo mount --bind /dev ~/temp/rootfs-edit/dev
sudo mount --bind /proc ~/temp/rootfs-edit/proc
sudo mount --bind /sys ~/temp/rootfs-edit/sys
```

* Unmounted the original ISO:
```
sudo umount ~/temp/mnt_iso
```

* I could then `chroot` into the filesystem:
```
sudo chroot ~/temp/rootfs-edit
```

* Added the `.ssh`  directory and assign the appropriate permissions:
```
mkdir -p /root/.ssh
chmod 700 /root/.ssh
```

* Added my public key and also assigned the right permissions:
```
echo "<PUBLIC_KEY>" >> /root/.ssh/authorized_keys

chmod 600 /root/.ssh/authorized_keys
```

* Allowed public key authentication:
```
sed -i 's/^#PubkeyAuthentication yes/PubkeyAuthentication yes/' /etc/ssh/sshd_config
```

* Updated the `root` user's password to a new DISA-STIG compliant password:
```
passwd root
```

* Exited out the `chroot`:
```
exit
```

* Umounted all filesystems and the `squashfs` mount:
```
sudo umount ~/temp/rootfs-edit/dev
sudo umount ~/temp/rootfs-edit/proc
sudo umount ~/temp/rootfs-edit/sys
sudo umount ~/temp/rootfs-edit
```

* Changed into my `temp` directory:

```
cd ~/temp
```

* Rebuilt the `squashfs.img`:

```
sudo mksquashfs squashfs-edit custom_iso/LiveOS/squashfs.img \
  -noappend \
  -comp xz \
  -Xbcj x86 \
  -b 1M \
  -no-xattrs
```

* Changed into the custom ISO directory:
```
cd ~/temp/custom_iso
```

* Created a new ISO (keep in mind the volume flag of `-V` needs to be set as `rocky86lts`. The ISO can be named to anything you desire with the `-o` flag):

* **Note** - on Ubuntu 25.04, I had to change the path to `isohdpfx.bin`:

```
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
  -o ~/temp/rocky86-custom-boot-generated-by-ubuntu.iso .
```

* I transferred the newly created `rocky86-custom-boot-generated-by-ubuntu.iso` image out of the Ubuntu VM and back to my Rocky Linux 10 host running `virt-manager`.

* I set the ISO up the same way in `virt-manager` as explained previously.

* I was able to log into the `root` account with my DISA-STIG password and also `ssh` into the machine as well.
