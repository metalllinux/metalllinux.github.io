---
title: "How Copy Data Via Rsync Using A Specific Port And"
category: "storage-and-filesystems"
tags: ["storage-and-filesystems", "copy", "data", "rsync", "specific"]
---

rsync -AvPr -e "ssh -i <private_key> -p <port_here>" --progress <user>@<address>:<remote_location> <local_location>