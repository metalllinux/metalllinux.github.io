---
title: "How To Set Up Handbrake Using Docker With Nvenc Fo"
category: "kubernetes-and-containers"
tags: ["kubernetes-and-containers", "handbrake", "docker", "nvenc"]
---

```
mkdir -p ~/.config/handbrake/
mkdir -p ~/to_encode_queue
mkdir -p ~/completed_videos
```
```
docker run -d -t \
    --name=handbrake \
    -p 5800:5800 \
    -p 5900:5900 \
    -v /home/howard/.config/handbrake:/config:rw \
    -v /home/howard/to_encode_queue:/storage:ro \
    -v /home/howard/completed_videos:/output:rw \
    --gpus all \
    zocker160/handbrake-nvenc:latest
```