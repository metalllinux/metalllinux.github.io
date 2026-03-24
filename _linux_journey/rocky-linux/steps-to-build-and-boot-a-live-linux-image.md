---
title: "Steps to Build and Boot a Live Linux Image (example is with CentOS Stream)"
category: "rocky-linux"
tags: ["rocky-linux", "steps", "build", "boot", "live"]
---

# Steps to Build and Boot a Live Linux Image (example is with CentOS Stream)

## Setting up the Build Environment on CentOS Stream 10.

* Set up a CentOS Stream 10 baremetal server with 8 vCPUs, 16GB of RAM and 512 GB of disk space.

* Install `lorax`:

```
sudo dnf install -y lorax
```

* Disable SELinux:

```
sudo setenforce 0
sudo sed -i 's/^SELINUX=.*/SELINUX=permissive/g' /etc/selinux/config
```

* Install the following packages for virtualisation and `root=live` boot:

```
sudo dnf install -y \
    dracut \
    dracut-live \
    dracut-network \
    dracut-squash \
    dracut-config-generic \
    squashfs-tools \
    httpd \
    qemu-kvm \
    libvirt \
    virt-install \
    device-mapper \
    device-mapper-libs \
    kpartx \
    iproute
```

* Add the following configuration to `/etc/libvirt/qemu.conf` to run as `root`:

```
user = "root"
group = "root"
```

* Set up the virtual bridge as detailed in https://docs.rockylinux.org/guides/virtualisation/libvirt-rocky/

* Enable and startthe `libvirt` service:

```
sudo systemctl enable --now libvirtd httpd
```

* Kickstart file:

```
# CentOS Stream 10 PXE Live Image - Minimal kickstart

lang en_US.UTF-8
keyboard us
timezone UTC --utc
rootpw --plaintext centos

# Installation source
url --url="https://mirror.stream.centos.org/10-stream/BaseOS/x86_64/os/"
repo --name="BaseOS" --baseurl=https://mirror.stream.centos.org/10-stream/BaseOS/x86_64/os/
repo --name="AppStream" --baseurl=https://mirror.stream.centos.org/10-stream/AppStream/x86_64/os/

# Network
network --bootproto=dhcp --activate

# Security
selinux --disabled
firewall --disabled

# Disk - use MBR label to avoid biosboot requirement
zerombr
clearpart --all --disklabel=msdos
bootloader --location=mbr
part / --size=6144

# Finish
shutdown

%packages
@core
kernel
dracut-live
dracut-network
dracut-config-generic
NetworkManager
openssh-server
-iwl*firmware
-libertas*firmware
%end

%post --log=/root/ks-post.log
systemctl enable NetworkManager sshd
systemctl set-default multi-user.target
echo "centos-live" > /etc/hostname
dnf clean all
rm -f /etc/machine-id && touch /etc/machine-id
%end
```

* Build the image:

```
sudo livemedia-creator \
    --make-pxe-live \
    --iso ~/CentOS-Stream-10-latest-x86_64-dvd1.iso \
    --ks centos-stream-10-live.ks \
    --resultdir ~/centos-stream-10-live_image \
    --project "CentOS Stream" \
    --releasever 10 \
    --ram 4096 \
    --vcpus 2 \
    --vnc vnc=:1
```

* `squashfs root filesystem`, `kernel` and `initramfs` should be built without issue:

```
ls -l ~/centos-stream-10-live_image/
total 2269332
-rw-------. 1 root root   58164844 Nov 25 15:49 initramfs-6.12.0-161.el10.x86_64.img
-rw-r--r--. 1 root root  756084736 Nov 25 15:49 live-rootfs.squashfs.img
-rw-r--r--. 1 root root 6444548096 Nov 25 15:47 lmc-disk-td8593hb.img
-rw-r--r--. 1 root root        211 Nov 25 15:49 PXE_CONFIG
-rwxr-xr-x. 1 root root   16042024 Nov 20 09:00 vmlinuz-6.12.0-161.el10.x86_64

```

* Set appropriate permissions on the kernel:

```
chown $(whoami):$(whoami) ~/centos-stream-10-live_image/vmlinuz-6.12.0-161.el10.x86_64
```

* Copy the image to the `/var/www/html` directory and apply appropriate permissions:

```
sudo cp ~/centos-stream-10-live_image/live-rootfs.squashfs.img /var/www/html/
sudo chmod 644 /var/www/html/live-rootfs.squashfs.img
```

* Set up the firewall to allow the HTTP server to be connected to:

```
sudo firewall-cmd --zone=libvirt --add-service=http --permanent
sudo firewall-cmd --zone=public --add-service=http --permanent
sudo firewall-cmd --reload
```

## Booting the Image

* Deploy the image and it successfully boots. You should be able to log in as the `root` user:

```
virt-install \
    --name livenet_test \
    --memory 4096 \
    --vcpus 2 \
    --disk none \
    --os-variant centos-stream10 \
    --network bridge=virbr0,model=virtio \
    --graphics none \
    --console pty,target_type=serial \
    --boot kernel=$HOME/centos-stream-10-live_image/vmlinuz-6.12.0-161.el10.x86_64,initrd=$HOME/centos-stream-10-live_image/initramfs-6.12.0-161.el10.x86_64.img,kernel_args="root=live:http://192.168.1.150/live-rootfs.squashfs.img ip=dhcp rd.live.ram rd.debug rd.live.debug console=ttyS0,115200n8" \
    --transient \
    --destroy-on-exit \
    2>&1 | tee virt-install.log
```
