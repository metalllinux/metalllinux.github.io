---
title: "How to analyse slow boot in RHEL-7 and later ?"
category: "rocky-linux"
tags: ["rocky-linux", "analyse", "slow", "boot", "rhel"]
---

# How to analyse slow boot in RHEL-7 and later ?

 Solution Verified - Updated June 27 2025 at 6:33 AM - English 
Environment
Red Hat Enterprise Linux 7
Red Hat Enterprise Linux 8
Red Hat Enterprise Linux 9
Red Hat Enterprise Linux 10
systemd
Issue
RHEL 7/RHEL 8/RHEL 9/ RHEL 10 is taking long time to boot. How can I find out which services are taking long time to start?
Resolution
The systemd-analyze command can be utilised to find out information about how much each service took to start. Check Diagnostics Steps for examples.
Diagnostic Steps
The systemd-analyze time provides overall information about the time taken system to start.
Raw
[root@server ~]# systemd-analyze time
Startup finished in 629ms (kernel) + 930ms (initrd) + 6.098s (userspace) = 7.658s
The systemd-analyze blame command identifies the time taken by a particular unit to start.
Raw
[root@server ~]# systemd-analyze blame
          4.048s network.service
          1.298s firewalld.service
          1.071s kdump.service
           824ms tuned.service
           592ms lvm2-pvscan@252:2.service
           555ms postfix.service
           522ms lvm2-monitor.service
           257ms boot.mount
           203ms systemd-logind.service
           125ms rhel-dmesg.service
...
At certain steps, the boot cannot proceed until all dependencies for the unit are satisfied. To view units at these critical point execute systemd-analyze critical-chain
Raw
[root@servert ~]# systemd-analyze critical-chain
The time after the unit is active or started is printed after the "@" character.
The time the unit takes to start is printed after the "+" character.

multi-user.target @6.089s
└─postfix.service @5.018s +555ms
  └─network.target @5.015s
    └─network.service @961ms +4.048s
      └─basic.target @960ms
        └─paths.target @959ms
          └─brandbot.path @959ms
            └─sysinit.target @954ms
              └─systemd-update-utmp.service @946ms +7ms
                └─auditd.service @896ms +48ms
                  └─systemd-tmpfiles-setup.service @865ms +27ms
                    └─rhel-import-state.service @816ms +45ms
                      └─local-fs.target @813ms
                        └─lvm2-monitor.service @288ms +522ms
                          └─lvm2-lvmetad.service @330ms
                            └─lvm2-lvmetad.socket @287ms
                              └─-.mount
                                └─system.slice
                                  └─-.slice
Product(s) Red Hat Enterprise LinuxComponent systemdCategory TroubleshootTags performance rhel rhel_10 rhel_7 rhel_8 rhel_9 systemd troubleshooting
This solution is part of Red Hat’s fast-track publication program, providing a huge library of solutions that Red Hat engineers have created while supporting our customers. To give you the knowledge you need the instant it becomes available, these articles may be presented in a raw and unedited form.
