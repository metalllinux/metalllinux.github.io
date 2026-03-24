---
title: "Kickstart File that Works with Rocky Linux 9"
category: "rocky-linux"
tags: ["rocky-linux", "kickstart", "file", "works", "rocky"]
---

# Kickstart File that Works with Rocky Linux 9

* Make a file called `kickstart.ks`

```
lang en_US.UTF-8
keyboard --xlayouts='us'
timezone Asia/Tokyo --utc

# Bootloader
bootloader --location=mbr --append="rhgb quiet crashkernel=auto"

# Disk partitioning
zerombr
clearpart --all --initlabel
part /boot/efi --fstype=efi --size=600
part /boot --fstype=xfs --size=1024
part pv.01 --fstype=lvmpv --size=1 --grow
volgroup VolGroup00 pv.01
logvol / --fstype=xfs --name=lv_root --vgname=VolGroup00 --size=1 --grow
logvol swap --fstype=swap --name=lv_swap --vgname=VolGroup00 --size=4096

# Network
network --bootproto=dhcp --device=eth0 --activate
network --hostname=rocky-kickstart.local

# Root password (SHA-512 hash)
rootpw --iscrypted $6$9KGJEGJ0jb6Rvza3$bguHcNu7V7.hqGeQFjeWmQEnQeAF1G/b8UsQrkvaeoMfTgb.EJEl9Kltlwn1pbCoIS7QHHDpXZP90tyDz/y7L. 

# Create admin user
user --name=admin --groups=wheel --password=$6$9KGJEGJ0jb6Rvza3$bguHcNu7V7.hqGeQFjeWmQEnQeAF1G/b8UsQrkvaeoMfTgb.EJEl9Kltlwn1pbCoIS7QHHDpXZP90tyDz/y7L. --iscrypted --gecos="Admin User"

# Skip interactive firstboot setup
firstboot --disable

# Accept EULA
eula --agreed

# SELinux and firewall
selinux --enforcing
firewall --enabled --service=ssh

# Package selection: minimal server
%packages
@^server-product-environment
chrony
%end

# Services to enable
%post --log=/root/ks-post.log
systemctl enable chronyd
%end
```

* Add the kickstart file to the ISO:

```
mkksiso --ks ./kickstart.ks ./<OLD>.iso ./<NEW>.iso
```

* Boot the ISO in virt-manager and observe that the installation happens automatically.
