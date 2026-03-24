---
title: "How Add And Remove Masquerade From Firewall Cmd"
category: "networking"
tags: ["networking", "add", "remove", "masquerade", "firewall"]
---

firewall-cmd --zone=public --add-masquerade --permanent

firewall-cmd --zone=public --remove-masquerade --permanent

