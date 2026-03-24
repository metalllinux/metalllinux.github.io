---
title: "Gc Threshold Troubleshooting"
category: "general-linux"
tags: ["threshold", "troubleshooting"]
---

Check MTU settings:
```
grep -i mtu sos_commands/kernel/sysctl_-a
```

They only lowered the garbage‑collection thresholds and stale time without touching the core NUD timers.

The kernel still waits its full default interval before ever sending a neighbour Solicitation.

You’ll need to reduce base_reachable_time_ms so entries leave the REACHABLE state much sooner.

You’ll also want to set gc_stale_time (or the per‑interface stale timer) so entries move into STALE more quickly.

Until those timers are adjusted, you’ll keep seeing “no route to host” after long idle periods.

i'd try like...

base_reachable_time_ms = 5000 # 5 seconds

gc_stale_time = 10 # 10 seconds

and if that isn't converging fast enough, retrans_time_ms can be tuned downwards to send solicitations every 30s instead of 60

tbh this is a trade off scenario. faster NUD means more solicitations, i.e. more traffic

also, this could be upstream network hardware rate limiting ICMP6... i wouldn't put it past this group

I think all the cali interfaces are the same some how

remember, too, that ipv6 has no arp. it's neighbour solicitation which is all multicast

they may need some sort of thing that monitors the GC queue and adjusts params based on some sort of backpressure heuristic