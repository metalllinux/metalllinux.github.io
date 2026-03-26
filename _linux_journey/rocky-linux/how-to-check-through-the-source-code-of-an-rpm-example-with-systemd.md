---
title: "How to Check Through The Source Code of an RPM, with systemd as an example:"
category: "rocky-linux"
tags: ["rocky-linux", "check", "through", "source", "code"]
---

# How to Check Through The Source Code of an RPM, with systemd as an example:

### Rocky Linux 9.6 systemd Source Code Review

* I pulled the latest `systemd` source RPM for Rocky Linux 9.6:

```
wget https://dl.rockylinux.org/pub/rocky/9/BaseOS/source/tree/Packages/s/systemd-252-51.el9_6.1.src.rpm
```

* Extracted the contents of the source RPM:

```
rpm -ivh ./systemd-252-51.el9_6.1.src.rpm
```

* Built the `systemd` RPM:

```
rpmbuild --nodeps -bp ~/rpmbuild/SPECS/systemd.spec
```

* Confirmed that indeed 20% of RAM is used in Rocky Linux 9.6:

```
grep TMPFS_LIMITS_RUN /home/myuser/rpmbuild/BUILD/systemd-252/src/shared/mount-util.h
#define TMPFS_LIMITS_RUN             ",size=20%,nr_inodes=800k"
```

