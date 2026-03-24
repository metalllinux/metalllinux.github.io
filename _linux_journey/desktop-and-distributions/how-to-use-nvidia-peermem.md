---
title: "How to Use nvidia-peermem"
category: "desktop-and-distributions"
tags: ["desktop-and-distributions", "nvidia", "peermem"]
---

# How to Use nvidia-peermem

Hi, guys! All good?

I’m facing this issue for a long time, so let’s go! I’m developing a linux device driver using GPUDirect RDMA in Cuda 12.2. Following the [documentation](https://docs.nvidia.com/cuda/gpudirect-rdma/), the nv-peer-mem was deprecated due to a race condition, and the new driver is the nvidia-peermem.

I accepted to use the nv-peer-mem, but I think that I achieved the bug… I’m having a inconstant behaviour that stucks my kernel some times in nvidia\_p2p\_put\_pages (nv-peer-mem).

So, please, How can I use the nvidia-peermem?

-   Environment: Jetpack 36.3 - Tegra 5.15.136 - Cuda 12.2

Hi,

Please find below for the changes in CUDA 12.2:

If the document doesn’t help, could you share more info about your issue? like code snippet or log?

Thanks.

Hi!

The section “changes in Cuda 11.4” reports that the module should be loaded manually. Do I still need to manually load for Cuda 12.2?

All the documentation I accessed, there is the note:  
“If the NVIDIA GPU driver is installed before MOFED, the GPU driver must be uninstalled and installed again to make sure **nvidia-peermem** is compiled with the RDMA APIs that are provided by MOFED.”

If I try to only modprobe the nvidia-peermem, a fatal error is returned: Module nvidia-peermem not found… It isn’t clear if I need to install anything or the module is native.

If necessary to uninstall and install the GPU drivers, should it be done using sdkmanager?

Is there a example of using nvidia-peermem? Is there any **documentation** about the module? I can’t access any information about it, I don’t even know the parameters of the methods.

Hi

There are some config required in the r36 branch:

Could you try if our _jetson-rdma-picoevb_ sample (`rel-36+`) can work successfully or not first?

Thanks.

Hi! Thanks a lot [@AastaLLL](https://forums.developer.nvidia.com/u/aastalll).  
Yes, the config required in r36 is to be used with the deprecated module nv\_peer\_mem. I’m trying to use the new module **nvidia-peermem**. The nv-peer-mem was running, but I’m suspecting that the module is resulting in a wrong and inconstant behaviour.

Hi,

Do you test it with your custom app?  
If so, does our sample work on your side?

Thanks.

Actually, I can’t test anything. Theoretically, I would insert the module and change the API to persistent API. However, I can’t insert the nvidia-peermem, because it isn’t installed. And I can’t install because the guide is not very clear. How to install in the Jetson…

Hi,

Could you share the command you use and the corresponding error?

The command for JetPack 6 can be found in the link below:

Thanks.

This topic was automatically closed 14 days after the last reply. New replies are no longer allowed.

