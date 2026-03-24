---
title: "Create A New User And A Home Directory For That Us"
category: "general-linux"
tags: ["create", "new", "user", "home", "directory"]
---

```
sudo useradd -m <NAME>
```
* Add them to the `wheel` group.
```
sudo usermod -aG wheel <NAME>
```