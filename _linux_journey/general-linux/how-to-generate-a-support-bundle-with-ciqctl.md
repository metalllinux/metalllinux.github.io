---
title: "How To Generate A Support Bundle With Ciqctl"
category: "general-linux"
tags: ["generate", "support", "bundle", "ciqctl"]
---

```
sudo ciqctl bundle
```
* This is the same as an `sosreport`
* To then generate a report on that, we then run:
```
sudo ciqctl report -s -p <support-bundle.tar.xz>
```
* Example output of the above command:
![Screenshot 2024-04-22 at 16.59.14.png](../_resources/Screenshot%202024-04-22%20at%2016.59.14-1.png)
* To run the report without a summary, we run:
```
sudo ciqctl report -p <support-bundle.tar.xz>
```
* That then outputs the same as `xsos -a <sosreport>`