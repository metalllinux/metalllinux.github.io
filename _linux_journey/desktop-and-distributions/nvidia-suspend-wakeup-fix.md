---
title: "NVIDIA Suspend and Wakeup Fix"
category: "desktop-and-distributions"
tags: ["desktop-and-distributions", "nvidia", "suspend", "wakeup", "fix"]
---

# NVIDIA Suspend and Wakeup Fix

Add these options to `/etc/modprobe.d/nvidia.conf`:

```
options nvidia_drm modeset=1
options nvidia NVreg_PreserveVideoMemoryAllocations=1 
options nvidia NVreg_RegistryDwords="RMUseSwI2c=0x01;RMI2cSpeed=100;RMDisableDP12=1"
```

Rebuild the `initramfs`:

```
dracut -f
```

Reboot:

```
reboot
```
