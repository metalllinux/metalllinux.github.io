---
title: "How to Create a Local Repository for DNF to Ingest"
category: "rocky-linux"
tags: ["rocky-linux", "create", "local", "repository", "dnf"]
---

# How to Create a Local Repository for DNF to Ingest

```
cat << 'EOF' > /etc/yum.repos.d/local.repo
[appstream86]
name=Local AppStream86
baseurl=file:///root/appstream86
enabled=1
gpgcheck=0

[baseos86]
name=Local BaseOS86
baseurl=file:///root/baseos86
enabled=1
gpgcheck=0

[centos8-openvswitch]
name=Local CentOS 8 Openvswitch
baseurl=file:///root/centos8-openvswitch
enabled=1
gpgcheck=0

[CIQ-DRIVERS-8]
name=Local CIQ Drivers 8
baseurl=file:///root/CIQ-DRIVERS-8
enabled=1
gpgcheck=0

[CIQ-FIPS-86]
name=Local CIQ FIPS 86
baseurl=file:///root/CIQ-FIPS-86
enabled=1
gpgcheck=0

[CIQ-LTS-86]
name=Local CIQ LTS 86
baseurl=file:///root/CIQ-LTS-86
enabled=1
gpgcheck=0

[EPEL8]
name=Local EPEL8
baseurl=file:///root/EPEL8
enabled=1
gpgcheck=0

[HPE_Linux]
name=Local HPE Linux
baseurl=file:///root/HPE_Linux
enabled=1
gpgcheck=0

[Rocky86-Nvidia]
name=Rocky86-Nvidia
baseurl=file:///root/Rocky86-Nvidia
enabled=1
gpgcheck=0

[SIG-Cloud-Next-8]
name=Local SIG-Cloud-Next-8
baseurl=file:///root/SIG-Cloud-Next-8
enabled=1
gpgcheck=0

[SIG-Cloud-Next-8-Nonfree]
name=Local SIG-Cloud-Next-8-Nonfree
baseurl=file:///root/SIG-Cloud-Next-8-Nonfree
enabled=1
gpgcheck=0
EOF
```

* Disable the default repositories:

```
sed -i 's/^enabled=1$/enabled=0/' /etc/yum.repos.d/Rocky-{AppStream,BaseOS,Extras}.repo
```

