---
title: "Character Ranges"
category: "learning-regular-expressions"
tags: ["learning-regular-expressions", "character", "ranges"]
---

* Example character sets -->
	* `/[0123456789]/`
		* Matches any ONE number.
	* `/[abcdefghijklmnopqrstuvwxyz]/`
		* Matches any ONE lowercase character.
	* `/[ABCDEFGHIJKLMNOPQRSTUVWXYZ]/`
		* Matches any ONE uppercase character.
* However if you wanted to match all 3 of the above, it would be a very long string.
* `-` range of characters.
	* This is a metacharacter.
* Can do it with letters, numbers and symbols.
* If a `-` is outside square brackets, it is a literal dash.
* Examples:
	* `[0-9]`
	* `[A-Za-z]`
* Caution:
	* `[50-99]` is not all numbers from 50 ~ 99.
		* It is only going to match a single character.
		* It cannot target two characters.
			* This would be the same expression as `[0-9]`
			* The regex engine will read it as a character set, which would include 5, 0-9 and 9.
			* Its not a number range, its a character range.
* If you want to match a phone number, you can repeat this 3 times:
* Example: `/[0-9][0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]/`
	* This would match "555-666-7890"
		* Works well with ID numbers, zip codes and so on.