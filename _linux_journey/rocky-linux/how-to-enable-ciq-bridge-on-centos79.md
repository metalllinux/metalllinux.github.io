---
title: "How to Enable CIQ Bridge on CentOS 7.9"
category: "rocky-linux"
tags: ["rocky-linux", "enable", "ciq", "bridge", "centos79"]
---

# How to Enable CIQ Bridge on CentOS 7.9

Provision a fresh CentOS 7.9 VM.

Enable CIQ Depot via:

sudo yum install -y [https://depot.ciq.com/public/files/depot-client/depot/depot.x86\_64.rpm](https://depot.ciq.com/public/files/depot-client/depot/depot.x86_64.rpm)
sudo depot login -u <USER> -t <TOKEN>
sudo depot enable bridge
sudo rm -f /etc/yum.repos.d/CentOS*

3. Execute `sudo yum update`
4. Kernel version updates to `3.10.0-1160.119.1.el7_9.ciqcbr.4.1` (at the time of writing)
5. Reboot the machine.
6. Run `uname -r` and confirm the new kernel is active.

