---
title: "Variables And Types"
category: "python-essential-training"
tags: ["python-essential-training", "variables", "types"]
---

* Defining a Variable:
* `x = 5`
* `print(x)`
	* Prints out the value 5.
* Variable names cannot have special characters, except for an underscore.
* Never start a variable with an uppercase letter.
	* Can confuse this with a Class.
* Can assign characters such as:
	* `name = 'Ryan'`
	* This is called a String.
		* Its literally a string of characters.
	* Each character in the string gets its own memory segment.
* There is a handy function for remembering the type of a variable (string, float etc).
	* `type(<variable_name>`
		* Will then output something like `str` for `string`.
* `x = 1`
	* `type(x)` outputs `1`
* Why are `floats` such as `1.2342` or `123456.7` are called `floats`?
	* In memory, the decimal point has to be stored in memory. Don't know whether all information is going to be on the left or right. It "floats" around, hence its called a float.
* Imaginary Numbers are the square root of Negative Numbers.
	* For these, the notation common in Engineering is `j`
	* Typing `type(2j)` outputs a `complex` number.
	* `1j * 1j` = `(-1+0j)` or `-1`
* Strings are declared with single or double quotes --> `'String 1'` or `"String 1"`
	* Double quotes are popular.
* Can add two strings together --> `'String 1' + 'String 2' = 'String 1 String 2'`
	* Or, concatenation.
* Can concatenate two numbers as strings, such as `'1' + '1' = '11'`
* Booleans are `True` and `False` values.
	* Double `==` sign is a statement, so for example `1 == 1 is equal to True`
	* `1 == 2`, which would be `False`.
	* `==` this is a comparison operator.
	* `=` is an assignment operator.