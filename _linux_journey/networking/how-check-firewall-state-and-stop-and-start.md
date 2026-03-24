---
title: "How Check Firewall State And Stop And Start"
category: "networking"
tags: ["networking", "check", "firewall", "state", "stop"]
---

sudo firewall-cmd --state
Stop the the firewalld

Again, type:
sudo systemctl stop firewalld
Disable the FirewallD service at boot time

sudo systemctl disable firewalld
sudo systemctl mask --now firewalld