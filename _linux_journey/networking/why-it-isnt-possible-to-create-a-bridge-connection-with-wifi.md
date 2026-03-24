---
title: "Why It Isn't Possible to Create a Virtual Bridge Connection with Wifi"
category: "networking"
tags: ["networking", "isnt", "possible", "create", "bridge"]
---

# Why It Isn't Possible to Create a Virtual Bridge Connection with Wifi

Unfortunately, you cannot directly add a WiFi interface as a bridge slave like you can with Ethernet. This is a fundamental limitation because:

Most WiFi drivers/firmware don't support bridging in client mode (they would need WDS - Wireless Distribution System support)
WiFi access points typically reject packets with MAC addresses different from the authenticated client

