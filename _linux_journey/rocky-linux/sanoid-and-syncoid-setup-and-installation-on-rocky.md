---
title: "Sanoid And Syncoid Setup And Installation On Rocky"
category: "rocky-linux"
tags: ["rocky-linux", "sanoid", "syncoid", "setup", "installation"]
---

* Set up `sanoid` on every node you want to send snapshots to.
* Enable the `epel` repository:
```
sudo dnf install -y epel-release
```
* Install `git`:
```
sudo dnf install -y git
```
* Enable the `crb` repository:
```
sudo dnf config-manager --enable crb
```
* Install the `sanoid` dependency packages:
```
sudo dnf install -y perl-Config-IniFiles perl-Data-Dumper perl-Capture-Tiny perl-Getopt-Long lzop mbuffer mhash pv
```
* Clone the repository:
```
sudo git clone https://github.com/jimsalterjrs/sanoid.git
```
* Change directory into the `sanoid` directory:
```
cd sanoid
```
* Make the directory safe:
```
git config --global --add safe.directory /home/howard/sanoid
```
* Checkout the stable release:
```
sudo git checkout $(git tag | grep "^v" | tail -n 1)
```
* Install the executable binaries:
```
sudo cp sanoid syncoid findoid sleepymutex /usr/local/sbin
```
* Create the `sanoid` configuration directory:
```
sudo mkdir /etc/sanoid
```
* Add the default `sanoid` configuration:
```
sudo cp sanoid.defaults.conf /etc/sanoid
```
* Create a blank configuration file:
```
sudo touch /etc/sanoid/sanoid.conf
```
* Place an example configuration file in the directory:
```
sudo cp sanoid.conf /etc/sanoid/sanoid.example.conf
```
* Create the `sanoid` `systemd` service:
```
cat << "EOF" | sudo tee /etc/systemd/system/sanoid.service
[Unit]
Description=Snapshot ZFS Pool
Requires=zfs.target
After=zfs.target
Wants=sanoid-prune.service
Before=sanoid-prune.service
ConditionFileNotEmpty=/etc/sanoid/sanoid.conf

[Service]
Environment=TZ=UTC
Type=oneshot
ExecStart=/usr/local/sbin/sanoid --take-snapshots --verbose
EOF
```
* Create one for the `sanoid` pruning service:
```
cat << "EOF" | sudo tee /etc/systemd/system/sanoid-prune.service
[Unit]
Description=Cleanup ZFS Pool
Requires=zfs.target
After=zfs.target sanoid.service
ConditionFileNotEmpty=/etc/sanoid/sanoid.conf

[Service]
Environment=TZ=UTC
Type=oneshot
ExecStart=/usr/local/sbin/sanoid --prune-snapshots --verbose

[Install]
WantedBy=sanoid.service
EOF
```
* Generate the `systemd` timer to execute `sanoid` every 15 minutes:
```
cat << "EOF" | sudo tee /etc/systemd/system/sanoid.timer
[Unit]
Description=Run Sanoid Every 15 Minutes
Requires=sanoid.service

[Timer]
OnCalendar=*:0/15
Persistent=true

[Install]
WantedBy=timers.target
EOF
```
* Update `systemd` on new service definitions:
```
sudo systemctl daemon-reload
```
* Enable the `sanoid` `prune` service:
```
sudo systemctl enable sanoid-prune.service
```
* Enable and start the `sanoid` timer:
```
sudo systemctl enable --now sanoid.timer
```
* Generate an `ssh` key on each machine you wish to share snapshots with, including the original machine:
```
ssh-keygen -b 4096
# Create the public/private key pair under:
/home/<user>/.ssh/id_rsa
# Do not set a password.
```
* Share `ssh` keys between all machines that you want to transfer snapshots from and to:
```
ssh-copy-id <user>@<ip_address>
```
* To ensure `syncoid` can push to and pull from a remote host, allow `zfs`  to be ran without `sudo`.
* Check the binary location of `zfs`:
```
which zfs
```
* Edit the `/etc/sudoers` file:
```
sudo visudo
```
* Add the following line:
```
## Allow the zfs binary to be executed without sudo
<user> ALL=NOPASSWD: <path of zfs binary>
```
* Create a `systemd` timer to sync snapshots on the remote host from the source host:
```
sudo tee -a /etc/systemd/system/syncoid.service << EOF
[Unit]
Description=Create and send snapshots from the source host to the remote host.
After=network.target

[Service]
ExecStart=/home/howard/scripts/syncoid.sh
Type=oneshot
User=howard
EOF
```
* Make a `timer` service file for `syncoid`:
```
sudo tee -a /etc/systemd/system/syncoid.timer << EOF
[Unit]
Description=Pull from source and create snapshots every day.

[Timer]
OnCalendar=*-*-* 00:00:00

[Install]
WantedBy=timers.target
EOF
```
* Enable the `timer`:
```
sudo systemctl enable syncoid.timer
```
* Start the `timer`:
```
sudo systemctl start syncoid.timer
```
* Create a `scripts` directory:
```
mkdir ~/scripts
```
* Make a script that the `systemd` service will then run:
```
tee -a ~/scripts/syncoid.sh <<EOF
#!/bin/bash
syncoid -r howard@192.168.1.101:sonic/anime tails/anime
syncoid -r howard@192.168.1.101:sonic/bitcoin tails/bitcoin
syncoid -r howard@192.168.1.101:sonic/children_shows tails/children_shows
syncoid -r howard@192.168.1.101:sonic/dance_videos tails/dance_videos
syncoid -r howard@192.168.1.101:sonic/documents tails/documents
syncoid -r howard@192.168.1.101:sonic/ebooks tails/ebooks
syncoid -r howard@192.168.1.101:sonic/films tails/films
syncoid -r howard@192.168.1.101:sonic/games tails/games
syncoid -r howard@192.168.1.101:sonic/gaming_videos tails/gaming_videos
syncoid -r howard@192.168.1.101:sonic/isos tails/isos
syncoid -r howard@192.168.1.101:sonic/linux tails/linux
syncoid -r howard@192.168.1.101:sonic/live_shows tails/live_shows
syncoid -r howard@192.168.1.101:sonic/music tails/music
syncoid -r howard@192.168.1.101:sonic/photos tails/photos
syncoid -r howard@192.168.1.101:sonic/shows tails/shows
syncoid -r howard@192.168.1.101:sonic/skateboarding tails/skateboarding
syncoid -r howard@192.168.1.101:sonic/software tails/software
EOF
```
* Make the script executable:
```
chmod +x ~/scripts/syncoid.sh
```
* Reload the `systemd` services:
```
sudo systemctl daemon-reload
```
* Disable SELinux:
```
sudo setenforce permissive
sudo sed -i 's/SELINUX=enforcing/SELINUX=permissive/' /etc/selinux/config
```
* Install `tmux`:
```
sudo dnf install -y tmux
```
* Start a `tmux` session:
```
tmux
```
* Start the service:
```
sudo systemctl start syncoid
```
* Pull snapshots from the source. Run this on the nodes that are pulling the snapshots:
```
syncoid -r howard@192.168.1.101:sonic/linux tails/linux
```
* List all snapshots available on the node:
```
zfs list -t snapshot
zfs list -rt all
```
* Destroy a snapshot:
```
zfs destroy pool/dataset/snapshot
```
* Apply the following `/etc/sanoid/sanoid.conf` file:
```
sudo tee /etc/sanoid/sanoid.conf <<EOF
[version]
version = 2

[template_tails]

# these settings don't make sense in a template, but we use the defaults file
# as our list of allowable settings also, so they need to be present here even if
# unset.
path =
recursive =
use_template =
process_children_only =
skip_children =

# See "Sanoid script hooks" in README.md for information about scripts.
pre_snapshot_script =
post_snapshot_script =
pre_pruning_script =
pruning_script =
script_timeout = 5
no_inconsistent_snapshot =
force_post_snapshot_script =

# for snapshots shorter than one hour, the period duration must be defined
# in minutes. Because they are executed within a full hour, the selected
# value should divide 60 minutes without remainder so taken snapshots
# are apart in equal intervals. Values larger than 59 aren't practical
# as only one snapshot will be taken on each full hour in this case.
# examples:
# frequent_period = 15 -> four snapshot each hour 15 minutes apart
# frequent_period = 5 -> twelve snapshots each hour 5 minutes apart
# frequent_period = 45 -> two snapshots each hour with different time gaps
# between them: 45 minutes and 15 minutes in this case
frequent_period = 15

# If any snapshot type is set to 0, we will not take snapshots for it - and will immediately
# prune any of those type snapshots already present.
#
# Otherwise, if autoprune is set, we will prune any snapshots of that type which are older
# than (setting * periodicity) - so if daily = 90, we'll prune any dailies older than 90 days.
autoprune = yes
frequently = 0
hourly = 0
daily = 60
weekly = 0
monthly = 0
yearly = 0
# pruning can be skipped based on the used capacity of the pool
# (0: always prune, 1-100: only prune if used capacity is greater than this value)
prune_defer = 0

# We will automatically take snapshots if autosnap is on, at the desired times configured
# below (or immediately, if we don't have one since the last preferred time for that type).
#
# Note that we will not take snapshots for a given type if that type is set to 0 above,
# regardless of the autosnap setting - for example, if yearly=0 we will not take yearlies
# even if we've defined a preferred time for yearlies and autosnap is on.
autosnap = 0
# hourly - top of the hour
hourly_min = 0
# daily - at 23:59 (most people expect a daily to contain everything done DURING that day)
daily_hour = 23
daily_min = 59
# weekly -at 23:30 each Monday
weekly_wday = 1
weekly_hour = 23
weekly_min = 30
# monthly - immediately at the beginning of the month (ie 00:00 of day 1)
monthly_mday = 1
monthly_hour = 0
monthly_min = 0
# yearly - immediately at the beginning of the year (ie 00:00 on Jan 1)
yearly_mon = 1
yearly_mday = 1
yearly_hour = 0
yearly_min = 0

# monitoring plugin - define warn / crit levels for each snapshot type by age, in units of one period down
# example hourly_warn = 90 means issue WARNING if most recent hourly snapshot is not less than 90 minutes old,
# daily_crit = 36 means issue CRITICAL if most recent daily snapshot is not less than 36 hours old,
# monthly_warn = 5 means issue WARNING if most recent monthly snapshot is not less than 5 weeks old... etc.
# the following time case insensitive suffixes can also be used:
# y = years, w = weeks, d = days, h = hours, m = minutes, s = seconds
#
# monitor_dont_warn = yes will cause the monitoring service to report warnings as text, but with status OK.
# monitor_dont_crit = yes will cause the monitoring service to report criticals as text, but with status OK.
#
# setting any value to 0 will keep the monitoring service from monitoring that snapshot type on that section at all.
monitor = no
monitor_dont_warn = no
monitor_dont_crit = no
frequently_warn = 0
frequently_crit = 0
hourly_warn = 90m
hourly_crit = 360m
daily_warn = 28h
daily_crit = 32h
weekly_warn = 0
weekly_crit = 0
monthly_warn = 32d
monthly_crit = 40d
yearly_warn = 0
yearly_crit = 0

# default limits for capacity checks (if set to 0, limit will not be checked)
# for overriding these values one needs to specify them in a root pool section! ([tank]\n ...)
capacity_warn = 80
capacity_crit = 95
EOF
```
