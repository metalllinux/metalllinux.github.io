---
title: "How Drop Multiple Collections From Mongo"
category: "general-linux"
tags: ["drop", "multiple", "collections", "mongo"]
---

```
var collectionsToDrop = ["collection1", "collection2", "collection3"]; 

  

collectionsToDrop.forEach(function(collectionName)  

{ 

  db[collectionName].drop(); 

}); 
```
