---
title: "If Receiving Ssh Errors When Connecting Make Sure"
category: "networking"
tags: ["networking", "receiving", "ssh", "errors", "when"]
---

ssh: connect to host 192.168.3.52 port 22: Connection refused
rsync: connection unexpectedly closed (0 bytes received so far) [sender]
rsync error: unexplained error (code 255) at io.c(228) [sender=3.2.3]

sudo dnf install openssh-server

sudo systemctl enable sshd

sudo systemctl start sshd
