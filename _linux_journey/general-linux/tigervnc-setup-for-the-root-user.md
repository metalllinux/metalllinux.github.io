---
title: "TigetVNC Setup"
category: "general-linux"
tags: ["tigervnc", "setup", "root", "user"]
---

### TigetVNC Setup
* I set up the FreeUPA Client to have a graphical environment (GNOME in this case):
```
sudo dnf group install -y "Server with GUI"
```
* I set the default target into `graphical` mode:
```
systemctl set-default graphical
```
* I installed the `tigervnc` package:
```
sudo dnf install -y tigervnc-server
```
* For the `service`, I set the display number as `3`:
```
sudo cp /usr/lib/systemd/system/vncserver@.service /etc/systemd/system/vncserver@:3.service
```
* Under `vncserver.users` I added my two FreeIPA Server users and assigned each of them to display `3`:
```
cat << "EOF" | sudo tee -a /etc/tigervnc/vncserver.users
:3=root
EOF
```
* I set the `vncpasswd`:
```
vncpasswd
```
* Selected `n` at the prompt for `view-only` password.
* Taking user `test-no-1` as an example, I ran the following configuration:
* I set the `gnome-session` to be the current session:
```
echo gnome-session > /root/.session
```
* I generated the `vnc` directory:
```
mkdir /root/.vnc
```
* I created the `vnc` configuration file:
```
cat << "EOF" | tee -a /root/.vnc/config
session=gnome
securitytypes=vncauth,tlsvnc
geometry=1920x1080
EOF
```
* Then as `root` I started the `vncserver`:
```
sudo systemctl enable --now vncserver@:3.service
```
* I added the appropriate firewall rules:
```
sudo firewall-cmd --permanent --add-service=vnc-server
sudo firewall-cmd --permanent --add-port=5902/tcp
sudo firewall-cmd --reload
```