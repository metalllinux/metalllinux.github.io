---
title: "Good Instructions on Repo Metadata Package Conflicts and How to Solve Them with dnf repoclosure"
category: "rocky-linux"
tags: ["rocky-linux", "good", "instructions", "repo", "metadata"]
---

# Good Instructions on Repo Metadata Package Conflicts and How to Solve Them with dnf repoclosure

The repo metadata is off because they have packages that require each other but only removed one ie ciq-lts92-rocky-release requires ciq-rocky92-repos and they removed some(all?) versions of ciq-rocky92-repos which is causing them problems. They should be using repoclosure to make sure that if they make any edits themselves that they have done so appropriately.

# List repos you want to check 
dnf repolist

# Repoclosure check of newest versions of packages
dnf repoclosure --repo <repo_to_check> --newest
If there are dependency issues they would show in a repoclosure check. Usually multiple repositories are grouped together for repoclosure to capture all dependencies (ie BaseOS + AppStream) but since in our case the repository is meant to capture all dependencies they only need to check the one.

 
