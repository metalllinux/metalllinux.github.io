---
title: "How To Send A Test Message From A Rocky Linux Serv"
category: "rocky-linux"
tags: ["rocky-linux", "send", "test", "message", "rocky"]
---

`echo "This is a test message" | s-nail -s "Test Email" user@other-rocky-linux-host.local`
* On the receiving server: `journalctl -fxu postfix`
