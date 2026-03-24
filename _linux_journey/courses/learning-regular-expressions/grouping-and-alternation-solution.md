---
title: "Grouping And Alternation Solution"
category: "learning-regular-expressions"
tags: ["learning-regular-expressions", "grouping", "alternation", "solution"]
---

* Challenge 1: Write a complex regex that matches "myself", "yourself" and "thyself" .
	* You can do this with `/(my|your|thy)self/`.
	* The above uses Alternation.
* Challenge 2: Write the same regex for "good", "goodness" and "goods".
	* `/good(ness|s)?/`
		* The `?` is used to match 0 or more times.
		* The `|s` also matches "goods".
		* Can mix alternation with repetion operators.
* Final Challenege 3: A regex which matches "do" or "does", then followed by "no", "not" or "nothing".
	* `[Dd]` makes sure it matches at the beginning of a sentence.
	* A longer match is preferred first by the regex engine.
		* `/[Dd]o(es)? (nothing|not|no)/`