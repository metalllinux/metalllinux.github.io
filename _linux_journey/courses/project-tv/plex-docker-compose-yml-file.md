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
      - /home/howard/plex/config:/config
      - /mnt/vector/children_shows:/children_shows
      - /mnt/vector/films:/films
      - /mnt/vector/live_shows:/live_shows
      - /mnt/vector/music:/music
      - /mnt/vector/photos:/photos
      - /mnt/vector/shows:/shows
      - /mnt/vector/tv:/tv
      - /mnt/vector/youtube_videos:/youtube_videos
    restart: unless-stopped
EOF
```