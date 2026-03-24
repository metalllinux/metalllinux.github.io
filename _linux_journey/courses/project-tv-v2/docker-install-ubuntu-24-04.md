---
title: "Docker Install Ubuntu 24.04"
category: "project-tv-v2"
tags: ["project-tv-v2", "docker", "install", "ubuntu"]
---

* Update `apt` repository:
```
sudo apt-get update
```
* Install `certificates` and `curl` packages:
```
sudo apt-get install -y ca-certificates curl
```
* Set up the keyrings:
```
sudo install -m 0755 -d /etc/apt/keyrings
```
* Pull down docker's GPG key:
```
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
```
* Add appropriate permissions to the `docker.asc` file:
```
sudo chmod a+r /etc/apt/keyrings/docker.asc
```
* Add the docker repository to the `apt` sources list:
```
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```
* Run another `apt update`:
```
sudo apt-get update
```
* Install the latest version of docker:
```
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
* Create the docker user:
```
sudo groupadd docker
```
* Add your current user to the `docker` group:
```
sudo usermod -aG docker $USER
```
* Activate the group changes to your user:
```
newgrp docker
```