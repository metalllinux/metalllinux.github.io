---
title: "How to Setup a PXE Server on Rocky Linux 9.x"
category: "rocky-linux"
tags: ["rocky-linux", "pxe", "boot", "rocky", "linux", "dnsmasq", "tftp", "httpd", "uefi"]
---

## Introduction

Using PXE to bootstrap nodes with an image is commonplace in many business environments and has made both deploying and managing an image across a fleet of nodes at scale trivial.

This article walks through deploying a PXE server on Rocky Linux 9.x to network-boot a UEFI client and install Rocky Linux 10.2. The setup uses `dnsmasq` in **proxy DHCP mode** — which works alongside an existing router DHCP server without conflict — `httpd` to serve the DVD installer tree over HTTP, and `tftp-server` to transfer the bootloader and kernel to PXE clients. Boot files are extracted directly from the Rocky Linux 10.2 DVD ISO; no external image generation tool is required.

This guide focuses on UEFI boot only.

## Prerequisites

- A node running Rocky Linux 9.x. This will be the PXE server.
- A Rocky Linux 10.2 DVD ISO on the server (e.g. at `/home/howard/isos/Rocky-10.2-x86_64-dvd1.iso`). Adjust the path to match your environment.
- A UEFI-capable client on the same subnet as the PXE server.
- An existing DHCP server on the network (e.g. a router). Proxy DHCP mode means `dnsmasq` will not conflict with it.
- `sudo` access on the PXE server.

## Instructions

### PXE Server Setup

- Update all packages:

```bash
sudo dnf update -y
```

- Install the required packages — `dnsmasq` (proxy DHCP + TFTP), `tftp-server`, and `httpd` (to serve the installer tree over HTTP):

```bash
sudo dnf install -y dnsmasq tftp-server httpd
```

- Set SELinux to permissive mode to avoid file-context conflicts with the TFTP and HTTP services:

```bash
sudo setenforce 0
sudo sed -i 's/^SELINUX=.*/SELINUX=permissive/' /etc/selinux/config
```

- Create the required directory structure:

```bash
sudo mkdir -p /var/lib/tftpboot/rocky10/EFI/BOOT
sudo mkdir -p /var/lib/tftpboot/EFI/BOOT
sudo mkdir -p /var/www/html/rocky10-dvd
sudo mkdir -p /mnt/dvd
sudo mkdir -p /tmp/efiboot
```

- Mount the Rocky Linux 10.2 DVD ISO:

```bash
sudo mount -o loop /home/howard/isos/Rocky-10.2-x86_64-dvd1.iso /mnt/dvd
```

- Copy the full DVD contents to the HTTP root. This directory provides both the Anaconda stage2 installer image and the package repositories (`BaseOS` and `AppStream`) over HTTP:

```bash
sudo cp -a /mnt/dvd/. /var/www/html/rocky10-dvd/
```

- Copy the PXE kernel and initial RAM disk from the ISO:

```bash
sudo cp /mnt/dvd/images/pxeboot/vmlinuz /var/lib/tftpboot/rocky10/
sudo cp /mnt/dvd/images/pxeboot/initrd.img /var/lib/tftpboot/rocky10/
```

- Mount the EFI boot image embedded in the ISO and copy the UEFI bootloader files:

```bash
sudo mount -o loop /mnt/dvd/images/efiboot.img /tmp/efiboot
sudo cp -a /tmp/efiboot/EFI/BOOT/. /var/lib/tftpboot/rocky10/EFI/BOOT/
sudo umount /tmp/efiboot
```

- Unmount the ISO (all required files have now been copied):

```bash
sudo umount /mnt/dvd
```

- Write the GRUB PXE boot menu.

**Important:** `grubx64.efi`, once loaded via TFTP, searches for `grub.cfg` at the **root of the TFTP server** — not relative to the subdirectory it was served from. GRUB walks through the following search sequence:

```
(tftp)/grub.cfg-<MAC-address>
(tftp)/grub.cfg-<IP-in-hex>
...
(tftp)/grub.cfg                 ← generic fallback
(tftp)/EFI/BOOT/grub.cfg        ← also checked
```

The `grub.cfg` must therefore be placed at `/var/lib/tftpboot/grub.cfg` **and** `/var/lib/tftpboot/EFI/BOOT/grub.cfg`. Placing it only in the `rocky10/EFI/BOOT/` subdirectory where `grubx64.efi` lives will cause GRUB to drop to an interactive shell instead of showing the boot menu.

```bash
cat << "EOF" | sudo tee /var/lib/tftpboot/grub.cfg
set default=0
set timeout=60

menuentry 'Rocky Linux 10.2 Install (PXE Boot)' {
    linuxefi /rocky10/vmlinuz inst.stage2=http://<server-ip>/rocky10-dvd inst.repo=http://<server-ip>/rocky10-dvd inst.text quiet
    initrdefi /rocky10/initrd.img
}
EOF

sudo cp /var/lib/tftpboot/grub.cfg /var/lib/tftpboot/EFI/BOOT/grub.cfg
sudo cp /var/lib/tftpboot/grub.cfg /var/lib/tftpboot/rocky10/EFI/BOOT/grub.cfg
```

Replace `<server-ip>` with the IP address of the PXE server. The `inst.text` kernel argument launches the Anaconda installer in text mode rather than the graphical interface — remove it to use the GUI.

- Configure `dnsmasq` in proxy DHCP mode. The `dhcp-range=<subnet>,proxy` directive tells `dnsmasq` to respond to PXE DHCP requests without assigning IP addresses, leaving that to the existing router:

```bash
cat << "EOF" | sudo tee /etc/dnsmasq.conf
# PXE Server - Proxy DHCP mode (works alongside existing router DHCP)
interface=enp2s0
bind-interfaces
log-dhcp

# Proxy DHCP: do not assign IPs, only respond to PXE boot requests
dhcp-range=192.168.1.0,proxy

# Tell UEFI clients which bootloader to fetch from TFTP
pxe-service=x86-64_EFI,"Rocky Linux 10.2 PXE",rocky10/EFI/BOOT/grubx64.efi

# TFTP server
enable-tftp
tftp-root=/var/lib/tftpboot
EOF
```

Replace `enp2s0` with the name of your network interface (use `ip a` to find it) and `192.168.1.0` with your subnet address if different.

- Enable and start `httpd`, `tftp`, and `dnsmasq`:

```bash
sudo systemctl enable --now httpd tftp dnsmasq
```

- Allow the required traffic through the firewall:

```bash
sudo firewall-cmd --add-service=tftp --permanent
sudo firewall-cmd --add-service=http --permanent
sudo firewall-cmd --add-service=dhcp --permanent
sudo firewall-cmd --add-port=4011/udp --permanent
sudo firewall-cmd --reload
```

The ports opened are:

- `tftp` — UDP 69 (TFTP file transfer for bootloader, kernel, and initrd)
- `http` — TCP 80 (HTTP installer tree served by `httpd`)
- `dhcp` — UDP 67 (proxy DHCP, to receive PXE DHCP DISCOVER broadcasts)
- `4011/udp` — proxy DHCP response port

### PXE Client Setup

Enable PXE network boot on the client machine from its UEFI firmware settings. The exact menu path varies by manufacturer, but generally involves:

- Enabling the onboard NIC / LAN controller.
- Enabling the **PXE Option ROM** or **Network Stack** for the NIC.
- Enabling **IPv4 PXE Support**.
- Setting the boot order so that **Network Boot** is listed before the local drive.

Restart the client. The boot sequence will be:

1. The UEFI firmware sends a DHCP DISCOVER with a PXE option.
2. The router assigns an IP address; `dnsmasq` (proxy DHCP) responds with the path to `grubx64.efi`.
3. The client fetches `grubx64.efi` from the TFTP server and GRUB starts.
4. GRUB searches the TFTP root for `grub.cfg` and displays the boot menu.
5. Select **Rocky Linux 10.2 Install (PXE Boot)** or wait 60 seconds for the auto-select timeout.
6. The kernel and initrd are fetched via TFTP; Anaconda then retrieves `install.img` over HTTP from `http://<server-ip>/rocky10-dvd`.
7. The installer launches — in text mode if `inst.text` is present in the kernel arguments.

## Conclusion

This guide walked through setting up a PXE server on Rocky Linux 9.x to serve Rocky Linux 10.2 to UEFI clients over the network. The setup uses `dnsmasq` in proxy DHCP mode, `httpd` to serve the full DVD installer tree, and boot files extracted directly from the DVD ISO. The proxy DHCP approach makes this safe to deploy on networks that already have a router acting as DHCP server.

The most important thing to get right is `grub.cfg` placement: it must live at the TFTP root (and `/EFI/BOOT/` at the TFTP root), not in the subdirectory where `grubx64.efi` is served from. Getting this wrong causes GRUB to silently drop to an interactive shell with no indication of what went wrong.
