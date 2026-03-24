---
title: "Ports to Allow Localsend Traffic on in Rocky Linux"
category: "rocky-linux"
tags: ["rocky-linux", "ports", "allow", "localsend", "traffic"]
---

# Ports to Allow Localsend Traffic on in Rocky Linux

```
sudo firewall-cmd --permanent --add-port=53317/tcp
sudo firewall-cmd --permanent --add-port=53317/udp
sudo firewall-cmd --reload
```

