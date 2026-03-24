---
title: "Useful DNF Command to Exclude Packages from Being Installed"
category: "rocky-linux"
tags: ["rocky-linux", "useful", "dnf", "command", "exclude"]
---

# Useful DNF Command to Exclude Packages from Being Installed

```
dnf --disablerepo="*" --enablerepo="custom-rocky-lts-9.2.x86_64" --exclude=dotnet-host-7.* install dotnet*
```

