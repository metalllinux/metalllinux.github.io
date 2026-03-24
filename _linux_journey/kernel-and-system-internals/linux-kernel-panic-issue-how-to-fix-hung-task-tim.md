---
title: "Linux Kernel panic issue: How to fix hung_task_timeout_secs and blocked for more than 120 seconds problem"
category: "kernel-and-system-internals"
tags: ["kernel-and-system-internals", "linux", "kernel", "panic", "issue"]
---

Seems there is a resource crunch. 
# Linux Kernel panic issue: How to fix hung_task_timeout_secs and blocked for more than 120 seconds problem

September 22, 2014 

[How to](https://www.blackmoreops.com/category/how-to/), [Linux](https://www.blackmoreops.com/category/linux/), [Linux Administration](https://www.blackmoreops.com/category/linux/administration/) 

[17 Comments](https://www.blackmoreops.com/2014/09/22/linux-kernel-panic-issue-fix-hung_task_timeout_secs-blocked-120-seconds-problem/#comments)

This guide shows how to fix hung_task_timeout_secs and blocked for more than 120 seconds problem in Linux.

A panic may occur as a result of a hardware failure or a software bug in the operating system. [![How to fix hung_task_timeout_secs and blocked for more than 120 seconds problem - blackMORE Ops](../_resources/How-to-fix-hung_task_timeout_sec_f1aa538eecb042f3b.jpg)](http://www.blackmoreops.com/wp-content/uploads/2014/09/How-to-fix-hung_task_timeout_secs-and-blocked-for-more-than-120-seconds-problem-blackMORE-Ops.jpg)In many cases, the operating system is capable of continued operation after an error has occurred. However, the system is in an unstable state and rather than risking security breaches and data corruption, the operating system stops to prevent further damage and facilitate diagnosis of the error and, in usual cases, restart. After recompiling a kernel binary image from source code, a kernel panic during booting the resulting kernel is a common problem if the kernel was not correctly configured, compiled or installed.  Add-on hardware or malfunctioning RAM could also be sources of fatal kernel errors during start up, due to incompatibility with the OS or a missing device driver.  A kernel may also go into *panic()* if it is unable to locate a root file system. During the final stages of kernel userspace initialisation, a panic is typically triggered if the spawning of init fails, as the system would then be unusable.

## Background

My server became unresponsive today (around 15:38hrs)

I’ve collected following logs that shows Memory and CPU usage and narrowed down `/var/log/messages`.

After doing a hard reboot, it came back online but I was unable to access it via `VNC` or `SSH`.

`VNC` connection showed an error (many errors but all contained `/proc/sys/kernel/hung_task_timeout_secs`“)

```
INFO: task jbd2/vda3-8:250 blocked for more than 120 seconds.
 Not tainted 2.6.32-431.11.2.el6.x86_64 #1
 kernel: "echo 0 > /proc/sys/kernel/hung_task_timeout_secs" disables this message.
```

## Step by step troubleshooting data and logs

## Check Memory usage

Following log shows server memory usage

```
someuser@servercore [/var/log]# sar -r

15:00:01 kbmemfree kbmemused %memused kbbuffers kbcached kbcommit %commit
15:20:01 476604 1396772 74.56 110140 707116 1201652 30.64
15:30:02 526240 1347136 71.91 110412 710536 1165148 29.71

15:55:53 LINUX RESTART

16:00:01 kbmemfree kbmemused %memused kbbuffers kbcached kbcommit %commit
16:10:01 517168 1356208 72.39 136040 588964 1196724 30.52
16:20:01 510580 1362796 72.75 137488 596560 1191664 30.39
```

As you can see, it’s not that high and I had plenty of free Memory.

## Check CPU usage

Following log shows CPU usage.

```
someuser@servercore [/var/log]# sar -u
15:00:01 CPU %user %nice %system %iowait %steal %idle
15:20:01 all 6.01 0.04 1.74 1.59 0.14 90.48
15:30:02 all 4.97 0.04 1.54 7.87 0.15 85.44
Average: all 7.20 0.06 2.19 2.69 0.26 87.60

15:55:53 LINUX RESTART

16:00:01 CPU %user %nice %system %iowait %steal %idle
16:10:01 all 9.13 0.04 2.78 6.98 0.31 80.76
16:20:01 all 4.21 0.04 1.39 3.49 0.15 90.73
```

Again, CPU wasn’t at 100%. This is now getting annoying that I can’t explain why I am getting into s\*\*tstorm for nothing.

Let’s check /`/var/log/messages` to find all the error logs related this this kernel panic

## Check Kernel Panic Logs

Now I am getting somewhere …

```
someuser@servercore [/var/log]# grep 'Aug 22 15' messages | grep -v Firewall | grep -v blackmore | grep -v operational | grep -v ec2
Aug 22 15:38:05 servercore kernel: INFO: task jbd2/vda3-8:250 blocked for more than 120 seconds.
Aug 22 15:38:05 servercore kernel: Not tainted 2.6.32-431.11.2.el6.x86_64 #1
Aug 22 15:38:05 servercore kernel: "echo 0 > /proc/sys/kernel/hung_task_timeout_secs" disables this message.
Aug 22 15:38:05 servercore kernel: jbd2/vda3-8 D 0000000000000000 0 250 2 0x00000000
Aug 22 15:38:06 servercore kernel: "echo 0 > /proc/sys/kernel/hung_task_timeout_secs" disables this message.
Aug 22 15:38:06 servercore kernel: Call Trace:
Aug 22 15:38:06 servercore kernel: INFO: task rs:main Q:Reg:1035 blocked for more than 120 seconds.
Aug 22 15:38:06 servercore kernel: Not tainted 2.6.32-431.11.2.el6.x86_64 #1
Aug 22 15:38:06 servercore kernel: "echo 0 > /proc/sys/kernel/hung_task_timeout_secs" disables this message.
Aug 22 15:38:06 servercore kernel: rs:main Q:Reg D 0000000000000000 0 1035 1 0x00000080
Aug 22 15:38:06 servercore kernel: Call Trace:
Aug 22 15:38:06 servercore kernel: INFO: task queueprocd - qu:1793 blocked for more than 120 seconds.
Aug 22 15:38:06 servercore kernel: Not tainted 2.6.32-431.11.2.el6.x86_64 #1
Aug 22 15:38:06 servercore kernel: "echo 0 > /proc/sys/kernel/hung_task_timeout_secs" disables this message.
Aug 22 15:38:06 servercore kernel: queueprocd - D 0000000000000000 0 1793 1 0x00000080
Aug 22 15:38:06 servercore kernel: Call Trace:
Aug 22 15:38:06 servercore kernel: Not tainted 2.6.32-431.11.2.el6.x86_64 #1
Aug 22 15:38:06 servercore kernel: "echo 0 > /proc/sys/kernel/hung_task_timeout_secs" disables this message.
Aug 22 15:38:06 servercore kernel: Call Trace:
Aug 22 15:38:06 servercore kernel: INFO: task httpd:30439 blocked for more than 120 seconds.
Aug 22 15:38:06 servercore kernel: Not tainted 2.6.32-431.11.2.el6.x86_64 #1
Aug 22 15:38:07 servercore kernel: "echo 0 > /proc/sys/kernel/hung_task_timeout_secs" disables this message.
Aug 22 15:38:07 servercore kernel: httpd D 0000000000000000 0 30439 2223 0x00000080
Aug 22 15:38:07 servercore kernel: Call Trace:
Aug 22 15:38:11 servercore kernel: INFO: task httpd:30482 blocked for more than 120 seconds.
Aug 22 15:38:11 servercore kernel: Not tainted 2.6.32-431.11.2.el6.x86_64 #1
Aug 22 15:38:11 servercore kernel: "echo 0 > /proc/sys/kernel/hung_task_timeout_secs" disables this message.
Aug 22 15:38:11 servercore kernel: httpd D 0000000000000000 0 30482 2223 0x00000080
Aug 22 15:38:11 servercore kernel: Call Trace:
Aug 22 15:39:54 servercore kernel: INFO: task jbd2/vda3-8:250 blocked for more than 120 seconds.
Aug 22 15:39:54 servercore kernel: Not tainted 2.6.32-431.11.2.el6.x86_64 #1
Aug 22 15:39:54 servercore kernel: "echo 0 > /proc/sys/kernel/hung_task_timeout_secs" disables this message.
Aug 22 15:39:54 servercore kernel: jbd2/vda3-8 D 0000000000000000 0 250 2 0x00000000
Aug 22 15:39:54 servercore kernel: Call Trace:
Aug 22 15:39:54 servercore kernel: INFO: task flush-253:0:263 blocked for more than 120 seconds.
Aug 22 15:39:54 servercore kernel: Not tainted 2.6.32-431.11.2.el6.x86_64 #1
Aug 22 15:39:54 servercore kernel: "echo 0 > /proc/sys/kernel/hung_task_timeout_secs" disables this message.
Aug 22 15:39:54 servercore kernel: flush-253:0 D 0000000000000000 0 263 2 0x00000000
Aug 22 15:39:54 servercore kernel: Call Trace:
Aug 22 15:39:56 servercore kernel: INFO: task rs:main Q:Reg:1035 blocked for more than 120 seconds.
Aug 22 15:39:56 servercore kernel: Not tainted 2.6.32-431.11.2.el6.x86_64 #1
Aug 22 15:39:56 servercore kernel: "echo 0 > /proc/sys/kernel/hung_task_timeout_secs" disables this message.
Aug 22 15:39:56 servercore kernel: rs:main Q:Reg D 0000000000000000 0 1035 1 0x00000080
Aug 22 15:39:56 servercore kernel: Call Trace:
Aug 22 15:42:11 servercore kernel: Clocksource tsc unstable (delta = -8589964877 ns)

15:55:53 LINUX RESTART
```

As you can see all the errors contained “`echo 0 > /proc/sys/kernel/hung_task_timeout_secs" disables this message.`” and “`blocked for more than 120 seconds`” somewhere.

Now let’s fix this problem once and for all..

## Solution for hung_task_timeout_secs

## Explanation

By default Linux uses up to 40% of the available memory for file system caching. After this mark has been reached the file system flushes all outstanding data to disk causing all following IOs going synchronous. For flushing out this data to disk this there is a time limit of 120 seconds by default. In the case here the IO subsystem is not fast enough to flush the data withing 120 seconds. As IO subsystem responds slowly and more requests are served, System Memory gets filled up resulting in the above error, thus serving HTTP requests.

## Testing

I tested this theory with the following:  
Change `vm.dirty_ratio` and `vm.dirty_backgroud_ratio`

```
someuser@servercore [/home/someuser]$ sudo sysctl -w vm.dirty_ratio=10
someuser@servercore [/home/someuser]$ sudo sysctl -w vm.dirty_background_ratio=5
```

Commit Change

```
someuser@servercore [/home/someuser]# sudo sysctl -p
```

## Make it permanent

When the server seemed more stable and no Kernel/Swap/Memory Panic for a week, I edited `/etc/sysctl.conf` file to make these permanent after reboot.

```
someuser@servercore [/home/someuser]$ sudo vi /etc/sysctl.conf
```

ADD 2 lines at the bottom

```
vm.dirty_background_ratio = 5
vm.dirty_ratio = 10
```

Save and exit.

```
someuser@servercore [/home/someuser]$ sudo reboot
```

That’s it. I never had this issue .. ever again..

Hope someone find this info useful.

## Reference

[Ronny Egners Blog – INFO: task blocked for more than 120 seconds.](http://blog.ronnyegner-consulting.de/2011/10/13/info-task-blocked-for-more-than-120-seconds/comment-page-1/)

[Previous How to check loaded and compiled modules in Apache in Linux?](https://www.blackmoreops.com/2014/09/18/how-to-check-loaded-and-compiled-modules-in-httpd-in-linux/)

[Next Find number of unique IP’s and active connections to Web server](https://www.blackmoreops.com/2014/09/25/find-number-of-unique-ips-active-connections-to-web-server/)

<a id="check-also-close"></a>[](#)

### Check Also

<img width="260" height="138" src="../_resources/Vulnerable-docker-environment-fo_8ee07d117d3c46409.png"/>](https://www.blackmoreops.com/2021/10/14/vulnerable-docker-environment-for-learning-to-hack/)

## [Vulnerable docker environment for learning to hack](https://www.blackmoreops.com/2021/10/14/vulnerable-docker-environment-for-learning-to-hack/)

Vulhub is an open-source collection of pre-built vulnerable docker environment for learning to hack. No pre-existing knowledge of docker is required, just execute two simple commands and you have a vulnerable environment.

<img width="260" height="138" src="../_resources/Fixing-VLC-is-not-supposed-to-be_565e49572aac46a9b.jpg"/>](https://www.blackmoreops.com/2015/11/02/fixing-vlc-is-not-supposed-to-be-run-as-root-sorry-error/)

## [How to run VLC player as root in Linux? Fixing “VLC is not supposed to be run as root. Sorry” error.](https://www.blackmoreops.com/2015/11/02/fixing-vlc-is-not-supposed-to-be-run-as-root-sorry-error/)

VLC is a free and open source cross-platform multimedia player and framework that plays most …

### 17 comments

1.  <img width="65" height="65" src="../_resources/f2ae34f81eb7452e6a601cf3a0e4ae8a_d3dce72cdbf246fe9.png"/>
    
    hdaz
    
    [October 8, 2014 at 8:16 am](https://www.blackmoreops.com/2014/09/22/linux-kernel-panic-issue-fix-hung_task_timeout_secs-blocked-120-seconds-problem/#comment-1878)
    
    This can be shortened a little be interesting to see the time of this v the multiple grep’s  
    grep ‘Aug 22 15’ messages | egrep -vi “Firewall | blackmore | operational | ec2”
    
    [Reply](#comment-1878)
    
2.  <img width="65" height="65" src="../_resources/0c37033727160639b5c88309b88784fd_daaf445332164e71a.png"/>
    
    matthew
    
    [June 9, 2015 at 9:38 pm](https://www.blackmoreops.com/2014/09/22/linux-kernel-panic-issue-fix-hung_task_timeout_secs-blocked-120-seconds-problem/#comment-3856)
    
    The sysctl -p command you use in ‘testing’ to commit the changes actually causes the values in the sysctl.conf file to be read back… so it’s not committing the changes, it’s removing them!  
    It would be correct to use sysctl -p after modifying the sysctl.conf file *to make the changes permanent*, there is no need to reboot the system!
    
    [Reply](#comment-3856)
    
3.  <img width="65" height="65" src="../_resources/b0c057dfde1be4b0f13855e22dfedc3f_c85778b375c648718.png"/>
    
    [bancaldo](http://bancaldo.wordpress.com/)
    
    [October 2, 2015 at 2:28 am](https://www.blackmoreops.com/2014/09/22/linux-kernel-panic-issue-fix-hung_task_timeout_secs-blocked-120-seconds-problem/#comment-5332)
    
    the /etc/sysctl.conf trick works for me. After a week no more problems during shutdown.  
    Thank You.
    
    [Reply](#comment-5332)
    
4.  <img width="65" height="65" src="../_resources/c06bc287a1b5267f3d9e78d92237c5e7_0b4d1c4d8ba148f18.jpg"/>
    
    [Evgenii Lepikhin](https://plus.google.com/+EvgeniiLepikhin)
    
    [December 22, 2015 at 4:59 am](https://www.blackmoreops.com/2014/09/22/linux-kernel-panic-issue-fix-hung_task_timeout_secs-blocked-120-seconds-problem/#comment-5606)
    
    > > For flushing out this data to disk this there is a time limit of 120 seconds by default.
    
    This is incorrect interpretation of the error message. “… blocked for more than 120 seconds” means process didn’t leave uninterruptible sleep after this mark. This state can be caused by waiting for disk IO, by vfork() and many other cases.
    
    [Reply](#comment-5606)
    
5.  <img width="65" height="65" src="../_resources/a336852e4ee566e6e798ad4b41a9bcf9_9bbd5250e6a9480d8.png"/>
    
    matt
    
    [July 2, 2016 at 2:11 am](https://www.blackmoreops.com/2014/09/22/linux-kernel-panic-issue-fix-hung_task_timeout_secs-blocked-120-seconds-problem/#comment-6094)
    
    Thank you! This solved my issues!
    
    [Reply](#comment-6094)
    
6.  <img width="65" height="65" src="../_resources/f5d549d7e8b7b869f17f5ba5defc776d_7982851bd442405db.png"/>
    
    [Areeb Yasir](http://areebyasir.com)
    
    [July 5, 2016 at 6:14 am](https://www.blackmoreops.com/2014/09/22/linux-kernel-panic-issue-fix-hung_task_timeout_secs-blocked-120-seconds-problem/#comment-6095)
    
    Very useful information, I have found there are usually two reasons for the blocked task issue  
    #1) Disk failure or faults  
    #2) Your issue here and I have run into it myself a few times (it can be common on a LiveCD if you are doing lots of IO and makes it seems like a network or disk problem when it is really not). I will try editing the kernel parameters manually next time I run into this issue.
    
    Thanks
    
    [Reply](#comment-6095)
    
7.  <img width="65" height="65" src="../_resources/138236dc465372d3cef8147244617d0b_358789ecf5d041999.png"/>
    
    [lelivreurdecroquettes.com](http://lelivreurdecroquettes.com)
    
    [October 8, 2016 at 6:48 pm](https://www.blackmoreops.com/2014/09/22/linux-kernel-panic-issue-fix-hung_task_timeout_secs-blocked-120-seconds-problem/#comment-6576)
    
    Ⅰ love reading thrօugh a post that will mаke men and women think.  
    Aⅼsо, tһank you foг allowing me to сomment!
    
    Loading...
    
    [Reply](#comment-6576)
    
8.  <img width="65" height="65" src="../_resources/b662dd28718074b71234cdc4d2481de2_832f10f5c17043d39.png"/>
    
    Vanderson
    
    [January 14, 2017 at 12:16 am](https://www.blackmoreops.com/2014/09/22/linux-kernel-panic-issue-fix-hung_task_timeout_secs-blocked-120-seconds-problem/#comment-11091)
    
    Thank you !!!
    
    Problem solved !!
    
    Loading...
    
    [Reply](#comment-11091)
    
9.  <img width="65" height="65" src="../_resources/83742c1849b35682c58a5a72ac1e2307_ff833086e4d340e88.png"/>
    
    Arnold
    
    [April 26, 2017 at 2:22 pm](https://www.blackmoreops.com/2014/09/22/linux-kernel-panic-issue-fix-hung_task_timeout_secs-blocked-120-seconds-problem/#comment-16410)
    
    Hi, I edited the /etc/sysctl.conf. Then reboot. It says. Can’t connect to default. Skipping. Shutting down managed connections……………. How long will it take?
    
    Loading...
    
    [Reply](#comment-16410)
    
10. <img width="65" height="65" src="../_resources/1ad6ba9dad62ab13c6dd2ee27dd7c1cb_a634b244332b4a638.png"/>
    
    changtonn
    
    [May 15, 2017 at 5:09 pm](https://www.blackmoreops.com/2014/09/22/linux-kernel-panic-issue-fix-hung_task_timeout_secs-blocked-120-seconds-problem/#comment-17281)
    
    Thank you very much, it’s useful
    
    Loading...
    
    [Reply](#comment-17281)
    
11. <img width="65" height="65" src="../_resources/b969afc0c2527a31e617c859473e9c32_0f436c1d025a4c709.png"/>
    
    Haidee
    
    [May 25, 2017 at 5:56 pm](https://www.blackmoreops.com/2014/09/22/linux-kernel-panic-issue-fix-hung_task_timeout_secs-blocked-120-seconds-problem/#comment-17667)
    
    Thanks a Lot . Problem solved :)
    
    Loading...
    
    [Reply](#comment-17667)
    
12. <img width="65" height="65" src="../_resources/2da88e82639ec3f31039a57fcf3f840e_306fd4956f86412e9.png"/>
    
    [lundgren@byu.net](http://gravatar.com/ablundgren)
    
    [August 15, 2017 at 3:38 am](https://www.blackmoreops.com/2014/09/22/linux-kernel-panic-issue-fix-hung_task_timeout_secs-blocked-120-seconds-problem/#comment-18409)
    
    Thank you!!
    
    Loading...
    
    [Reply](#comment-18409)
    
13. <img width="65" height="65" src="../_resources/picture_type_large__md5_daf545f3_5bac5f23e19c42859.gif"/>
    
    [Thomas de Graaf](https://www.facebook.com/app_scoped_user_id/100000481510352/)
    
    [August 18, 2017 at 8:49 pm](https://www.blackmoreops.com/2014/09/22/linux-kernel-panic-issue-fix-hung_task_timeout_secs-blocked-120-seconds-problem/#comment-18412)
    
    Works great. Thank you!
    
    Loading...
    
    [Reply](#comment-18412)
    
14. <img width="65" height="65" src="../_resources/2309b501b9e844963c9591fd225d76cf_3e228f89c59f4dd48.png"/>
    
    [خرید سرور مجازی](https://rasanegar.com)
    
    [December 19, 2017 at 1:21 pm](https://www.blackmoreops.com/2014/09/22/linux-kernel-panic-issue-fix-hung_task_timeout_secs-blocked-120-seconds-problem/#comment-19933)
    
    it helped figuring out our problem  
    but that was related to CGI process and we managed to solve the main issue  
    Thanks
    
    Loading...
    
    [Reply](#comment-19933)
    
15. <img width="65" height="65" src="../_resources/d81a6bc173817b807c2e48dfa54b1148_11b92e9d4deb4839b.jpg"/>
    
    John Holcomb
    
    [May 18, 2019 at 7:45 am](https://www.blackmoreops.com/2014/09/22/linux-kernel-panic-issue-fix-hung_task_timeout_secs-blocked-120-seconds-problem/#comment-25316)
    
    still great post, thanks!
    
    Loading...
    
    [Reply](#comment-25316)
    
16. <img width="65" height="65" src="../_resources/316fa0e48c1b9b67cd5742e21215cc34_a8535eae33044ca7a.png"/>
    
    [xmnx](https://xamnx.blogspot.com/)
    
    [April 2, 2020 at 7:50 pm](https://www.blackmoreops.com/2014/09/22/linux-kernel-panic-issue-fix-hung_task_timeout_secs-blocked-120-seconds-problem/#comment-25505)
    
    Problem solved on my Rsyslog server in production ^^  
    Thanks!
    
    Loading...
    
    [Reply](#comment-25505)
    
17. <img width="65" height="65" src="../_resources/1b066c01bcd5a81468be8fb575568620_df898647ccd445819.png"/>
    
    Jan Dohnal
    
    [November 15, 2020 at 5:27 am](https://www.blackmoreops.com/2014/09/22/linux-kernel-panic-issue-fix-hung_task_timeout_secs-blocked-120-seconds-problem/#comment-25600)
    
    Hi, do you change sysctl configuration on Virtual machine, or on Host machine? A have same problem with Ubuntu (Libvirt and Apache virtual machine) :(
    
    Loading...
    
    [Reply](#comment-25600)
    

### Leave your solution or comment to help others.

This site uses Akismet to reduce spam. [Learn how your comment data is processed](https://akismet.com/privacy/).

#### Recent Comments

- ![](../_resources/e80f08dd01e542e7d23a945101963899_377e6c86f2a241679.jpg)
    
    [blackMORE: wow, I didn't even knew people are reading my blog. I started it off as a person...](https://www.blackmoreops.com/2014/12/13/fixing-error-package-packagename-not-available-referred-another-package-may-mean-package-missing-obsoleted-available-another-source-e-pa/#comment-29786)
- ![](../_resources/f2778475456c868e06c2d343bd97e25d_607f239633714543a.png)
    
    [df: I didn't know dpkg code bro! Thanks a lot! It works......](https://www.blackmoreops.com/2015/11/17/install-angry-ip-scanner-on-kali-linux/#comment-29749)
- ![](../_resources/4e4cd9584c1ba4c9676f110d700d02da_250576ec9ed147309.png)
    
    [Tj: load debconf preconfiguration file failed kali linux I am keep getting this erro...](https://www.blackmoreops.com/2014/04/08/detailed-guide-installing-kali-linux-on-virtualbox/#comment-29681)
- ![](../_resources/0f827731c31b932a5c147b1b181ce016_52e3bb72509047688.png)
    
    [mcdvoice: That was so helpful. Thanks for sharing with us. I appreciated what you done....](https://www.blackmoreops.com/2018/10/31/crack-a-wep-key-of-an-open-network-without-user-intervention-with-wesside-ng/#comment-29583)
- ![](../_resources/6a8cbd4b768697e627739c3b114a52fc_9cc7edd804ee484fb.png)
    
    [Foxy: Thank you so much I didn't know what to do and this fixed everything...](https://www.blackmoreops.com/2013/12/28/enable-usb-boot-in-gigabyte-motherboard/#comment-29554)

#### Recent Posts

- <img width="100" height="68" src="../_resources/00004-3236332826-110x75_4614c9a576124064a6e967c662.png"/>](https://www.blackmoreops.com/2024/11/05/wsl-ai-development-setup-guide/)
    
    ### [Complete WSL AI Development Environment Guide: CUDA, Ollama, Docker & Stable Diffusion Setup](https://www.blackmoreops.com/2024/11/05/wsl-ai-development-setup-guide/)
    
    November 5, 2024
- <img width="100" height="68" src="../_resources/Docker-NextCloud-Error-on-UNRAID_32fc4148631440178.png"/>](https://www.blackmoreops.com/2024/06/18/please-use-the-command-line-updater-because-updating-via-browser-is-disabled-in-your-config-php-error-on-nextcloud/)
    
    ### [Please use the command line updater because updating via browser is disabled in your config.php error on NextCloud](https://www.blackmoreops.com/2024/06/18/please-use-the-command-line-updater-because-updating-via-browser-is-disabled-in-your-config-php-error-on-nextcloud/)
    
    June 18, 2024
- <img width="110" height="75" src="../_resources/Identify-Hardcoded-Secrets-In-St_76e2cfa2329c42cea.png"/>](https://www.blackmoreops.com/2024/03/05/whispers-a-powerful-static-code-analysis-tool-for-credential-detection/)
    
    ### [Whispers: A Powerful Static Code Analysis Tool for Credential Detection](https://www.blackmoreops.com/2024/03/05/whispers-a-powerful-static-code-analysis-tool-for-credential-detection/)
    
    March 5, 2024
- [![Enabling AMD GPU for Hashcat on Kali Linux: A Quick Guide](../_resources/Hashcat-110x75_9b309b32ff8c4440b0fea97c7f4528d5.jpg)](https://www.blackmoreops.com/2024/03/05/enabling-amd-gpu-for-hashcat-on-kali-linux/)
    
    ### [Enabling AMD GPU for Hashcat on Kali Linux: A Quick Guide](https://www.blackmoreops.com/2024/03/05/enabling-amd-gpu-for-hashcat-on-kali-linux/)
    
    March 5, 2024
- <img width="100" height="89" src="../_resources/With-Wireshark-Or-TCPdump-You-Ca_c01466294f5a4216a.png"/>](https://www.blackmoreops.com/2024/03/05/identifying-harmful-activity-on-your-captured-traffic/)
    
    ### [Identifying harmful activity on your captured traffic](https://www.blackmoreops.com/2024/03/05/identifying-harmful-activity-on-your-captured-traffic/)
    
    March 5, 2024

#### Tags

[AMD](https://www.blackmoreops.com/tag/amd/) [Bash](https://www.blackmoreops.com/tag/bash/) [Browser](https://www.blackmoreops.com/tag/browser/) [Command Line Interface (CLI)](https://www.blackmoreops.com/tag/cli/) [Cracking](https://www.blackmoreops.com/tag/cracking/) [Display](https://www.blackmoreops.com/tag/display/) [DNS](https://www.blackmoreops.com/tag/dns/) [Docker](https://www.blackmoreops.com/tag/docker/) [encryption](https://www.blackmoreops.com/tag/encryption/) [Firewall](https://www.blackmoreops.com/tag/firewall/) [grep](https://www.blackmoreops.com/tag/grep/) [hack](https://www.blackmoreops.com/tag/hack/) [Hacking](https://www.blackmoreops.com/tag/hacking/) [Hacking Tools](https://www.blackmoreops.com/tag/hacking-tools/) [How to](https://www.blackmoreops.com/tag/how-to/) [Kali Linux](https://www.blackmoreops.com/tag/kali-linux/) [Kali Linux 2.0](https://www.blackmoreops.com/tag/kali-linux-2-0/) [Kali Linux Tools](https://www.blackmoreops.com/tag/kali-linux-tools/) [Kali Sana](https://www.blackmoreops.com/tag/kali-sana/) [Kali Tools](https://www.blackmoreops.com/tag/kali-tools/) [Linux](https://www.blackmoreops.com/tag/linux/) [Linux Administration](https://www.blackmoreops.com/tag/administration/) [Logs](https://www.blackmoreops.com/tag/logs/) [Malware](https://www.blackmoreops.com/tag/malware/) [Memory](https://www.blackmoreops.com/tag/memory/) [metasploit](https://www.blackmoreops.com/tag/metasploit-2/) [Monitor](https://www.blackmoreops.com/tag/monitor/) [Monitoring](https://www.blackmoreops.com/tag/monitoring/) [News](https://www.blackmoreops.com/tag/news/) [News Articles](https://www.blackmoreops.com/tag/news-articles/) [Others](https://www.blackmoreops.com/tag/others/) [Penetration Test](https://www.blackmoreops.com/tag/penetration-test/) [Phishing](https://www.blackmoreops.com/tag/phishing/) [PPA](https://www.blackmoreops.com/tag/ppa/) [Proxy](https://www.blackmoreops.com/tag/proxy/) [Python](https://www.blackmoreops.com/tag/python/) [rant](https://www.blackmoreops.com/tag/rant/) [Recommended](https://www.blackmoreops.com/tag/recommended/) [Security](https://www.blackmoreops.com/tag/security/) [SSD](https://www.blackmoreops.com/tag/ssd/) [SSH](https://www.blackmoreops.com/tag/ssh/) [Traffic](https://www.blackmoreops.com/tag/traffic/) [United States Computer Emergency Readiness Team](https://www.blackmoreops.com/tag/united-states-computer-emergency-readiness-team/) [US-Cert](https://www.blackmoreops.com/tag/us-cert/) [US-Cert Alerts](https://www.blackmoreops.com/tag/us-cert-alerts/)

#### Tags

[AMD](https://www.blackmoreops.com/tag/amd/) [Bash](https://www.blackmoreops.com/tag/bash/) [Browser](https://www.blackmoreops.com/tag/browser/) [Command Line Interface (CLI)](https://www.blackmoreops.com/tag/cli/) [Cracking](https://www.blackmoreops.com/tag/cracking/) [Display](https://www.blackmoreops.com/tag/display/) [DNS](https://www.blackmoreops.com/tag/dns/) [Docker](https://www.blackmoreops.com/tag/docker/) [encryption](https://www.blackmoreops.com/tag/encryption/) [Firewall](https://www.blackmoreops.com/tag/firewall/) [grep](https://www.blackmoreops.com/tag/grep/) [hack](https://www.blackmoreops.com/tag/hack/) [Hacking](https://www.blackmoreops.com/tag/hacking/) [Hacking Tools](https://www.blackmoreops.com/tag/hacking-tools/) [How to](https://www.blackmoreops.com/tag/how-to/) [Kali Linux](https://www.blackmoreops.com/tag/kali-linux/) [Kali Linux 2.0](https://www.blackmoreops.com/tag/kali-linux-2-0/) [Kali Linux Tools](https://www.blackmoreops.com/tag/kali-linux-tools/) [Kali Sana](https://www.blackmoreops.com/tag/kali-sana/) [Kali Tools](https://www.blackmoreops.com/tag/kali-tools/) [Linux](https://www.blackmoreops.com/tag/linux/) [Linux Administration](https://www.blackmoreops.com/tag/administration/) [Logs](https://www.blackmoreops.com/tag/logs/) [Malware](https://www.blackmoreops.com/tag/malware/) [Memory](https://www.blackmoreops.com/tag/memory/) [metasploit](https://www.blackmoreops.com/tag/metasploit-2/) [Monitor](https://www.blackmoreops.com/tag/monitor/) [Monitoring](https://www.blackmoreops.com/tag/monitoring/) [News](https://www.blackmoreops.com/tag/news/) [News Articles](https://www.blackmoreops.com/tag/news-articles/) [Others](https://www.blackmoreops.com/tag/others/) [Penetration Test](https://www.blackmoreops.com/tag/penetration-test/) [Phishing](https://www.blackmoreops.com/tag/phishing/) [PPA](https://www.blackmoreops.com/tag/ppa/) [Proxy](https://www.blackmoreops.com/tag/proxy/) [Python](https://www.blackmoreops.com/tag/python/) [rant](https://www.blackmoreops.com/tag/rant/) [Recommended](https://www.blackmoreops.com/tag/recommended/) [Security](https://www.blackmoreops.com/tag/security/) [SSD](https://www.blackmoreops.com/tag/ssd/) [SSH](https://www.blackmoreops.com/tag/ssh/) [Traffic](https://www.blackmoreops.com/tag/traffic/) [United States Computer Emergency Readiness Team](https://www.blackmoreops.com/tag/united-states-computer-emergency-readiness-team/) [US-Cert](https://www.blackmoreops.com/tag/us-cert/) [US-Cert Alerts](https://www.blackmoreops.com/tag/us-cert-alerts/)

#### Email Subscription

Subscribe to our email newsletter.

Enter your e-mail address

#### Categories

Categories

#### Archives

Archives

Designed by [blackMORE Ops](https://www.blackmoreops.com)

© Copyright 2025, All Rights Reserved

## Discover more from blackMORE Ops

Subscribe now to keep reading and get access to the full archive.

Type your email…

[Continue reading](#)

**Privacy Policy on Cookies Usage**

Some services used in this site uses cookies to tailor user experience or to show ads.