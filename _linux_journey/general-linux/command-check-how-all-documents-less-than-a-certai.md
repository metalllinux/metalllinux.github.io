---
title: "Command Check How All Documents Less Than A Certai"
category: "general-linux"
tags: ["command", "check", "all", "documents", "less"]
---

mongo --quiet <db> --eval '<collection>.count({<field>:{$lt:1672531200000}})'