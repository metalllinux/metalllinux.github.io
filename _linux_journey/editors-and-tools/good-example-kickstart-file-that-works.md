---
title: "Perform a text based installation"
category: "editors-and-tools"
tags: ["editors-and-tools", "good", "example", "kickstart", "file"]
---

```
# Perform a text based installation
text
 
# Set the installation language
lang en_US.UTF-8
 
# Set the keyboard layout
keyboard us
 
# Enable the firewall
firewall --enabled
 
# Set the local timezone
timezone --utc UTC
 
# Network configuration via DHCP
network --bootproto dhcp
 
# Set the root user password
rootpw --iscrypted <encrypted_password_here>
 
# Clear the existing storage
zerombr
clearpart --all --initlabel
 
# Automatically create the default storage layout
autopart
 
# Included packages
%packages
@^minimal-environment
%end
 
# Reboot the node
reboot
````