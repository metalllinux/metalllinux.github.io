---
title: "Add An Ssh Key To The Ssh Agent Before Pulling Rep"
category: "networking"
tags: ["networking", "add", "ssh", "key", "ssh"]
---

* These commands have to be ran in BASH
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/<private_key_here>

* Also make sure the following is added if you are pulling or downloading repositories from GitHub
```
Host github.com
  IdentityFile ~/.ssh/<private_key_here>
```
