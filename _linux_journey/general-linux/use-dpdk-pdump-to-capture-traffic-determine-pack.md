---
title: "Use Dpdk Pdump To Capture Traffic Determine Pack"
category: "general-linux"
tags: ["dpdk", "pdump", "capture", "traffic", "determine"]
---

`dpdk-pdump -- --pdump 'port=0,queue=*,rx-dev=/tmp/rx.pcap,tx-dev=/tmp/tx.pcap'
* Packet capture to analyse traffic flow and dropped packets.
* https://doc.dpdk.org/guides/tools/pdump.html