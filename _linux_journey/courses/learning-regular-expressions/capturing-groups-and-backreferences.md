---
title: "Capturing Groups And Backreferences"
category: "learning-regular-expressions"
tags: ["learning-regular-expressions", "capturing", "groups", "backreferences"]
---

* How to use backreferences to access the captures.
* Grouped expressions are captured by default.
	* The regex engine captures it by default.
* Matched data in parenthesis is stored in memory for later use.
	* For example, we have a regex with `/a(ppl)e/` which matches "apple" and captures "ppl".
		* The actual data that was matched is stored, not the expression.
	* Another example is `/a(ppl|ngl)e/` matches "angle" and captures "ngl".
* The regex engine captures the matching text, even if you don't use it.
	* Backreferences refer to captured data.
* Backreference Metacharacters
	* `\1` Backreference to first capture.
	* `\2` Backreference to second capture.
	* `\3` Backreference to third capture.
* Most regex engines support `\1` ~ `\9`
	* Some engines support `\10` ~ `\99` (not recommended)
		* Difficult to tell the difference between a backreference of `\99` from a backreference of `\9`, followed by the regular character of `9`.
	* Some engines us `$1` through `$9` syntax instead.
* A backreference can be used in two ways:
	* Can be used inside the same expression or after the match.
* Cannot use backreferences inside character classes.
	* They are different concepts.
* A third example is `/(apples) to \1/` matches "apples to apples"
* A fourth example is `/(ab):(cd):(ef):\3:\2:\1/` matches "ab:cd:ef:ef:cd:ab".
	* Three expressions are captured.
	* Puts them in reverse order.
* A fifth example is alternation `/<(i|em)>.+?<\/\1>/` matches "<i>regex</i>" or "<em>regex</em>"
	* However `/<(i|em)>.+?<\/\1>/` does not match "<i>regex</em>"
* A sixth example is to find duplicate words with `/\b(\w+)\b\s+\1/` which will highlight "the the" in the below pattern.
Paris in the
the spring.