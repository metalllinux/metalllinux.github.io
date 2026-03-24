---
title: "Systemd Timer For Syncoid Pype.Dev"
category: "storage-and-filesystems"
tags: ["storage-and-filesystems", "systemd", "timer", "syncoid", "pypedev"]
---

- ## [Pype.dev](https://pype.dev/./)
    
    my mental data-lake
    

- [Archive](https://pype.dev/./archive.html)
- [Tags](https://pype.dev/./tags.html)
- [Github](https://github.com/pypeaday/pype.dev)
- ☼
- <a id="search-toggle"></a>[](# "Search (Ctrl + Shift + F)")

# Systemd timer for syncoid

Dec 21, 2022 - ⧖ 1 min

I have a bash script called `syncoid-job` which boils down to a barebones -

```
#!/bin/bash

syncoid --no-sync-snap --sendoptions=w --no-privilege-elevation $SYNOIC_USER@$SERVER:tank/encrypted/nas tank/encrypted/nas
```

I want to run this script hourly but as my user (notice the no-privilege-elevation flag)

First - create a systemd unit file at `/etc/systemd/system/syncoid-replication.service`

```
[Unit]
Description=ZFS Replication With Syncoid

[Service]
Type=oneshot
ExecStart=/$HOME/dotfiles/syncoid-job
User=$USER
Group=$GROUP

[Install]
WantedBy=multi-user.target
```

Then we save the unit file, enable the service, and then start it

```
systemctl enable syncoid-replication.service
systemctl start syncoid-replication.service
```

> Note this will run that script... so be ready for syncoid to do its thing

Now for the timer... We create `/etc/systemd/system/syncoid-replication.timer`

```
[Unit]
Description=Run syncoid-replication every hour

[Timer]
OnCalendar=hourly

[Install]
WantedBy=timers.target
```

Hit it with a `systemctl enable syncoid-replication.timer` and you're in business!

-  <img width="40" height="40" src="../_resources/pypeaday_b212de18eac8484f8092be29120808c6.png"/> Nicholas Payne](https://pype.dev/author-nicpayne.html)

Dec 21, 2022 - ⧖ 1 min

- [zfs](https://pype.dev/./tag-zfs.html)
- [homelab](https://pype.dev/./tag-homelab.html)
- [tech](https://pype.dev/./tag-tech.html)

Related zfs content

- [D and uninterruptable sleep](https://pype.dev/./d-and-uninterruptable-sleep.html)
- [lsof to find what's using your filesystem](https://pype.dev/./lsof-to-find-what-s-using-your-filesystem.html)
- [Changing ZFS key for child datasets of encrypted dataset after migration](https://pype.dev/./changing-zfs-key-for-child-datasets-of-encrypted-dataset-after-migration.html)
- [Limit zfs list to avoid docker vomit](https://pype.dev/./limit-zfs-list-to-avoid-docker-vomit.html)

Powered by [Marmite](https://github.com/rochacbruno/marmite) | [CC-BY_NC-SA](https://creativecommons.org/licences/by-nc-sa/4.0/)