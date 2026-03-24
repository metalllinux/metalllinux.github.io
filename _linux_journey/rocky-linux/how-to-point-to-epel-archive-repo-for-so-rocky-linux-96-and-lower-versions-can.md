---
title: "How to Point to the EPEL Repository Archive to Download Packages that are No Longer Available for Rocky Linux 9.6 and lower distribution versions."
category: "rocky-linux"
tags: ["rocky-linux", "point", "epel", "archive", "repo"]
---

# How to Point to the EPEL Repository Archive to Download Packages that are No Longer Available for Rocky Linux 9.6 and lower distribution versions.

You can modify /etc/yum.repos.d/epel.repo and change the epel repo to the following:
 
[epel]
name=Extra Packages for Enterprise Linux 9.6 - $basearch
baseurl=https://dl.fedoraproject.org/pub/archive/epel/9.6/Everything/$basearch/
enabled=1
gpgcheck=1
countme=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-9.6

