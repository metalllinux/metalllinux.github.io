---
title: "My Mongo Commands And Check Alerts"
category: "general-linux"
tags: ["mongo", "commands", "check", "alerts"]
---

Checks in Local Model DB:

mongo local_model_db --eval 'db.local_model_collection.find({ m: { $regex: "MODEL_NAME" } }).pretty().toArray()

mongo triggered_rule_db --eval 'db.triggered_rules_20230727_collection.find({ src_asset: { $regex: /DFTSVC/i } }).pretty().toArray()''