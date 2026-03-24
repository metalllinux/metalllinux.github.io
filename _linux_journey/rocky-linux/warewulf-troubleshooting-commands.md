---
title: "Warewulf Troubleshooting Commands"
category: "rocky-linux"
tags: ["rocky-linux", "warewulf", "troubleshooting", "commands"]
---

sudo wwctl node set cpu-10-26 --container=rocky9.2_opx-10.14 
sudo wwctl node list -a cpu-10-26
sudo wwctl configure node cpu-10-
sudo wwctl overlay build
sudo wwctl node power off cpu-10-26
sudo wwctl node power on cpu-10-26
sudo wwctl container list
sudo wwctl container show rocky9.2_opx-10.14
sudo wwctl node delete cpu-10-26
sudo wwctl node add cpu-10-26 --container=IMAGE --ipaddr=IP
sudo wwctl node set cpu-10-26 --profile=quanah --container=IMAGE
sudo wwctl configure node cpu-10-26 
sudo wwctl overlay build -a
sudo wwctl node list -a cpu-10-26
sudo wwctl node power off cpu-10-26 
sudo wwctl node power on cpu-10-26