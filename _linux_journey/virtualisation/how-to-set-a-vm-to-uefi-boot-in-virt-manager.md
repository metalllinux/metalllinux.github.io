---
title: "How to Set a VM to UEFI Boot in virt-manager?"
category: "virtualisation"
tags: ["virtualisation", "uefi", "boot", "virt", "manager"]
---

# How to Set a VM to UEFI Boot in virt-manager?

* Replace the `os` XML portion with the following: 

* For Rocky Linux 10:

```
<os>
  <type arch="x86_64" machine="pc-q35-rhel10.0.0">hvm</type>
  <loader readonly="yes" type="pflash">/usr/share/edk2/ovmf/OVMF_CODE.fd</loader>
  <nvram>/var/lib/libvirt/qemu/nvram/rocky8_VARS.fd</nvram>
  <boot dev="hd"/>
</os>
```

* For Rocky Linux 9:

```
 <os>
  <type arch="x86_64" machine="pc-q35-rhel9.6.0">hvm</type>
  <loader readonly="yes" type="pflash">/usr/share/edk2/ovmf/OVMF_CODE.fd</loader>
  <nvram>/var/lib/libvirt/qemu/nvram/rocky9_VARS.fd</nvram>
  <boot dev="hd"/>
</os>
```
