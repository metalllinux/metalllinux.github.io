---
title: "My Ansible Commands"
category: "automation-and-configuration"
tags: ["automation-and-configuration", "ansible", "commands"]
---

date;ansible all -i /opt/exabeam_installer/inventory -m shell -a order=sorted -f 1 --args="df -h"