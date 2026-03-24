---
title: "rsync to tails"
category: "storage-and-filesystems"
tags: ["storage-and-filesystems", "rsync", "crontab"]
---

```
# rsync to tails
0 0 * * * rsync --ignore-existing -azvr --progress /mnt/sonic/anime/ howard@192.168.1.102:/mnt/tails/anime/
0 0 * * * rsync --ignore-existing -azvr --progress /mnt/sonic/cartoons/ howard@192.168.1.102:/mnt/tails/cartoons/
0 0 * * * rsync --ignore-existing -azvr --progress /mnt/sonic/documents/ howard@192.168.1.102:/mnt/tails/documents/
0 0 * * * rsync --ignore-existing -azvr --progress /mnt/sonic/ebooks/ howard@192.168.1.102:/mnt/tails/ebooks/
0 0 * * * rsync --ignore-existing -azvr --progress /mnt/sonic/games/ howard@192.168.1.102:/mnt/tails/games/
0 0 * * * rsync --ignore-existing -azvr --progress /mnt/sonic/linux/ howard@192.168.1.102:/mnt/tails/linux/
0 0 * * * rsync --ignore-existing -azvr --progress /mnt/sonic/live_shows/ howard@192.168.1.102:/mnt/tails/live_shows/
0 0 * * * rsync --ignore-existing -azvr --progress /mnt/sonic/movies/ howard@192.168.1.102:/mnt/tails/movies/
0 0 * * * rsync --ignore-existing -azvr --progress /mnt/sonic/music/ howard@192.168.1.102:/mnt/tails/music/
0 0 * * * rsync --ignore-existing -azvr --progress /mnt/sonic/photos/ howard@192.168.1.102:/mnt/tails/photos/
0 0 * * * rsync --ignore-existing -azvr --progress /mnt/sonic/shows/ howard@192.168.1.102:/mnt/tails/shows/
```