---
title: "How Setup And Install A Vnc Server With Kde On Roc"
category: "desktop-and-distributions"
tags: ["desktop-and-distributions", "setup", "install", "vnc", "server"]
---

```
sudo dnf install -y tigervnc-server
```
```
sudo cp /usr/lib/systemd/system/vncserver@.service /etc/systemd/system/vncserver@:3.service
```
```
sudo tee -a /etc/tigervnc/vncserver.users <<EOF
:3=howard
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
sudo systemctl enable --now vncserver@:3.service
```
```
sudo firewall-cmd --permanent --add-service=vnc-server
sudo firewall-cmd --permanent --add-port=5902/tcp
```
```
sudo firewall-cmd --reload
```