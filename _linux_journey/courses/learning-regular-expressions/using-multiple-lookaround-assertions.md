---
title: "Using Multiple Lookaround Assertions"
category: "learning-regular-expressions"
tags: ["learning-regular-expressions", "multiple", "lookaround", "assertions"]
---

* `/\b(?=\w{6,})sea(?!shore)\w+\b/`
	* Contains multiple lookaround assertions.
* Matches words starting with "sea".
* Asserts 6 or more characters.
* Asserts not "seashore".
* A second example: "Find film titles with three or more words where every word is capitalised".
	* `/^(?=(\b\w+ ){2,})(?!.+\s[a-z]).+$/`
	* Matches "Cool Hand Luke"
	* Does not match "Forrest Gump" or "Chariots of Fire"
		* Because of lowercase.
* Match using bookends.
	* `(?<=["']).+(?=["'])/` matches characters inside quotes.
* `/(?<=<em>).+(?=<\/em>)/` matches characters inside HTML em-tags.
* `/(?<=[a-z])(?=[A-Z])/` matches zero-width position before a camel-case letter in "QuickTime" (useful for find-replace)
* Multiple assertions impact performance.
	* Multiple layers of regular expressions to check.
	* Use anchors (especially at the start) to reduce searching.
	* Put simplest/fastest assertions first.
* Example: Password Validation.
	* Passwords must be 10 or characters long.
	* Password must include uppercase letter, lowercase letter, number and symbol.
* `/\A[A-Za-z]{10,}\Z/` matches "secretword" and "SECRETWORD".
	* allow either of the characters to match.
* Another version is `/\A(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*]).{10,}\Z/`
	* If the string has an uppercase letter, lowercaes letter or a digit.
* Text Containing Two Words:
	* `/^(?=.*\bgive\b)(?=.*\btake\b).+$/`
		* Matches the whole string if the words "give" and "take" both exist somewhere in the string, in any order.
			* Can anchor to search whole text, paragraph or a line.
* Add Commas to Numbers
	* `/(\d{1,3})(?=(\d{3})+(?!\d))/`
		* Matches numbers 1~3.
		* Matches 1~3 digits when followed by digits evenly divisible by 3.
		* Find and replace with "\1,"
			* 1234567.89 becomes 1,234,567.89