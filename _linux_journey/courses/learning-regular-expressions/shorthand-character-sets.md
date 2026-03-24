---
title: "Shorthand Character Sets"
category: "learning-regular-expressions"
tags: ["learning-regular-expressions", "shorthand", "character", "sets"]
---

* Saves typing.
* `\d`
	* Means digit.
	* The equivalent is `[0-9]`
* `\w`
	* Word character.
	* The equivalent is `[a-zA-Z0-9_]`
* `\s`
	* Whitespace.
	* The equivalent is `[\t\r\n]`
		* Tabs, line returns and line feed.
* The negative of each is:
* `\D`
	* Not a digit.
	* The equivalent is `[^0-9]`
* `\W`
	* Not a word character.
	* The equivalent is `[^a-zA-Z0-9]`
* `\S`
	* Not whitespace.
	* The equivalent is `[^ \t\r\n]`
* Older Unix boxes likely don't support these. All newer regex engines do support them.
* Caution:
	* `\w`
 	* The equivalent is `[a-zA-Z0-9_]`
 	* Underscore is a word character.
		* For the underscore, regex is a primary tool used for programmers and an `_` is often used in programming for variable names etc. This is why an underscore is included.
	* A hypen is not considered a word character.
* Examples: `/\d\d\d\d/` matches "1984", but not "text".
* `/\w\w\w/` matches "ABC", "123" and "1_A".
* `/\w\s\w\w/` matches "I am", but not "Am I"
* `/[\w\-]/` matches any word character or hyphen.
* `/[^\d]/` is the same as `/\D/` and `/[^0-9]/`
* Caution --> `/[^\d\s]/` is not the same as `/[\D\S]`.
	* `/[^\d\s]/` = NOT digit OR space character.
		* Find any one character that is not a digit or space.
	* `/[\D\S]/` = EITHER NOT digit OR NOT space character.
* Example `/\d\d\d\d/` matches "1984"
* Example `/\w/` matches "blue-green paint" (not the "-" or the whitespace)
	* They are not considered word characters.
	* To match the hypen as well, we use `/[\w\-]/`
* Example: `/[^\d\s]/` only matches "abc" out of "1234 5678 abc"
* Example: `/[\D\S]/` matches everything in "1234 5678 abc" including whitespaces.
* 