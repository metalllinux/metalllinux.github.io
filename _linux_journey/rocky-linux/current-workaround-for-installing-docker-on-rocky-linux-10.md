---
title: "Current Workaround for Installing Docker on Rocky Linux 10"
category: "rocky-linux"
tags: ["rocky-linux", "current", "workaround", "installing", "docker"]
---

# Current Workaround for Installing Docker on Rocky Linux 10

# Add the RHEL 9 Docker repository instead
sudo dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

# Modify the baseurl to use RHEL 9 packages
sudo sed -i 's|$releasever|9|g' /etc/yum.repos.d/docker-ce.repo

# Try installing again
sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

sudo systemctl --now enable docker

sudo usermod -a -G docker $(whoami)

newgrp docker
