---
title: "Initial Rsync From Main Backup Host To Media Serve"
category: "project-tv-v2"
tags: ["project-tv-v2", "initial", "rsync", "main", "backup"]
---

```
rsync --ignore-existing -azvr --progress howard@192.168.1.101:/mnt/sonic/children_shows/ /mnt/vector/children_shows/

rsync --ignore-existing -azvr --progress howard@192.168.1.101:/mnt/sonic/dance_videos/ /mnt/vector/dance_videos/

rsync --ignore-existing -azvr --progress howard@192.168.1.101:/mnt/sonic/films/ /mnt/vector/films/

rsync --ignore-existing -azvr --progress howard@192.168.1.101:/mnt/sonic/gaming_videos/ /mnt/vector/gaming_videos/

rsync --ignore-existing -azvr --progress howard@192.168.1.101:/mnt/sonic/live_shows/ /mnt/vector/live_shows/

rsync --ignore-existing -azvr --progress howard@192.168.1.101:/mnt/sonic/music/ /mnt/vector/music/

rsync --ignore-existing -azvr --progress howard@192.168.1.101:/mnt/sonic/photos/ /mnt/vector/photos/

rsync --ignore-existing -azvr --progress howard@192.168.1.101:/mnt/sonic/shows/ /mnt/vector/shows/
```