---
title: "Sending Test Messages With Nc"
category: "general-linux"
tags: ["sending", "test", "messages"]
---

echo "test data" | nc <IP> <port>

echo "test data" | socat - TCP:<IP>:<port>
