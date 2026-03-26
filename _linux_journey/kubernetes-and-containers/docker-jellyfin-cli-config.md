---
title: "Docker Jellyfin Cli Config"
category: "kubernetes-and-containers"
tags: ["kubernetes-and-containers", "docker", "jellyfin", "cli", "config"]
---

docker run -d \
 --name jellyfin \
 --user 1000:1000 \
 --net=host \
 --volume /home/myuser/jellyfin/config:/config \
 --volume /home/myuser/jellyfin/cache:/cache \
 --mount type=bind,source=/mnt/mypool/movies,target=/movies \
 --mount type=bind,source=/mnt/mypool/tv_shows,target=/tv_shows \
 --mount type=bind,source=/mnt/mypool/anime,target=/anime \
 --mount type=bind,source=/mnt/mypool/media-c,target=/live_shows \
 --mount type=bind,source=/mnt/mypool/music,target=/music \
 --restart=unless-stopped \
 jellyfin/jellyfin

 docker run -d \
 --name jellyfin \
 --user 1000:1000 \
 --net=host \
 --volume /home/myuser/jellyfin/config:/config \
 --volume /home/myuser/jellyfin/cache:/cache \
 --mount type=bind,source=/mnt/mypool/anime,target=/anime \
 --mount type=bind,source=/mnt/mypool/media-c,target=/live_shows \
 --mount type=bind,source=/mnt/mypool/movies,target=/movies \
 --mount type=bind,source=/mnt/mypool/tv_shows,target=/tv_shows \
 --restart=unless-stopped \
 jellyfin/jellyfin