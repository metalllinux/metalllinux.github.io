---
title: "Greedy Expressions"
category: "learning-regular-expressions"
tags: ["learning-regular-expressions", "greedy", "expressions"]
---

* This is a principle. Need to understand how regex engines make that choice.
* For example: `/\d+\w+\d+/`
	* To apply to a filename such as `01_FY_07_report_99.xls`
	* The regex engine could decide to return "01_FY_07"
	* Or "01_FY_07_report_99"
	* Which would should the regex engine return?
* Another example is `/".+", ".+"/`
	* It will run through "Milton", "Waddams", "Initech, Inc."
	* It could find "Milton", "Waddams"
	* It could find "Milton", "Waddams", "Initech, Inc."
* For the above problems, we need to know how the regex engine deals with them.
* Standard repetition quantifiers are greedy.
	* By "greedy", the expression tries to match the longest possible string.
	* Defers to achieving overall match.
		* For example `/.+\jpg/` matches "filename.jpg"
		* The + is greedy, but "gives back" the ".jpg" to make the match.
* Greedy gives back as little as possible.
* Another example `/.*[0-9]+/` matches "Page 266".
	* The `.*` portion matches "Page 26".
	* `[0-9]+` portion matches only "6".
* It matches as much as possible before giving control to the next expression part.
* Regex engines are eager.
	* Want to match as quickly as possible.
* Regex engines are greedy.
* 