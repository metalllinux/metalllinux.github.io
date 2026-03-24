---
title: "How Run Tailscale Commands In Docker"
category: "kubernetes-and-containers"
tags: ["kubernetes-and-containers", "run", "tailscale", "commands", "docker"]
---

A few examples:

docker exec tailscaled tailscale --socket /tmp/tailscaled.sock down

docker exec tailscaled tailscale --socket /tmp/tailscaled.sock up --advertise-exit-node --accept-dns=false