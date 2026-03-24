---
title: "Setup Zfs On Nixos"
category: "storage-and-filesystems"
tags: ["storage-and-filesystems", "setup", "zfs", "nixos"]
---

    Edit /etc/nixos/configuration.nix and add the following options:

    boot.supportedFilesystems = [ "zfs" ];
    boot.zfs.forceImportRoot = false;
    networking.hostId = "yourHostId";

    Where hostID can be generated with:

    head -c4 /dev/urandom | od -A none -t x4

    Apply configuration changes:

    nixos-rebuild boot

    Reboot:

    reboot

