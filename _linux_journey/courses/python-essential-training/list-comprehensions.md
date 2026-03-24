---
title: "List Comprehensions"
category: "python-essential-training"
tags: ["python-essential-training", "list", "comprehensions"]
---

* Comprehension here does not mean "understanding", more like comprehensive.
* For example, we have the following:
```
myList = [1,2,3,4,5]
[2*item for item in myList]
```
* The output for that would be:
```
[2, 4, 6, 8, 10]
```
* `item` can be any variable name you want.
	* Make sure it is the same variable name used in the entire code block.
* It allows you to iterate over the list you have.
* List Comprehensions with Filters:
```
# Provides a list with members from 0 ~ 99
myList = list(range(100))
filteredList = [item for item in myList if item % 10 == 0]
```
* `%` is the modulus operator. It in this case provides the remainder, after diving by the number on the right-hand side (in this case 10).
	* If the remainder in this case is equal to `0`, then the statement is true.
* You will then receive an output similar to:
```
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
```
* If you want to show all numbers that are either `1` or `2`:
```
filteredList = [item for item in myList if item % 10 < 3]
filteredList
```
* Will output:
```
[0, 1, 2, 10, 11, 12, 20, 21, 22, 30] and so on
```
* List Comprehensions with Functions
* `split` function splits a string based on the characters that you give it.
* For instance:
```
myString = 'My name is Howard. I am awesome'
myString.split('.')
```
* This will output the following and split the above into two sentences:
```
['My name is Howard', 'I am awesome']
```
* If nothing is passed in, the `split` function will split on spaces. For example:
```
myString.split()
```
* Will output:
```
['My', 'name', 'is', 'Howard.', 'I', 'am', 'awesome']
```
* To clean up the above output, we can use:
```
def cleanWord(word):
# Replaces anything with a `.` with an empty space
# The next function .lower() makes the string lowercase
    return word.replace('.', '').lower()

# To use this in a List Comprehension, we use:
[cleanWord(word) for word in myString.split()]
```
* Calling one function , one after the other, is called `Chaining Functions`.
	* Be careful not to use it too often, as it can lead to long lines of code.
* Running the above function `[cleanWord(word) for word in myString.split()]` will result in an output of:
```
['my', 'name', 'is', 'Howard', 'I', 'am', 'awesome']
```
* We can also clean and filter at the same time and have the lowercase words in the text.
	* Can do something like this:
```
[cleanWord(word) for word in myString.split() if len (cleanWord(word)) < 3]
```
* This will output all of the 1 and 2 letter words in the text, such as:
```
['my', 'is', 'i', 'in']
```
* Nested List Comprehensions
* An example is:
```
# This is splitting the original text into sentences, then performing an inner list comprehension on each sentence
[cleanWord(word) for word in sentence.split()] for sentence in myString.split('.')]
```
* This will output a "list of lists", like a 2D structure.
```
[['my', 'name', 'is', 'Howard'], ['I', 'am', 'awesome']]
```
* Allows you to write clean, readable and "Pythonic" code and is recommended by Python programmers.