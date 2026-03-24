---
title: "How Completely Remove Systemd Services"
category: "automation-and-configuration"
tags: ["automation-and-configuration", "completely", "remove", "systemd", "services"]
---

systemctl stop [servicename]
systemctl disable [servicename]
rm /etc/systemd/system/[servicename]
rm /etc/systemd/system/[servicename] # and symlinks that might be related
rm /usr/lib/systemd/system/[servicename] 
rm /usr/lib/systemd/system/[servicename] # and symlinks that might be related
systemctl daemon-reload
systemctl reset-failed