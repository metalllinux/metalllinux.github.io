---
title: "Enable Autologin For Sddm"
category: "project-tv-v2"
tags: ["project-tv-v2", "enable", "autologin", "sddm"]
---

* Create the config file:
```
cat << "EOF" | sudo tee /etc/sddm.conf
[General]
InputMethod=

[Autologin]
User=howard
Session=plasma.desktop
EOF
```