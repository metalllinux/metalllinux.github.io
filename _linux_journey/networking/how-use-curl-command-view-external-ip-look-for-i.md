---
title: "How Use Curl Command View External Ip Look For I"
category: "networking"
tags: ["networking", "curl", "command", "view", "external"]
---

curl -6 icanhazip.com

IP V6

curl -4 icanhazip.com
OR
curl ifconfig.me

IP V4

Doing the same thing with wget:

wget -4 -qO - icanhazip.com

IP V4

wget -6 -qO - icanhazip.com

IP V6