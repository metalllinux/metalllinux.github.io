---
title: "Upgrade all packages and restart monthly:"
category: "project-tv-v2"
tags: ["project-tv-v2", "monthly", "cron", "job", "upgrade"]
---

* Open up the `root` crontab:

```
sudo crontab -e
```

* Add the following:

```
# Upgrade all packages and restart monthly:

0 0 * * 5 [ "$(date +\%m -d tomorrow)" != "$(date +\%m)" ] && TZ=Asia/Tokyo bash -c 'apt update && apt -y upgrade && apt -y autoremove && reboot'

`
