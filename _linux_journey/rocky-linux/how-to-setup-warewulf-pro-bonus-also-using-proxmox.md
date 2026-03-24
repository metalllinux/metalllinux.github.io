---
title: "How to Setup Warewulf Pro - Bonus, Also Using Proxmox"
category: "rocky-linux"
tags: ["rocky-linux", "setup", "warewulf", "pro", "bonus"]
---

# How to Setup Warewulf Pro - Bonus, Also Using Proxmox

## Proxmox VE 9.1.1 + Rocky Linux 9.7 + Warewulf Pro 4.6.3 Testing

* Set up a Rocky Linux 9.7 VM with 4 vCPUs, 4096 MB RAM and a 100GB Disk. Updated all packages to the latest versions.

* Installed the Depot client:

```
dnf install -y https://depot.ciq.com/public/download/depot-client/depot/depot.el8.x86_64.rpm
```

* Logged in with my credentials:

```
depot login -u <USER> -t <TOKEN>
```

* Enabled the `warewulf-pro` repository:

```
depot enable warewulf-pro
```

* Installed the latest version of Warewulf Pro (`4.6.4-1`):

```
dnf install warewulf
```

* Installed the Warewulf Pro Interface:

```
dnf -y install cockpit warewulf-cockpit
systemctl enable --now cockpit.socket
```

* Set up my Warewulf configuration with this file:

```
sudo tee /etc/warewulf/warewulf.conf <<EOF
WW_INTERNAL: 45
ipaddr: 192.168.2.20
netmask: 255.255.255.0
network: 192.168.2.0
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
  range start: 192.168.2.253
  range end: 192.168.2.253
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
api:
  enabled: true
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

* Configured the system:

```
wwctl configure --all
```

* Enabled the `warewulfd` service:

```
systemctl enable --now warewulfd
```

* Set up this firewalld configuration:

```
firewall-cmd --permanent --zone=internal --add-interface=ens18

firewall-cmd --permanent --zone=internal \
  --add-service=warewulf \
  --add-service=dhcp \
  --add-service=tftp \
  --add-service=nfs

firewall-cmd --reload
```

* Generated an Admin token for the API:

```
dnf install -y mkpasswd
echo "users:
  - name: admin
    password hash: $(mkpasswd --method=bcrypt)" >/etc/warewulf/auth.conf
```

* Restarted `warewulfd`:

```
systemctl restart warewulfd
```

* Installed the `slurm` overlays from Depot:

```
dnf install https://ciq-portal:6l7d-2hjc-2mmq@depot.ciq.com/my/warewulf-pro/warewulf-overlays/Packages/warewulf-overlays-slurm-1.1.0-1.el9.noarch.rpm
```

```
wwctl overlay list -a | grep -i slurm
slurm                etc/                                                                 false
slurm                etc/munge/                                                           false
slurm                etc/munge/munge.key.ww                                               false
slurm                etc/slurm/                                                           false
slurm                etc/slurm/cgroup.conf.ww                                             false
slurm                etc/sysconfig/                                                       false
slurm                etc/sysconfig/slurmd.ww                                              false
```

* Set my CIQ Portal username and password as credentials:

```
export WAREWULF_OCI_USERNAME=ciq-portal
export WAREWULF_OCI_PASSWORD=6l7d-2hjc-2mmq
```

* Imported the `rockylinux-slurm:24` image from the Warewulf Pro repository:

```
wwctl image import docker://depot.ciq.com/warewulf-pro/warewulf-node-images/rockylinux-slurm:24 slurm-24
```

* Available Warewulf Images after the import:

```
wwctl image list
IMAGE NAME
----------
slurm-24
```

* Successfully shelled into the image:

```
wwctl image shell slurm-24
Image build will be skipped if the shell ends with a non-zero exit code.
[warewulf:slurm-24] /# exit
exit
```

* Built the image:

```
wwctl image build slurm-24
```

* Set the following as runtime overlay for the image:

```
wwctl profile set default --runtime-overlays=slurm
```

* Created a Compute Node VM in Proxmox. The steps were I clicked "Create VM" --> Added a name --> "Next" --> "OS" - Do not use any media --> "System" - "Next" --> "Disks" - "Next" --> "CPU" Cores = 4 --> "Memory" 8096 MiB --> "Network" - Ensured for the "Bridge" device that my virtual interface of "vmbr0" was selected --> "Finish".

* (I have attached screenshots of my entire VM Compute Node setup process in Proxmox)

* Then under "Options", I changed "Boot Order" so that only "net0" was selected.

* Then in "Hardware" I acquired the VM's Mac Address.

* I then added the Compute Node VM to the Warewulf Controller Node and added its MAC address and assigned it an IP:

```
wwctl node add compute-node-1 --ipaddr 192.168.2.253 --hwaddr BC:24:11:6D:C6:12 --profile default
```

* Built the overlays:

```
wwctl overlay build
```

* Set the netmask, gateway and DNS for the default profile:

```
wwctl profile set default -M 255.255.255.0
wwctl profile set default -G 192.168.2.20
```

* Set the DNS for the `default` profile:

```
wwctl profile set default --nettagadd DNS1=8.8.8.8
wwctl profile set default --nettagadd DNS2=8.8.4.4
```

* Tested with a community image. I imported the Community Rocky Linux 9 image:

```
wwctl image import docker://ghcr.io/warewulf/warewulf-rockylinux:9 rockylinux-9
```

* Built the image afterwards:

```
wwctl image build rockylinux-9
```

* Set the image to the `default` profile:

```
wwctl profile set default --image rockylinux-9
```

* The community image is then successfully booted on the Compute Node VM.

* I then set the `default` profile to the `slurm` image from the Warewulf Pro repository from earlier:

```
wwctl profile set default --image slurm-24
```

* This also booted without issue. I could boot the Compute Node with the Warewulf Pro `slurm-24` image.

