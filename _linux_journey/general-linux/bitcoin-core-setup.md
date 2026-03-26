---
title: "Bitcoin Core Setup"
category: "general-linux"
tags: ["bitcoin", "core", "setup"]
---

* Download the client:
```
wget https://bitcoin.org/bin/bitcoin-core-28.1/bitcoin-28.1-x86_64-linux-gnu.tar.gz
```
* Create the pool:
```
sudo zfs create mypool/bitcoin
```
* Change the user ownership:
```
sudo chown -R myuser:myuser /mnt/mypool/bitcoin/
```
* Install the EPEL package:
```
sudo dnf install -y epel-release
```
* Install `snapd`:
```
sudo dnf install -y snapd
```
* Start the `systemd` service:
```
sudo systemctl enable --now snapd.socket
```
* Restart the system:
```
sudo reboot
```
* Install Bitcoin Core:
```
sudo snap install bitcoin-core
```
* Provide the snap access to the `/mnt` directory:
```
sudo snap connect bitcoin-core:removable-media
```