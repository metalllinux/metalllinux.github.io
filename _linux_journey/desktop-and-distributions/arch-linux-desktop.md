---
title: "Connect with iwctl"
category: "desktop-and-distributions"
tags: ["desktop-and-distributions", "arch", "linux", "desktop"]
---

```
# Connect with iwctl
iwctl
station wlan0 scan
station wlan0 connect <SSID>

# Once the base install is complete, using nmtui to connect to a WiFi connection if needed.

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

pacman -S grub grub-btrfs efibootmgr networkmanager network-manager-applet dialog wpa_supplicant mtools dosfstools base-devel linux-headers avahi xdg-user-dirs xdg-utils gvfs gvfs-smb nfs-utils inetutils dnsutils bluez bluez-utils cups alsa-utils pipewire pipewire-alsa pipewire-pulse pipewire-jack bash-completion openssh rsync reflector acpi acpi_call tlp virt-manager qemu edk2-ovmf bridge-utils dnsmasq vde2 openbsd-netcat iptables-nft ipset firewalld nss-mdns acpid os-prober ntfs-3g snapper sof-firmware wget unzip pipewire-audio man bluez-utils playerctl

# Additional software
sudo pacman -S firefox bitwarden  libreoffice wireplumber gimp xournalpp fish wl-clipboard signal-desktop transmission-cli vivaldi gpodder cmus mpv audacious

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
useradd -m myuser

echo myuser:password | chpasswd

usermod -aG libvirt myuser

# To be able to access the cups interface at localhost:631
usermod -aG sys myuser

echo "myuser ALL=(ALL) ALL" >> /etc/sudoers.d/myuser

# Edit the mkinitcpio file.
vim /etc/mkinitcpio.conf

# Add the following into the MODULES section. i915 is for Intel, amdgpu is for AMD.
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

# Set up snapper
sudo umount /.snapshots
sudo rm -r /.snapshots
sudo snapper -c shadow create-config / 
sudo btrfs subvolume delete /.snapshots
sudo mkdir /.snapshots
sudo mount -a
sudo chmod 750 /.snapshots
sudo vim /etc/snapper/configs/shadow
# Change ALLOW_USERS to ALLOW_USERS="myuser"
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
yay -S snap-pac-grub snapper-gui
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

# Change permissions of Snapper
sudo chmod a+rx /.snapshots
# The user is always root.
sudo chown :<your_group> /.snapshots
# For now, these are read-only - check the Arch Wiki on how to make these write enabled.

# AMD Card Setup
# Enable the multilib repo under /etc/pacman.conf
[multilib]
Include = /etc/pacman.d/mirrorlist

sudo pacman -S mesa
sudo pacman -S lib32-mesa
sudo pacman -S vulkan-radeon
sudo pacman -S xf86-video-amdgpu
sudo pacman -S lib32-vulkan-radeon
sudo pacman -S libva-mesa-driver
sudo pacman -S lib32-libva-mesa-driver

# Add this to mkinitcpio.conf into the MODULES section.
MODULES=(amdgpu radeon)

# Regenerate the initramfs with:
mkinitcpio -p linux

# Add the following kernel command line parameters to /etc/default/grub
# These go after "quiet splash"
radeon.cik_support=0 radeon.si_support=0 amdgpu.cik_support=1 amdgpu.si_support=1 amdgpu.dc=1

# Then regenerate the grub config with:
sudo grub2-mkconfig -o /boot/grub

# How Set QT Applications to Dark Mode
sudo pacman -S qt5ct
# Add the environment variable to /etc/environment
QT_QPA_PLATFORMTHEME=qt5ct
# Launch qt5ct
# Select "Fusion"
# Select "darker"
# Re-login and launch an example QT app (Libreoffice is good)

# Install Joplin
yay -S joplin-desktop

# Install handbrake
yay -S handbrake-full

# Install Skype
yay -S skypeforlinux-bin

# Install this to enable media playback controls for Bluetooth Headphones
yay -S mpris-proxy-service

# Install the playerctl systemd unit:
yay -S playerctld-systemd-unit

####
Beware of firewalld, if it is active, it will block all cups and scanner ports unless those ports are allowed.
####

# Epson EW-052A Printer Install
yay -S epson-inkjet-printer-escpr
sudo firewall-cmd --permanent --add-port=631/tcp
sudo firewall-cmd --permanent --add-port=5353/udp
sudo firewall-cmd --permanent --add-port=9100-9102/tcp
sudo firewall-cmd --reload

# Epson EW-052A Scanner Install
sudo pacman -S sane-airscan
sudo pacman -S imagescan
# Create this file:
/etc/utsushi/utsushi.conf
# Add the following:
[devices]
myscanner.udi    = esci:networkscan://<IP_HERE>:1865
myscanner.vendor = Epson
myscanner.model  = EW-052A
# To find the IP, install arp-scan
sudo pacman -S arp-scan
# Scan with the following:
sudo arp-scan --interface=wlp60s0 --localnet
# To find your scanner, run scanimage -L
# To scan a document, use the following syntax:
scanimage --device-name "airscan:w1:EPSON EW-052A Series" --format png --resolution 300 > output.png

# Install KDE
sudo pacman -S --noconfirm xorg sddm plasma kde-applications vlc papirus-icon-theme
sudo systemctl enable sddm
reboot

# Install deepin
sudo pacman -S deepin deepin-kwin lightdm
sudo pacman -S deepin-album deepin-boot-maker deepin-calculator deepin-camera deepin-clipboard deepin-clone deepin-community-wallpapers deepin-compressor deepin-device-formatter deepin-draw deepin-editor deepin-font-manager deepin-grand-search deepin-movie deepin-music deepin-picker deepin-printer  	deepin-screen-recorder deepin-screensaver-pp deepin-terminal deepin-voice-note
systemctl enable lightdm

# Install sway
sudo pacman -S sway swaybg swaylock swayidle terminator dmenu xorg-xwayland gammastep swaybg brigtnessctl grim slurp ranger pavucontrol waybar otf-font-awesome

# Install ly
yay -S ly-git
sudo systemctl enable ly.service

# Set up sway config.
mkdir .config/sway
cp /etc/sway/config .config/sway

reboot

# Set dark mode for GTK applications

Create
~/.config/gtk-3.0/settings.ini

Add the following.

[Settings]
gtk-application-prefer-dark-theme=1

Restart the application for the changes to take effect.

# Create the Alacritty configuration file
~/.config/alacritty/alacritty.toml

# How To Automatically Re-direct Audio in Arch to Bluetooth Headphones with pipewire

# Create

~/.config/pipewire/pipewire-pulse.conf.d/switch-on-connect.conf

# Add the following

# override for pipewire-pulse.conf file
pulse.cmd = [
    { cmd = "load-module" args = "module-always-sink" flags = [ ] }
    { cmd = "load-module" args = "module-switch-on-connect" }
]

* Restart `pulseaudio` or reboot.

# Set up Japanese Support.
sudo pacman -S fcitx5-im
# Install all options

sudo pacman -S fcitx-configtool

# Add the following to /etc/profile
GTK_IM_MODULE=fcitx
QT_IM_MODULE=fcitx

# Install UT Dictionary
yay -S fcitx5-mozc-ut
# Select option 2

# If there are package conflicts, don't install fcitx5-mozc-ut and run sudo pacman -S fcitx-mozc

# Don't run the fcitx-configtool from the commandline, open it after running fcitx in the top right-hand corner.

# Install Japanese Fonts
sudo pacman -S otf-ipafont

# Install Image viewer
yay -S nomacs

# Install starcraft theme

wget -qO- https://raw.githubusercontent.com/Rokin05/starcraft-kde/master/install.sh | sh

# Install and setup fonts.
sudo pacman -S cantarell-fonts

kwriteconfig5 --file kdeglobals --group General --key fixed "Monospace,9,-1,5,50,0,0,0,0,0"

kwriteconfig5 --file kdeglobals --group General --key font "Cantarell,9,-1,5,50,0,0,0,0,0,Regular"

kwriteconfig5 --file kdeglobals --group General --key menuFont "Cantarell,10,-1,5,25,0,0,0,0,0,Light"

kwriteconfig5 --file kdeglobals --group General --key smallestReadableFont "Cantarell,8,-1,5,50,0,0,0,0,0,Regular"

kwriteconfig5 --file kdeglobals --group General --key toolBarFont "Cantarell,9,-1,5,25,0,0,0,0,0,Light"

kwriteconfig5 --file kdeglobals --group WM --key activeFont "Cantarell,9,-1,5,50,0,0,0,0,0,Regular"

qdbus org.kde.KWin /KWin reconfigure

kquitapp5 plasmashell && kstart5
plasmashell

# Kvantum
# Edit /etc/profile
sudo vim /etc/profile

# Add the following line.
QT_STYLE_OVERRIDE=kvantum

# Install Browser Extension in Ungoggled Chromium

# Install browser extensions manually.
# Enable Developer Mode in the Extensions Tab.

# Follow the instructions here to install manually ublock origin: https://github.com/gorhill/uBlock/tree/master/dist#install 


```