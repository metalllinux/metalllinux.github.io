---
title: "CVM Testing in Azure"
category: "general-linux"
tags: ["cvm", "testing", "azure"]
---

# CVM Testing in Azure

Once you get that sorted, it'll boot in Confidential Mode with no disk encryption using a standard kernel. Use a DCasv5/6 or ECasv5/6 shape. The DCv2 doesn't support Confidential.

If you need to test with CVM OS Disk Encryption, you need to swap the basic kernel for a UKI, remove Grub and Certwrapper, remove all traces of the non-UKI, and configure the EFI such that it boots directly into the UKI.

