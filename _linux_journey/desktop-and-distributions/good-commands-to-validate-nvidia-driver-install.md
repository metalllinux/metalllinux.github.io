---
title: "Good Commands to Validate NVIDIA Driver Installation"
category: "desktop-and-distributions"
tags: ["desktop-and-distributions", "good", "commands", "validate", "nvidia"]
---

# Good Commands to Validate NVIDIA Driver Installation

5. Some easy commands to validate nvidia:
rpm -qf /bin/nvidia-cuda-mps-control /bin/nvidia-persistenced /bin/nvidia-smi /bin/nvidia-ngx-updater

modinfo nvidia | grep -E '^version|^*name|^sig'

The first will ensure some of the key nvidia CUDA packages and programs are installed - if the rpm command returns an error on any of those files, something is missing.

The second checks the nvidia kernel module (driver) stats, and filters by version (570.133.20), name, and secureboot signature info (should read as Ctrl IQ, Inc.)
You don't actually need to run nvidia hardware to do the modinfo .  You will need to be running a system with the proper FIPS kernel though - cannot be done in a builder chroot.

