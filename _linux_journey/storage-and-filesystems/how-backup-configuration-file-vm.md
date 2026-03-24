---
title: "How Backup Configuration File Vm"
category: "storage-and-filesystems"
tags: ["storage-and-filesystems", "backup", "configuration", "file"]
---

* Check VM list with:

virsh list

* Then dump the xml with:

virsh dumpxml VMname > /backup/VM.xml