---
title: "While"
category: "python-essential-training"
tags: ["python-essential-training", "while"]
---

* One small mistake and your program might run forever.
* A good class to use to test while loops in Python is the `datetime` class.
```
from datetime import datetime
```
* while loops
* We can get the current time using:
```
datetime.now()
```
* Can get the exact seconds, for example with:
```
datetime.now().second
```
* An example while loop that waits for 2 seconds and then prints out a message:
```
wait_until = datetime.now().second + 2
while datetime.now().second != wait_until:
     print('Still waiting!')
print(f'We are at {wait_until} seconds!')
```
* The `f` above is an `f statement`
* To make the above better and more efficient, we are going to use the `pass` statement.
```
wait_until = datetime.now().second + 2

while datetime.now().second != wait_until:
     pass

print(f'We are at {wait_until} seconds!')
```
* The `pass` statement says "nothing to see here, move along" and it does preserve the indentation (required for while loops) and is a great placeholder.
	* If you are writing a function or a class definition and don't want to fill it in yet, you can just write `pass`.
* Another way to write this is using the `break` statement:
```
wait_until = datetime.now().second + 2
# Generally shouldn't use while True
while True:
     if datetime.now().second == wait_until:
         print(f'We are at {wait_until} seconds!')
		      break
```
* The `break` statement breaks out of the current loop that it is in.
* The `break` statement goes up the lines of code and goes to the `print` and says, "is this a loop", then goes further up at the `if` and says "is this a loop?", nope, and goes to the `while` and the break out of it and exits the loop.
	* The `break` statement will only break out of the first `while` loop that is encounters.
* As an example, this would not work:
```
while True:
     while datetime.now().second == wait_until:
         print(f'We are at {wait_until} seconds!')
		      break
```
* The `break` statement would only break out of `while datetime.now().second == wait_until:`
* The final `control statement` for loops is `continue`
	* This skips any lines that follow it inside of the `while` loop.
* For example:
```
wait_until = datetime.now().second + 2

while datetime.now().second != wait_until:
     continue
	    print('Still waiting!')

print(f'We are at {wait_until} seconds!')
```
* The above `continue` will eventually exit the loop and print the following statement: `print(f'We are at {wait_until} seconds!')`
* It is not a common usage of `continue`.
	* Usually you see a `continue` statement used inside an `if` statement to prevent the code in the loop for executing, if some condition is met.
	* An example is:
```
wait_until = datetime.now().second + 2

while True:
     if datetime.now().second < wait_until:
	        continue
		  break

print(f'We are at {wait_until} seconds!')
```
* When the above continue statement is met, it skips all else in the loop, which is the `break` statement. Once the `if datetime.now().second < wait_until:` is no longer true, the `continue`statement is no longer hit and it goes to the `break` statement.
* `continue` and `break` are not techinically and logically necessary. They can help you rearrange and rewrite code for other programmers to read.