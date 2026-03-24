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
sudo vim /etc/systemd/system/tails-mount.service
[Unit]
Description=Mount bcachefs
After=network-online.target
Wants=network-online.target

[Service]
Type=oneshot
ExecStart=/home/howard/scripts/tails-mount.sh

[Install]
WantedBy=multi-user.target

# Create the directory to mount the drives
sudo mkdir /mnt/tails

# Create the following boot script
mkdir ~/scripts
vim ~/scripts/tails-mount.sh 

#!/bin/bash
# Mount the bcachefs devices
mount -t bcachefs /dev/sda:/dev/sdc /mnt/tails

# Make the script executable
chmod +x ~/scripts/tails-mount.sh

# Disable SELinux
sudo setenforce 0
sudo sed -i --follow-symlinks 's/SELINUX=enforcing/SELINUX=permissive/g' /etc/sysconfig/selinux

# Set permissions on the drives:
sudo chown howard:howard -R /mnt/tails

# Enable and start the services
sudo systemctl enable --now tails-mount.service

# Set up ssh keys between nodes
# On each node, run
ssh-keygen -t rsa -b 4096

# Copy the generated key to the node of choice:
ssh-copy-id -i ~/.ssh/<public_key_here> username@remote-server.org

# systemd service files for rsync transfer
# Create the following service file:
sudo vim /etc/systemd/system/sonic-send.service

# Add this to the service file:
[Unit]
Description=rsync files to tails
After=network.target

[Service]
ExecStart=/home/howard/scripts/sonic-send.sh
Restart=always
User=howard

# Create the script in /home/howard/scripts/sonic-send.sh
# Add the following:
#!/bin/bash
# rsync to tails
rsync -e "ssh -i /home/howard/.ssh/sonic" --ignore-existing -azvr --progress /mnt/sonic/anime/ howard@192.168.1.102:/mnt/tails/anime/
rsync -e "ssh -i /home/howard/.ssh/sonic" --ignore-existing -azvr --progress /mnt/sonic/cartoons/ howard@192.168.1.102:/mnt/tails/cartoons/
rsync -e "ssh -i /home/howard/.ssh/sonic" --ignore-existing -azvr --progress /mnt/sonic/documents/ howard@192.168.1.102:/mnt/tails/documents/
rsync -e "ssh -i /home/howard/.ssh/sonic" --ignore-existing -azvr --progress /mnt/sonic/ebooks/ howard@192.168.1.102:/mnt/tails/ebooks/
rsync -e "ssh -i /home/howard/.ssh/sonic" --ignore-existing -azvr --progress /mnt/sonic/games/ howard@192.168.1.102:/mnt/tails/games/
rsync -e "ssh -i /home/howard/.ssh/sonic" --ignore-existing -azvr --progress /mnt/sonic/linux/ howard@192.168.1.102:/mnt/tails/linux/
rsync -e "ssh -i /home/howard/.ssh/sonic" --ignore-existing -azvr --progress /mnt/sonic/live_shows/ howard@192.168.1.102:/mnt/tails/live_shows/
rsync -e "ssh -i /home/howard/.ssh/sonic" --ignore-existing -azvr --progress /mnt/sonic/movies/ howard@192.168.1.102:/mnt/tails/movies/
rsync -e "ssh -i /home/howard/.ssh/sonic" --ignore-existing -azvr --progress /mnt/sonic/music/ howard@192.168.1.102:/mnt/tails/music/
rsync -e "ssh -i /home/howard/.ssh/sonic" --ignore-existing -azvr --progress /mnt/sonic/photos/ howard@192.168.1.102:/mnt/tails/photos/
rsync -e "ssh -i /home/howard/.ssh/sonic" --ignore-existing -azvr --progress /mnt/sonic/shows/ howard@192.168.1.102:/mnt/tails/shows/

# rsync to knuckles
rsync -e "ssh -i /home/howard/.ssh/sonic" --ignore-existing -azvr --progress /mnt/sonic/anime/ howard@192.168.1.103:/mnt/knuckles/anime/
rsync -e "ssh -i /home/howard/.ssh/sonic" --ignore-existing -azvr --progress /mnt/sonic/cartoons/ howard@192.168.1.103:/mnt/knuckles/cartoons/
rsync -e "ssh -i /home/howard/.ssh/sonic" --ignore-existing -azvr --progress /mnt/sonic/documents/ howard@192.168.1.103:/mnt/knuckles/documents/
rsync -e "ssh -i /home/howard/.ssh/sonic" --ignore-existing -azvr --progress /mnt/sonic/ebooks/ howard@192.168.1.103:/mnt/knuckles/ebooks/
#rsync -e "ssh -i /home/howard/.ssh/sonic" --ignore-existing -azvr --progress /mnt/sonic/games/ howard@192.168.1.103:/mnt/knuckles/games/
rsync -e "ssh -i /home/howard/.ssh/sonic" --ignore-existing -azvr --progress /mnt/sonic/linux/ howard@192.168.1.103:/mnt/knuckles/linux/
rsync -e "ssh -i /home/howard/.ssh/sonic" --ignore-existing -azvr --progress /mnt/sonic/live_shows/ howard@192.168.1.103:/mnt/knuckles/live_shows/
rsync -e "ssh -i /home/howard/.ssh/sonic" --ignore-existing -azvr --progress /mnt/sonic/movies/ howard@192.168.1.103:/mnt/knuckles/movies/
rsync -e "ssh -i /home/howard/.ssh/sonic" --ignore-existing -azvr --progress /mnt/sonic/music/ howard@192.168.1.103:/mnt/knuckles/music/
rsync -e "ssh -i /home/howard/.ssh/sonic" --ignore-existing -azvr --progress /mnt/sonic/photos/ howard@192.168.1.103:/mnt/knuckles/photos/
rsync -e "ssh -i /home/howard/.ssh/sonic" --ignore-existing -azvr --progress /mnt/sonic/shows/ howard@192.168.1.103:/mnt/knuckles/shows/

# Make the script executable:
chmod +x ~/scripts/sonic-send.sh



