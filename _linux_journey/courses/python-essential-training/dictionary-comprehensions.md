---
title: "Dictionary Comprehensions"
category: "python-essential-training"
tags: ["python-essential-training", "dictionary", "comprehensions"]
---

* Generate dictionaries for iterable structures.
* Very similar to list comprehensions.
* An example is a list of `tuoles` that we will be using as our key value pairs.
	* Tuples work just like lists, however you cannot alter the value of Tuples once they have been declared.
```
animalList = [('a', 'aardvark'), ('b', 'bear'), ('c', 'cat'), ('d', 'dog')]
animals = {item[0]: item[1] for item in animalList}
animals
```
* This will output the following:
```
{'a': 'aardvark', 'b': 'bear', 'c': 'cat', 'd': 'dog'}
```
* Need to define the key and value, separated by a colon.
* There is a much nicer way to write the above statement as well.
```
animals = {key: value for key, value in animalList}
animals
```
* That will output the same thing:
```
{'a': 'aardvark', 'b': 'bear', 'c': 'cat', 'd': 'dog'}
```
* Whatever is between the `for` and `in` of this statement, is what each Tuple of `animalList` is being assigned to.
* Python allows you to unpack values into multiple variables, as long as the number of variables you are assigning values to matches the elements in the data structure.
* We are unpacking the above items into pairs of value variables.
* What if we want to take the animal dictionary and turn it back into a list.
	* We can use the `items` function.
* `animals.items()` will return:
```
dict_items([('a', 'aardvark'), ('b', 'bear'), ('c', 'cat'), ('d', 'dog')])
```
* Can turn it back into the original animal list as above with:
```
list(animals.items())
```
* Will output:
```
[('a', 'aardvark'), ('b', 'bear'), ('c', 'cat'), ('d', 'dog')]
```
* What if we want each item to have a structure different:
	* We can use a list comprehension. 
```
[{'letter': key, 'name': value} for key, value in animals.items()]
```
* That will output:
```
[{'letter': 'a', 'name': 'aardvark'}],
{'letter': 'b', 'name': 'bear'},
{'letter': 'c', 'name': 'cat'},
{'letter': 'd', 'name': 'dog'},
```
* Very powerful to process and format data in Python.