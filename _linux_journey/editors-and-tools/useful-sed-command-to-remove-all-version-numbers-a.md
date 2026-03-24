---
title: "Useful Sed Command To Remove All Version Numbers A"
category: "editors-and-tools"
tags: ["editors-and-tools", "useful", "sed", "command", "remove"]
---

```
sed 's/\([^-]*\)-[^-]*$/\1/'
```
```
\([^-]*\) captures the package name up until the first hyphen (this assumes that the package name contains no hyphens after the initial one).
-[^-]*$ matches the first hyphen followed by any characters (which we expect to be the version) until the end of the string.
\1 refers to the part of the string captured by \([^-]*\), which is just the package name, excluding the version.
```