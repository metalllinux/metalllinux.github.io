---
title: "!/bin/bash"
category: "project-tv-v2"
tags: ["project-tv-v2", "automatically", "start", "stop", "docker"]
---

* Create the `BASH` script to start the containers:
```
cat << "EOF" | tee /home/myuser/scripts/docker-containers-start.sh
#!/bin/bash

# Mirakurun and EPGSTATION
cd /home/myuser/git/docker-mirakurun-epgstation/ && docker compose up -d

# Jellyfin
cd /home/myuser/docker_compose_files/jellyfin/ && docker compose up -d
EOF
```
* Make the script executable:
```
chmod +x /home/myuser/scripts/docker-containers-start.sh
```
* Create the `BASH` script to stop the containers:
```
cat << "EOF" | tee /home/myuser/scripts/docker-containers-stop.sh
#!/bin/bash

# Mirakurun and EPGSTATION
cd /home/myuser/git/docker-mirakurun-epgstation/ && docker compose down

# Jellyfin
cd /home/myuser/docker_compose_files/jellyfin/ && docker compose down
EOF
```
* Make the script executable:
```
chmod +x /home/myuser/scripts/docker-containers-stop.sh
```
* Add the scripts to KDE Autostart.