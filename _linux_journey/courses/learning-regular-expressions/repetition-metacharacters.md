---
title: "Repetition Metacharacters"
category: "learning-regular-expressions"
tags: ["learning-regular-expressions", "repetition", "metacharacters"]
---

* Three metacharacters that are required to learn:
	* `*` = Preceding item , zero or more times.
	* `+` = Preceding item, one or more times
	* `?` = Preceding item, zero or one time.
* All three go after something in a regex.
* Common regex:
	* `/.+/` matches any string of characters, except a line return.
		* An example is `/Good .+\./` matches "Good morning", "Good day.", "Good evening." and "Good night."
* `/\d+/` matches "90210"
* `/\s[a-z]+ed\s/` matches lowercase words ending in "ed".
* `/\s[a-z]+ed\s/` matches lowercase words ending in "ed"
* `/apples*/` matches "apple", "apples" and "applesssssss"
* `/apples+/` matches "apples" and "applesssssss", but not "apple"
* `/apples?/` matches "apple" and "apples", but not "applesssssss"
* `/\d\d\d\d*/` matches numbers with three digits or more.
* `/\d\d\d+/` matches numbers with three digits or more.
* `/colou?r/` matches "colour" and "colour".