---
title: "How Output Json File From Mongo Db"
category: "general-linux"
tags: ["output", "json", "file", "mongo"]
---

mongo --quiet <db> --eval 'db.<collection>.find({$and:[{"<field>":"<value>"},{"field":"<value>"}]}).forEach(printjson)'