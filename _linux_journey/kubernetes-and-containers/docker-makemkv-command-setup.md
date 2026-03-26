---
title: "Docker Makemkv Command Setup"
category: "kubernetes-and-containers"
tags: ["kubernetes-and-containers", "docker", "makemkv", "command", "setup"]
---

`docker run -d --name=makemkv --privileged -p 5800:5800 -e USER_ID=1000 -e GROUP_ID=1000 -v /docker/appdata/makemkv:/config:rw -v /home/myuser:/storage:ro -v /home/myuser/makemkv/output:/output:rw --device /dev/sg0 jlesage/makemkv`

Current Version:

docker run -d --name=makemkv -p 5800:5800 -e USER_ID=1000 -e GROUP_ID=1000 -v /docker/appdata/makemkv:/config:rw -v /home/myuser/videos:/storage:ro -v /home/myuser/videos:/output:rw --device /dev/sr0 --device /dev/sr1 --device /dev/sg0 --device /dev/sg1 jlesage/makemkv

If running the above configuration with only 1 USB blu-ray drive attached, can run the following instead:

docker run -d --name=makemkv -p 5800:5800 -e USER_ID=1000 -e GROUP_ID=1000 -v /docker/appdata/makemkv:/config:rw -v /home/myuser/Videos:/storage:ro -v /home/myuser/Videos:/output:rw --device /dev/sg1 jlesage/makemkv

If running on Ubuntu, use:

docker run -d --name=makemkv --privileged -p 5800:5800 -e USER_ID=1000 -e GROUP_ID=1000 -v /docker/appdata/makemkv:/config:rw -v /home/myuser/videos:/storage:ro -v /home/myuser/videos:/output:rw --device /dev/sr0 --device /dev/sr1 --device /dev/sg0 --device /dev/sg1 jlesage/makemkv

Make sure as well the drive is connected and a disk inserted BEFORE running the above steps to set up the container.
