---
title: "Grouping Metacharacters"
category: "learning-regular-expressions"
tags: ["learning-regular-expressions", "grouping", "metacharacters"]
---

* Two important metacharacters:
	* `(`
		* Start grouped expression.
	* `)`
		* End grouped expression.
* We use these to group portions of the expression, so that they can be used in different ways.
* Can apply repetition operators to the group.
* We can create a group of alternation expressions.
* Capture group for use in matching and replacing.
* An example, `/(abc)+/` matches "abc" and "abcabcabc"
* Another example is `/(in)?dependent/` matches "independent" and "dependent"
* To make a single character optional, a nice example is `/run(s)?/` is the same as `/runs?`.
	* Helps with readability and nothing wrong doing it that way.
* With `/(\d{3})-(\d{3}-\d{4})/`, we have captured two different groups.
	* This matches "555-666-7890"
		* Using `$1` grabs just "555".
		* `$2` grabs "666-7890"
			* You can then modify the number with `($1) $2` which would look like "(555) 666-7890"
* Can add parenthesis like so `/(\d{3})-(\d{3})-(\d{4})/` and you can format it like `$1.$2.$3` which would make it look like "555.666.7890"
	* Can add text as well like "Tel: 555.666.7890"
		* A `\` is sometimes used instead of a `$` for some regex engines.
	