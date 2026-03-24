---
title: "How To Install Ansible Builder On Rocky Linux 9.X"
category: "rocky-linux"
tags: ["rocky-linux", "install", "ansible", "builder", "rocky"]
---

* Install the `python3-pip` package:
```
sudo dnf install -y python3-pip
```
* Upgrade `pip`:
```
pip3 install --upgrade pip
```
* Install the `ansible-builder` package:
```
pip3 install ansible-builder
```


* Example Execution Environment setup:
* Install `docker` on a Rocky Linux 9.x host.
* Install `git`:
```
sudo dnf install -y git
```
* Clone this repository:
```
git clone https://github.com/ssimpson89/main-ee/
```
* Go through the above steps.
* Change into the `main-ee` directory:
```
cd main-ee
```
* Build the Execution Environment with this command:
```
ansible-builder build -v3 -t ghcr.io/ssimpson89/ascender-ee --container-runtime=docker
```
* Check that the image was built:
```
docker images
```