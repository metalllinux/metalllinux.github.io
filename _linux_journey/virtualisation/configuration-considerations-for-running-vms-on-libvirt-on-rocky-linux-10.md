---
title: "Configuration Considerations for Running VMs on libvirt on Rocky Linux 10"
category: "virtualisation"
tags: ["virtualisation", "libvirt", "kvm", "qemu", "virt-manager", "rocky-linux-10", "rocky-linux"]
---

Rocky Linux 10 ships with QEMU 9.x and libvirt 10.x — significantly newer than the versions found on Rocky Linux 9. This combination introduces stricter XML validation and removes block driver support that older tooling relied upon. This article documents a concrete failure encountered when creating a VM in virt-manager and explains the underlying cause and fix.

## The Error

When attempting to create a new VM via the virt-manager wizard on Rocky Linux 10, the installation fails with:

```
Unable to complete install: 'unsupported configuration: storage type 'dir' requires use of storage format 'fat''
```

The traceback points to `libvirt.libvirtError: unsupported configuration: storage type 'dir' requires use of storage format 'fat'` raised during `virDomainCreateXML()`.

The virt-manager wizard had generated the following CD-ROM disk entry in the domain XML, pointing at a directory rather than an ISO file:

```xml
<disk type="dir" device="cdrom">
  <source dir="/home/howard/torrents/Rocky-9.8-x86_64-dvd"/>
  <target dev="sda" bus="sata"/>
  <readonly/>
</disk>
```

## Why libvirt Rejects This

libvirt 10.x added strict validation: when a disk source uses `type="dir"`, the driver format must be declared as `fat`. This is because the only way QEMU can present a host directory to a guest is as a virtual FAT filesystem. Earlier libvirt versions were more permissive and would silently pass the configuration through; libvirt 10.x refuses to do so.

Adding `<driver name="qemu" type="fat"/>` to satisfy the validation check produces a second, harder failure:

```
Unable to complete install: 'internal error: process exited while connecting to monitor:
qemu-kvm: -blockdev {"driver":"vvfat","dir":"/home/howard/torrents/Rocky-9.8-x86_64-dvd",...}:
Unknown driver 'vvfat''
```

## Why the Second Error Occurs

libvirt translates `type="dir"` with `format="fat"` into a QEMU `-blockdev` argument using the `vvfat` (Virtual VFAT) block driver. QEMU 9.x **removed the `vvfat` driver entirely**. There is no workaround that preserves `type="dir"` — the driver simply does not exist in the version of QEMU shipped with Rocky Linux 10.

## The Root Cause

The Rocky Linux torrent downloads the ISO file into a named subdirectory alongside its checksums, rather than placing the ISO directly in the download root. The directory contents look like this:

```
Rocky-9.8-x86_64-dvd/
├── CHECKSUM
├── Rocky-9.8-x86_64-dvd.iso
├── Rocky-9.8-x86_64-dvd.iso.CHECKSUM
├── Rocky-9.8-x86_64-dvd.iso.CHECKSUM.asc
└── Rocky-9.8-x86_64-dvd.iso.manifest
```

When the path provided to virt-manager is the directory rather than the `.iso` file inside it, virt-manager generates `type="dir"` for the CD-ROM disk entry. On Rocky Linux 9 and earlier hosts this would have worked via `vvfat`; on Rocky Linux 10 it does not.

## The Fix

Point the CD-ROM disk entry directly at the ISO file. Change the disk entry from:

```xml
<disk type="dir" device="cdrom">
  <driver name="qemu" type="fat"/>
  <source dir="/home/howard/torrents/Rocky-9.8-x86_64-dvd"/>
  <target dev="sda" bus="sata"/>
  <readonly/>
</disk>
```

To:

```xml
<disk type="file" device="cdrom">
  <driver name="qemu" type="raw"/>
  <source file="/home/howard/torrents/Rocky-9.8-x86_64-dvd/Rocky-9.8-x86_64-dvd.iso"/>
  <target dev="sda" bus="sata"/>
  <readonly/>
</disk>
```

In virt-manager, this can be corrected before starting the installation by enabling **Customise configuration before install** on the final step of the New VM wizard, navigating to the SATA CD-ROM device, and updating the source path to point to the `.iso` file directly.

## Summary

| Component | Change in Rocky Linux 10 |
|---|---|
| libvirt 10.x | Requires `format="fat"` when `type="dir"` is used for a disk source |
| QEMU 9.x | Removed the `vvfat` block driver entirely |
| Effect | Directory-based CD-ROM sources no longer work under any configuration |
| Fix | Always point the CD-ROM source at an ISO file (`type="file"`) |
