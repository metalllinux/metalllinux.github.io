---
title: "Wiki.js Installation"
category: "rocky-linux-kubernetes-setup"
tags: ["rocky-linux-kubernetes-setup", "wiki", "installation"]
---

# Wiki.js Installation

## System Requirements

* System requirements needs 2 cores, 1GB of RAM and 1GB of storage.

* Install `snap` support:

```
sudo dnf install -y epel-release

sudo dnf -y upgrade

sudo dnf install -y snapd

sudo systemctl enable --now snapd.socket
```

* Reboot the machine afterwards:

```
sudo reboot
```

* Install `helm`:

```
sudo snap install helm --classic
```

* Add the Wiki.js Helm Repository:

```
helm repo add requarks https://charts.js.wiki
```

* Install Wiki.js:

```
helm install wiki-js-release requarks/wiki
```

* Ultimately doesn't deploy, but a good test.

