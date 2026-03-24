---
title: "!/bin/bash"
category: "project-tv-v2"
tags: ["project-tv-v2", "refresh", "firefox", "when", "home"]
---

* Create the following BASH script:
```
cat << "EOF" | tee /home/howard/scripts/firefox-refresh.sh
#!/bin/bash
wmctrl -a Firefox
xdotool key F5
EOF
```
* Make the script executable:
```
chmod +x /home/howard/scripts/firefox-refresh.sh
```
* Install these packages:
```
sudo apt install -y wmctrl
sudo apt install -y xdotool
```
* Under `Custom Shortcuts` in KDE, go to `New` --> `Global Shortcut` --> `Command/URL` and set this action:
```
/home/howard/scripts/firefox-refresh.sh
```