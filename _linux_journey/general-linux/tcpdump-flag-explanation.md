---
title: "Tcpdump Flag Explanation"
category: "general-linux"
tags: ["tcpdump", "flag", "explanation"]
---

    "nn": Don't resolve hostnames or port numbers to their symbolic names. Instead, display them as numerical values.
    "vv": Increase the verbosity level of the output. This flag causes tcpdump to print more information about the packets it captures, including protocol headers and packet payloads.
    "A": Print packets in ASCII format. This flag can be used to decode and display application-level protocols such as HTTP.
    "s0": Don't truncate packet capture data. By default, tcpdump will truncate packets to 68 bytes of data. This flag disables that behaviour and captures the entire packet.