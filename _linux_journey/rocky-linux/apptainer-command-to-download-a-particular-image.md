---
title: "Apptainer Command To Download A Particular Image"
category: "rocky-linux"
tags: ["rocky-linux", "apptainer", "command", "download", "particular"]
---

`apptainer pull --force --disable-cache oras://ghcr.io/jasonyangshadow/ubuntu:24.04`
```
Active: DefaultRemote
Remotes:
    DefaultRemote:
        URI: cloud.apptainer.org
        System: true
        Exclusive: false
    myotherremote:
        URI: enterprise2.example.com
        System: false
        Exclusive: false
Credentials:
    - URI: docker://demo.goharbor.io
      Insecure: false
    - URI: oras://ghcr.io
      Insecure: false
    - URI: oras://repository.ciq.com
      Insecure: false
```