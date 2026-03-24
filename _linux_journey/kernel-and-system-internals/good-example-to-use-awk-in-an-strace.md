---
title: "Good Example To Use Awk In An Strace"
category: "kernel-and-system-internals"
tags: ["kernel-and-system-internals", "good", "example", "awk", "strace"]
---

```
awk '{if ($NF ~ /<[^0][0-9]*\.[0-9]+>/) print $NF}'
<1.132353>
<21.702587>
<45.219999>
<1.073246>
<1.178245>
<1.881480>
<1.403893>
<1.139094>
<1.222343>
<1.796142>
<1.177618>
<26.971516>
<26.978402>
<1.283196>
<20.816721>
<14.124869>
```