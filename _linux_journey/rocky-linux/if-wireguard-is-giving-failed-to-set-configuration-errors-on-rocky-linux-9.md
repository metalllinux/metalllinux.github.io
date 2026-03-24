---
title: "If Wireguard is Giving 'Failed to set DNS configuration' errors on Rocky Linux 9"
category: "rocky-linux"
tags: ["rocky-linux", "wireguard", "giving", "failed", "configuration"]
---

# If Wireguard is Giving "Failed to set DNS configuration" errors on Rocky Linux 9

Run this command:

```
sudo systemctl enable --now systemd-resolved
```

