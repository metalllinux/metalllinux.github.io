---
title: "Working Vikunja Docker Container Auto Start Servic"
category: "kubernetes-and-containers"
tags: ["kubernetes-and-containers", "working", "vikunja", "docker", "container"]
---

```
[Unit]
Description=Vikunja Task Manager
Requires=docker.service
After=docker.service

[Service]
Restart=always
ExecStart=/usr/bin/docker start -a hungry_galois
ExecStop=/usr/bin/docker stop -t 2 hungry_galois

[Install]
WantedBy=default.target
```
sudo systemctl enable docker-vikunja.service