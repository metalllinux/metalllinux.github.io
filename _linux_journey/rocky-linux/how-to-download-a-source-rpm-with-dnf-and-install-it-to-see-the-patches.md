---
title: "How to Download a Source RPM with DNF and Install it to See the Patches"
category: "rocky-linux"
tags: ["rocky-linux", "download", "source", "rpm", "dnf"]
---

# How to Download a Source RPM with DNF and Install it to See the Patches

* Install the `rpmbuild` package:

```
dnf install -y rpmbuild
```

* Download the source RPM that you want, for example:

```
dnf download --source openssh
```

* Install the downloaded RPM like the following:

```
rpm --install ./openssh-8.7p1-47.el9_7.rocky.0.1.src.rp
```

* Check the home directory and you'll see the `rpmbuild` directory available. Inside will be the `SOURCES` and `SPEC` directories. Patches are available under `SOURCES`.
