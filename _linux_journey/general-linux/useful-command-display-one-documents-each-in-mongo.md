---
title: "Useful Command Display One Documents Each In Mongo"
category: "general-linux"
tags: ["useful", "command", "display", "one", "documents"]
---

db.<collection_name>.find({},{_id:1,"displayName":1})