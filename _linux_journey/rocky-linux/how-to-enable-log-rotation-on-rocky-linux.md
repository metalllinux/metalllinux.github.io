---
title: "How to Enable Log Rotation on Rocky Linux"
category: "rocky-linux"
tags: ["rocky-linux", "enable", "log", "rotation", "rocky"]
---

# How to Enable Log Rotation on Rocky Linux

Create or edit this file:

```
/etc/logrotate.d/messages
```


Add the following contents to your file and edit the parameters to suit your environment (12 messages files are stored with the below settings):

```
/var/log/messages {
    weekly
    rotate 12
    compress
    delaycompress
    missingok
    notifempty
    create 0640 root root
    sharedscripts
    postrotate
        /usr/bin/systemctl kill -s HUP rsyslog.service > /dev/null 2>&1 || true
    endscript
}
```

As a test, force a log rotation:

```
sudo logrotate -f /etc/logrotate.conf
```

Check under /var/log/ and you should observe a messages file generated with a timestamp of the current date, similar to the below:

```
[myuser@rocky-linux810 ~]$ ls -lh /var/log/messages*
-rw-r-----. 1 root root 174 Jul  1 16:32 /var/log/messages
-rw-r-----. 1 root root 161 Jul  1 16:30 /var/log/messages-20250701
```
