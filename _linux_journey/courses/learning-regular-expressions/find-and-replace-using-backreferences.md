---
title: "Find And Replace Using Backreferences"
category: "learning-regular-expressions"
tags: ["learning-regular-expressions", "find", "replace", "backreferences"]
---

* Captures can be available outside of regular expressions.
* This is found in programming languages, code editors.
* Backreferences can be used in find-and-replace operations.
	* An example is "I love hot coffee."
		* Find: `/(love) hot/`
		* Replace: `*\1*`
		* Use a backreference to find the first capture.
	* Another example is a list of names like so:
Stephen King
Margaret Atwood
Douglas Adams
* We have the above list and we want to reverse each one, so that the format is: last name, first name.
	* Find: `/^(.+) (.+)$/` Replace: `\2, \1`
	* Then it shows the following:
King, Stephen
Atwood, Margaret
Adams, Douglas
* Can create regular expression.
* Test against sample data.
* Add capturing groups
* Write replacement strings using backreferences (\1 or $1)
* Include anything not captured that should be retained.
* `/^.+ .+$/`
	* Simple wildcard repeat regex that matches all of the above names.
* `/^(.+) (.+)$/`
	* Same, but captured within parenthesis.
* Can then press the `Replace` but in regexr and to get the above result, can do `\2, \1`. It then displays the results as:
King, Stephen
Atwood, Margaret
Adams, Douglas
* To match either one of the following:
self-reliance
reliance
	* We can do alternation to match both of them.
	* We can do `/(self-)?reliance/` or `/((self-)?reliance)/`
		* When replacing, you can put asterixs around it like so `*\1*` which adds asterisks around the search terms. 
		* Can replace with HTML, for example `<strong>$1</strong>` ($1 or \1 depending on the regex editor you use).
		
	
	