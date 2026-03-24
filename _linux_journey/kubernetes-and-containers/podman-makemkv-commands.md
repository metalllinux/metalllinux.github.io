---
title: "Podman Makemkv Commands"
category: "kubernetes-and-containers"
tags: ["kubernetes-and-containers", "podman", "makemkv", "commands"]
---

**MakeMKV podman Container Setup**

sudo podman run -d --name=makemkv --privileged -p 5800:5800 -e USER_ID=1000 -e GROUP_ID=1000 -v /home/howard/MakeMKV/config:/home/howard/MakeMKV/config -v /home/howard:/home/howard -v /home/howard/MakeMKV/output:/home/howard/MakeMKV/output --device /dev/sg0 jlesage/makemkv

**Updated Version**

sudo podman run -d --name=makemkv --privileged -p 5800:5800 -e USER_ID=1000 -e GROUP_ID=1000 -v /home/howard/MakeMKV/config:/home/howard/MakeMKV/config -v /home/howard:/home/howard -v /home/howard/MakeMKV/output:/home/howard/MakeMKV/output --device /dev/sg0 jlesage/makemkv

**Debian 11 Version**

sudo podman run -d --name=makemkv --privileged -p 5800:5800 -v /home/howard/.makemkv/config:/home/howard/.makemkv/config -v /home/howard:/home/howard -v /home/howard/.makemkv/output:/home/howard/.makemkv/output --device /dev/sg0 docker.io/jlesage/makemkv
