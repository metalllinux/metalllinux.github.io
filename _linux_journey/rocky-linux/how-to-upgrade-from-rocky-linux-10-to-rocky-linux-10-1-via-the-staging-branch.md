---
title: "How to Upgrade from Rocky Linux 10 to Rocky Linux 10.1 via the Staging Branch"
category: "rocky-linux"
tags: ["rocky-linux", "upgrade", "rocky", "linux", "rocky"]
---

# How to Upgrade from Rocky Linux 10 to Rocky Linux 10.1 via the Staging Branch

* Create a new repository for the staging packages:

```
sudo vim /etc/yum.repos.d/rocky-staging.repo
```

* Add the following contents:

```
[rocky-staging-baseos]
name=Rocky Linux 10.1 Staging - BaseOS
baseurl=https://dl.rockylinux.org/stg/rocky/10.1/BaseOS/$basearch/os/
enabled=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-Rocky-10

[rocky-staging-appstream]
name=Rocky Linux 10.1 Staging - AppStream
baseurl=https://dl.rockylinux.org/stg/rocky/10.1/AppStream/$basearch/os/
enabled=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-Rocky-10

[rocky-staging-extras]
name=Rocky Linux 10.1 Staging - Extras
baseurl=https://dl.rockylinux.org/stg/rocky/10.1/extras/$basearch/os/
enabled=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-Rocky-10
```

* Disable all other repositories, aside from the Rocky Linux Staging repository:

```
sudo sed -i 's/enabled=1/enabled=0/g' /etc/yum.repos.d/*.repo
sudo dnf config-manager --enable rocky-staging-baseos rocky-staging-appstream rocky-staging-extras
```

* Upgrade all packages:

```
sudo dnf upgrade -y
```

* Reboot the machine.
