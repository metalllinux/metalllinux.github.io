---
title: "How to Remove a Submitted PR and then Split the Commits Into Two Separate PRs with Git"
category: "editors-and-tools"
tags: ["editors-and-tools", "remove", "submitted", "then", "split"]
---

# How to Remove a Submitted PR and then Split the Commits Into Two Separate PRs with Git

* Delete the PR online.

* Then in your local repository:

```
git fetch upstream
```

```
git checkout main
```

* Check the upstream remotes:

```
git remote -v
```

* Take the output from the above `git remote -v` command and use `git remote add` like so:

```
git remote add upstream https://github.com/rocky-linux/documentation.git
```

* Run `git reset`:

```
git reset --hard upstream/main
```

* Create a separate branch for the first PR, specifying a unique branch name and the commit that was included in the original PR. An example is below:

```
git checkout -b packer-kickstart-url upstream/main
git cherry-pick 5b5f141
git push -u origin packer-kickstart-url
```

* Do the same thing for the second PR branch:

```
git checkout -b iso-creation-kickstart-link upstream/main
git cherry-pick e19099b
git push -u origin iso-creation-kickstart-link
```

* Then create a PR for each branch.
