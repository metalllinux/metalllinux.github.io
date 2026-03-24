---
title: "Identification And Removal Of Indices"
category: "general-linux"
tags: ["identification", "removal", "indices"]
---

1. Identify the oldest index
 
$ curl -ks https://localhost:9200/_cat/indices |sort -k3 | less
 
2. Remove one or more oldest index to free up the space
 
$curl -ks -XDELETE https://localhost:9200/<index>-YYYY.MM.DD
 
e.g.:-
 
$curl -ks -XDELETE https://localhost:9200/<index>-2021.09.10