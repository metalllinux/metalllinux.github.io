---
title: "wwctl container shell rockylinux-9"
category: "rocky-linux"
tags: ["rocky-linux", "timezone", "container", "change"]
---

    not sure if the dates on the nodes are okay, they all read GMT, not PDT (like the warewulf server).  Is this an issue?  Do we fix that in the container?

 
You definitely can set the timezone in the container. You can't use timedatectl, because that requires systemd to be running (which isn't in a wwctl container shell session). But you can just set the appropriate symlink. For example, here's how you could set the system timezone to Denver time (where I live):
 

# wwctl container shell rockylinux-9
Container image is rebuilt depending on the exit status of the last command.

Run "true" or "false" to enforce or abort image rebuild.
[rockylinux-9|write] Warewulf> ln -sf /usr/share/zoneinfo/America/Denver /etc/localtime

 
You could also do this with an overlay.
 

# wwctl overlay create tz-denver
# mkdir -p /var/lib/warewulf/overlays/tz-denver/rootfs/etc
# ln -s /usr/share/zoneinfo/America/Denver /var/lib/warewulf/overlays/tz-denver/rootfs/etc/localtime

 
Just add that tz-denver overlay (or whatever you'd call yours on your side) to a node to configure it for that timezone.
 
We're actually working on making this a bit easier for Warewulf v4.6.0 right now: https://github.com/warewulf/warewulf/pull/1303
 
Next question:
 

    isn't there a way to change the overlays for wwinit to set the dns servers? 

 
Absolutely! As of Warewulf v4.5.0 you can set "network tags" on your network interfaces to configure DNS. Any tag that starts with DNS will work; though DNS1, DNS2, etc. is typical. (This behaviour is implemented by the generic overlay in v4.5.x.)
 

# wwctl node set --nettagadd="DNS1=1.1.1.1,DNS2=1.0.0.1" wwnode1

 
These tags direct your network configuration system (e.g., NetworkManager) to use these DNS resolvers. Later Warewulf v4.5.x releases also configure /etc/resolv.conf manually; but that file is best treated as dynmaic in most cases now. In v4.6.0 this will be easier to customise.)
 
For both of these suggestions, don't forget to rebuild your container image and/or overlays as necessary.
 
I hope this information is useful to you. Like I said, let us know if you need any further assistance with Warewulf. As for the rest of this case, I'll leave that to our engineer and the rest of the CSX team.