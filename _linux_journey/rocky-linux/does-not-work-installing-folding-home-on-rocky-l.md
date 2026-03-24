---
title: "Does Not Work Installing Folding@Home On Rocky L"
category: "rocky-linux"
tags: ["rocky-linux", "work", "installing", "foldinghome", "rocky"]
---

```
dnf config-manager --set-enabled crb
dnf install epel-release
```
```
sudo dnf -y install git python3-scons gcc-c++ openssl-devel zlib-devel bzip2-devel lz4-devel systemd-devel rpm-build systemd-rpm-macros
```
```
git clone https://github.com/cauldrondevelopmentllc/cbang
git clone https://github.com/foldingathome/fah-client-bastet
```
```
export CBANG_HOME=$PWD/cbang
scons -C cbang
scons -C fah-client-bastet
scons -C fah-client-bastet package
```
```
sudo dnf install -y ./fah-client-bastet/fah_client-8.4.8-1.x86_64.rpm
```
```
File locations:

  Logs: /var/log/fah-client
  Data: /var/lib/fah-client

Service commands:

  systemctl status --no-pager -l fah-client
  sudo systemctl start fah-client
  sudo systemctl stop fah-client
  sudo systemctl restart fah-client

Access the web interface by going to:

  https://v8-4.foldingathome.org/

```