---
title: "Docker Compose Handbrake Setup"
category: "kubernetes-and-containers"
tags: ["kubernetes-and-containers", "docker", "compose", "handbrake", "setup"]
---

* Create the docker directory:
```
mkdir -p /home/howard/docker_compose_files/handbrake
```
* Create the required directories:
```
mkdir -p /home/howard/handbrake/config

mkdir -p /home/howard/handbrake/storage

mkdir -p /home/howard/handbrake/watch

mkdir -p /home/howard/handbrake/output
```
* Generate the compose file:
```
cat << "EOF" | tee /home/howard/docker_compose_files/handbrake/docker-compose.yml
version: '3'
services:
  handbrake:
    image: jlesage/handbrake
    ports:
      - "5800:5800"
    volumes:
      - "/home/howard/handbrake/config:/config:rw"
      - "/home/howard/handbrake/storage:/storage:ro"
      - "/home/howard/handbrake/watch:/watch:rw"
      - "/home/howard/handbrake/output:/output:rw"
EOF
```
* Change into the docker-compose directory:
```
cd /home/howard/docker_compose_files/handbrake
```
* Bring up the container:
```
docker compose up -d
```
* Bring up the application with:
```
<IP>:5800
```