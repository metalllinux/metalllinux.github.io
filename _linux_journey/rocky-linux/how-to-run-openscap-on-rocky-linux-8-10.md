---
title: "How To Run Openscap On Rocky Linux 8.10"
category: "rocky-linux"
tags: ["rocky-linux", "run", "openscap", "rocky", "linux"]
---

* First install the packages:
```
dnf install -y scap-security-guide openscap-scanner
```
* Running the scan:
```
oscap xccdf eval --profile xccdf_org.ssgproject.content_profile_cis /usr/share/xml/scap/ssg/content/ssg-rl8-ds.xml
```