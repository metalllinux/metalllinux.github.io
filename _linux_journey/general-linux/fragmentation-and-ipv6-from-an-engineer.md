---
title: "Fragmentation And Ipv6 From An Engineer"
category: "general-linux"
tags: ["fragmentation", "ipv6", "engineer"]
---

 fragmentation by routers is not allowed, but by the sending host it is. (This doesn't change anything in troubleshooting this issue I think. I mention it only because your wording seemed to imply fragmentation is completely not a thing in v6, which is false.)
Also, MTU of the entire path need to be taken into account with v4 as well, because the v4 "don't fragment' flag usually is set. (Again, just for our own understanding for troubleshooting future issues.)

There's also the ICMP vs. ICMPv6 difference, but looks like specifically for echo request/reply it's same size https://en.wikipedia.org/wiki/ICMPv6#Format
In general, MTU differences causing issues is commonly associated with excessive filtering of ICMP (or in this case ICMPv6) messages.

IPV6 headers are 40-bytes in length.