---
title: "make changes"
category: "editors-and-tools"
tags: ["editors-and-tools", "successfully", "send", "pull", "request"]
---

* Fork the project you want to contribute to first.
```
git config --global user.name "John Doe"
git config --global user.email johndoe@example.com
git clone <repo_here>
cd <repo>
git pull
git checkout -b whatever_my_branch_name_is
# make changes
git add .
git commit -m "Updated configuration.rst"
git push --set-upstream origin whatever_my_branch_name_is
```
* Then go onto GitHub and create a Pull Request there on the main page of the reposit