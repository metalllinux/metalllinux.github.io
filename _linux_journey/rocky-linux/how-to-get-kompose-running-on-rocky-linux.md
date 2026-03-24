---
title: "How To Get Kompose Running On Rocky Linux"
category: "rocky-linux"
tags: ["rocky-linux", "kompose", "running", "rocky", "linux"]
---

curl -L https://github.com/kubernetes/kompose/releases/download/v1.34.0/kompose-linux-amd64 -o kompose
chmod +x kompose
Then run `./kompose` with the yaml files you want to convert with `kompose convert`