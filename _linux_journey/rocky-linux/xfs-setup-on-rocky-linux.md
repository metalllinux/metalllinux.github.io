---
title: "XFS Setup on Rocky Linux"
category: "rocky-linux"
tags: ["rocky-linux", "xfs", "setup", "rocky", "linux"]
---

# XFS Setup on Rocky Linux

* Create the mount points:

```
sudo mkdir -p /mnt/sonic /mnt/tails /mnt/knuckles
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
sudo mkfs.xfs -L sonic -m bigtime=1,inobtcount=1 /dev/sdb1
sudo mkfs.xfs -L tails -m bigtime=1,inobtcount=1 /dev/sdc1
```

* Find the UUIDs of the drives from `sudo blkid` 

* With the UUIDs in hand, add them to `/etc/fstab`:

```
cat << "EOF" | sudo tee -a /etc/fstab
UUID=7651ae01-4cc6-4e62-bb05-4a317ab9bfe2 /mnt/sonic xfs defaults,inode64 0 0
UUID=57f1ea7f-a956-4c48-bcff-bb14445b1a85 /mnt/tails xfs defaults,inode64 0 0
UUID=ac2d2dfa-b6c2-417a-9613-780ffeb93c2f /mnt/knuckles xfs defaults,inode64 0 0
EOF
```

* Reboot:

```
sudo reboot
```

* Change ownership of the directories:

```
sudo chown howard:howard -R /mnt/sonic/
sudo chown howard:howard -R /mnt/tails/
sudo chown howard:howard -R /mnt/knuckles/
```

* Create the directory structure:

```
mkdir -p /mnt/sonic/anime /mnt/sonic/bitcoin /mnt/sonic/children_shows /mnt/sonic/dance_videos /mnt/sonic/documents /mnt/sonic/ebooks /mnt/sonic/films /mnt/sonic/games /mnt/sonic/isos /mnt/sonic/linux /mnt/sonic/live_shows /mnt/sonic/music /mnt/sonic/photos /mnt/sonic/shows /mnt/sonic/skateboarding /mnt/sonic/software

mkdir -p /mnt/tails/anime /mnt/tails/bitcoin /mnt/tails/children_shows /mnt/tails/dance_videos /mnt/tails/documents /mnt/tails/ebooks /mnt/tails/films /mnt/tails/games /mnt/tails/isos /mnt/tails/linux /mnt/tails/live_shows /mnt/tails/music /mnt/tails/photos /mnt/tails/shows /mnt/tails/skateboarding /mnt/tails/software

mkdir -p /mnt/knuckles/anime /mnt/knuckles/bitcoin /mnt/knuckles/children_shows /mnt/knuckles/dance_videos /mnt/knuckles/documents /mnt/knuckles/ebooks /mnt/knuckles/films /mnt/knuckles/games /mnt/knuckles/isos /mnt/knuckles/linux /mnt/knuckles/live_shows /mnt/knuckles/music /mnt/knuckles/photos /mnt/knuckles/shows /mnt/knuckles/skateboarding /mnt/knuckles/software
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
rsync -AvPr /mnt/sonic/anime/* howard@192.168.1.102:/mnt/sonic/anime/ && rsync -AvPr /mnt/sonic/bitcoin/* howard@192.168.1.102:/mnt/sonic/bitcoin/ && rsync -AvPr /mnt/sonic/children_shows/* howard@192.168.1.102:/mnt/sonic/children_shows/ && rsync -AvPr /mnt/sonic/dance_videos/* howard@192.168.1.102:/mnt/sonic/dance_videos/ && rsync -AvPr /mnt/sonic/documents/* howard@192.168.1.102:/mnt/sonic/documents/ && rsync -AvPr /mnt/sonic/ebooks/* howard@192.168.1.102:/mnt/sonic/ebooks/ && rsync -AvPr /mnt/sonic/films/* howard@192.168.1.102:/mnt/sonic/films/ && rsync -AvPr /mnt/sonic/games/* howard@192.168.1.102:/mnt/sonic/games/ && rsync -AvPr /mnt/sonic/isos/* howard@192.168.1.102:/mnt/sonic/isos/ && rsync -AvPr /mnt/sonic/linux/* howard@192.168.1.102:/mnt/sonic/linux/ && rsync -AvPr /mnt/sonic/live_shows/* howard@192.168.1.102:/mnt/sonic/live_shows/ && rsync -AvPr /mnt/sonic/music/* howard@192.168.1.102:/mnt/sonic/music/ && rsync -AvPr /mnt/sonic/photos/* howard@192.168.1.102:/mnt/sonic/photos/ && rsync -AvPr /mnt/sonic/shows/* howard@192.168.1.102:/mnt/sonic/shows/ && rsync -AvPr /mnt/sonic/skateboarding/* howard@192.168.1.102:/mnt/sonic/skateboarding/ && rsync -AvPr /mnt/sonic/software/* howard@192.168.1.102:/mnt/sonic/software/
```

* If copying data locally between drives, run:

```
rsync -AvPr /mnt/sonic/* /mnt/knuckles/ 
```
