---
title: "XFS Setup on Rocky Linux"
category: "rocky-linux"
tags: ["rocky-linux", "xfs", "setup", "rocky", "linux"]
---

# XFS Setup on Rocky Linux

* Create the mount points:

```
sudo mkdir -p /mnt/server-a /mnt/server-b /mnt/server-c
```

* Use `fdisk` to prepare each disk. Create one partition across the whole disk:

```
sudo fdisk /dev/sd<LETTER>
> g
> n
> p 
> 1
>
> w
```

* Format the disks with the XFS filesystem using these options:

```
sudo mkfs.xfs -L server-a -m bigtime=1,inobtcount=1 /dev/sdb1
sudo mkfs.xfs -L server-b -m bigtime=1,inobtcount=1 /dev/sdc1
```

* Find the UUIDs of the drives from `sudo blkid` 

* With the UUIDs in hand, add them to `/etc/fstab`:

```
cat << "EOF" | sudo tee -a /etc/fstab
UUID=7651ae01-4cc6-4e62-bb05-4a317ab9bfe2 /mnt/server-a xfs defaults,inode64 0 0
UUID=57f1ea7f-a956-4c48-bcff-bb14445b1a85 /mnt/server-b xfs defaults,inode64 0 0
UUID=ac2d2dfa-b6c2-417a-9613-780ffeb93c2f /mnt/server-c xfs defaults,inode64 0 0
EOF
```

* Reboot:

```
sudo reboot
```

* Change ownership of the directories:

```
sudo chown myuser:myuser -R /mnt/server-a/
sudo chown myuser:myuser -R /mnt/server-b/
sudo chown myuser:myuser -R /mnt/server-c/
```

* Create the directory structure:

```
mkdir -p /mnt/server-a/anime /mnt/server-a/bitcoin /mnt/server-a/media-d /mnt/server-a/media-b /mnt/server-a/documents /mnt/server-a/ebooks /mnt/server-a/films /mnt/server-a/games /mnt/server-a/isos /mnt/server-a/linux /mnt/server-a/media-c /mnt/server-a/music /mnt/server-a/media-a /mnt/server-a/shows /mnt/server-a/media-e /mnt/server-a/software

mkdir -p /mnt/server-b/anime /mnt/server-b/bitcoin /mnt/server-b/media-d /mnt/server-b/media-b /mnt/server-b/documents /mnt/server-b/ebooks /mnt/server-b/films /mnt/server-b/games /mnt/server-b/isos /mnt/server-b/linux /mnt/server-b/media-c /mnt/server-b/music /mnt/server-b/media-a /mnt/server-b/shows /mnt/server-b/media-e /mnt/server-b/software

mkdir -p /mnt/server-c/anime /mnt/server-c/bitcoin /mnt/server-c/media-d /mnt/server-c/media-b /mnt/server-c/documents /mnt/server-c/ebooks /mnt/server-c/films /mnt/server-c/games /mnt/server-c/isos /mnt/server-c/linux /mnt/server-c/media-c /mnt/server-c/music /mnt/server-c/media-a /mnt/server-c/shows /mnt/server-c/media-e /mnt/server-c/software
```

* Make sure that `tmux` is installed on the machine you are sending the data from:

```
sudo dnf install -y tmux
```

* Start a `tmux` session:

```
tmux
```

* Copy the public `ssh` key from the sending machine to the receiving machine:

```
ssh-copy-id user@<remote_machine>
```

* Start the migration:

```
rsync -AvPr /mnt/server-a/anime/* myuser@192.168.1.y:/mnt/server-a/anime/ && rsync -AvPr /mnt/server-a/bitcoin/* myuser@192.168.1.y:/mnt/server-a/bitcoin/ && rsync -AvPr /mnt/server-a/media-d/* myuser@192.168.1.y:/mnt/server-a/media-d/ && rsync -AvPr /mnt/server-a/media-b/* myuser@192.168.1.y:/mnt/server-a/media-b/ && rsync -AvPr /mnt/server-a/documents/* myuser@192.168.1.y:/mnt/server-a/documents/ && rsync -AvPr /mnt/server-a/ebooks/* myuser@192.168.1.y:/mnt/server-a/ebooks/ && rsync -AvPr /mnt/server-a/films/* myuser@192.168.1.y:/mnt/server-a/films/ && rsync -AvPr /mnt/server-a/games/* myuser@192.168.1.y:/mnt/server-a/games/ && rsync -AvPr /mnt/server-a/isos/* myuser@192.168.1.y:/mnt/server-a/isos/ && rsync -AvPr /mnt/server-a/linux/* myuser@192.168.1.y:/mnt/server-a/linux/ && rsync -AvPr /mnt/server-a/media-c/* myuser@192.168.1.y:/mnt/server-a/media-c/ && rsync -AvPr /mnt/server-a/music/* myuser@192.168.1.y:/mnt/server-a/music/ && rsync -AvPr /mnt/server-a/media-a/* myuser@192.168.1.y:/mnt/server-a/media-a/ && rsync -AvPr /mnt/server-a/shows/* myuser@192.168.1.y:/mnt/server-a/shows/ && rsync -AvPr /mnt/server-a/media-e/* myuser@192.168.1.y:/mnt/server-a/media-e/ && rsync -AvPr /mnt/server-a/software/* myuser@192.168.1.y:/mnt/server-a/software/
```

* If copying data locally between drives, run:

```
rsync -AvPr /mnt/server-a/* /mnt/server-c/ 
```
