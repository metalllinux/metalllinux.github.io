---
title: "Start virt-manager After 2 Minutes Script"
category: "project-tv-v2"
tags: ["project-tv-v2", "start", "virt", "manager", "after"]
---

# Start virt-manager After 2 Minutes Script

```
cat << "EOF" | tee /home/myuser/scripts/virt-manager_start.sh
#!/bin/bash

sleep 30

virt-manager
EOF
```
* Make it executable:
```
chmod +x /home/myuser/scripts/virt-manager_start.sh
```

