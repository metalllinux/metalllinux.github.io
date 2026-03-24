---
title: "Negative Character Sets"
category: "learning-regular-expressions"
tags: ["learning-regular-expressions", "negative", "character", "sets"]
---

* `^`
	* This is the negative metacharacter.
		* Carrot symbol or upper pointing arrow.
* The character set is not any one of several characters.
* You add the `^` as the first character inside the set.
* `[/^aeiou]/` matches any one constant (non-vowel).
* Another example is `/see[^mn]/` would match "seek" and "sees", but not "seem" or "seen".
	* Does not match "see", since there is nothing after it.
	* It would match "see." and "see ", since the full stop and space are still considered characters.
* Also works with ranges as well, for example `[^a-zA-Z]`
	* This negates the entire character set.
	* 