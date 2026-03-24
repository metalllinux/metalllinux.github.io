---
title: "Change to root user"
category: "general-linux"
tags: ["great", "nixos", "installation", "guide"]
---

NixOS Installation Cheat Sheet
https://www.ml4w.com
https://gitlab.com/stephan-raabe/dotfiles/nixos
Preparation
# Change to root user
sudo -i
# Load keyboard layout (if needed)
loadkeys de-latin1
# Check internet connection
ping www.archlinux.org
# Show available hard discs
lsblk
# Start with the partitions
parted /dev/vda -- mklabel gpt
parted /dev/vda -- mkpart primary 512MB -8GB
parted /dev/vda -- mkpart primary linux-swap -8GB 100%
parted /dev/vda -- mkpart ESP fat32 1MB 512MB
parted /dev/vda -- set 3 esp on
# Format the partitions
mkfs.ext4 -L nixos /dev/vda1
mkswap -L swap /dev/vda2
swapon /dev/vda2
mkfs.fat -F 32 -n boot /dev/vda3 # (for UEFI systems only)
mount /dev/disk/by-label/nixos /mnt
mkdir -p /mnt/boot # (for UEFI systems only)
mount /dev/disk/by-label/boot /mnt/boot # (for UEFI systems only)
Base Installation
# Generate nixos configuration into the new system
nixos-generate-config --root /mnt
# Open and edit the configuration file
nano /mnt/etc/nixos/configuration.nix
# Add vim if needed
# Save with CTRL-o
# Exit with CTRL-x
# Start the installation
nixos-install
# Reboot the system
reboot
# Login as root user (username root + password from the installation)
# Load keyboard layout (if needed)
loadkeys de-latin1
# Add system user
useradd -c 'Firstname Lastname' -m yourusername
passwd yourusername
# Open configuration file
vim /etc/nixos/configuration.nix
# Setup your user
users.users.yourusername = {
isNormalUser= true;
home = "/home/yourusername";
description = "Firstname Lastname";
extraGroups= [ "wheel" ];
};
# Save the file and reboot
reboot
# Login with your user
Install Qtile
# Open the configuration file
sudo vim /etc/nixos/configuration.nix
# Add additional packages for Qtile
environment.systemPackages = with pkgs; [
vim
wget
qtile
alacritty
chromium
git
picom
rofi
nitrogen
xfce.mousepad
];
programs.thunar.enable = true;
# Enable xserver and load qtile
# Configure keymap in X11
services.xserver.layout = "de";
services.xserver.enable = true;
services.xserver.windowManager.qtile.enable = true;
# Rebuild the configuration
nixos-rebuild switch
# shutdown
sudo shutdown –h now
# Enable 3D in your Virtual Machine
# Restart the VM
# Login to qtile with lightdm display manager