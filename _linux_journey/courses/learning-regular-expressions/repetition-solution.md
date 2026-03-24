---
title: "Repetition Solution"
category: "learning-regular-expressions"
tags: ["learning-regular-expressions", "repetition", "solution"]
---

* First challenge was to match "self", "himself", "myself", "thyself", "herself" etc
	* Can use `/\w+\*self/`
		* Need to use the `*`, so that "self" is included as well (zero or more times).
* Second challenge was to match "virtue" and "virtues" to `virtue[s]?`
	* The `?` can represent 0 or 1 time as well.
* Next task was to find a work that starts with a capital T and has 12 characters.
	* `/T\w{11}` because we already have one character at the start as "T".
* Last task is to find everything that is inside quotation marks. But to ignore anything that is not within quotes.
	* Need at least 1 character inside them.
		* Something like `/"(.|\n)+?"/`
			* This shows only the phrases within quotes and also returns text between quotes that has line returns as well.