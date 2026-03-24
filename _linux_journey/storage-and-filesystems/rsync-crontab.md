---
title: "rsync documents from dethklok to mustakrakish"
category: "storage-and-filesystems"
tags: ["storage-and-filesystems", "rsync", "crontab"]
---

crontab -e

```
# rsync documents from dethklok to mustakrakish
0 0 * * * rsync --ignore-existing -azvr --progress /mnt/dethklok/documents/ /mnt/mustakrakish/documents/

# rsync movies from dethklok to mustakrakish
0 0 * * * rsync --ignore-existing -azvr --progress /mnt/dethklok/movies/ /mnt/mustakrakish/movies/

# rsync pictures from dethklok to mustakrakish
0 0 * * * rsync --ignore-existing -azvr --progress /mnt/dethklok/pictures/ /mnt/mustakrakish/pictures/
```
crontab -l

rsync --ignore-existing -azvr --progress /mnt/dethklok/pictures/* /mnt/sonic/photos/; rsync --ignore-existing -azvr --progress /mnt/dethklok/anime/* /mnt/sonic/anime/; rsync --ignore-existing -azvr --progress /mnt/dethklok/cartoons/* /mnt/sonic/cartoons/; rsync --ignore-existing -azvr --progress /mnt/dethklok/ebooks/* /mnt/sonic/ebooks/; rsync --ignore-existing -azvr --progress /mnt/dethklok/games/* /mnt/sonic/games/; rsync --ignore-existing -azvr --progress /mnt/dethklok/live_shows/* /mnt/sonic/live_shows/; rsync --ignore-existing -azvr --progress /mnt/dethklok/movies/* /mnt/sonic/movies/; rsync --ignore-existing -azvr --progress /mnt/dethklok/music/* /mnt/sonic/music/; rsync --ignore-existing -azvr --progress /mnt/dethklok/tv_shows/* /mnt/sonic/shows/