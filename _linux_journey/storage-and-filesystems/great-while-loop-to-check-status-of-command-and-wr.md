---
title: "Great While Loop To Check Status Of Command And Wr"
category: "storage-and-filesystems"
tags: ["storage-and-filesystems", "great", "while", "loop", "check"]
---

while true; do     echo "$(date '+TIME:%Y-%m-%d%H:%M:%S') $(kubectl get deployments -v=6)" | tee -a kubectl_get_deployments_log;     sleep 1; done