---
title: "The Wildcard Metacharacter"
category: "learning-regular-expressions"
tags: ["learning-regular-expressions", "wildcard", "metacharacter"]
---

* `.`
	* Any character except newline.
* `/h.t` matches "hat", "hot" and "hit", but not "heat"
* The wildcard is only a single character.
* Broadest match possible.
* Most common metacharacter.
* Most common mistake.
* `/9.00/` matches "9.00", "9500" and "9-00"
* A good regular expression should match the text you want to target and ONLY that text, nothing more.
* Don't want any false positives.
* Each symbol represents only 1 character in the string.
* `/g.d` matches "g d" (spaces are matched as well).
* It even matches other symbols like `#`
* A line break is also considered a character. However, it does not match.
* `/.a.a.a/` will match "banana", "papaya"
	* The above example is identifying common traits.