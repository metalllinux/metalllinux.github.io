---
title: "Backreferences To Optional Expressions"
category: "learning-regular-expressions"
tags: ["learning-regular-expressions", "backreferences", "optional", "expressions"]
---

* Capturing optional expressions.
	* `/a?typical/` matches "typical" and "atypical"
	* If an optional character is inside parenthesis, zero-wdith matches are still captured.
		* `/(A?)B/` matches "AB" and captures "A"
		* `/(A?)B/` matches "B" and captures "".
		* `/(a?)typical/` matches "typical" and captures "".
* Backreference to a zero-width capture is also zero-width.
	* An example expression is `/(a?)typical & \1political/` matches "atypical & apolitical".
* Can make Group Expressions optional.
	* `/(un)?willing/` matches "willing" and "unwilling"
	* An optional group is only captured if it matches.
	* Another example is `/(A)?B/` matches "AB" and captures "A".
	* `/(A)?B/` matches "B" but captures nothing.
	* `/(un)?willing/` matches "willing" but captures nothing.
* An optional group that did not match, will not be captured. It has no backreference.
* `/(un)?willing & \1able/` matches "unwilling & unable"
	* To not match the above, we can use `/(un)?willing & \1able/` does not match "willing & able"
		* The above is true in every regex engine apart from JavaScript.
			* JavaScript's regex engine captures optional groups. Can make backreferences to them.
* Solution: capture the optional group.
	* `/((un)?)willing & \1able/` matches "unwilling & unable".
	* `/((un)?)willing & \1able/` matches "willing & able".
		* `(un)?` matches, captured by inner parenthesis, assigned to \1.
		* `(un)?` does not match, captured by outer parenthese, assigned to \1.