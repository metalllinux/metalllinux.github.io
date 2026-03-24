---
title: "How to Add a Static DHCP Entry into Warewulf 4.5.x and 4.6.x"
category: "rocky-linux"
tags: ["rocky-linux", "add", "static", "dhcp", "entry"]
---

[](https://kb.ciq.com/)[Contact us](https://ciq.com/company/contact-us/)

[Mounting NFS Shares on Warewulf Nodes Using Systemd Overlays](https://kb.ciq.com/article/add-nfs-share-warewulf)[How to Add a Static DHCP Entry into Warewulf 4.5.x and 4.6.x](https://kb.ciq.com/article/add-static-dhcp-warewulf)[Installing NVIDIA Drivers with CUDA in a Warewulf Image](https://kb.ciq.com/article/cuda-nfs-overlay)[How to Setup Ignition with Warewulf on Rocky Linux 8.x](https://kb.ciq.com/article/disk-management)[Enabling Two-Stage Booting with Dracut on an Existing Warewulf Image](https://kb.ciq.com/article/enable-two-stage-booting-dracut-warewulf)[Install NVIDIA Drivers in a Warewulf Container](https://kb.ciq.com/article/installing-nvidia-drivers)[IPMI not working with wwctl power command for the LANPlus interface](https://kb.ciq.com/article/ipmi-not-working-with-wwctl-power-command)[Pxe Boot with Compressed Container Images](https://kb.ciq.com/article/pxe-boot-when-using-compressed-container-images)[Add a Root Password to Warewulf Compute Nodes](https://kb.ciq.com/article/set-root-password-warewulf)[Troubleshooting PXE Booting, Node Provisioning.](https://kb.ciq.com/article/troubleshoot-pxe-booting)[Unable to Mount Root FS After Warewulf Upgrade](https://kb.ciq.com/article/unable-to-mount-root-fs-on-unknown-block)[Warewulf Config for Infinibad Interfaces](https://kb.ciq.com/article/warewulf-config-for-infinibad-interfaces)[Updating a Container's Kernel in Warewulf](https://kb.ciq.com/article/warewulf-container-kernel-upgrade)[DHCP Not Discovering Nodes if Set as Static](https://kb.ciq.com/article/warewulf-dhcp-best-practices)[How to Enable Kdump in Warewulf Nodes](https://kb.ciq.com/article/warewulf-enable-kdump)[Warewulf High Availability Considerations](https://kb.ciq.com/article/warewulf-ha-considerations)[Best Practices for Applying OS Updates Across Node Images](https://kb.ciq.com/article/warewulf-node-os-update-best-practices)[How to Limit Tmpfs for Taking Swap Space](https://kb.ciq.com/article/warewulf-tmpfs-swap-memory)[Troubleshooting Warewulf Client Timeout Issues](https://kb.ciq.com/article/wwclient-timeout-issues)

[Articles](https://kb.ciq.com/) › [Warewulf](https://kb.ciq.com/articles?category=warewulf)

# How to Add a Static DHCP Entry into Warewulf 4.5.x and 4.6.x

[hosts](https://kb.ciq.com/articles?tag=hosts)[static](https://kb.ciq.com/articles?tag=static)[template](https://kb.ciq.com/articles?tag=template)[warewulf](https://kb.ciq.com/articles?tag=warewulf)[dhcp](https://kb.ciq.com/articles?tag=dhcp)

Stephen Simpson  
Senior Customer Support Engineer

Feb 14, 2025

## Introduction

This article will cover assigning an IP address via DHCP using Warewulf, to a device that is not managed directly by Warewulf itself. This is useful in instances where you want to assign an address to a Network Attached Storage (NAS) device or similar non-compute node.

The implementation can be done by modifying the included DHCP template that comes with Warewulf.

## Resolution

First, backup the DHCP template (this is optional but recommended):

```bash
# For Warewulf 4.5.x
cp /var/lib/warewulf/overlays/host/rootfs/etc/dhcp/dhcpd.conf.ww /var/lib/warewulf/overlays/host/rootfs/etc/dhcp/dhcpd.conf.bak

# For Warewulf 4.6.x
cp /usr/share/warewulf/overlays/host/rootfs/etc/dhcp/dhcpd.conf.ww /usr/share/warewulf/overlays/host/rootfs/etc/dhcp/dhcpd.conf.ww.bak
```

There are two implementation methods available: adding the entries directly or creating a separate entry under `/etc/dhcp/hosts.conf` and including each host there. Both of these will be explained below.

### Option 1 - Add entries directly

You'll add each individual entry directly to the `dhcpd.conf` file. You will use the following entry as an example:

```bash
host MyDevice {
    hardware ethernet 00:11:22:33:44:55;
    fixed-address 10.0.0.5;
}
```

Edit the following template file `/var/lib/warewulf/overlays/host/rootfs/etc/dhcp/dhcpd.conf.ww` for Warewulf 4.5.x using [vi](https://docs.rockylinux.org/books/admin_guide/05-vi/) or the text editor of your choice.

Alternatively for Warewulf 4.6.x, edit this template file instead: `/usr/share/warewulf/overlays/host/rootfs/etc/dhcp/dhcpd.conf.ww`

At the bottom of the `dhcpd.conf.ww` file, we are looking for the line `{{/* dhcp enabled */}}`.

Move this under the `{{- end}}` line.

In between the `{{/* dhcp enabled */}}` and `{{- end}}` lines, add your host entry, similar to the example below:

```bash
...
{{end -}}{{/* range NetDevs */}}
{{end -}}{{/* range AllNodes */}}
{{end -}}{{/* if static */}}
{{- else}}
{{abort}}
{{- end}}

host MyDevice {
    hardware ethernet 00:11:22:33:44:55;
    fixed-address 10.0.0.5;
}

{{/* dhcp enabled */}}
```

Add as many hosts as required.

Run the `wwctl configure dhcp` command to update the DHCP config.

Verify your hosts were added correctly using `cat /etc/dhcpd.conf`.

### Option 2 - Include a separate hosts file

Instead of adding each host to the template individually, you can also create a separate file and then include this in the main template.

Create a `hosts.conf` file under `/etc/dhcp/`.

Edit the `hosts.conf` file and add each individual host. Please see example host additions below:

```bash
host MyDevice {
    hardware ethernet 00:11:22:33:44:55;
    fixed-address 10.0.0.5;
}

host MyOtherDevice {
    hardware ethernet AA:BB:CC:DD:EE:FF;
    fixed-address 10.0.0.6;
}
```

Now edit the template.

Similar to "Option 1 - add entries directly", we are looking for the `{{/* dhcp enabled */}}` line in the file.

Move the `{{/* dhcp enabled */}}` line under the `{{- end}}` line.

In the middle of the `{{/* dhcp enabled */}}` and `{{- end}}` lines, add your host information.

Edit the `dhcpd.conf.ww` template file.

For Warewulf 4.5.x, this file is located under `/var/lib/warewulf/overlays/host/rootfs/etc/dhcp/dhcpd.conf.ww`.

For Warewulf 4.6.x, this file is found under `/usr/share/warewulf/overlays/host/rootfs/etc/dhcp/dhcpd.conf.ww`. Exactly as before, you want to find the `{{/* dhcp enabled */}}` line.

Move this under the `{{- end}}` line.

Add your newly created `hosts.conf` via the `Include` line between the `{{- end}}` and `{{/* dhcp enabled */}}` lines. Below is an example:

```bash
...
{{end -}}{{/* range NetDevs */}}
{{end -}}{{/* range AllNodes */}}
{{end -}}{{/* if static */}}
{{- else}}
{{abort}}
{{- end}}

{{ Include "/etc/dhcp/hosts.conf" }}

{{/* dhcp enabled */}}
```

Again, run the `wwctl configure dhcp` command to update the DHCP config.

You can verify your hosts were added by checking the output of the `cat /etc/dhcpd.conf` command.

## Conclusion

You have successfully assigned an IP address to a device via DHCP using Warewulf, therefore opening a world of possibilities to assign IPs to any device on your network; not just compute nodes. This shows just how flexible Warewulf is as a DHCP server, as well as for cluster management.

## References & related articles

VI Text Editor: [Link](https://docs.rockylinux.org/books/admin_guide/05-vi/)  
Warewulf Configuration: [Link](https://warewulf.org/docs/main/contents/configuration.html#warewulf-conf)