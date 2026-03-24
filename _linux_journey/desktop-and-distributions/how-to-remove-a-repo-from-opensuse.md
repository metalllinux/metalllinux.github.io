---
title: "How To Remove A Repo From Opensuse"
category: "desktop-and-distributions"
tags: ["desktop-and-distributions", "remove", "repo", "opensuse"]
---

* Check for current repos:
```
sudo zypper repos
```
* Remove the repo:
```
sudo zypper removerepo <repository_alias_or_number>
```