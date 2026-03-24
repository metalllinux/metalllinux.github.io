---
title: "How Restart Multiple Services At Once With Ansible"
category: "automation-and-configuration"
tags: ["automation-and-configuration", "restart", "multiple", "services", "once"]
---

ansible all -i <inventory_file> -m shell -a 'sudo systemctl restart elasticsearch-{a..f}'