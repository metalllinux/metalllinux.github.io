---
title: "How To Compare Commits Between Two Branches"
category: "general-linux"
tags: ["compare", "commits", "between", "two", "branches"]
---

* Clone the repo you want.
* Change into the directory.
* Check the available branches to find each branch name with `git branch -a`.
* For example, to check all of the commits that are present in `release-1.4` that do not exist in `release-1.3`, run this command:
```
git log --oneline remotes/origin/release-1.3..remotes/origin/release-1.4
```
* To find out more information about a particular commit, use the `git show` command:
```
git show <commit>
```