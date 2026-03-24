---
title: "How To Add Text At A Certain Line Number With Sed"
category: "editors-and-tools"
tags: ["editors-and-tools", "add", "text", "certain", "line"]
---

ansible <server_group> -i <path_to_inventory_file> -a order=sorted -f 1 -m shell --args="sed -i '10i <TEXT>' <file>"