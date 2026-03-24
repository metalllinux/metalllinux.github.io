---
title: "How To Setup A Node With Ciq Depot"
category: "general-linux"
tags: ["setup", "node", "ciq", "depot"]
---

```
Disable Mountain LTS Repo

mtn dnf disable lts-8.6

Enable Depot and Update

sudo yum install -y https://depot.ciq.com/public/files/depot-client/depot/depot.x86_64.rpm
sudo depot register -u [USER STRING] -t [USER TOKEN]
sudo depot dnf
sudo dnf update

Next, reboot the server. Optionally, you can disable the base repo's that point to the default Rocky Linux mirrorlist after you have rebooted

sudo dnf config-manager --set-disabled baseos appstream extras
 
Final DistroSync

sudo dnf distrosync --refresh --allowerasing
 
This final step will update the kernel. 
 
You should now be on Rocky Linux 8.10 LTS. Please let me know if you have any questions or if you have any questions or concerns! If you run into any problems please do not hesitate to reach out. Thank you! 
```