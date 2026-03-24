---
title: "Access Syncthing Web Ui Other Machine"
category: "general-linux"
tags: ["access", "syncthing", "web", "other", "machine"]
---

The default listening address is 127.0.0.1:8384, so you can only access the GUI from the same machine. This is for security reasons. To access the web GUI from another computer, change the GUI listen address through the web UI from 127.0.0.1:8384 to 0.0.0.0:8384 or change the config.xml:

<gui enabled="true" tls="false">
  <address>127.0.0.1:8384</address>
to

<gui enabled="true" tls="false">
  <address>0.0.0.0:8384</address>

The config file is located at:
~/.config/syncthing/config.xml