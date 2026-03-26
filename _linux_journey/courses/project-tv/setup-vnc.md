---
title: "Setup Vnc"
category: "project-tv"
tags: ["project-tv", "setup", "vnc"]
---

```
sudo dnf install -y tigervnc-server
```
```
sudo cp /usr/lib/systemd/system/vncserver@.service /etc/systemd/system/vncserver@:3.service
```
```
sudo tee -a /etc/tigervnc/vncserver.users <<EOF
:3=myuser
EOF
```
```
vncpasswd
```
* Select `n` to `Would you like to enter a view-only password?`
```
mkdir ~/.vnc
```
```
tee -a ~/.vnc/config <<EOF
session=kde
securitytypes=vncauth,tlsvnc
geometry=3840x2160
EOF
```
```
tee -a ~/.vnc/config <<EOF
session=gnome
securitytypes=vncauth,tlsvnc
geometry=1920x1080
EOF
```
```
sudo systemctl enable --now vncserver@:3.service
```
```
sudo firewall-cmd --permanent --add-service=vnc-server
sudo firewall-cmd --permanent --add-port=5902/tcp
```
```
sudo firewall-cmd --reload
```