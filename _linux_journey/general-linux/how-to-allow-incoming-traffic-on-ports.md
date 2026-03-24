---
title: "How To Allow Incoming Traffic On Ports"
category: "general-linux"
tags: ["allow", "incoming", "traffic", "ports"]
---

sudo firewall-cmd --zone=public --add-port=PORT_NUMBER/tcp --permanent
sudo firewall-cmd --reload