---
title: "Use Yumdownloader To Only Download Packages In Cen"
category: "general-linux"
tags: ["yumdownloader", "only", "download", "packages", "cen"]
---

```
yum install -y yum-utils
yumdownload <package_name>
```
* To download a specific package version, use:
```
yumdownload <package_name>-<version>
```
* You can find out all of the available packages by running `yum --showduplicates list httpd`