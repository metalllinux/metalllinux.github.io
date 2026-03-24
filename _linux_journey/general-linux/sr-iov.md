---
title: "Sr Iov"
category: "general-linux"
tags: ["iov"]
---

* Single Root I/O Virtualisation
* Virtualisation technologies are good, but can use a lot of I/O.
* One way to reduce performance issues regarding I/O, is to enable SR-IOV capabilities, allow a PCIe device to be multiple separate physical PCIe devices.
* SR-IOV provides an isolation of resources, that enable scalability of VMs and enable a near-bare metal performance for I/O operations.
* Important Terms:
* Physical Functions (PF) - Full PCIe devices that include the SR-IOV capabilities and abilities to move data in and out of the device.
* Virtual Functions (VFs)- ’Lightweight’ PCIe functions that contain the resources necessary for data movement, but have a carefully minimised set of configuration resources.