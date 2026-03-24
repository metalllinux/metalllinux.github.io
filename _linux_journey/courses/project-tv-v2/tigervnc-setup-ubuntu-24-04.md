---
title: "Tigervnc Setup Ubuntu 24.04"
category: "project-tv-v2"
tags: ["project-tv-v2", "tigervnc", "setup", "ubuntu"]
---

* Installed required packages:
```
sudo apt install -y tigervnc-standalone-server 
```
* Set the `vnc` password:
```
vncpasswd 
```
* Select `n` at the prompt for a view-only password.
* Start the TigerVNC service:
```
tigervncserver -xstartup /etc/X11/Xsession -SecurityTypes VncAuth,TLSVnc -geometry 3840x2160 -localhost no :1 
```
* Stop the VNC session:
```
tigervncserver -kill :1
```
* Make sure you are notigervncserver -kill :1
t logged into a Plasma session on the host.