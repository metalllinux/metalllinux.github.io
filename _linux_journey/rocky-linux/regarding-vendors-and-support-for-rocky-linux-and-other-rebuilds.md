---
title: "Regarding Vendors and Support for Rocky Linux and Other Rebuilds"
category: "rocky-linux"
tags: ["rocky-linux", "regarding", "vendors", "support", "rocky"]
---

# Regarding Vendors and Support for Rocky Linux and Other Rebuilds

Yes.  Depends on the software in question - many vendors will say "we will only support RHEL, full stop.  No Rocky, Alma, Oracle or whatever-else."
Was a common thing in the heyday of CentOS, and is still a common thing

Some even have installers that will do things like check /etc/redhat-release or /etc/os-release.  If it's found that it's not RHEL, it will simply refuse to install.

Linux administrators everywhere, including myself, have "made it work no matter what" in the past by editing /etc/os-release or whatever to make Rocky/CentOS/etc. look like RHEL to the installer program.
It's not recommended in a production environment, but it does happen :upside_down_face: .  Often times "tricking" the installer is enough to get the thing set up, and afterwards it runs just as it would on RHEL.
