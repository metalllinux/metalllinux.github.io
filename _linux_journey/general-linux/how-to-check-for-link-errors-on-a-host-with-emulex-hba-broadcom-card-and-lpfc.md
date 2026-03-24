---
title: "How to Check for Link-level Errors on a Host with Emulex HBA Broadcom Card and lpfc driver"
category: "general-linux"
tags: ["check", "link", "errors", "host", "emulex"]
---

# How to Check for Link-level Errors on a Host with Emulex HBA Broadcom Card and lpfc driver

* Need to install `sysfsutils` package.

* Run the following:

```
systool -c fc_host -v
```

