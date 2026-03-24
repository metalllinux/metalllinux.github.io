---
title: "Strings"
category: "python-essential-training"
tags: ["python-essential-training", "strings"]
---

* Slicing
	* Literally taking a slice out of a string and returning it.
```
name = 'My name is Super Howard'
```
* To get the first character of the string, we can do: `name[0]` = `M`
* Second character, `name[1]` = `y`.
* To get the first 7 characters, we can do:
```
name[0:7]
```
* This outputs to `'My name'`
	* It gets all of the character up to index 7.
	* There is also shorthand with `name[:7]`
* If you want to get all of the characters from index 11 onwards, you can do `name[11:]` 
* The slicing syntax is the same when you work with List as well.
	* `myList = [1,2,3,4,5]`
		* Can get a slice of that list, such as `myList[2:4]`
			* `[3, 4]`
* Can get the length of a string, for example `len(name)` = `24`.
* `len(myList)` = `5`.
	* Shows the 5 elements from the list.
* Formatting
	* String contention.
		* `'My number is: '+str(5)`
		* Type in `f` which stands for format. `f'My number is {5}'`
		* Can also write expressions inside the curly braces.