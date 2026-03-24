---
title: "What Are Regular Expressions"
category: "learning-regular-expressions"
tags: ["learning-regular-expressions", "are", "regular", "expressions"]
---

* Allow to search and match parts of text.
	* They describe the patterns that identify those parts.
* They are symbols representing a text pattern.
* The plural of regex refers to `Formal language interpreted by a regular expression processor`
* Regular expressions are not a programming language.
* Used for `matching`, `searching` and `replacing` text.
* Defined set of rules that the computer understands.
* No variables.
* No instructions.
* Cannot make decisions.
* Used by programming languages.
* Sometimes you'll see it written `RegexP` at the end.
* Usage Examples:
	* Test credit card number.
	* Test email address valid format.
	* Search documents for differences in wording.
	* Replace all occurrences of "Bob", "Bobby", "B" with "Robert"
	* Count how many times "training" is preceded by "computer", "video" or "online".
	* Use regex to write a description of the desired pattern using symbols.
* For a phone number, for example `555-973-2468`, we use the following to describe that pattern in symbols:
	* `\d\d\d-\d\d\d-\d\d\d\d`
* Once the pattern is defined, the regex processor uses the description to look for matching results.
* Regex Matches:
	* Matches
	* Regex matches text if it correctly describes the text.
	* Text matches a regex is it correctly described by the expression.