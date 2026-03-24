---
title: "What is mc_forwarding"
category: "general-linux"
tags: ["forwarding"]
---

# What is mc_forwarding

## What is `mc_forwarding`?

`mc_forwarding` (multicast forwarding) is a Linux kernel parameter that controls whether a network interface can forward multicast packets between networks. It's found at `/proc/sys/net/ipv4/conf/<interface>/mc_forwarding`.

## Key Concepts

**Multicast forwarding** means taking multicast packets received on one network interface and forwarding them out through another interface - essentially acting as a multicast router.

## Values and behaviour

- **`0` (disabled)**: The interface will only process multicast packets destined for itself. It won't forward multicast packets to other interfaces.
- **`1` (enabled)**: The interface can forward multicast packets between different network segments.

## When is it needed?

1. **Multicast Router**: When your Linux system acts as a multicast router between different networks
2. **IPTV/Streaming**: Forwarding multicast streams from one network segment to another
3. **Multi-homed servers**: Servers with multiple network interfaces that need to relay multicast traffic

## When is it NOT needed?

1. **Single network segment**: If all your multicast participants are on the same network
2. **End hosts**: Regular computers that only send/receive multicast (not forward it)
3. **Container-to-container on same bridge**: Containers on the same virtual bridge can exchange multicast without forwarding

## Example Scenario

```
Network A (192.168.1.0/24) --- [Linux Router] --- Network B (10.0.0.0/24)
                                 mc_forwarding=1
```

Without `mc_forwarding=1`, multicast traffic from Network A won't reach Network B through the Linux router.

## Why it requires CONFIG_MROUTE

The kernel must be compiled with `CONFIG_IP_MROUTE` (IPv4 multicast routing) support. This includes:
- Multicast routing tables
- IGMP (Internet Group Management Protocol) support
- PIM (Protocol Independent Multicast) support
