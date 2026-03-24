---
title: "Command To Clear Out Dmesg Logs"
category: "kernel-and-system-internals"
tags: ["kernel-and-system-internals", "command", "clear", "out", "dmesg"]
---

date;ansible all -i /opt/exabeam_installer/inventory -m shell -a order=sorted -f 1 --args="sudo dmesg --clear"