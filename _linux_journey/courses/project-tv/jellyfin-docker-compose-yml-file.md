---
title: "Jellyfin Docker Compose.Yml File"
category: "project-tv"
tags: ["project-tv", "jellyfin", "docker", "composeyml", "file"]
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
      - /mnt/mediapool/media-d:/data/media-d
      - /mnt/mediapool/films:/data/films
      - /mnt/mediapool/media-c:/data/media-c
      - /mnt/mediapool/music:/data/music
      - /mnt/mediapool/media-a:/data/media-a
      - /mnt/mediapool/shows:/data/shows
      - /mnt/mediapool/youtube:/data/youtube
    ports:
      - 8096:8096
    restart: unless-stopped
EOF
```
* `cd ~/docker_compose_files/jellyfin/`
* `docker compose up -d`