---
title: "Character Sets Solution"
category: "learning-regular-expressions"
tags: ["learning-regular-expressions", "character", "sets", "solution"]
---

* Example --> `/live[sd]/` matches "lives" and "lived"
* Example, to not select "virtues" and only select "virtue" --> `/virtue[^s]/` We can exclude a character, but it will still match a character.
* Example `/\d\./` would match the sequence of numbers "1984."
* To match a certain number of characters: `/c\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w/` then only matches the 16 character word "circumnavigation".
* 