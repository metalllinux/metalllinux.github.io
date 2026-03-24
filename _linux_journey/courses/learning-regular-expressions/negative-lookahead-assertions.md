---
title: "Negative Lookahead Assertions"
category: "learning-regular-expressions"
tags: ["learning-regular-expressions", "negative", "lookahead", "assertions"]
---

* True if a grouped expression is not ahead of the current position.
* Reject overall match if a group expression matches.
* Group is not included in the match or captured.
* Negative Lookahead Metacharacter is:
	* `?!` Group is a negative lookahead assertion.
	* `?` modifies the group.
	* `!` makes the group into a negative lookahead assertion.
* An example is `/(?!seashore)sea/` matches "sea" in "seaside" but not "seashore".
* A second example is `/\b(?!re)\w+\b/` matches words not starting in "re".
	* It matches "cycle", but not "recycle".
* A third example is `/\b\w+(?!er)\b/` matches words not ending in "er".
	* It matches "run" and "running", but not "runner".
* Not merely the opposite of positive lookahead assertions.
	* This rejects whole expressions, not just simple character matches.
	* Can find "sales tax" instead of "sales" for example .
* A fourth example is "The green frog chased the green bug in the green grass." We can use a word boundary such as `/\bgreen\b/`, which finds all the words of "green".
	* To miss out the "green" before "frog" and capture the other words, we use `/\bgreen\b(?! frog)/`, which captures the "green" before "bug" and the "green" before "grass".
		* To find only the last instance of "green", which is "green" before "grass", we can use `/\bgreen\b(?!.*green)/`
* Do not match lines that begin with a code comment indicate `#`.
	* We can do this with negative lookahead assertion, which is `/^(?!\s*#).+$/`