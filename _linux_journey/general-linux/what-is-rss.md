---
title: "What Is Rss"
category: "general-linux"
tags: ["rss"]
---

Receive side scaling (RSS) is a technology that enables the distribution of received packets between multiple RX queues using a predefined hash function. It enabled multicore CPU to process packets from different queues on different cores.

Symmetric RSS promise is to populate two-way packets from the same TCP connection to the same RX queue. As a result statistics on the different connections could be stored in the per-queue data structures avoiding any need for locking.

* https://haryachyy.wordpress.com/2019/01/18/learning-dpdk-symmetric-rss/