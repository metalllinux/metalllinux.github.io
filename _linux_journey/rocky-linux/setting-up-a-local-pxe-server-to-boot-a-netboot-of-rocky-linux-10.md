---
title: "Setting Up a Local PXE Server to Boot a Netboot Install of Rocky Linux 10"
category: "rocky-linux"
tags: ["rocky-linux", "setting", "local", "pxe", "server"]
---

# Setting Up a Local PXE Server to Boot a Netboot Install of Rocky Linux 10

* Installed the required packages:

```
sudo dnf install -y lorax httpd tftp-server dnsmasq  
```

* Enabled the `httpd` service:

```
sudo systemctl enable --now httpd
```

* Enabled the tftp service:

```
sudo systemctl enable --now tftp
```

* Download the Rocky Linux 10 DVD ISO:

```
wget https://download.rockylinux.org/pub/rocky/10/isos/x86_64/Rocky-10.0-x86_64-dvd1.iso
```

 * Unpacked the DVD ISO and created the BaseOS and AppStream repositories:

```
mkdir /mnt/dvd
sudo mount -o loop ~/Rocky-10.0-x86_64-dvd1.iso /mnt/dvd
sudo mkdir -p /var/www/html/rocky10-dvd
sudo cp -av /mnt/dvd/. /var/www/html/rocky10-dvd/
```

* Generated a Rocky Linux 10 image with Lorax:
```
sudo lorax --product "RockyLinux" --version "10" --release "10" --source "https://download.rockylinux.org/pub/rocky/10/BaseOS/x86_64/os/" --source "https://download.rockylinux.org/pub/rocky/10/AppStream/x86_64/os/" --isfinal --logfile lorax.log --buildarch x86_64 --volid "RL10_LIVENET" /tmp/lorax-out
```

* Copied out the boot files to the TFTP server:

``` 
sudo mkdir -p /var/lib/tftpboot/rocky10
sudo cp /tmp/lorax-out/images/pxeboot/{vmlinuz,initrd.img} /var/lib/tftpboot/rocky10/
```

* Copied over the necessary installer stage 2 files:

```
sudo cp -r /tmp/lorax-out/images/ /var/www/html/rocky10/
```

* Mounted the required boot files:

```
mkdir /tmp/efiboot
sudo mount -o loop /tmp/lorax-out/images/efiboot.img /tmp/efiboot
```

* Created the boot directory:

```
sudo mkdir -p /var/lib/tftpboot/rocky10/EFI/BOOT
```

* Copied over the files to the boot directory:

```
sudo cp -av /tmp/efiboot/EFI/BOOT/* /var/lib/tftpboot/rocky10/EFI/BOOT/
```

* Edited `grub.cfg` under `/var/lib/tftpboot/rocky10/EFI/BOOT/grub.cfg` and applied the boot and repo configuration:

```
cat << "EOF" | sudo tee /var/lib/tftpboot/rocky10/EFI/BOOT/grub.cfg
menuentry 'Rocky Linux 10 Install (PXE Boot)' {
    linuxefi /rocky10/vmlinuz inst.stage2=http://192.168.1.150/rocky10 inst.repo=http://192.168.1.150/rocky10-dvd
    initrdefi /rocky10/initrd.img
}
EOF
```

* Edited `dnsmasq.conf` to boot via PXE: 

```
cat << "EOF" | sudo tee /etc/dnsmasq.conf
# Enable DHCP on libvirt default network (192.168.1.0/24)
interface=enp2s0
bind-interfaces
domain-needed
bogus-priv
log-dhcp

# DHCP range for PXE clients
dhcp-range=192.168.1.2,192.168.1.249,12h

# PXE boot loader (UEFI)
dhcp-boot=rocky10/EFI/BOOT/grubx64.efi

# Enable TFTP and set root
enable-tftp
tftp-root=/var/lib/tftpboot
EOF
```
 
* Restarted the `dnsmasq` and `httpd` services:

```
sudo systemctl restart dnsmasq
sudo systemctl restart httpd
```
 
Allow the appropriate services through `firewalld`:

```
sudo firewall-cmd --add-service=tftp --permanent
sudo firewall-cmd --add-service=http --permanent
sudo firewall-cmd --add-service=dns --permanent
sudo firewall-cmd --add-service=dhcp --permanent
sudo firewall-cmd --reload
```

Disable SELinux:

```
sudo setenforce 0
sudo sed -i 's/^SELINUX=.*/SELINUX=permissive/' /etc/selinux/config
```
