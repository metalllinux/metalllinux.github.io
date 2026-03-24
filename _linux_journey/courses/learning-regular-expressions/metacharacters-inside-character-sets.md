---
title: "Metacharacters Inside Character Sets"
category: "learning-regular-expressions"
tags: ["learning-regular-expressions", "metacharacters", "inside", "character", "sets"]
---

* Most metacharacters inside character sets are already escaped.
* No need to escape them again.
* An example of this is `/h[a.]t/` which matches "hat" and "h.t", but not "hot".
	* The dot is a literal full stop.
* Exception characters are `] - ^ \`
	* `]` is the end of a character set.
	* `-` is for character ranges.
	* `^` carrot is for negative character sets.
		* If you want to use the literal versions of these characters, need to escape them with `\`
* Example `/var[[(][0-9][\])]/`
	* This has a delimited with a number inside.
		* In the above example, the `\]` had to be escaped.
* Another example is `/file[0\-\\_]1/`
* Another example is `/2013[-/]10[-/]05/`
* Another example `/h[a.]t/`
	* This matches "hat ", "h.t", but not "hot"
* Another example is `/var[([][0-9][\])]/` which parses:
	* "var(3)" "var[4]"
* Another example: `/file[0\-\\_]1/`
	* Matches the following: "file01", "file-1", "file\1" and "file_1"