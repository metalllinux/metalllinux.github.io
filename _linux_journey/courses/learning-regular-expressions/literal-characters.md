---
title: "Literal Characters"
category: "learning-regular-expressions"
tags: ["learning-regular-expressions", "literal", "characters"]
---

* Simple matches.
* Literal characters (a character of `A` in a regex, matches the same `A` character in a string).
* `/car/` matches "car".
* `/car/` also matches the first 3 letters of "carnival".
* Searches are case-sensitive by default.
* Can go to flags and set `case insensitive` to match
* Spaces are characters as well, so `/car/` does not match "c a r"
* Standard (non-global) matching.
	* The earliest (leftmost) match is always preferred.
	* Reads the string from left to right. --> `/zz/` only matches the first set of `zz` in "pizzazz".
* Global Matching
	* Finds all the matches throughout the text.
	* All of the `zz` in "pizzazz" would be matched.
* 