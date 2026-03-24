---
title: "Data Structures"
category: "python-essential-training"
tags: ["python-essential-training", "data", "structures"]
---

* These include the following:
* `Lists`
	* `my_list = [1,2,3,4]`
	* `print(my_list)`
[1,2,3,4]
* Can also use strings:
	* `my_list = ['list', 'of', 'strings']`
* Can have list of strings, integers, booleans, a list within a list etc:
	* `my_list = ['1', 'list', 'False', []]
* List of lists:
	* `my_list = [[1,2,3],[False, True],[]]`
* There is a function that Lists use called `length`.
	* `len(my_list` and we're using the list just above.
		* The output is `3`.
* `Sets`
	* Identical to a list, however all elements inside it have to be unique.
	* Can define a set with curl brackets such as `my_set = {1,2,3,4,5}`.
		* Then print it with: `print(my_set)` displays:
{1,2,3,4,5}
	* To find the type used, you can run `type(my_set)`. It will then output: `set`.
	* Can use the `length` function as well, in this case `len(my_set)` = `5`.
	* Another example is:
	* `my_set = {1,1,2,2}`
	* `len(my_set)`
`2`
		* The output is `2`, because every element in the set needs to be unique.
	* Then if you print with `print(my_set)`, can only see the following two elements:
		`{1, 2}`
* Order of elements in a List is very important.
* For example `[1,2] == [2,1]`, which is `False`
* However for a Set, the following is `True`.
	* `{1,2} == {2,1}` = `True`
* `Tuples`
	* Declared in parenthesis, such as:
	* `my_tuple = (1,2,3)`
	* Very similar to Lists.
	* `len(my_tuple)` = `3`.
	* The order of Tuples is also important:
		* `(1,2) == (2,1)` = `False`.
	* The difference with Tuples, is that things cannot be appended or added to them.
	* For example, `my_list.append(4)`
	* `print(my_list)` (from before), adds the number `4` to the list.
		* If however you do `my_tuple.append(4)`, this is not allowed. You are not able to modify tuples.
			* One a tuple is declared, you can't add or change any of its values.
	* Why use Tuples?
		* They are memory efficient.
			* Python will usually pre-allocate a chunk of memory to a list.
				* However with Tuples these use only the exact amount of memory it needs.
				* Useful for storing smaller values such as `x/y coordinates`.
					* Much more memory efficient than lists.
* `Dictionaries`
`my_dictionary = {
			'apple': 'A red fruit',
			'bear': 'A scary animal'
}`
* Key Value pairs are placed inside of dictionaries.
* If you then run `my_dictionary['apple']` outputs `'A red fruit'`
	* If provides you the `definition/value` of what you get back from the `key`.
* The keys have to be unique. For example:
`my_dictionary = {
			'apple': 'A red fruit',
			'bear': 'A scary animal'
			'apple': 'Sometimes a green fruit'
}`
* Then run `my_dictionary['apple']`, you get `'Sometimes a green fruit'`
* Sets and Dictionaries
	* Both are defined with curl brackets.
	* Sets have unique values, dictionaries have unique keys.
	* The order doesn't matter.