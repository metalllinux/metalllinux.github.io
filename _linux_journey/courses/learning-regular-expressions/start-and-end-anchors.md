---
title: "Start And End Anchors"
category: "learning-regular-expressions"
tags: ["learning-regular-expressions", "start", "end", "anchors"]
---

* Specify a starting or ending point that needs to be considered when searching for a pattern.
* `^`
	* Start of a string/line.
* `$`
	* End of a string/line.
* `\A`
	* Start of a string, never the end of a line.
* `\Z` End of a string, never the end of a line.
	* The `^` character also indicates a negative character set.
* Start and End Anchors.
	* Reference a position, not an actual character.
	* They are known as `Zero-width`
* Just telling you the pattern, the string and its position.
* An example is `/^apple/` or `/\Aapple/`
	* To enture it is the first word in the string, we can add the caret `^` at the beginning, to ensure it is at the front of the string.
		* If the word is somewhere else in the string, it will not match.
			* The same is true for the `\A`
* Another example is `/apple$/` or `/apple\Z/`
	* Use the `$` sign to incicate it should be at the end of a string.
		* Only finds a match, if it is the last 5 characters of that string.
		* `\Z` works in the same way.
* A third example is `/^apple$/` or `/\Aapple\Z/`
	* The regular expression should completely define the string we're looking at.
		* From the beginning to the end.
	* `^` and `$` are support in all regex engines. `\A` and `\Z` are newer however.
		* The exception to the above is JavaScript.
* PCRE --> Perl Compatible Regular Expression.
	* Many programming languages use this.
		* This supports all 4 types of regex listed above.
* `/^def/` only matches "def" out of "defabcdef", it will not match the second "def" in the string.
* `/def$/` will only match the end of string such as "defadefdef" and ignore the first "def".
* For example with `/apples\Z/` this will match the last "apples" in "apples to apples to apples"
	* Javascript will not recognise this.
* Can also define the entire string with `/\Aapples\Z/` which only matches "apples" because the entire string has been defined.
	* Literally defines it from A-Z
* The next example is `/\w+@\w+\.[a-z]{3}` which matches "someone@nowhere.com".