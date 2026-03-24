---
title: "Define A Character Set"
category: "learning-regular-expressions"
tags: ["learning-regular-expressions", "define", "character"]
---

* `[`
	* Begin a character set.
* `]`
	* End a a character set.
* Any one of several characters will match.
* Willy only match 1 character.
* Order of the characters does not matter.
* `/aeiou/`
	* Matches any ONE vowel.
* `/gr[ea]y/`
	* matches "grey" and "grey".
* `/gr[ea]t/`
	* does NOT match "great".
		* Does not have the same meaning.
		* "grat" and "gret" would match, because it is a SINGLE character, not two characters.
* `/[AEIOUaeiou]`
	* Matches the "A" and the "e" in "Apples".
	* Even if the order is swapped around, the result is the same.
* Can also check for a range of numbers with:
	* `/#[0123456789]/`
		* This would match "Contestant 1", "Contestant 2" but not "Contestant 99" (it would only match "Contestant 9")
* Can also do it for punctuation as well:
	* `/Notice[:!,]`
		* Would match "Notice: keep off the grass" and "Notice! Keep off the grass"
* 