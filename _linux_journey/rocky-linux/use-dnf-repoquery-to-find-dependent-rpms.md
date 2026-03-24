---
title: "Use dnf repoquery to find dependent RPMs"
category: "rocky-linux"
tags: ["rocky-linux", "dnf", "repoquery", "find", "dependent"]
---

# Use dnf repoquery to find dependent RPMs

* An example is below. You need to install the RPM first for this to work:
```
dnf repoquery --whatrequires dotnet-host
```

