---
title: "How To Create A New Branch In Git"
category: "editors-and-tools"
tags: ["editors-and-tools", "create", "new", "branch", "git"]
---

`git checkout -b my_branch`
`git add .`
* `git add` adds all of the local files in your directory.
`git commit -m "CUSP-357 - Add Bundle Plugin test for activemq" .`
* This then commits everything in the local directory and we provide a number and a description:
```
git-commit(1)
           Record changes to the repository.
```
`git push --set-upstream origin ciqctl_testing`
* This pushes it upstream using the name of the branch.
```
git-push(1)
           Update remote refs along with associated objects.
```
* Regarding `git push`:
```
That sets the upstream for the project. So with that branch if you run git push it'll know where to push it
```