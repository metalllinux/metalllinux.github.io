---
title: "How to set up tlog on Linux hosts for terminal logging"
category: "general-linux"
tags: ["tlog", "linux", "hosts", "terminal", "logging"]
---

# How to set up tlog on Linux hosts for terminal logging 

Terminal logging may sound like a bit of an invasion of privacy, but there are a lot of reasons why you may want to know what commands your users are running. Whether it's for compliance reasons or just good system administration, sometimes you just want to know what your users are doing. If you're managing a fleet of Linux systems and need to know what the folks you've entrusted with a shell are up to, you might want to consider `tlog`. `tlog` is a terminal I/O logger that's included with RHEL and several other distributions. It logs more than just keystrokes; it also logs the output received. It can be used to literally replay a session.

In this article, I walk you through a basic `tlog` configuration and demonstrate some of the power it wields. Linux is pretty good at logging actions. It can, for example, log commands which were run via `sudo`. The **secure** log can tell you who's logged in or failed to log in, but nothing out of the box centrally logs every _action_ taken by an unprivileged user. Yes, most shells keep a history, but users can modify or even delete that if they know what they're doing. The `tlog` utility itself isn't foolproof, but an extra layer of logging can't hurt. However, it does have its limitations and concerns, which the linked Red Hat documentation below outlines. Also, `tlog` logs in JSON so that it can be parsed or even replayed later.

My goal is to show you the power of `tlog` along with [Cockpit](https://www.redhat.com/en/blog/linux-system-administration-management-console-cockpit). Cockpit, if you're not aware, is a web administration interface included with RHEL. Using Cockpit is optional, and if you'd like to use `tlog` without it, that's just fine. Simply skip over the instruction steps that include Cockpit configuration.

_**\[ You might also enjoy: [Setting up logrotate in Linux](https://www.redhat.com/sysadmin/setting-logrotate) \]**_

## Set up tlog

For this how-to, I'm using a freshly installed minimal RHEL 8.3 system. The official Red Hat Enterprise Linux 8 documentation on terminal logging can be found [here](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html-single/recording_sessions/index). To get started, all you need is a RHEL 8 system with a subscription. This process should also be nearly identical on CentOS 8. Install `tlog` and Cockpit and then enable session recording in sssd (the System Security Services Daemon). You can use `tlog` in a few other ways, but this approach lets you manage `tlog` via sssd, instead of per user.

First, install the required packages:

```
[root@gangrif-tlogtest ~]# yum install -y tlog cockpit cockpit-session-recording
```

Once the installation is complete, enable and start Cockpit:

```
[root@gangrif-tlogtest ~]# systemctl enable cockpit.socket --now
Created symlink /etc/systemd/system/sockets.target.wants/cockpit.socket → /usr/lib/systemd/system/cockpit.socket.
```

You can test Cockpit by pointing your web browser to `https://your-server's-IP:9090`. If that doesn't work, you may need to enable Cockpit in the host-based or network-based firewall. In my case, that was not necessary.

Next, add `tlog` to the sssd configuration. The sssd daemon allows many customizations to your authentication stack, including things like remote user directories. In this case, you're using it for local `tlog` integration. There are a few ways to set this up. I'm going to add `tlog` session recording to a specific group called **suspicious-users**, so any user added to that group gets logged. You can log individual users or all users if you'd like. Add the following configuration to `/etc/sssd/conf.d/sssd-session-recording.conf`. Be sure that this file is owned by **root:root**, and users/others cannot read or write the file. Sssd is picky about this for good reason.

```
[root@gangrif-tlogtest ~]# cat /etc/sssd/conf.d/sssd-session-recording.conf
[session_recording]
scope = some
groups = suspicious-users
```

If you do not, or cannot, use sssd, there is an option that manually configures `tlog` for users. The option is outlined in the previously mentioned documentation.

After placing that file, restart sssd. Now, test the configuration.

## Log user sessions

That **gangrif** user, he looks suspicious. Put him in the **suspicious-users** group that `tlog` is configured to record.

```
[root@gangrif-tlogtest tlog]# groupmems -g suspicious-users -a gangrif
[root@gangrif-tlogtest ~]# id gangrif
uid=1000(gangrif) gid=1000(gangrif) groups=1000(gangrif),10(wheel),1001(suspicious-users)
```

When you log in as **gangrif**, a nice warning banner is displayed that indicates you're being watched. This banner can be modified or removed by using the **notice** directive in `/etc/tlog/tlog-rec-session.conf`. You may be required to tell users that they're being monitored. To me, `tlog` is more powerful if you're not notifying a potential attacker that they're being monitored. Telling them what you've got in place just lets them know what to try to disable.

```
[nlager@batou-lan ~]$ ssh gangrif@10.8.109.214
gangrif@10.8.109.214's password:
Web console: https://gangrif-tlogtest.tamlab.rdu2.redhat.com:9090/ or https://10.8.109.214:9090/

Last login: Tue Dec 22 15:29:44 2020 from 10.10.116.62

ATTENTION! Your session is being recorded!

[gangrif@gangrif-tlogtest ~]$
```

## View the session in Cockpit

By default, `tlog` logs to the system journal. The easiest way to get your logged data back out is to use the Cockpit **session-logging** panel. It's actually pretty slick and well put together. You can replay a session and see what commands were entered, including typos, commands that were typed but failed, or commands that were closed by using **Ctrl+C**. If you press the **log view** button, this viewer will even show you related system logs that updated during the session. It really is a nice tool.

[![Display of Cockpit results](https://www.redhat.com/rhdc/managed-files/styles/wysiwyg_full_width/private/sysadmin/2021-01/TLOG1.png.webp?itok=zR5rckm0)](https://www.redhat.com/rhdc/managed-files/sysadmin/2021-01/TLOG1.png)

## Switch from the system journal to file logging

If you're not using Cockpit, viewing the logs gets a little more complicated, as the data you're looking for is in the system journal. In this case, I found it easiest to just switch `tlog` over to recording to a file. You could also log to syslog, which would have a similar effect and perhaps be easier to maintain. For the sake of simplicity, I'm just going to write directly to a file. I should warn you that moving `tlog` logs out of the system journal and into a file breaks the Cockpit integration.

First, create a place to store the files, and make sure it's writable by the **tlog** user. I added a directory in `/var/log` called `tlog` and set the ownership to **tlog:tlog**.

Next, in `/etc/tlog/tlog-rec-session.conf`, tell `tlog` where to store its logs. You'll find stanzas in the file for different configurations. One is labeled **File writer parameters**. This parameter allows you to define the path for the output file. The configuration for my path looked like this:

```
    // File writer parameters
    "file": {
            // The "file" writer log file path.
            "path" : "/var/log/tlog/tlog.log"
    },
```

Now tell `tlog` to use the file writer instead of the default, which is the journal. At the bottom of the config file, you'll find a line just before the closing **}** that contains a **//"writer": "journal"** setting. Change that setting to **file,** like so:

```
        // The type of "log writer" to use for logging. The writer needs
        // to be configured using its dedicated parameters.
        "writer" : "file"
}
```

The next time your target user logs in, the file `/var/log/tlog/tlog.log` should be created, and sessions logged there. You'll want to set up log rotation on this, and if you have an external logger, you should send this file there. This data is only useful if it's available when you need it. If an attacker finds it and deletes it, it won't do you any good.

## View the session with tlog-play

Once you have these logs in a file, you can have a look at them. You could use `journalctl`, but as the logs are JSON-formatted, they are not easy for humans to read. As an example, my `rm -rf` command example from above looks sort of like this:

```
{"ver":"2.2","host":"gangrif-tlogtest.tamlab.rdu2.redhat.com","rec":"2a5a7ca40dd6424e91f587c0e012e623-3cf2-1f1e2d","user":"gangrif","term":"xterm-256color","session":31,"id":1,"pos":0,"timing":"=185x50+31>61+136>1+105>1+135>1+193>1+218>1+202>4+161>4+111>1+167>1+181>1+93>1+196>1+1412>2+2>166+1897>1+251>1+208>1+159>1+73>1+110>1+90>1+73>1+119>1+285>1+504>1+143>1+136>1+961>1+175>1+144>1+865>4","in_txt":"","in_bin":[],"out_txt":"\u001b]0;gangrif@gangrif-tlogtest:~\u0007[gangrif@gangrif-tlogtest ~]$ rm rf\b\u001b[K\b\u001b[K-rf /\r\nrm: it is dangerous to operate recursively on '/'\r\nrm: use --no-preserve-root to override this failsafe\r\n\u001b]0;gangrif@gangrif-tlogtest:~\u0007[gangrif@gangrif-tlogtest ~]$ mwahahaha!!!!   \b\u001b[K","out_bin":[]}
```

The information is not easy to read, but luckily there's a tool that makes this simple. You can use `tlog-play` with the journal-recorded sessions, and it allows you to specify the recording ID to output that specific recording. When parsing a file instead, the recording ID doesn't work. All of the recordings end up in the same file, and you can't just play them all because the session IDs aren't the same. You have to split them out. You can identify the session ID you'd like to watch, and then `grep` that session ID into a new file before `tlog-play` will be happy with it. Perhaps syslog can be configured to automatically split these files as they're written.

```
[root@gangrif-tlogtest tlog]# grep 2a5a7ca40dd6424e91f587c0e012e623-3da9-1fdf38 tlog.log >> session.log
[root@gangrif-tlogtest tlog]# tlog-play -i session.log
[gangrif@gangrif-tlogtest ~]$ rm -rf /
rm: it is dangerous to operate recursively on '/'
rm: use --no-preserve-root to override this failsafe
[gangrif@gangrif-tlogtest ~]$ logout

[root@gangrif-tlogtest tlog]#
```

The session gets played out on the screen using the timing data from the JSON log. It's pretty slick. You can imagine how this might be useful while performing forensics after an outage or a compromise has been detected. You could even use `tlog` for things like recording a demo of something at the command line.

_**\[ Get this free book from Red Hat and O'Reilly - [Kubernetes Operators: Automating the Container Orchestration Platform](https://developers.redhat.com/books/kubernetes-operators?intcmp=701f20000012ngPAAQ). \]**_ 

## Wrap up

All this talk about monitoring your user's input may raise some questions. Like, do password entries get logged? What about SSH sessions that jump to another host? What about X sessions? The documentation lists X sessions as a caveat but `tlog` does not capture them. Password logging is off by default but can be enabled, if needed.

So, whether it's for compliance or just recording a slick demo of some new technology, I hope this article helps you get the job done using `tlog.`

