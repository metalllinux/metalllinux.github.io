---
title: "Podman Makemkv Commands"
category: "kubernetes-and-containers"
tags: ["kubernetes-and-containers", "podman", "makemkv", "commands"]
---

**MakeMKV podman Container Setup**

sudo podman run -d --name=makemkv --privileged -p 5800:5800 -e USER_ID=1000 -e GROUP_ID=1000 -v /home/myuser/MakeMKV/config:/home/myuser/MakeMKV/config -v /home/myuser:/home/myuser -v /home/myuser/MakeMKV/output:/home/myuser/MakeMKV/output --device /dev/sg0 jlesage/makemkv

**Updated Version**

sudo podman run -d --name=makemkv --privileged -p 5800:5800 -e USER_ID=1000 -e GROUP_ID=1000 -v /home/myuser/MakeMKV/config:/home/myuser/MakeMKV/config -v /home/myuser:/home/myuser -v /home/myuser/MakeMKV/output:/home/myuser/MakeMKV/output --device /dev/sg0 jlesage/makemkv

**Debian 11 Version**

sudo podman run -d --name=makemkv --privileged -p 5800:5800 -v /home/myuser/.makemkv/config:/home/myuser/.makemkv/config -v /home/myuser:/home/myuser -v /home/myuser/.makemkv/output:/home/myuser/.makemkv/output --device /dev/sg0 docker.io/jlesage/makemkv
