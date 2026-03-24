---
title: "Cuda On Warewulf Rocky Linux 9 Image With Rocky Li"
category: "rocky-linux"
tags: ["rocky-linux", "cuda", "warewulf", "rocky", "linux"]
---

```
dnf upgrade -y
```
```
dnf install -y https://github.com/warewulf/warewulf/releases/download/v4.6.0/warewulf-4.6.0-1.el8.x86_64.rpm
```
```
systemctl restart firewalld
firewall-cmd --permanent --add-service=warewulf
firewall-cmd --permanent --add-service=dhcp
firewall-cmd --permanent --add-service=nfs
firewall-cmd --permanent --add-service=tftp
firewall-cmd --reload
```
```
tee /etc/warewulf/warewulf.conf <<EOF
WW_INTERNAL: 45
ipaddr: 192.168.1.11
netmask: 255.255.255.0
network: 192.168.1.0
warewulf:
  port: 9873
  secure: false
  update interval: 60
  autobuild overlays: true
  host overlay: true
  syslog: false
  datastore: /usr/share
  grubboot: false
dhcp:
  enabled: true
  template: default
  range start: 192.168.1.254
  range end: 192.168.1.255
  systemd name: dhcpd
tftp:
  enabled: true
  tftproot: /var/lib/tftpboot
  systemd name: tftp
  ipxe:
    "00:00": undionly.kpxe
    "00:07": ipxe-snponly-x86_64.efi
    "00:09": ipxe-snponly-x86_64.efi
    00:0B: arm64-efi/snponly.efi
nfs:
  enabled: true
  export paths:
  - path: /home
    export options: rw,sync
    mount options: defaults
    mount: true
  - path: /opt
    export options: ro,sync,no_root_squash
    mount options: defaults
    mount: false
  systemd name: nfs-server
container mounts:
- source: /etc/resolv.conf
  dest: /etc/resolv.conf
  readonly: true
paths:
  bindir: /usr/bin
  sysconfdir: /etc
  localstatedir: /var/lib
  ipxesource: /usr/share/ipxe
  srvdir: /var/lib
  firewallddir: /usr/lib/firewalld/services
  systemddir: /usr/lib/systemd/system
  wwoverlaydir: /var/lib/warewulf/overlays
  wwchrootdir: /var/lib/warewulf/chroots
  wwprovisiondir: /var/lib/warewulf/provision
  wwclientdir: /warewulf
EOF
```
```
systemctl enable --now warewulfd
```
```
wwctl configure --all
```
```
restorecon -Rv /var/lib/tftpboot/
```
```
wwctl container import docker://ghcr.io/warewulf/warewulf-rockylinux:9 rockylinux-nvidia-9
```
```
wwctl container shell rockylinux-nvidia-9
```
```
dnf -y install dnf-plugins-core epel-release kernel-headers
```
```
dnf config-manager --add-repo https://developer.download.nvidia.com/compute/cuda/repos/rhel9/$(arch)/cuda-rhel9.repo
```
```
wwctl container import docker://ghcr.io/warewulf/warewulf-rockylinux:9 rockylinux-9 --build
wwctl profile set default --container rockylinux-9
```
```
wwctl profile set -y default --netmask=255.255.240.0 --gateway=10.25.96.3
wwctl profile list
```
```
dnf -y module install nvidia-driver:latest-dkms
```
```
dkms status | grep nvidia
```
```
exit
```
```
wwctl container build
```
```
wwctl container syncuser --write rockylinux-nvidia-9
```
```
wwctl node add node1 --ipaddr=192.168.1.254 --discoverable=true
```
```
wwctl node set node1 --container rockylinux-nvidia-9
```
* Turn on the Compute Node and it will then boot.

```
wget https://developer.download.nvidia.com/compute/cuda/12.8.1/local_installers/cuda_12.8.1_570.124.06_linux.run
```
```
chmod +x cuda_12.8.1_570.124.06_linux.run
```
```
./cuda_12.8.1_570.124.06_linux.run --toolkit --override --silent
```
```
sudo dnf -y install nfs-utils
```
```
sudo systemctl enable --now nfs-server
```
```
echo "/usr/local/cuda *(rw,sync,no_subtree_check)" | sudo tee -a /etc/exports
```
```
sudo exportfs -ra
```
```
sudo wwctl overlay create cuda-nfs
```
```
sudo wwctl overlay edit cuda-nfs -p /etc/systemd/system/usr-local-cuda.mount
```
* Add the following information:
```
[Unit]
Description=Mount NFS share for CUDA
After=network-online.target
Requires=network-online.target

[Mount]
What=your_nfs_server:/usr/local/cuda  # Change this to your server and export path
Where=/usr/local/cuda
Type=nfs
Options=defaults,noatime,nolock

[Install]
WantedBy=multi-user.target
```
* Set appropriate permissions:
```
sudo wwctl overlay chmod cuda-nfs /etc/systemd/system/usr-local-cuda.mount 0644
```
```
sudo wwctl overlay edit cuda-nfs -p /etc/systemd/system/multi-user.target.wants/usr-local-cuda.mount.ww
```
* Add this to the file:
```
{{ softlink "/etc/systemd/system/usr-local-cuda.mount" }}
```

```
sudo wwctl overlay mkdir cuda-nfs /usr/local/cuda
```
```
sudo wwctl profile set default -O $(sudo wwctl profile list default -a | grep SystemOverlay | awk '{ print $3 }'),cuda-nfs
```
```
sudo wwctl overlay build
```