---
title: "Use Proton = 7 If Have Nvidia 470 Drivers"
category: "desktop-and-distributions"
tags: ["desktop-and-distributions", "proton", "nvidia", "drivers"]
---

Reasoning:

The wine and dxvk versions you mention aren't the ones you use in the log which is proton experimental and dxvk master (well close to).

Anyway master dxvk requires vulkan 1.3 now which needs at least the 510 driver for Nvidia. Which means it's not the 515 driver that is used.