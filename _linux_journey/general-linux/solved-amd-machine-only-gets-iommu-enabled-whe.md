---
title: "[Solved] Amd Machine Only Gets Iommu Enabled Whe"
category: "general-linux"
tags: ["solved", "amd", "machine", "only", "gets"]
---

[![Proxmox Support Forum](../_resources/Proxmox-logo-500px_0137ee700889439c97d669eca038f79.png)](https://forum.proxmox.com)

[](https://forum.proxmox.com/search/ "Search")

- [Home](https://forum.proxmox.com)
    
- [Forums](https://forum.proxmox.com/)
    
- [What's new](https://forum.proxmox.com/whats-new/)
    
- [Members](https://forum.proxmox.com/members/)
    

[Log in](https://forum.proxmox.com/login/) [Register](https://forum.proxmox.com/register/)

- [New posts](https://forum.proxmox.com/whats-new/posts/)
    
- [Search forums](https://forum.proxmox.com/search/?type=post)
    

# \[SOLVED\] 

AMD machine only gets IOMMU enabled when setting intel_iommu=on... false positive?

- *Thread starter
    
    * Thread starter <a id="js-XFUniqueId5"></a>[rhobinn](https://forum.proxmox.com/members/rhobinn.163540/)
- *Start date
    
    * Start date [Sep 29, 2022](https://forum.proxmox.com/threads/amd-machine-only-gets-iommu-enabled-when-setting-intel_iommu-on-false-positive.115920/)

- [](https://forum.proxmox.com)
- [Forums](https://forum.proxmox.com/)
- [Proxmox Virtual Environment](https://forum.proxmox.com/#proxmox-virtual-environment.11)
- [Proxmox VE: Installation and configuration](https://forum.proxmox.com/forums/proxmox-ve-installation-and-configuration.16/)
https://forum.proxmox.com/threads/amd-machine-only-gets-iommu-enabled-when-setting-intel_iommu-on-false-positive.115920/
I have set up GPU passthrough with a few computers (all intel) but I have one that eludes me, and I don't have a clue what's happening:  
I'm trying to get IOMMU enabled and keep failing  
<br/>First, this is my hardware:  
<br/>AMD ryzen 3900x  
Gigabyte 570x gaming X  
GeForce RTX 3080Ti GAMING X TRIO  
<br/>I'm using Proxomox 7.2-3  
Linux 5.15.30-2-pve #1 SMP PVE 5.15.30-3 (Fri, 22 Apr 2022 18:08:27 +0200)  
<br/><br/>My bios is updated to the last version (F37d), and have this settings (have tried them enabling and disabling each one of them one by one):  
IOMMU: Enabled  
CSM: Disabled  
Above 4G decoding: Enabled  
Resizable BAR: Disabled  
ACS: Enabled  
<br/>I have another GPU (cuadro p620) but that's only for monitor output... and the bios is set to output on this one  
the 3080 card seems to be on its own IOMMU Group (25)  
<br/>lspci -nnv | grep VGA  
`04:00.0 VGA compatible controller [0300]: NVIDIA Corporation GP107GL [Quadro P620] [10de:1cb6] (rev a1) (prog-if 00 [VGA controller]) 0a:00.0 VGA compatible controller [0300]: NVIDIA Corporation Device [10de:2208] (rev a1) (prog-if 00 [VGA controller])`  
<br/>lspci -s 0a:00 -n  
`0a:00.0 0300: 10de:2208 (rev a1) 0a:00.1 0403: 10de:1aef (rev a1)`  
<br/>find /sys/kernel/iommu_groups/ -type l  
`/sys/kernel/iommu_groups/0/devices/0000:00:01.0 /sys/kernel/iommu_groups/1/devices/0000:00:01.2 /sys/kernel/iommu_groups/2/devices/0000:00:02.0 /sys/kernel/iommu_groups/3/devices/0000:00:03.0 /sys/kernel/iommu_groups/4/devices/0000:00:03.1 /sys/kernel/iommu_groups/5/devices/0000:00:04.0 /sys/kernel/iommu_groups/6/devices/0000:00:05.0 /sys/kernel/iommu_groups/7/devices/0000:00:07.0 /sys/kernel/iommu_groups/8/devices/0000:00:07.1 /sys/kernel/iommu_groups/9/devices/0000:00:08.0 /sys/kernel/iommu_groups/10/devices/0000:00:08.1 /sys/kernel/iommu_groups/11/devices/0000:00:14.3 /sys/kernel/iommu_groups/11/devices/0000:00:14.0 /sys/kernel/iommu_groups/12/devices/0000:00:18.3 /sys/kernel/iommu_groups/12/devices/0000:00:18.1 /sys/kernel/iommu_groups/12/devices/0000:00:18.6 /sys/kernel/iommu_groups/12/devices/0000:00:18.4 /sys/kernel/iommu_groups/12/devices/0000:00:18.2 /sys/kernel/iommu_groups/12/devices/0000:00:18.0 /sys/kernel/iommu_groups/12/devices/0000:00:18.7 /sys/kernel/iommu_groups/12/devices/0000:00:18.5 /sys/kernel/iommu_groups/13/devices/0000:01:00.0 /sys/kernel/iommu_groups/14/devices/0000:02:01.0 /sys/kernel/iommu_groups/15/devices/0000:02:02.0 /sys/kernel/iommu_groups/16/devices/0000:02:03.0 /sys/kernel/iommu_groups/17/devices/0000:02:04.0 /sys/kernel/iommu_groups/18/devices/0000:07:00.0 /sys/kernel/iommu_groups/18/devices/0000:02:08.0 /sys/kernel/iommu_groups/18/devices/0000:07:00.3 /sys/kernel/iommu_groups/18/devices/0000:07:00.1 /sys/kernel/iommu_groups/19/devices/0000:08:00.0 /sys/kernel/iommu_groups/19/devices/0000:02:09.0 /sys/kernel/iommu_groups/20/devices/0000:09:00.0 /sys/kernel/iommu_groups/20/devices/0000:02:0a.0 /sys/kernel/iommu_groups/21/devices/0000:03:00.0 /sys/kernel/iommu_groups/22/devices/0000:04:00.1 /sys/kernel/iommu_groups/22/devices/0000:04:00.0 /sys/kernel/iommu_groups/23/devices/0000:05:00.0 /sys/kernel/iommu_groups/24/devices/0000:06:00.0 /sys/kernel/iommu_groups/25/devices/0000:0a:00.0 /sys/kernel/iommu_groups/25/devices/0000:0a:00.1 /sys/kernel/iommu_groups/26/devices/0000:0b:00.0 /sys/kernel/iommu_groups/27/devices/0000:0c:00.0 /sys/kernel/iommu_groups/28/devices/0000:0c:00.1 /sys/kernel/iommu_groups/29/devices/0000:0c:00.3 /sys/kernel/iommu_groups/30/devices/0000:0c:00.4`  
<br/>My sistem supports remapping  
<br/>dmesg | grep 'remapping'  
`[ 0.370033] x2apic: IRQ remapping doesn't support X2APIC mode [ 0.635832] AMD-Vi: Interrupt remapping enabled`  
<br/>I added to /etc/modules the modules suggested  
`vfio vfio_iommu_type1 vfio_pci vfio_virqfd`  
<br/>I have tried different things in the fail /etc/default/grub  
but if I put  
<br/>GRUB_CMDLINE_LINUX_DEFAULT="amd_iommu=on"  
<br/>I get this from dmesg | grep -e DMAR -e IOMMU  
`[ 0.629125] pci 0000:00:00.2: AMD-Vi: IOMMU performance counters supported [ 0.634719] pci 0000:00:00.2: AMD-Vi: Found IOMMU cap 0x40 [ 0.635124] perf/amd_iommu: Detected AMD IOMMU #0 (2 banks, 4 counters/bank).`  
<br/>I have tried different options:  
\-quiet  
\-vfio-pci.ids=10de:1e81,10de:10f8,10de:1ad8,10de:1ad9  
\-modprobe.blacklist=radeon,nouveau,nvidia,nvidiafb,nvidia-gpu"  
\-  
and every time I get exactly the same message  
<br/>only when I add:  
\-pcie_acs_override=downstream,multifunction  
it adds the line to the dmesg results:  
`[ 0.000000] Warning: PCIe ACS overrides enabled; This may allow non-IOMMU protected peer-to-peer DMA`  
<br/>but I cannot seem to be able to enable IOMMU  
<br/>but...  
by mistake I used  
intel_iommu=on  
<br/>and then I get  
<br/>dmesg | grep -e DMAR -e IOMMU  
<br/>`[ 0.084082] DMAR: IOMMU enabled [ 0.627289] pci 0000:00:00.2: AMD-Vi: IOMMU performance counters supported [ 0.632809] pci 0000:00:00.2: AMD-Vi: Found IOMMU cap 0x40 [ 0.633146] perf/amd_iommu: Detected AMD IOMMU #0 (2 banks, 4 counters/bank).`  
<br/>and I don't know if that is actually correct...  
why does this happen? it is not an intel processor... why does IOMMU turns on when I set intel_iommu=on??  
is it a false positive?  
or that's correct and I should use intel_iommu=on?  
<br/>what should I do?  
<br/>to test the GPU on the VM...  
im gonna be running a simulation software GROMACS, and installing it and compiling it is long... so I haven't gotten to it  
I will try it later to see if with the intel ON setting works...  
<br/>but meanwhile, what do you think is happening? why IOMMU only "works" when I set it to intel instead of AMD?? what should I do?

<a id="js-XFUniqueId13"></a>[![leesteken](../_resources/93939_d61f027c4a814269bc287a8208a3a523.jpg)](https://forum.proxmox.com/members/leesteken.93939/)

#### <a id="js-XFUniqueId14"></a>[leesteken](https://forum.proxmox.com/members/leesteken.93939/)

##### Distinguished Member

**[Proxmox Subscriber](https://www.proxmox.com/en/proxmox-ve/pricing)**

May 31, 2020

6,726

1,901

228

- [Sep 29, 2022](https://forum.proxmox.com/threads/amd-machine-only-gets-iommu-enabled-when-setting-intel_iommu-on-false-positive.115920/post-501335)

- <a id="js-XFUniqueId36"></a>[](https://forum.proxmox.com/threads/amd-machine-only-gets-iommu-enabled-when-setting-intel_iommu-on-false-positive.115920/post-501335)
- [#2](https://forum.proxmox.com/threads/amd-machine-only-gets-iommu-enabled-when-setting-intel_iommu-on-false-positive.115920/post-501335)

`amd_iommu` is on by default.  
<br/>Invalid parameters are ignored, therefore `amd_iommu=on` is ignored (because it is not [defined](https://www.kernel.org/doc/html/v5.15/admin-guide/kernel-parameters.html)) as well as `intel_iommu=on` (because it does not apply to your system). Resulting in `amd_iommu` being enabled just as it would when you don't add any parameters.  
I also think you are using the check for IOMMU being enabled for Intel systems, which does not apply.  
You have several IOMMU groups (0 upto 30), so IOMMU is definitely enabled (which it is by default) and I don't see any problems.  
<br/>If you are having problems with a VM with passthrough, it's not because IOMMU is not enabled but probably because the GPU is used during boot and by Proxmox. The various work-arounds are in [this thread](https://forum.proxmox.com/threads/problem-with-gpu-passthrough.55918/) from several months ago.

- <img width="16" height="16" src="../_resources/1f44d_8f6341c519344345af698af35e3931dd.png"/>

Reactions: [rhobinn](https://forum.proxmox.com/posts/501335/reactions)

<a id="js-XFUniqueId19"></a>[R](https://forum.proxmox.com/members/rhobinn.163540/)

#### <a id="js-XFUniqueId20"></a>[rhobinn](https://forum.proxmox.com/members/rhobinn.163540/)

##### Member

Sep 29, 2022

5

0

6

- [Oct 1, 2022](https://forum.proxmox.com/threads/amd-machine-only-gets-iommu-enabled-when-setting-intel_iommu-on-false-positive.115920/post-501563)

- <a id="js-XFUniqueId37"></a>[](https://forum.proxmox.com/threads/amd-machine-only-gets-iommu-enabled-when-setting-intel_iommu-on-false-positive.115920/post-501563)
- [#3](https://forum.proxmox.com/threads/amd-machine-only-gets-iommu-enabled-when-setting-intel_iommu-on-false-positive.115920/post-501563)

solved here  
https://forum.proxmox.com/threads/is-gpu-passthrough-working.115919/

[You must log in or register to reply here.](https://forum.proxmox.com/login/)

Share:

<a id="js-XFUniqueId26"></a>[LinkedIn](#_xfUid-1-1736320317) <a id="js-XFUniqueId27"></a>[Reddit](#_xfUid-1-1736320317) <a id="js-XFUniqueId28"></a>[Email](#_xfUid-1-1736320317) <a id="js-XFUniqueId30"></a>[Link](#_xfUid-1-1736320317)

- [](https://forum.proxmox.com)
- [Forums](https://forum.proxmox.com/)
- [Proxmox Virtual Environment](https://forum.proxmox.com/#proxmox-virtual-environment.11)
- [Proxmox VE: Installation and configuration](https://forum.proxmox.com/forums/proxmox-ve-installation-and-configuration.16/)

## About

The Proxmox community has been around for many years and offers help and support for Proxmox VE, Proxmox Backup Server, and Proxmox Mail Gateway.  
We think our community is one of the best thanks to people like you!

### Quick Navigation

[Home](https://forum.proxmox.com) [Get Subscription](https://www.proxmox.com/proxmox-virtual-environment/pricing) [Wiki](https://pve.proxmox.com/wiki) [Downloads](https://www.proxmox.com/downloads) [Proxmox Customer Portal](https://my.proxmox.com/) [About](https://www.proxmox.com/about/company)

### Get your subscription!

The Proxmox team works very hard to make sure you are running the best software and getting stable updates and security enhancements, as well as quick enterprise support. Tens of thousands of happy customers have a Proxmox subscription. Get yours easily in our online shop.

[Buy now!](https://shop.proxmox.com)

- <a id="uix_widthToggle--trigger"></a>
- <a id="js-XFUniqueId31"></a>[Proxmox Support Forum - Light Mode](https://forum.proxmox.com/misc/style)

- [Contact us](https://www.proxmox.com/en/about/contact)
- [Terms and rules](https://forum.proxmox.com/help/terms/)
- [Privacy policy](https://www.proxmox.com/en/privacy-policy)
- [Help](https://forum.proxmox.com/help/)
- [Home](https://forum.proxmox.com)
- [](#top "Top")
- [RSS](https://forum.proxmox.com/forums/-/index.rss "RSS")

[Community platform by XenForo<sup>®</sup> © 2010-2024 XenForo Ltd.](https://xenforo.com)

- <a id="js-XFUniqueId32"></a>[](https://git.proxmox.com)
- <a id="js-XFUniqueId33"></a>[](https://bugzilla.proxmox.com)
- <a id="js-XFUniqueId34"></a>[](https://www.youtube.com/user/ProxmoxVE)

- This site uses cookies to help personalise content, tailor your experience and to keep you logged in if you register.  
    By continuing to use this site, you are consenting to our use of cookies.
    
    [Accept](https://forum.proxmox.com/account/dismiss-notice) [Learn more…](https://forum.proxmox.com/help/cookies)