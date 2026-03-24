---
title: "How Run Smartctl Short Tests"
category: "general-linux"
tags: ["run", "smartctl", "short", "tests"]
---

sudo smartctl -t short /dev/sdc; sleep 125; sudo smartctl -a /dev/sdc > /tmp/smart_self-test_host1.txt