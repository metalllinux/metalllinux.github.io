---
title: "If Observe Ld Preload Issue On Rocky Linux 10 With Steam Installed Solution"
category: "rocky-linux"
tags: ["rocky-linux", "observe", "preload", "issue", "rocky"]
---

sudo mkdir -p /usr/lib/x86_64-linux-gnu
sudo ln -sf /usr/lib64/libwayland-client.so.0 /usr/lib/x86_64-linux-gnu/libwayland-client.so.0
