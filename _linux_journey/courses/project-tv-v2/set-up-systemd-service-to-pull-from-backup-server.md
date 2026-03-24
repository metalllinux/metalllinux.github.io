---
title: "!/bin/bash"
category: "project-tv-v2"
tags: ["project-tv-v2", "systemd", "service", "pull", "backup"]
---

* Create the scripts directory:
```
mkdir -p /home/howard/scripts
```
* Create the script file:
```
cat << "EOF" | tee /home/howard/scripts/sonic_pull.sh
#!/bin/bash
rsync --ignore-existing -azvr --progress howard@192.168.1.101:/mnt/sonic/anime/ /mnt/vector/anime/

rsync --ignore-existing -azvr --progress howard@192.168.1.101:/mnt/sonic/children_shows/ /mnt/vector/children_shows/

rsync --ignore-existing -azvr --progress howard@192.168.1.101:/mnt/sonic/dance_videos/ /mnt/vector/dance_videos/

rsync --ignore-existing -azvr --progress howard@192.168.1.101:/mnt/sonic/films/ /mnt/vector/films/

rsync --ignore-existing -azvr --progress howard@192.168.1.101:/mnt/sonic/gaming_videos/ /mnt/vector/gaming_videos/

rsync --ignore-existing -azvr --progress howard@192.168.1.101:/mnt/sonic/live_shows/ /mnt/vector/live_shows/

rsync --ignore-existing -azvr --progress howard@192.168.1.101:/mnt/sonic/music/ /mnt/vector/music/

rsync --ignore-existing -azvr --progress howard@192.168.1.101:/mnt/sonic/photos/ /mnt/vector/photos/

rsync --ignore-existing -azvr --progress howard@192.168.1.101:/mnt/sonic/shows/ /mnt/vector/shows/
EOF
```
* Make the script executable:
```
chmod +x /home/howard/scripts/sonic_pull.sh
```
* Create the `systemd` `service` file:
```
cat << "EOF" | sudo tee /etc/systemd/system/sonic-pull.service
[Unit]
Description=Pull the latest files from the Sonic Server.
After=network.target

[Service]
Type=oneshot
ExecStart=/home/howard/scripts/sonic_pull.sh
User=howard
EOF
```
* Create the associated `timer` file:
```
cat << "EOF" | sudo tee /etc/systemd/system/sonic-pull.timer
[Unit]
Description=rsync directories from sonic to tails every month

[Timer]
OnCalendar=monthly
Persistent=true
Unit=sonic-pull.service

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
ssh-copy-id -i ~/.ssh/id_rsa.pub howard@192.168.1.101
```
* Enable and start the `timer`:
```
sudo systemctl enable --now sonic-pull.timer
```
* Start the service immediately with:
```
sudo systemctl start sonic-pull
```