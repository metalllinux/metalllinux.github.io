---
title: "Sanoid Setup Ubuntu 24.04"
category: "project-tv-v2"
tags: ["project-tv-v2", "sanoid", "setup", "ubuntu"]
---

* Install the required packages:
```
sudo apt install -y debhelper libcapture-tiny-perl libconfig-inifiles-perl pv lzop mbuffer build-essential git
```
* Clone the repository:
```
git clone https://github.com/jimsalterjrs/sanoid.git
```
* Change into the `sanoid` directory:
```
cd sanoid
```
* Run the `ln` command:
```
ln -s packages/debian .
```
* Build the Debian package:
```
dpkg-buildpackage -uc -us
```
* Install the Debian package:
```
sudo apt install -y ../sanoid_*_all.deb
```
* Enable the `sanoid` timer:
```
sudo systemctl enable --now sanoid.timer
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
Environment=TZ=Asia/Tokyo
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
Environment=TZ=Asia/Tokyo
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
* Apply the following `/etc/sanoid/sanoid.conf` file:
```
sudo tee /etc/sanoid/sanoid.conf <<EOF
[version]
version = 2

[template_vector]

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