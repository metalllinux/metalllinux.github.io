---
title: "Jellyfin Docker Compose.Yml File"
category: "project-tv"
tags: ["project-tv", "jellyfin", "docker", "composeyml", "file"]
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
      - /mnt/vector/children_shows:/data/children_shows
      - /mnt/vector/films:/data/films
      - /mnt/vector/live_shows:/data/live_shows
      - /mnt/vector/music:/data/music
      - /mnt/vector/photos:/data/photos
      - /mnt/vector/shows:/data/shows
      - /mnt/vector/youtube:/data/youtube
    ports:
      - 8096:8096
    restart: unless-stopped
EOF
```
* `cd ~/docker_compose_files/jellyfin/`
* `docker compose up -d`