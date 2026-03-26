---
title: "Plex Docker Compose.Yml File"
category: "project-tv"
tags: ["project-tv", "plex", "docker", "composeyml", "file"]
---

```
cat << "EOF" | tee ~/docker_compose_files/plex/docker-compose.yml
---
services:
  plex:
    image: lscr.io/linuxserver/plex:latest
    container_name: plex
    network_mode: host
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Asia/Tokyo
      - VERSION=docker
	  - PLEX_CLAIM=claim-q9sNahz8hKAemjnw-UYe
    volumes:
      - /home/myuser/plex/config:/config
      - /mnt/mediapool/media-d:/media-d
      - /mnt/mediapool/films:/films
      - /mnt/mediapool/media-c:/media-c
      - /mnt/mediapool/music:/music
      - /mnt/mediapool/media-a:/media-a
      - /mnt/mediapool/shows:/shows
      - /mnt/mediapool/tv:/tv
      - /mnt/mediapool/youtube_videos:/youtube_videos
    restart: unless-stopped
EOF
```