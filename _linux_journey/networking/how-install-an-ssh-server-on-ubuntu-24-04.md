---
title: "How Install An Ssh Server On Ubuntu 24.04"
category: "networking"
tags: ["networking", "install", "ssh", "server", "ubuntu"]
---

* Update all repositories:
```
sudo apt update
```
* Install these packages:
```
sudo apt install -y openssh-client openssh-server
```
* Start and enable the `ssh` service:
```
sudo systemctl enable --now ssh
```