---
title: "How Backup Docker Containers"
category: "kubernetes-and-containers"
tags: ["kubernetes-and-containers", "backup", "docker", "containers"]
---

sudo docker start <container-id>

Create Snapshot:

sudo docker commit -p 6cb599fe30ea my-backup

Saving it as a `tar` file:

sudo docker save -o ~/my-backup.tar my-backup