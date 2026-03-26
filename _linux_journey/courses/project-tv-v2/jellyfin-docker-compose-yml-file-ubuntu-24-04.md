---
title: "Jellyfin Docker Compose.Yml File Ubuntu 24.04"
category: "project-tv-v2"
tags: ["project-tv-v2", "jellyfin", "docker", "composeyml", "file"]
---

```
cat << "EOF" | tee /home/myuser/docker_compose_files/jellyfin/docker-compose.yml
---
services:
  jellyfin:
    image: lscr.io/linuxserver/jellyfin:latest
    container_name: jellyfin
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Asia/Tokyo
    volumes:
      - /home/myuser/jellyfin/config:/config
      - /home/myuser/jellyfin/cache:/cache
      - /mnt/mediapool/anime:/data/anime
      - /mnt/mediapool/media-d:/data/media-d
      - /mnt/mediapool/media-b:/data/media-b
      - /mnt/mediapool/films:/data/films
      - /mnt/mediapool/gaming_videos:/data/gaming_videos
      - /mnt/mediapool/media-c:/data/media-c
      - /mnt/mediapool/music:/data/music
      - /mnt/mediapool/media-a:/data/media-a
      - /mnt/mediapool/shows:/data/shows
      - /mnt/mediapool/skateboarding:/data/skateboarding
      - /mnt/mediapool/tv:/data/tv
    ports:
      - 8096:8096
    restart: unless-stopped
EOF
```
* `cd ~/docker_compose_files/jellyfin/`
* `docker compose up -d`
