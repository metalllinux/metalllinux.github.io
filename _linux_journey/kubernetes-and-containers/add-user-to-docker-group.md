---
title: "Add User To Docker Group"
category: "kubernetes-and-containers"
tags: ["kubernetes-and-containers", "add", "user", "docker", "group"]
---

`sudo groupadd docker`
`sudo usermod -aG docker $USER`
* Log out and then back in or run the following command:
`newgrp docker`