---
title: "Initial Rsync From Main Backup Host To Media Serve"
category: "project-tv-v2"
tags: ["project-tv-v2", "initial", "rsync", "main", "backup"]
---

```
rsync --ignore-existing -azvr --progress myuser@192.168.1.101:/mnt/server-a/media-d/ /mnt/mediapool/media-d/

rsync --ignore-existing -azvr --progress myuser@192.168.1.101:/mnt/server-a/media-b/ /mnt/mediapool/media-b/

rsync --ignore-existing -azvr --progress myuser@192.168.1.101:/mnt/server-a/films/ /mnt/mediapool/films/

rsync --ignore-existing -azvr --progress myuser@192.168.1.101:/mnt/server-a/gaming_videos/ /mnt/mediapool/gaming_videos/

rsync --ignore-existing -azvr --progress myuser@192.168.1.101:/mnt/server-a/media-c/ /mnt/mediapool/media-c/

rsync --ignore-existing -azvr --progress myuser@192.168.1.101:/mnt/server-a/music/ /mnt/mediapool/music/

rsync --ignore-existing -azvr --progress myuser@192.168.1.101:/mnt/server-a/media-a/ /mnt/mediapool/media-a/

rsync --ignore-existing -azvr --progress myuser@192.168.1.101:/mnt/server-a/shows/ /mnt/mediapool/shows/
```