---
title: "!/bin/bash"
category: "project-tv-v2"
tags: ["project-tv-v2", "systemd", "service", "pull", "backup"]
---

* Create the scripts directory:
```
mkdir -p /home/myuser/scripts
```
* Create the script file:
```
cat << "EOF" | tee /home/myuser/scripts/server-a_pull.sh
#!/bin/bash
rsync --ignore-existing -azvr --progress myuser@192.168.1.101:/mnt/server-a/anime/ /mnt/mediapool/anime/

rsync --ignore-existing -azvr --progress myuser@192.168.1.101:/mnt/server-a/media-d/ /mnt/mediapool/media-d/

rsync --ignore-existing -azvr --progress myuser@192.168.1.101:/mnt/server-a/media-b/ /mnt/mediapool/media-b/

rsync --ignore-existing -azvr --progress myuser@192.168.1.101:/mnt/server-a/films/ /mnt/mediapool/films/

rsync --ignore-existing -azvr --progress myuser@192.168.1.101:/mnt/server-a/gaming_videos/ /mnt/mediapool/gaming_videos/

rsync --ignore-existing -azvr --progress myuser@192.168.1.101:/mnt/server-a/media-c/ /mnt/mediapool/media-c/

rsync --ignore-existing -azvr --progress myuser@192.168.1.101:/mnt/server-a/music/ /mnt/mediapool/music/

rsync --ignore-existing -azvr --progress myuser@192.168.1.101:/mnt/server-a/media-a/ /mnt/mediapool/media-a/

rsync --ignore-existing -azvr --progress myuser@192.168.1.101:/mnt/server-a/shows/ /mnt/mediapool/shows/
EOF
```
* Make the script executable:
```
chmod +x /home/myuser/scripts/server-a_pull.sh
```
* Create the `systemd` `service` file:
```
cat << "EOF" | sudo tee /etc/systemd/system/server-a-pull.service
[Unit]
Description=Pull the latest files from the Server-A.
After=network.target

[Service]
Type=oneshot
ExecStart=/home/myuser/scripts/server-a_pull.sh
User=myuser
EOF
```
* Create the associated `timer` file:
```
cat << "EOF" | sudo tee /etc/systemd/system/server-a-pull.timer
[Unit]
Description=rsync directories from server-a to server-b every month

[Timer]
OnCalendar=monthly
Persistent=true
Unit=server-a-pull.service

[Install]
WantedBy=timers.target
EOF
```
* Create an `ssh` key (no password):
```
ssh-keygen -t rsa -b 4096
```
* Copy the `ssh` key to the backup server:
```
ssh-copy-id -i ~/.ssh/id_rsa.pub myuser@192.168.1.101
```
* Enable and start the `timer`:
```
sudo systemctl enable --now server-a-pull.timer
```
* Start the service immediately with:
```
sudo systemctl start server-a-pull
```