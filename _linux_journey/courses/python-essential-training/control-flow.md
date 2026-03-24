---
title: "Control Flow"
category: "python-essential-training"
tags: ["python-essential-training", "control", "flow"]
---

* Three main types of Control Flow:
* If / Else Statements
```
a = False
if a:
     print('It is true!')
	   print('Also print this')
```
* The above is an `if` block.
* Can `out-dent` as well, for example:
```
a = False
if a:
     print('It is true!')
	   print('Also print this')
print('Always print this')
```
Will then print `print('Always print this')`
* If `a` is true, it will print all of the below 3 lines:
```
a = True
if a:
     print('It is true!')
	   print('Also print this')
print('Always print this')
```
It is true!
Also print this
Always print this
* To add an `else` statement, you can do:
```
a = True
if a:
     print('It is true!')
	   print('Also print this')
else:
     print('It is false!')
print('Always print this')
```
* Can add a lot of indents, for example:
```
a = True
b = True
if a:
     print('It is true!')
	   print('Also print this')
	   if b:
	        print('Both are true')
else:
     print('It is false!')
print('Always print this')
```
It is true!
Also print this
Both are true
Always print this
* Another example:
```
a = True
b = True
c = True
if a:
     print('It is true!')
	   print('Also print this')
	   if b:
	        print('Both are true')
			     if c:
				        print('All three are true')
else:
     print('It is false!')
print('Always print this')
```
It is true!
Also print this
Both are true
All three are true
Always print this
* If any of the above are set to `False`, you never reach line: `print('All three are true')`
* In order to avoid excessive indenting, Python has another tool call the `Loop`
* Loops
	* For Loops iterate over what Python calls `iterables`.
	* A list is a type of iterable:
```
a = [1,2,3,4,5]
for item in a:
		print(item)
```
Outputs:
1
2
3
4
5
* The `item` is just a variable being declared in the line.
* While Loops
	* These keep looping until the boolean that is passed becomes false.
```
a = 0
while a < 5:
    print(a)
	   a = a + 1
```
* Without the following line, the above loop would not end: `a = a + 1`
	* Good to implement a while loop if conditions are changing.