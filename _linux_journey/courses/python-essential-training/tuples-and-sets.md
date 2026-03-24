---
title: "Tuples And Sets"
category: "python-essential-training"
tags: ["python-essential-training", "tuples", "sets"]
---

* Data Structures.
* A set is declared using curly brackets.
```
mySet = {'a', 'b', 'c'}
mySet
```
* You can also define it by passing any iterable object of the constructor of the set class.
```
mySet = set(['a', 'b', 'c'])
```
* If you use a Tuple, you receive the same set:
```
mySet = set(('a', 'b', 'c'))
```
* A common pattern in programming is duplicate removal from a list.
* You can convert a list to a set and then back again, sets can only contain unique values.
```
myList = ['a', 'b', 'b', 'c', 'c']
myList = list(set(myList))
myList
```
* The above will then remove duplicates and show `['a', 'b', 'c']`
* Properties of Sets:
	* The order does not matter.
	* Declared with curly brackets.
	* All elements are unique.
	* Sets are randomised.
	* The order of elements in the list, may not be the same coming back out.
		* Because of this, you can't fetch elemets by index.
```
mySet[0]
```
* The above will output an error.
* In Python, object is `subscriptable`, if it contains items that can be accessed by an Index.
* It contains ordered, accessible sub elements.
* For example:
```
number = 1
1[0]
```
* You would receive an output for the above message.
	* It doesn't make sense to get the first element in a big random pile.
* You can add elements to a set, for example:
	* `mySet.add('d')`
		* The `add` function tosses the element onto the pile.
		* Outputs: `{'a', 'b', 'c', 'd'}`
* Like with lists, you can use the `membership` operator to return boolean values.
	* `'a' in mySet`
		* Outputs to `True`, because we have `a`.
	* `'z' in mySet`:
		* `False`
* Can use the length function as well, for example `len(mySet)` = `4`
* Set dose have a pop function and you pop the element off the set.
```
while len(mySet):
		 print(mySet.pop())
```
* Will output and remove the following:
```
a
b
c
d
```
* If you want to remove a specific element, you can do that with:
```
mySet.discard('a')
```
* It will not throw an error, even though `mySet` is empty.
* Will then output `{'b', 'c'}`
* Tuples
	* Very much like Lists - have an order and declared with parenthesis. 
	* Ordered and subscriptable.
	* Cannot be modified.
```
myTuple = ('a', 'b', 'c')
myTuple
```
* Will output:
```
('a', 'b', 'c')
```
* To get the first element of the Tuple:
	* `myTuple[0]` = `a`.
* If you try to assign a Tuple, such as `myTuple[0] = 'd'`, this will throw an error.
* Why Use Tuples?
	* More efficient than lists.
	* They don't grow or change.
	* Store compactly in memory.
	* Often used by default.
* Write a Python function with multiple values, separated by commas.
```
def returnMultipleValues():
# The syntax below is preferred
    return 1,2,3
# Call it and put whatever it is returning into the type function:
type(returnMultipleValues())
```
* This will output --> `tuple`
* Can also use a Tuple as `myTuple = 1,2,3` (without any parentheses).
	* Best to add parentheses around any tuple.
* The below is called `unpacking values`:
* Can set multiple values in a row, for example --> `a, b, c = returnMultipleValues()`
```
print(a)
print(b)
print(c)
```
* Shows output as:
```
1
2
3
```