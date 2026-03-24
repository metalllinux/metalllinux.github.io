---
title: "How To Have The Elrepo Set Up On Rocky Linux And U"
category: "rocky-linux"
tags: ["rocky-linux", "elrepo", "rocky", "linux"]
---

sudo rpm --import https://www.elrepo.org/RPM-GPG-KEY-elrepo.org
sudo yum install https://www.elrepo.org/elrepo-release-9.el9.elrepo.noarch.rpm
sudo dnf config-manager --enable elrepo-kernel
sudo dnf config-manager --enable elrepo-extras
sudo dnf update
sudo dnf install kernel-ml
sudo grubby --set-default /boot/vmlinuz-6.11.5-1.el9.elrepo.x86_64
sudo reboot