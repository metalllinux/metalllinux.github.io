---
title: "How Add A Ssh Key Via A Config File For Use With G"
category: "networking"
tags: ["networking", "add", "ssh", "key", "config"]
---

* SSH will look for the user's ~/.ssh/config file. I have mine configured for Bitbucket as:
```
Host bitbucket.org
  AddKeysToAgent yes
  IdentityFile ~/.ssh/bitbucket_ciq
``