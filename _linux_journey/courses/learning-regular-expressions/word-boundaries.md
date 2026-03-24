---
title: "Word Boundaries"
category: "learning-regular-expressions"
tags: ["learning-regular-expressions", "word", "boundaries"]
---

* We can anchor regular expressions to word boundaries.
* That is the start or the end of a word.
* `\b` --> Word boundary (start/end of word)
* `\B` --> Not a word boundary.
	* This one is not used regularly.
* Reference a position, not an actual character.
* Word boundary exists before the first word character.
* Before the first word character in the string.
* After the last word character in the string.
* Between a word character and a non-word character.
* Word chracters: [A-Za-z0-9_]
	* When we change from something in the above character set, to something that is not within the character set, that is a word boundary.
* An example, we have `/\b\w+\b/` which finds four matches in "This is a test."
	* There is a word boundary before the "T".
	* Boundary before the "t" and the "."
* `/\b\w+\b/` matches all of "abc_123", but only part of "top-notch".
	* Word characters do not include hyphens.
* `/\bNew\bYork\b/` does not match "New York".
	* There is a boundary after the "w" before the " ".
	* There is a second boundary after the " " before the "Y".
	* Cannot substitute a word boundary instead of a space.
* `/\bNew\b \bYork\b/` matches "New York".
	* The " " is a character.
* `/\B\w+\B/` find two matches in "This is a test." ("hi" and "es")
* `/e\b/`
	* This matches the letter "e" at the end of all words that end with "e".
* Similarly with `/\ba\b/`, this matches "a" on its own.
* Allows to make your regex more efficient and faster.
* Another example is `/\b\w+s\b/`
	* This is looking for a word that ends in "s".
	* `+` is 1 or more times.
	* The above will try to match "We picked apples."