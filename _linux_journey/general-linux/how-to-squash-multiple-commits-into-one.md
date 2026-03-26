---
title: "How To Squash Multiple Commits Into One"
category: "general-linux"
tags: ["squash", "multiple", "commits", "into", "one"]
---

git checkout main
git pull
git log --name-status
Will look like the following:
```
[owood@localhost ciqctl]$ git log --name-status 
commit ef586d7c96e55db9aef8a084c99bad3a6ad8f776 (HEAD -> main, origin/main, origin/HEAD)
Author: Example User <user@example.com>
Date:   Thu May 2 07:41:02 2024 +0000

    Merged in ciqctl_testing (pull request #6)
    
    CUSP-357 - Add Bundle Plugin test for anaconda
    
    Approved-by: Owen Wood

M       internal/bundle/plugin/anaconda.go
A       internal/bundle/plugin/anaconda_test.go
A       test/testdata/bundle/root/anaconda-ks.cfg
```
You can use `git --squash`