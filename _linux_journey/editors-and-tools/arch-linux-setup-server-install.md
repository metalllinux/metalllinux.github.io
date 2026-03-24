---
title: "Find a keyboard map"
category: "editors-and-tools"
tags: ["editors-and-tools", "arch", "linux", "setup", "server"]
---

```
# Find a keyboard map
find /usr/share/kbd/keymaps/ -type f -name "*search_term*"
# US keyboard
loadkeys us
loadkeys jp106
setfont ter-132n
timedatectl set-ntp true
# Set up mirrors.
reflector -c Japan -a 6 --sort rate --save /etc/pacman.d/mirrorlist
# Syncronise the server.
pacman -Syy
# Partition the disk using gdisk to create GPT labels.
gdisk /dev/vda
# New partition.
n
# Partition 1.
1
# First sector is fine.
enter
# Last sector.
+300M
# EFI system partition code is ef00
ef00
# Second partition (swap).
n
2
# First sector is okay as it is.
# Last sector is 1GB.
+1G
# Code for the swap is 8200
8200
# Partition 3
# Accept all of the defaults and no need to type in a partition code.
n
# Write changes to the disk.
w
Y
# Format the partitions.
mkfs.fat -F32 /dev/vda1
mkswap /dev/vda2
swapon /dev/vda2
# Enable encryption
cryptsetup luksFormat /dev/vda3
# Provide a password.
# Open the partition.
cryptsetup luksOpen /dev/vda3 shadow 
# Format the encrypted partition.
mkfs.btrfs /dev/mapper/shadow
# Mount VDA3 to create subvolumes.
mount /dev/mapper/shadow /mnt
cd /mnt
# Create the subvolumes.
btrfs su cr @
btrfs su cr @home
btrfs su cr @snapshots
btrfs su cr @var_log
# Exit the directory.
cd
# Unmount
umount /mnt
# Mount each subvolume.
mount -o noatime,compress=zstd,space_cache=v2,discard=async,subvol=@ /dev/mapper/shadow /mnt
# Create the directories.
mkdir -p /mnt/{boot,home,.snapshots,var_log}
# Back to mounting subvolumes.
mount -o noatime,compress=zstd,space_cache=v2,discard=async,subvol=@home /dev/mapper/shadow /mnt/home
mount -o noatime,compress=zstd,space_cache=v2,discard=async,subvol=@snapshots /dev/mapper/shadow /mnt/.snapshots
mount -o noatime,compress=zstd,space_cache=v2,discard=async,subvol=@var_log /dev/mapper/shadow /mnt/var_log
# Mount boot partition.
mount /dev/vda1 /mnt/boot
# Install initial packages.
pacstrap /mnt base linux linux-firmware vim intel-ucode btrfs-progs git
# Generate Mount Points
genfstab -U /mnt >> /mnt/etc/fstab
# Enter the installation directory.
arch-chroot /mnt
# Create symbolic links
ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime
# Synchronise the hardware clock
hwclock --systohc
# Set locales.
vim /etc/locale.gen
locale-gen
vim /etc/locale.conf
LANG=en_US.UTF-8
# Set vconsole settings.
vim /etc/vconsole.conf
KEYMAP=us
# Set the hostname.
vim /etc/hostname
# Enter the name of the machine only.
# Configure the hosts file for IPV4 and IPV6.
vim /etc/hosts
127.0.0.1<tab>localhost
::1<tab>localhost
127.0.1.1<tab><YOUR_HOSTNAME>.localdomain<tab><YOUR_HOSTNAME>
# Provide password to the root user.
echo root:password | chpasswd
# Install other packages required for the system.
pacman -S grub grub-btrfs efibootmgr networkmanager network-manager-applet dialog wpa_supplicant mtools dosfstools base-devel linux-headers avahi xdg-user-dirs xdg-utils gvfs gvfs-smb nfs-utils inetutils dnsutils bluez bluez-utils cups alsa-utils pipewire pipewire-alsa pipewire-pulse pipewire-jack bash-completion openssh rsync reflector acpi acpi_call tlp virt-manager qemu edk2-ovmf bridge-utils dnsmasq vde2 openbsd-netcat iptables-nft ipset firewalld sof-firmware nss-mdns acpid os-prober ntfs-3g snapper
# Select qemu-full
# Remove iptables - y
# Install Intel GPU drivers.
pacman -S --noconfirm xf86-video-intel
# Regenerate the image.
mkinitcpio -p linux
# Next we install grub.
grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB 
grub-mkconfig -o /boot/grub/grub.cfg
# Start services.
systemctl enable NetworkManager
systemctl enable bluetooth
systemctl enable cups.service
systemctl enable sshd
systemctl enable avahi-daemon
systemctl enable tlp # You can comment this command out if you didn't install tlp, see above
systemctl enable reflector.timer
systemctl enable fstrim.timer
systemctl enable libvirtd
systemctl enable firewalld
systemctl enable acpid
# Add user.
useradd -m ermanno
echo howard:password | chpasswd
usermod -aG libvirt howard
echo "howard ALL=(ALL) ALL" >> /etc/sudoers.d/howard
# Edit the mkinitcpio file.
vim /etc/mkinitcpio.conf
# Add the following into the MODULES section.
MODULES=(btrfs)	
# Add encrypt before the filesystems hook
HOOKS=(base udev autodetect modconf block encrypt filesystems keyboard fsck)
# Save the file.
# Regenerate mkinitcpio
mkinitcpio -p linux
blkid
# Need UUID of the /dev/vda3 (the device itself)
blkid >> /etc/default/grub
vim /etc/default/grub
# Under GRUB_CMDLINE_LINUX_DEFAULT="loglevel=3 quiet" add cryptdevice=<UUID of device>:<name of device> root=/dev/mapper/shadow and remove the quotations as well. It looks like this:
GRUB_CMDLINE_LINUX_DEFAULT="loglevel=3 quiet cryptdevice=UUID=<UUID_HERE>:shadow root=/dev/mapper/shadow"
# Save the file.
# Rebuild the grub configuration file.
grub-mkconfig -o /boot/grub/grub.cfg
exit
reboot
```