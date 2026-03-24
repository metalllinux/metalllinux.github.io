---
title: "Notation Conventions And Modes"
category: "learning-regular-expressions"
tags: ["learning-regular-expressions", "notation", "conventions", "modes"]
---

* Usually define a regex by placing it inside two `/`
	* `/abc/`
	* The `/` are delimiters, which tell us we are using a regex.
	* The `/` is not part of the expression, they are the delimiters that hold it.
	* Most of the time, the `/` are not used.
	* The `/` is to contrast it again the text strings that are being used to match it.
* With the above example, the characters `abc` are going to match a text string called `"abc"`
* With our javascript tool, we use those text strings without quotes.
* Expression Flags
	* Indicates different modes that are used with the regex.
	* Standard: `/re/`
	* Global: `/re/g`
		* Match this over and over again throughout the document.
		* Find all the matches and look globally.
		* If this isn't used, it will only look for the first match.
	* Case Insensitive: `/re/i`
	* Multiline: `/re/m`
		* Can our regular expression match text that stretches across more than 1 line.
		* By default, regex cannot span more than 1 line.
* `grep` gets its name from `g/re/p`
	* The global flag used to be at the beginning for regex, that's why it uses `g` at the front.
	* This stood for `Global Regular Expression Print`