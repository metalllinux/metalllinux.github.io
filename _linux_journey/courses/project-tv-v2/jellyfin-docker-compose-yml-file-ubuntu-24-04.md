---
title: "Jellyfin Docker Compose.Yml File Ubuntu 24.04"
category: "project-tv-v2"
tags: ["project-tv-v2", "jellyfin", "docker", "composeyml", "file"]
---

```
cat << "EOF" | tee /home/howard/docker_compose_files/jellyfin/docker-compose.yml
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
      - /home/howard/jellyfin/config:/config
      - /home/howard/jellyfin/cache:/cache
      - /mnt/vector/anime:/data/anime
      - /mnt/vector/children_shows:/data/children_shows
      - /mnt/vector/dance_videos:/data/dance_videos
      - /mnt/vector/films:/data/films
      - /mnt/vector/gaming_videos:/data/gaming_videos
      - /mnt/vector/live_shows:/data/live_shows
      - /mnt/vector/music:/data/music
      - /mnt/vector/photos:/data/photos
      - /mnt/vector/shows:/data/shows
      - /mnt/vector/skateboarding:/data/skateboarding
      - /mnt/vector/tv:/data/tv
    ports:
      - 8096:8096
    restart: unless-stopped
EOF
```
* `cd ~/docker_compose_files/jellyfin/`
* `docker compose up -d`
