---
title: "How to Setup Apptainer on Ubuntu 24.04"
category: "rocky-linux"
tags: ["rocky-linux", "setup", "apptainer", "ubuntu2404"]
---

# How to Setup Apptainer on Ubuntu 24.04

Run the following to install Apptainer:

```
sudo apt update
sudo apt install -y software-properties-common
sudo add-apt-repository -y ppa:apptainer/ppa
sudo apt update
sudo apt install -y apptainer
```

Allow Unprivilged users to create an unprivileged user namespace:

```
sudo sh -c 'echo kernel.apparmor_restrict_unprivileged_userns=0 \
    >/etc/sysctl.d/90-disable-userns-restrictions.conf'
sudo sysctl -p /etc/sysctl.d/90-disable-userns-restrictions.conf
```

