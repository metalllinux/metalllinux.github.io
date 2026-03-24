---
title: "How to use tlog to record and playback recorded user sessions?"
category: "rocky-linux"
tags: ["rocky-linux", "tlog", "record", "playback", "recorded"]
---

# How to use tlog to record and playback recorded user sessions? 

[Skip to navigation](https://access.redhat.com/solutions/3902881#pfe-navigation) [Skip to main content](https://access.redhat.com/solutions/3902881#cp-main)

### Utilities

-   [Subscriptions](https://access.redhat.com/management/)
-   [Downloads](https://access.redhat.com/downloads/)
-   [Red Hat Console](https://console.redhat.com/)
-   [Get Support](https://access.redhat.com/support/)

[![Red Hat Customer Portal](https://access.redhat.com/chrome_themes/nimbus/img/red-hat-customer-portal.svg)](https://access.redhat.com/)

## Environment

-   Red Hat Enterprise Linux 8

## Issue

-   How to install and use the `tlog` to record user sessions and check the recorded session?

## Resolution

-   Install the required packages:

```
# yum install tlog
Updating Subscription Management repositories.
Updating Subscription Management repositories.
Last metadata expiration check: 0:12:43 ago on Mon 11 Feb 2019 01:14:29 AM EST.
Dependencies resolved.
===================================================================================================================
 Package                                 Arch                                      Version                                      Repository                                                                Size
===================================================================================================================
Installing:
 tlog                                    x86_64                                    5-1.el8                                      rhel-8-for-x86_64-appstream-beta-rpms                                    117 k

Transaction Summary
===================================================================================================================
Install  1 Package

Total download size: 117 k
Installed size: 290 k
Is this ok [y/N]: y
Downloading Packages:
tlog-5-1.el8.x86_64.rpm         41 kB/s | 117 kB     00:02    
-------------------------------------------------------------------------------------------------------------------
Total                                               41 kB/s | 117 kB     00:02    
Running transaction check
Transaction check succeeded.
Running transaction test
Transaction test succeeded.
Running transaction
  Preparing        :                                                                          1/1
Installed: tlog-5-1.el8.x86_64
  Running scriptlet: tlog-5-1.el8.x86_64                                                      1/1
  Installing       : tlog-5-1.el8.x86_64                                                      1/1
  Running scriptlet: tlog-5-1.el8.x86_64                                                      1/1
Installed: tlog-5-1.el8.x86_64
  Verifying        : tlog-5-1.el8.x86_64                                                      1/1

Installed:
  tlog-5-1.el8.x86_64                                                                                                                                                                                          

Complete!
```

-   Start recording for the session with the command:

```
# tlog-rec --file-path=/var/log/tlog.log
```

-   perform some tasks to be recorded.
-   Playback the recorded session from the CLI:

```
# tlog-play --file-path=/var/log/tlog.log
```
