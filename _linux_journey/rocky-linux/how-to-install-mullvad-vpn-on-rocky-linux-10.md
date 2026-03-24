---
title: "How to Install Mullvad VPN on Rocky Linux 10"
category: "rocky-linux"
tags: ["rocky-linux", "install", "mullvad", "vpn", "rocky"]
---

# How to Install Mullvad VPN on Rocky Linux 10

* Add this repository:

```
sudo dnf config-manager --add-repo https://repository.mullvad.net/rpm/stable/mullvad.repo
```

* Pull down the `libXScrnSaver` package from the Rocky Linux 9 AppStream:

```
wget dl.rockylinux.org/pub/rocky/9/AppStream/x86_64/os/Packages/l/libXScrnSaver-1.2.3-10.el9.x86_64.rpm
```

* Install the package:

```
sudo dnf install -y libXScrnSaver-1.2.3-10.el9.x86_64.rpm
```

* Install Mullvad VPN:

```
sudo dnf install -y mullvad-vpn
```
