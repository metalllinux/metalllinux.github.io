---
title: "Docker Jellyfin Cli Config"
category: "kubernetes-and-containers"
tags: ["kubernetes-and-containers", "docker", "jellyfin", "cli", "config"]
---

docker run -d \
 --name jellyfin \
 --user 1000:1000 \
 --net=host \
 --volume /home/howard/jellyfin/config:/config \
 --volume /home/howard/jellyfin/cache:/cache \
 --mount type=bind,source=/mnt/mustakrakish/movies,target=/movies \
 --mount type=bind,source=/mnt/mustakrakish/tv_shows,target=/tv_shows \
 --mount type=bind,source=/mnt/mustakrakish/anime,target=/anime \
 --mount type=bind,source=/mnt/mustakrakish/live_shows,target=/live_shows \
 --mount type=bind,source=/mnt/mustakrakish/music,target=/music \
 --restart=unless-stopped \
 jellyfin/jellyfin
 
 docker run -d \
 --name jellyfin \
 --user 1000:1000 \
 --net=host \
 --volume /home/howard/jellyfin/config:/config \
 --volume /home/howard/jellyfin/cache:/cache \
 --mount type=bind,source=/mnt/mustakrakish/anime,target=/anime \
 --mount type=bind,source=/mnt/mustakrakish/live_shows,target=/live_shows \
 --mount type=bind,source=/mnt/mustakrakish/movies,target=/movies \
 --mount type=bind,source=/mnt/mustakrakish/tv_shows,target=/tv_shows \
 --restart=unless-stopped \
 jellyfin/jellyfin