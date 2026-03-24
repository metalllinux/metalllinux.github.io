---
title: "Regarding Dnf And Priority In Repositories"
category: "rocky-linux"
tags: ["rocky-linux", "regarding", "dnf", "priority", "repositories"]
---

In DNF, the priority mechanism determines which repository's packages are preferred when multiple repositories provide the same package. The repository with the lower priority value is given preference. Therefore, in your case, the repository with a priority of 20 will have its packages prioritised over the repository with a priority of 50 when you run dnf update