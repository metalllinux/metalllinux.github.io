---
title: "Positive Lookahead Assertions"
category: "learning-regular-expressions"
tags: ["learning-regular-expressions", "positive", "lookahead", "assertions"]
---

* Two types --> lookahead and lookbehind.
	* Further divided into positive and negative.
* Positive Lookahead Assertion:
	* True if grouped expression is ahead of current position.
		* Tells the regex engine to pause and check the content further down the line before it proceeds.
	* Defines an additonal condition that must be met.
	* If the lookahead expression fails, the whole match fails.
* Group is not included in the match.
	* Always non-capturing groups.
* Supported by most regex engine, but not Unix tools.
	* Introduced with Perl.
* The metacharacter for this is:
	* `?=` Group is a positive lookahead assertion.
		* The `?` modifies the group.
		* The `=` makes it into a lookahead assertion.
* Example, `/sea/` matches "sea" in "seashore" and "seaside".
* Using a positive lookahead assertion, that makes it `/(?=seashore)sea/` matches "sea" in "seashore", but not "seaside".
	* Only "sea" would be matched and not seashore.
* Lookaround assertions return true/false.
* Lookaround assertions do not change the engine's position.
	* Like pressing pause on a primary match, so that a secondary match can take place.
* Lookahead assertions examine the same characters as the expression.
* Another example is `/\d{4}/` matches "2025" in "2025-01-01" and "01-01-2025"
	* Add a positive lookahead assertion:
		* `/(?=\d{4}-\d{2}-\d{2})\d{4}/`
* Matches "2025" in "2025-01-01" if the date comes first.
* Does not match "01-01-2025".
* Does not match "2025-1-1" or "2025".
* A third example is to find the right date format. We have the following values:
2025-01-01
01-01-2025
2025-1-1
2025
	* `/(?=\d{4}-\d{2}-\d{2})\d{4}/`
		* This matches the "2025" from "2025-01-01".
		* Can also reverse this before considering something a match:
			*  `/\d{4}(?=-\d{2}-\d{2})/`
* A fourth example is trying to find all words followed by punctuation, but not including the punctuation itself.
	* To find all the words, we can use `/\b[A-Za-z']+\b/`
	* To find words with punctuation that follows after them, we can use `/\b[A-Za-z']+\b[,;:.?!]/`
	* To then use a lookahead assertion, we can use `/\b[A-Za-z']+\b(?=[,;:.?!)/`
		* This finds each word and then looks ahead to see if the next character is punctuation. Then it only matches those words.
* A fifth example is `/(\b\w+\b)(?=.*\1)/` which matches any word that is ued again later in the text.
	* 