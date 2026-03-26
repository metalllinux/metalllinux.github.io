---
title: "How To Install Bcachefs On Rocky Linux"
category: "rocky-linux"
tags: ["rocky-linux", "install", "bcachefs", "rocky", "linux"]
---

Install the latest ELRepo kernel-ml
sudo dnf groupinstall "Development Tools"
sudo yum install epel-release
sudo dnf config-manager --set-enabled crb
sudo dnf install libaio-devel libsodium-devel libblkid-devel libzstd-devel zlib-devel userspace-rcu-devel lz4-devel libuuid-devel valgrind-devel keyutils-libs-devel findutils udev systemd-devel llvm-devel
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y --no-modify-path
. "$HOME/.cargo/env"
git clone https://github.com/koverstreet/bcachefs-tools
cd bcachefs-tools/
sudo dnf install clang-libs
sudo dnf install clang
make
sudo make install
cd ..
rm -Rf ./bcachefs-tools/

# bcachefs setup (RAID0)
```
sudo bcachefs format --compression=zstd:15 /dev/sd<X> /dev/sd<X>
```
# bcachefs setup (RAID1)
sudo bcachefs format --compression=zstd:15 /dev/sda /dev/sdb --replicas=2

# Create a systemd mount to mount at boot
sudo vim /etc/systemd/system/server-b-mount.service
[Unit]
Description=Mount bcachefs
After=network-online.target
Wants=network-online.target

[Service]
Type=oneshot
ExecStart=/home/myuser/scripts/server-b-mount.sh

[Install]
WantedBy=multi-user.target

# Create the directory to mount the drives
sudo mkdir /mnt/server-b

# Create the following boot script
mkdir ~/scripts
vim ~/scripts/server-b-mount.sh 

#!/bin/bash
# Mount the bcachefs devices
mount -t bcachefs /dev/sda:/dev/sdc /mnt/server-b

# Make the script executable
chmod +x ~/scripts/server-b-mount.sh

# Disable SELinux
sudo setenforce 0
sudo sed -i --follow-symlinks 's/SELINUX=enforcing/SELINUX=permissive/g' /etc/sysconfig/selinux

# Set permissions on the drives:
sudo chown myuser:myuser -R /mnt/server-b

# Enable and start the services
sudo systemctl enable --now server-b-mount.service

# Set up ssh keys between nodes
# On each node, run
ssh-keygen -t rsa -b 4096

# Copy the generated key to the node of choice:
ssh-copy-id -i ~/.ssh/<public_key_here> username@remote-server.org

# systemd service files for rsync transfer
# Create the following service file:
sudo vim /etc/systemd/system/server-a-send.service

# Add this to the service file:
[Unit]
Description=rsync files to server-b
After=network.target

[Service]
ExecStart=/home/myuser/scripts/server-a-send.sh
Restart=always
User=myuser

# Create the script in /home/myuser/scripts/server-a-send.sh
# Add the following:
#!/bin/bash
# rsync to server-b
rsync -e "ssh -i /home/myuser/.ssh/server-a" --ignore-existing -azvr --progress /mnt/server-a/anime/ myuser@192.168.1.y:/mnt/server-b/anime/
rsync -e "ssh -i /home/myuser/.ssh/server-a" --ignore-existing -azvr --progress /mnt/server-a/cartoons/ myuser@192.168.1.y:/mnt/server-b/cartoons/
rsync -e "ssh -i /home/myuser/.ssh/server-a" --ignore-existing -azvr --progress /mnt/server-a/documents/ myuser@192.168.1.y:/mnt/server-b/documents/
rsync -e "ssh -i /home/myuser/.ssh/server-a" --ignore-existing -azvr --progress /mnt/server-a/ebooks/ myuser@192.168.1.y:/mnt/server-b/ebooks/
rsync -e "ssh -i /home/myuser/.ssh/server-a" --ignore-existing -azvr --progress /mnt/server-a/games/ myuser@192.168.1.y:/mnt/server-b/games/
rsync -e "ssh -i /home/myuser/.ssh/server-a" --ignore-existing -azvr --progress /mnt/server-a/linux/ myuser@192.168.1.y:/mnt/server-b/linux/
rsync -e "ssh -i /home/myuser/.ssh/server-a" --ignore-existing -azvr --progress /mnt/server-a/media-c/ myuser@192.168.1.y:/mnt/server-b/media-c/
rsync -e "ssh -i /home/myuser/.ssh/server-a" --ignore-existing -azvr --progress /mnt/server-a/movies/ myuser@192.168.1.y:/mnt/server-b/movies/
rsync -e "ssh -i /home/myuser/.ssh/server-a" --ignore-existing -azvr --progress /mnt/server-a/music/ myuser@192.168.1.y:/mnt/server-b/music/
rsync -e "ssh -i /home/myuser/.ssh/server-a" --ignore-existing -azvr --progress /mnt/server-a/media-a/ myuser@192.168.1.y:/mnt/server-b/media-a/
rsync -e "ssh -i /home/myuser/.ssh/server-a" --ignore-existing -azvr --progress /mnt/server-a/shows/ myuser@192.168.1.y:/mnt/server-b/shows/

# rsync to server-c
rsync -e "ssh -i /home/myuser/.ssh/server-a" --ignore-existing -azvr --progress /mnt/server-a/anime/ myuser@192.168.1.z:/mnt/server-c/anime/
rsync -e "ssh -i /home/myuser/.ssh/server-a" --ignore-existing -azvr --progress /mnt/server-a/cartoons/ myuser@192.168.1.z:/mnt/server-c/cartoons/
rsync -e "ssh -i /home/myuser/.ssh/server-a" --ignore-existing -azvr --progress /mnt/server-a/documents/ myuser@192.168.1.z:/mnt/server-c/documents/
rsync -e "ssh -i /home/myuser/.ssh/server-a" --ignore-existing -azvr --progress /mnt/server-a/ebooks/ myuser@192.168.1.z:/mnt/server-c/ebooks/
#rsync -e "ssh -i /home/myuser/.ssh/server-a" --ignore-existing -azvr --progress /mnt/server-a/games/ myuser@192.168.1.z:/mnt/server-c/games/
rsync -e "ssh -i /home/myuser/.ssh/server-a" --ignore-existing -azvr --progress /mnt/server-a/linux/ myuser@192.168.1.z:/mnt/server-c/linux/
rsync -e "ssh -i /home/myuser/.ssh/server-a" --ignore-existing -azvr --progress /mnt/server-a/media-c/ myuser@192.168.1.z:/mnt/server-c/media-c/
rsync -e "ssh -i /home/myuser/.ssh/server-a" --ignore-existing -azvr --progress /mnt/server-a/movies/ myuser@192.168.1.z:/mnt/server-c/movies/
rsync -e "ssh -i /home/myuser/.ssh/server-a" --ignore-existing -azvr --progress /mnt/server-a/music/ myuser@192.168.1.z:/mnt/server-c/music/
rsync -e "ssh -i /home/myuser/.ssh/server-a" --ignore-existing -azvr --progress /mnt/server-a/media-a/ myuser@192.168.1.z:/mnt/server-c/media-a/
rsync -e "ssh -i /home/myuser/.ssh/server-a" --ignore-existing -azvr --progress /mnt/server-a/shows/ myuser@192.168.1.z:/mnt/server-c/shows/

# Make the script executable:
chmod +x ~/scripts/server-a-send.sh



