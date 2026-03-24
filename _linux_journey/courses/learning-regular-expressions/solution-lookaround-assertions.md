---
title: "Solution Lookaround Assertions"
category: "learning-regular-expressions"
tags: ["learning-regular-expressions", "solution", "lookaround", "assertions"]
---

* Match the line for every U.S. President: 46
	* `/^\d{1,2},.+,\d{4},(?:\d{4})?,.+,.+,.+$/gm`
* Whose home state was not Virginia or Massachusetts: 37
	* `...,(?!Virginia|Massachusetts).+,...`
* Whose last name is longer than 7 characters: 15
	* `[A-Za-z.\s]+? \s [A-Za-z\s]+,` 
		* First expressions says to use any letter.
			* Any period or space repeated lazily, not greedy.
				* The space comes after that.
	* `...,[A-Za-z.\s]+?\s[A-Za-z\s]{8,},`
	* Can also be a positive lookahead assertion as well:
		* `...,(?=[A-Za-z.\s]+?\s[A-Za-z\s]{8,},).+,`
* Whose name dose not include a middle initial: 29
	* `...,[A-Za-z\s]+,...`
	* `...,[^.]+,...`
		* The above would look like `...,(?=[^.]+,).+,...`
* Whose term in office began on or after 1900: 21
	* `...,(?=19|20)\d{4},...`
	* `...,(?:19|20)\d{2},...`
	* Should be only 1 president whom meets all the above requirements.
* `/^.+$/` matches each line from beginning to end.
* You can then put all of the above requirements together into one string.
* The above would match the following string only:
"26,Theodore Roosevelt,1901,1909,Republican,New York, https://en.wikipedia.org/wiki/Theodore_Roosevelt"
* Don't get frustrated if your regex don't work out at the start.
