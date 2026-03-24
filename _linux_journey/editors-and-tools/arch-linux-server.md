---
title: "Find a keyboard map"
category: "editors-and-tools"
tags: ["editors-and-tools", "arch", "linux", "server"]
---

```
# Find a keyboard map
find /usr/share/kbd/keymaps/ -type f -name "*search_term*"

# US keyboard
loadkeys us

# Japanese keyboard
loadkeys jp106

# Set font if needed
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
pacstrap /mnt base linux linux-firmware vim intel-ucode/amd-ucode btrfs-progs git

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

# en_US is easiest

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

pacman -S grub grub-btrfs efibootmgr networkmanager network-manager-applet dialog wpa_supplicant mtools dosfstools base-devel linux-headers avahi xdg-user-dirs xdg-utils gvfs gvfs-smb nfs-utils inetutils dnsutils bash-completion openssh rsync reflector acpi acpi_call dnsmasq vde2 openbsd-netcat iptables-nft ipset firewalld nss-mdns acpid ntfs-3g snapper sof-firmware wget unzip man

# Remove iptables - y

# Install Intel GPU drivers.
pacman -S --noconfirm xf86-video-intel

# Nvidia Drivers - for example with an Nvidia GTX 1060
pacman -S nvidia

# Add 32 bit Support for Nvidia Cards
# Enable the multilib repo first under /etc/pacman.conf
[multilib]
Include = /etc/pacman.d/mirrorlist
# Then install the lib32 package
sudo pacman -S lib32-nvidia-utils

# Remove kms under HOOKS in the /etc/mkinitcpio.conf file 

# Regenerate the image.
mkinitcpio -p linux

# Next we install grub.
grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB 

grub-mkconfig -o /boot/grub/grub.cfg

# Start services.
systemctl enable NetworkManager
systemctl enable sshd
systemctl enable avahi-daemon
systemctl enable reflector.timer
systemctl enable fstrim.timer
systemctl enable firewalld
systemctl enable acpid

# Add user.
useradd -m howard

echo howard:password | chpasswd

echo "howard ALL=(ALL) ALL" >> /etc/sudoers.d/howard

# Edit the mkinitcpio file.
vim /etc/mkinitcpio.conf

# Add the following into the MODULES section. i915 is for Intel, amdgpu is for an AMD GPU.
MODULES=(btrfs i915)	

# Add encrypt before the filesystems hook

HOOKS=(base udev autodetect modconf block encrypt filesystems keyboard fsck)

# Save the file.

# Regenerate mkinitcpio
mkinitcpio -p linux

blkid

# Need UUID of the /dev/vda3 (the device itself)
blkid | grep vda3 >> /etc/default/grub

vim /etc/default/grub
# Under GRUB_CMDLINE_LINUX_DEFAULT="loglevel=3 quiet" add cryptdevice=UUID=<UUID of device>:<name of device> root=/dev/mapper/shadow and remove the quotations as well. It looks like this:

GRUB_CMDLINE_LINUX_DEFAULT="loglevel=3 quiet cryptdevice=UUID=<UUID_HERE>:shadow root=/dev/mapper/shadow"

# Save the file.

# Rebuild the grub configuration file.
grub-mkconfig -o /boot/grub/grub.cfg

exit

reboot

# Log in as your regular user.

# Change passwords for all users.

# Set up snapper
sudo umount /.snapshots
sudo rm -r /.snapshots
sudo snapper -c shadow create-config / 
sudo btrfs subvolume delete /.snapshots
sudo mkdir /.snapshots
sudo mount -a
sudo chmod 750 /.snapshots
sudo vim /etc/snapper/configs/shadow
# Change ALLOW_USERS to ALLOW_USERS="howard"
# Change timeline cleanup
TIMELINE_MIN_AGE="1800"
TIMELINE_LIMIT_HOURLY="5"
TIMELINE_LIMIT_DAILY="7"
TIMELINE_LIMIT_WEEKLY="0"
TIMELINE_LIMIT_MONTHLY="0"
TIMELINE_LIMIT_YEARLY="0"
# Save the file.

# Enable snapper
sudo systemctl enable --now snapper-timeline.timer 
sudo systemctl enable --now snapper-cleanup.timer 

# Install yay
git clone https://aur.archlinux.org/yay
cd yay
makepkg -si PKGBUILD
# Accept all of the install prompts.
cd

# Install snapper packages
yay -S snap-pac-grub
rm -Rf ./yay

# Back up the boot partition.
sudo mkdir /etc/pacman.d/hooks
sudo vim /etc/pacman.d/hooks/50-bootbackup.hook
# Add the following
[Trigger]
Operation = Upgrade
Operation = Install
Operation = Remove
Type = Path
Target = boot/*
[Action]
Depends = rsync
Description = Backing up /boot...
When = PreTransaction
Exec = /usr/bin/rsync -a --delete /boot /.bootbackup
#There is a space between /boot and /.bootbackup
# Change permissions of Snapper
sudo chmod a+rx /.snapshots
# The user is always root.
sudo chown :<your_group> /.snapshots
# For now, these are read-only - check the Arch Wiki on how to make these write enabled.

reboot

# Set up networking
* Find the interfaces
`nmcli connection show`
* Set the network information like the below format:
nmcli connection modify <connection_name> ipv4.method manual ipv4.addresses <static_ip_address>/<subnet_mask> ipv4.gateway <gateway_ip_address> ipv4.dns <dns_server_ip>
* Bring the connection up to enable the changes.
`nmcli connection up <connection_name>`
* Check that the network information has been saved.
`nmcli device show <connection_name>`

# bcachefs setup (RAID0)

sudo pacman -S bcachefs-tools
sudo bcachefs format --compression=zstd:15 /dev/sd<X> /dev/sd<X>

# bcachefs setup (RAID1)
sudo bcachefs format --compression=zstd:15 /dev/sda /dev/sdb --replicas=2

# Create a systemd mount to mount at boot
vim /etc/systemd/system/tails-mount.service
[Unit]
Description=Mount bcachefs
After=network-online.target
Wants=network-online.target

[Service]
Type=oneshot
ExecStart=/home/howard/scripts/tails-mount.sh

[Install]
WantedBy=multi-user.target

# Create the directory to mount the drives
sudo mkdir /mnt/tails

# Create the following boot script
mkdir ~/scripts
vim ~/scripts/tails-mount.sh 

#!/bin/bash
# Mount the bcachefs devices
mount -t bcachefs /dev/sda:/dev/sdc /mnt/tails

# Make the script executable
chmod +x ~/scripts/tails-mount.sh

# Enable and start the services
sudo systemctl enable --now tails-mount.service

# Set permissions on the drives:
sudo chown howard:howard -R /mnt/tails

# ZFS setup
yay -S zfs-utils-git
yay -S zfs-linux-git
zpool import -d /dev/disk/by-id <pool_name_here>

# Set up ssh keys between nodes
# On each node, run
ssh-keygen -t rsa -b 4096

# Copy the generated key to the node of choice:
ssh-copy-id -i ~/.ssh/<public_key_here> username@remote-server.org

# tmux Installation
sudo pacman -S tmux
yay -S tmux-bash-completion-git

# systemd service files for rsync transfer
# Create the following service file:
vim /etc/systemd/system/sonic-send.service

# Add this to the service file:
[Unit]
Description=Rsync files to tails
After=network.target

[Service]
ExecStart=/home/howard/scripts/sonic-send.sh
Restart=always
User=howard

# Create the script in /home/howard/scripts/sonic-send.sh
# Add the following:
#!/bin/bash
# rsync to tails
rsync -e "ssh -i /home/howard/.ssh/sonic" --ignore-existing -azvr --progress /mnt/sonic/anime/ howard@192.168.1.102:/mnt/tails/anime/
rsync -e "ssh -i /home/howard/.ssh/sonic" --ignore-existing -azvr --progress /mnt/sonic/cartoons/ howard@192.168.1.102:/mnt/tails/cartoons/
rsync -e "ssh -i /home/howard/.ssh/sonic" --ignore-existing -azvr --progress /mnt/sonic/documents/ howard@192.168.1.102:/mnt/tails/documents/
rsync -e "ssh -i /home/howard/.ssh/sonic" --ignore-existing -azvr --progress /mnt/sonic/ebooks/ howard@192.168.1.102:/mnt/tails/ebooks/
rsync -e "ssh -i /home/howard/.ssh/sonic" --ignore-existing -azvr --progress /mnt/sonic/games/ howard@192.168.1.102:/mnt/tails/games/
rsync -e "ssh -i /home/howard/.ssh/sonic" --ignore-existing -azvr --progress /mnt/sonic/linux/ howard@192.168.1.102:/mnt/tails/linux/
rsync -e "ssh -i /home/howard/.ssh/sonic" --ignore-existing -azvr --progress /mnt/sonic/live_shows/ howard@192.168.1.102:/mnt/tails/live_shows/
rsync -e "ssh -i /home/howard/.ssh/sonic" --ignore-existing -azvr --progress /mnt/sonic/movies/ howard@192.168.1.102:/mnt/tails/movies/
rsync -e "ssh -i /home/howard/.ssh/sonic" --ignore-existing -azvr --progress /mnt/sonic/music/ howard@192.168.1.102:/mnt/tails/music/
rsync -e "ssh -i /home/howard/.ssh/sonic" --ignore-existing -azvr --progress /mnt/sonic/photos/ howard@192.168.1.102:/mnt/tails/photos/
rsync -e "ssh -i /home/howard/.ssh/sonic" --ignore-existing -azvr --progress /mnt/sonic/shows/ howard@192.168.1.102:/mnt/tails/shows/

# rsync to knuckles
rsync -e "ssh -i /home/howard/.ssh/sonic" --ignore-existing -azvr --progress /mnt/sonic/anime/ howard@192.168.1.103:/mnt/knuckles/anime/
rsync -e "ssh -i /home/howard/.ssh/sonic" --ignore-existing -azvr --progress /mnt/sonic/cartoons/ howard@192.168.1.103:/mnt/knuckles/cartoons/
rsync -e "ssh -i /home/howard/.ssh/sonic" --ignore-existing -azvr --progress /mnt/sonic/documents/ howard@192.168.1.103:/mnt/knuckles/documents/
rsync -e "ssh -i /home/howard/.ssh/sonic" --ignore-existing -azvr --progress /mnt/sonic/ebooks/ howard@192.168.1.103:/mnt/knuckles/ebooks/
#rsync -e "ssh -i /home/howard/.ssh/sonic" --ignore-existing -azvr --progress /mnt/sonic/games/ howard@192.168.1.103:/mnt/knuckles/games/
rsync -e "ssh -i /home/howard/.ssh/sonic" --ignore-existing -azvr --progress /mnt/sonic/linux/ howard@192.168.1.103:/mnt/knuckles/linux/
rsync -e "ssh -i /home/howard/.ssh/sonic" --ignore-existing -azvr --progress /mnt/sonic/live_shows/ howard@192.168.1.103:/mnt/knuckles/live_shows/
rsync -e "ssh -i /home/howard/.ssh/sonic" --ignore-existing -azvr --progress /mnt/sonic/movies/ howard@192.168.1.103:/mnt/knuckles/movies/
rsync -e "ssh -i /home/howard/.ssh/sonic" --ignore-existing -azvr --progress /mnt/sonic/music/ howard@192.168.1.103:/mnt/knuckles/music/
rsync -e "ssh -i /home/howard/.ssh/sonic" --ignore-existing -azvr --progress /mnt/sonic/photos/ howard@192.168.1.103:/mnt/knuckles/photos/
rsync -e "ssh -i /home/howard/.ssh/sonic" --ignore-existing -azvr --progress /mnt/sonic/shows/ howard@192.168.1.103:/mnt/knuckles/shows/

# Make the script executable:
chmod +x ~/scripts/sonic-send.sh

# Create the systemd timer file
vim /etc/systemd/system/sonic-send.timer

[Unit]
Description=rsync directories from sonic to tails every month

[Timer]
OnCalendar=monthly
Persistent=true
Unit=sonic-send.service

[Install]
WantedBy=timers.target

# Enable and start the timer
sudo systemctl enable --now sonic-send.timer

# If you want to start the service straight away, use
sudo systemctl start sonic-send

# Track the journal with
journalctl -fu sonic-send
```