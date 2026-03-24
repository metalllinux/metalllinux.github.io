---
title: "Mass Remove Older Mongo Documents"
category: "general-linux"
tags: ["mass", "remove", "older", "mongo", "documents"]
---

1. mongo
2. use <db_name>
3. var count=0; db.local_model_collection.find({hd:{$lt:1672531200000}}).forEach(function(myDoc){print(count++); db.local_model_collection.remove(myDoc)})