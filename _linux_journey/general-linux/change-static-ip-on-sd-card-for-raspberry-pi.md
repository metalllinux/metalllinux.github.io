---
title: "Change Static Ip On Sd Card For Raspberry Pi"
category: "general-linux"
tags: ["change", "static", "card", "raspberry"]
---

sudo nano /etc/dhcpcd.conf

Now scroll to the bottom, and add the following text:

interface INTERFACE
static ip_address=YOURSTATICIP/24
static routers=YOURGATEWAYIP
static domain_name_servers= YOURGATEWAYIP
