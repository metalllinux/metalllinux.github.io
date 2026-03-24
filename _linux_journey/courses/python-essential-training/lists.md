---
title: "The 2 --> is a Step Size of 2"
category: "python-essential-training"
tags: ["python-essential-training", "lists"]
---

* In Python, Strings and Lists are very similar types.
* The slicing syntax for Strings is also applicable to Lists.
```
myList = [1,2,3,4,5]
myList[3:]
```
* Outputs: `[4, 5]`
* Can also pass in a third value as well.
```
# The 2 --> is a Step Size of 2
myList[0:6:2]
```
* Will output `[1, 3, 5]`.
* The equivalent to that is:
```
myList[::2]

```
```
myList[0:6:3]
```
* Will output: `[1, 4]`
* We can also use the `range` function.
	* Its a sequence type.
	* Its like a Tuple - has an order, is immutable and isn't frequently used except for looping through code.
	* For example:
```
for i in range(100): 
    print(i)
```
* This will output the following:
```
0
1
2
3
4
5
and so on to
100
```
* Can take this same range and convert it to a list.
```
myList = list(range(100))
# If we take that and go through every other number:
myList[::2]
```
* The output is:
```
[0
2,
4,
6,
up to 100
]
```
* Can do multiple step sizes.
* If you enter a negative number, you step through the list backwards.
```
myList[::-1]
[99,
98,
97,
96,
etc
]
```
* Modifying Lists.
```
myList = [1,2,3,4]
myList.append(5)
print(myList)
```
* Will output:
```
[1, 2, 3, 4, 5]
```
* `append` adds an item to the list.
* If you want to insert an item in any position, can use `insert`.
```
# The index is 3
myList.insert(3, 'a new value')
```
* Will output:
```
[1, 2, 3, 'a new value', 4, 5]
```
* To remove something from a list, we do:
```
myList.remove('a new value')
myList
```
* The output is then:
```
[1, 2, 3, 4, 5]

```
* If the item you want isn't in the list, it will throw an error.
* The second way to remove an item from a list is with `pop`.
```
myList.pop()
```
* Takes one item off the end of the list.
* Run `myList` again and we get:
```
[1, 2, 3, 4]

```
* Can also run this:
```
# The while statement evaluate to False, when the length of myList = 0
while len(myList):
    print(myList.pop())
```
* If you then run `myList`, you will see that all of the values have been removed.
```
a = [1,2,3,4,5]
b = a
a.append(6)
print(b)
```
* This will then print out the following:
```
[1, 2, 3, 4, 5, 6]
```
* We can use the `copy` function to make an identical copy of the list and store that separately in memory.
```
a = [1,2,3,4,5]
b = a.copy()
a.append(6)
print(a)
print(b)
```
* That will output:
```
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5]
```
* Lists are one of the most fundamental and useful data structures in Python.