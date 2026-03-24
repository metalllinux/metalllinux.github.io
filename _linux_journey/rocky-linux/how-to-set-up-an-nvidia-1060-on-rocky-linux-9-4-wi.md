---
title: "The below option will reboot the machine."
category: "rocky-linux"
tags: ["rocky-linux", "nvidia", "rocky", "linux"]
---

```
sudo dnf install rpmfusion-free-release epel-release
sudo dnf install --nogpgcheck   https://mirrors.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-$(rpm -E %rhel).noarch.rpm
sudo crb enable
sudo dnf update
sudo reboot
sudo dnf install kmod-nvidia
sudo dnf install xorg-x11-drv-nvidia-cuda
# The below option will reboot the machine.
sudo init 6
curl -s -L https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo |   sudo tee /etc/yum.repos.d/nvidia-container-toolkit.repo
sudo yum install -y nvidia-container-toolkit
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker
```