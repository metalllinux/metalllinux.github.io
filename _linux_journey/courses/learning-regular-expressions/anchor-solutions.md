---
title: "Anchor Solutions"
category: "learning-regular-expressions"
tags: ["learning-regular-expressions", "anchor", "solutions"]
---

* First challenge --> how many paragraphs start with the capital letter "I" as a single word.
	* Make sure you're not using global mode.
	* Need to switch to multiline mode.
	* Word boundary is useful here.
		* `/^I\b/`
			* Need to make sure you are using the caret character, not `\A`.
* Second challenge --> How many paragraphs end with a `?`
	* Need to leave it in multiline mode and use global mode.
	* Need to use the `$` to say it is the end.
	* `\Z` would not match here, because it is not the end of a string, just the end of a line.
	* `/\?$/`
* Final challenge --> Find all words that have exactly 15 letters, including hyphenated ones. 
	* Use quantified repetition.
	* Need to use word boundaries.
	* `/\b[\w\-]{15}\b/`
	* Underscores are included by default.
	* Need to be aware of hyphens.