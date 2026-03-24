---
title: "Efficiency When Using Alternation"
category: "learning-regular-expressions"
tags: ["learning-regular-expressions", "efficiency", "when", "alternation"]
---

* Regex engines are eager and greedy.
* An example of this is `/(peanut|peanutbutter)` which only matches the "peanut"  of "peanutbutter"
	* This is because the regex engine reads from left to right.
* To rewrite this another way, we can use `/peanut(butter)?/` which then matches "peanutbutter" as a whole.
* We can also tell it to be lazy with `/peanut(butter)??/` which then matches only "peanut"
* Alternation regular expression for "abcdefghijklmnopqrstuvwxyz"
	* `/(abc|def|ghi|jkl)/`
		* If you remove the global flag, it will only match "abc"
		* Adding in `/(xyz|abc|def|ghi|jkl)/` will also only match "abc"
* `/(three|see|thee|tree)/` bounces back and forth between matching "I think those are thin trees".
* Put simplest (most efficient) expression first.
	* For example, a complicated expression like `/\w+_\d{2,4}|\d{4}_export|export_\d{2}/`
		* A better way would be `/export_\d{2}|\d{4}_export|\w+_\d{2,4}/`