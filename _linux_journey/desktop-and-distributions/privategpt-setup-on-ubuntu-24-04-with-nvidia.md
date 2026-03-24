---
title: "Privategpt Setup On Ubuntu 24.04 With Nvidia"
category: "desktop-and-distributions"
tags: ["desktop-and-distributions", "privategpt", "setup", "ubuntu", "nvidia"]
---

* Install `vim`:
```
sudo apt install -y vim
```
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
* Configure the Nvidia production repository:
```
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
  && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
```
* Update the repository package list:
```
sudo apt-get update
```
* Install the Nvidia Container Toolkit packages:
```
sudo apt-get install -y nvidia-container-toolkit
```
* Enable the NVIDIA Container Runtime on Docker:
```
sudo nvidia-ctk runtime configure --runtime=docker
```
* Restart Docker:
```
sudo systemctl restart docker
```
* Reload the units:
```
sudo systemctl daemon-reload
```
* Run a sample CUDA container for testing:
```
sudo docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
```
* Clone the PrivateGPT repository:
```
git clone https://github.com/zylon-ai/private-gpt.git
```
* Change into the `private-gpt` directory:
```
cd private-gpt
```
* Bring up the container with this command:
```
sudo docker compose --profile ollama-cuda up -d
```
* Install `nvtop`:
```
sudo apt install -y nvtop
```
* Export all files from Joplin as Markdown.
* Concatenate all markdown files with:
```
cat *.md > combined.md
```
* Upload the concatenated files to PrivateGPT at `<address:8001>`