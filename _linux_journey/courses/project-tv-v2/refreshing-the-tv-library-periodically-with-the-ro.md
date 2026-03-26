---
title: "Refreshing The Tv Library Periodically With The Ro"
category: "project-tv-v2"
tags: ["project-tv-v2", "refreshing", "library", "periodically"]
---

* Set up the VM with IP address information and hostname.
* Run the `ssh` server:
```
sudo systemctl enable --now sshd
```
* Open up the appropriate `firewalld` service:
```
sudo firewall-cmd --permanent --add-service=ssh
sudo firewall-cmd --reload
```
* Add the FlatHub repository:
```
flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
```
* Reboot:
```
reboot
```
* Install the JellyFin Media Player from Flathub:
```
flatpak install flathub com.github.iwalton3.jellyfin-media-player
```
* Install the EPEL repo:
```
sudo dnf install -y epel-release
```
* Install the `xdotool` package:
```
sudo dnf install -y xdotool
```
* Log out and then select the `Standard Xorg` option and then log back in again.
* Create the scripts directory:
```
mkdir ~/scripts
```
* Create this file:
```
cat << "EOF" | tee ~/scripts/refresh_library.sh
#!/bin/bash
export DISPLAY=:0
sleep 1
xdotool mousemove 1248 81 click 1
sleep 1
xdotool mousemove 317 777 click 1
sleep 1
xdotool mousemove 96 334 click 1
sleep 1
xdotool mousemove 96 380 click 1
sleep 1
xdotool mousemove 710 358 click 1
sleep 1
xdotool mousemove 722 392 click 1
sleep 1
xdotool mousemove 634 750 click 1
sleep 1
xdotool mousemove 92 89 click 1
EOF
```
* Make the script executable:
```
chmod +x ~/scripts/refresh_library.sh
```
* Open up a cron tab:
```
crontab -e
```
* Add the following:
```
0 * * * * /home/myuser/refresh_library.sh
```
* Add the GNOME Extensions extension into Firefox and install Dash to Dock - disable the overlay when GNOME first boots.