---
title: "How Create Tailscale Docker Container With Exit No"
category: "kubernetes-and-containers"
tags: ["kubernetes-and-containers", "create", "tailscale", "docker", "container"]
---

docker run -d --name=tailscaled -v /var/lib:/var/lib -v /dev/net/tun:/dev/net/tun --network=host --cap-add=NET_ADMIN --restart unless-stopped --cap-add=NET_RAW --env TS_EXTRA_ARGS=--advertise-exit-node --env TS_ACCEPT_DNS=false --env TS_AUTHKEY=tskey-auth-kLphae7CNTRL-QZQDU2GX9CbVMApbQQTmBb8amuzwji7w tailscale/tailscale