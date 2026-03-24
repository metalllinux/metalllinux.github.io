---
title: "ksoftirq Discussion on the Nvidia Forums"
category: "kernel-and-system-internals"
tags: ["kernel-and-system-internals", "ksoftirq", "discussion", "nvidia", "forums"]
---

# ksoftirq Discussion on the Nvidia Forums

During some testing, I’ve noticed something with my TX2 under heavy Ethernet load. The ksoftirq process goes nuts and uses 100% CPU time. Seems an easy way to trigger this is starting an iperf server on the TX2, and connecting with a Gig-E laptop.

I’ve seen this behaviour on L4T r28.1 and r32.1. Enabling irqbalance seems to help a little bit on r32.1, but still seeing network stalls, and lots of interrupts reported in /proc/softirq. Irqbalance and r28.1 seems a bad combination, still reporting higher CPU load, and also spamming “Ethernet interrupt while in poll!” both to the console and to the system log at around 110 Hz.

While in talks with my contact at ConnectTech, they suggested something I’d like to try, using ethtool to increase network card TX/RX buffers. Apparently this has helped in other applications. However, the current eqos driver for the onboard Ethernet device does not appear to support this? They suggested a different driver was used in past versions of L4T and did work?

Any thoughts, or things I can try to get network performance a little more reliable?

 ![](https://sea2.discourse-cdn.com/nvidia/user_avatar/forums.developer.nvidia.com/linuxdev/96/10243_2.png "linuxdev")

Hi,

Could you help share the data you have observed and the method to reproduce this issue?

Though I initially noticed it while having the TX2 act as a network server, it seems easiest to stress this with iperf. On the TX2, run:

```
$ sudo apt-get install iperf
$ iperf -s
```

Then from the client, run:

```
$ iperf -c [tx2 IP address]
```

Then run “top” in a second console on the TX2. The ksoftirq/0 process should spike to 100%.

Another interesting datapoint. I have my TX2 mounted on a ConnnectTech Elroy board, and needed to install a second network adapter for increased network bandwidth. This adapter is a Syba half size mPCIE Ethernet adapter using a Realtek R8168 chipset. Not only does the Realtek adapter show a higher transfer speed in iperf, but there’s no apparent CPU spike in ksoftirq.

Fair warning that I am using a kernel compiled from the ConnectTech BSP sources. However, the ConnectTech guys felt this might be an upstream issue, and that I should ask here.

Some kernel design information might be useful…

The kernel scheduler determines what process gets what time and which CPU core to use. Basically running drivers. The drivers themselves probably have certain pieces of code which talk directly to the hardware, and there is no avoiding locking a core to that task during that time. For example, i/o to a physical address of the hardware might only be applicable at certain times on a shared bus. The kernel must use atomic/non-divisible operations during that time and preemption will not be possible.

However, there are times when things are done in the kernel which do not require locking the CPU core to a given function. When that code is run scheduling becomes much more like user space and the ksoftirq management software can migrate that code and run it based on fair sharing times. Atomic operations are not required for this. Ksoftirq times indicates purely software operations or operations which can be preempted are sharing cores (this is a “good thing”).

A bad kernel driver will do both mandatory atomic operations and any related operations without ever unlocking the CPU core. A good kernel driver design will put the atomic code in one place, and the code which can be preempted somewhere else. Then mandatory locking will occur only for the part of the code which needs this (someone must know this and program accordingly), and code which can share time and not corrupt or fail with multitasking will be handled separately with ksoftirq. During the time of mandatory locking nobody else can use that core and the code will not share (the system will become less responsive…it’s good to have more CPU cores for that case, but cache misses mean extra cores are still not as good as sharing of a core).

Seeing a large amount of traffic resulting in ksoftirq running says the authors had a good driver design for that hardware (someone separated atomic from sharable operations). However, differences in ethernet hardware do exist. Not all ethernet hardware has the same features. In some cases some hardware actually offloads work to the ethernet chipset and the kernel does not need to do that work. Other hardware may depend on the CPU for parts of the work. An example would be hardware compression versus software compression, and some (but not all) chipsets will support hardware compression…hardware compression would be lower latency and lower CPU load, but the work would still be done…only that work would be done in the ethernet hardware instead of CPU. This latter case would not show CPU load and would avoid ksoftirq, but the reason would _not_ be due to bad design: The reason would be due to non-CPU hardware performing the same task, and this is a “good thing” if the compression hardware exists (I don’t know what the existing hardware supports, this is just a contrived example).

If an ethernet driver were to do all of the work in atomic/non-preemptable fashion, but not need to do so, then you would also see a lack of load on ksoftirq. However, this would be bad design. If code can be offloaded to ksoftirq, but is not offloaded, then the CPU core is locked longer than needed and unable to share or multitask for excessive lengths of time. The work would still be done, but the work would be done for that driver and would not show up under ksoftirq.

In your case there are these possibilities:

-   The ethernet hardware is offloading work so ksoftirq is not needed for the system not loading ksoftirq.
-   The driver without ksoftirq loading is failing good design and the work is being performed atomically within the driver: Side effect being a less responsive system and seeing the load somewhere other than ksoftirq.
-   Something in the design or operation of the low softirq case does not require the work which ksoftirq was doing for high ksoftirq load. This is possible and not unreasonable in cases where perhaps different network settings are being used (the hardware and drivers could be the same, but the data and parameters being processed differ). A contrived example might be one system is using jumbo frames (low load) and the other is not (high load)...it would appear to be the driver's or hardware's fault, but in reality it would be a case of different loads from different data handling and the observer not knowing about the jumbo frame differences.

Hi linuxdev,

Thanks for the response, though it may have be less helpful than you intended.

What I’m after is a way for my TX2 to receive simultaneous high throughput streams via NFS, and my TX2’s onboard Ethernet sustains measurably less throughput in my application. Understanding apparent driver quality doesn’t get me any closer to determining whether or not I can do anything about the asymmetric performance. I do understand some boards do have internal bus limitations (some ODroids for example), and if that’s the case than so be it.

On the chance that the ksoftirq performance is an unnecessary spinlock somewhere, it’s worth asking.

What has helped in other applications has been to bump the TX/RX buffers to decrease the interrupt rate. Understood that depending on the Ethernet hardware, this may not be possible with that controller’s feature set. It may not even help much, if the long pole in the tent is something like a long-running PIO transfer.

Really happy to find this topic.

I would like to confirm same issue. It is clearly seen ksoftirqd/0 load with 100% CPU0 utilisation on 900+Mbit/s network traffic speed with Jetson acting as receiver.

It is worth saving machine resourses. So i tried to run iperf test with external Realtek rtl8111 PCI Express card as topicstarter hinted and it works like a charm. No SoftIRQ overhead, 83.5% machine idle (all cores forced by jetson\_clocks to 2GHz), consistent 954MBit/s link reported by iperf (jumbo 9k on both sides). Happy with it.

I guess i would prefer to run carrier with pci express realtek card rather than fighting with EQOS onboard network card drivers. Something definitely wrong with them.

Although maybe a good Samaritan will fix it someday? :)

Hi [@e3737c](https://forums.developer.nvidia.com/u/e3737c),

Could you file a new topic and share us how to reproduce this issue?

As a fair warning, we found a possible kernel issue with the 4.9 kernel (tested on L4T r32.1 and r32.4.3), where we were seeing occasional data corruption between the RealTek Ethernet driver and a ASMedia ASM1061 SATA controller, resulting in both filesystem and network data (ssh) corruption.

This doesn’t seem to happen with the 4.4 kernel (L4T r28.1).

We were unsuccessful in isolating the issue with ConnectTech support, and eventually swapped the second Ethernet with an Intel chipset, and have not seen the issue since.

Your mileage may vary.

hi timothy,

Thank you for sharing your experience.

I could not confirm any issues at the moment with rtl8111 rev. F / r8168 driver / L4T R32.3.1 kernel 4.9.140, but we have a short test period, things can change in the long run. The only problem we’ve seen with rtl8111 was PCIe driver probe failure but it was on another SBC and doesn’t related to Jetson at all.

Intel is really good network card vendor but since we develop own electronics rather than using end product it seems to be costly option for us to switch IC vendor. Anyway i’m happy to know we could try Intel IC if some data corruption occurs.

Hi WayneWWW,

I have some doubts is it really good option to start new topic? I literally cannot add anything more to the problem described by topic starter except to confirm that this issue exists on L4T R32.3.1. It looks like we found hardware solution but it doesn’t eliminate possible software issue with onboard network card under heavy network load.

**There is no update from you for a period, assuming this is not an issue any more.  
Hence we are closing this topic. If need further support, please open a new one.  
Thanks**

Hello,

It is fine to use this topic to track. I am just used to asking users filing new topic instead of letting old topic jumping out again.

I am sorry that maybe I missed this one last year.

What I want to know is

1.  Detailed steps to reproduce issue on TX2 devkit. Any other peripheral connected?
    
2.  How is the reproduce rate? I mean how often to do hit this issue?
    
3.  Are you able to reproduce issue on latest release?

