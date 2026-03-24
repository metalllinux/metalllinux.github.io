---
title: "Use the MTR Tool to Report Network Latency"
category: "networking"
tags: ["networking", "mtr", "tool", "report", "network"]
---

# Use the MTR Tool to Report Network Latency

* Example:

```
mtr --report --report-cycles 100 git.savannah.gnu.org
Start: 2025-08-26T08:56:08+0900
HOST: ciq-rocky-linux10           Loss%   Snt   Last   Avg  Best  Wrst StDev
  1.|-- 2400:2411:ea20:5000:f2f8:  0.0%   100    2.5   2.6   2.1   5.0   0.4
  2.|-- 2400:2411:ea20:5000::fffe  0.0%   100    4.0   4.0   3.2   5.2   0.4
  3.|-- ???                       100.0   100    0.0   0.0   0.0   0.0   0.0
  4.|-- ???                       100.0   100    0.0   0.0   0.0   0.0   0.0
  5.|-- 2400:2000:bb1a:2404::1     0.0%   100   13.7  18.8   8.0  51.2   7.9
  6.|-- 2400:2000:2:0:1a::39       0.0%   100   20.6   9.4   7.6  21.1   2.8
  7.|-- ???                       100.0   100    0.0   0.0   0.0   0.0   0.0
  8.|-- ???                       100.0   100    0.0   0.0   0.0   0.0   0.0
  9.|-- ???                       100.0   100    0.0   0.0   0.0   0.0   0.0
 10.|-- ???                       100.0   100    0.0   0.0   0.0   0.0   0.0
 11.|-- ???                       100.0   100    0.0   0.0   0.0   0.0   0.0
 12.|-- 2001:504:47::59cd:0:1      1.0%   100  176.7 171.5 154.5 255.8  12.1
 13.|-- vcs2.savannah.gnu.org     11.0%   100  325.7 211.9 188.6 325.7  14.3
```

