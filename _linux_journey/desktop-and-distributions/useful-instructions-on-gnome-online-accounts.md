---
title: "Useful Instructions On Gnome Online Accounts"
category: "desktop-and-distributions"
tags: ["desktop-and-distributions", "useful", "instructions", "gnome", "online"]
---

Ensure that the sssd.service is running. If not, enable it by running, as root, systemctl enable --now sssd.service and reboot.
To reproduce the error, before upgrading gnome-online-accounts :
Run this "script"/set of commands. The password, when prompted in both cases, is Secret123. Paste and run the whole "script" as one shell command. kinit -c KCM:$UID:1 employee@DEMO1.FREEIPA.ORG; klist ; kinit -l 20s -r1s -c KCM:$UID:2 employee@DEMO1.FREEIPA.ORG ; kswitch -c KCM:$UID:2 ; klist; sleep 20; klist -l
Once that set of commands finishes, in it's output, you should see that the second cache item is expired. It should look like this: employee@DEMO1.FREEIPA.ORG     KCM:1050:2 (Expired)
Check the output of top or htop to show that the sssd_kcm process is consuming a lot of CPU resources.
Perform a reboot and check the resource utilisation of the sssd_kcm process as described in the previous steps above to prove that the behaviour is consistent.
Download the attached package to the system under test.
Upgrade the gnome-online-accounts package by running the command dnf upgrade /<path/to>/gnome-online-accounts-3.28.2-7.el8.1.x86_64.rpm either as root or prefixed with sudo.
Then reboot.
This should resolve the unnecessary utilisation of CPU resources by sssd_kcm. Performing the steps under step 2 above should not result in high CPU loads.****