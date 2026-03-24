---
title: "Alternation Metacharacters"
category: "learning-regular-expressions"
tags: ["learning-regular-expressions", "alternation", "metacharacters"]
---

* `|` means "Match previous or next expression".
* `|` is like an OR operator.
* Either match the expression on the left or the expression on the right.
* Ordered, leftmost expression gets precedence.
* Multiple choices can be daisy-chained.
* Group alternation expressions to keep them distinct.
* `/apple|orange/` matches "apple" and "orange".
* `/abc|def|ghi|jkl/` matches "abc", "def", "ghi" and "jkl".
* `/apple(juice|sauce)/` is not the same as `/applejuice|sauce/`.
* `/w(eilie)rd` matches "weird" and "wierd".
* `/(AA|BB|CC){4}/` matches "AABBAACC" and "CCCCBBBB".
* `/w(ei|ie)rd/` matchs "wierd" or "wierd"
* `/apple(juice|sauce)/` matches both "applejuice" and "applesauce"
* `(AA|BB|CC){4}` matches "AABBBBAA"