---
title: "1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, FizzBuzz, 16"
category: "python-essential-training"
tags: ["python-essential-training", "else"]
---

* If statements with "FizzBuzz"
```
# 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, FizzBuzz, 16
```
* Classic problem in programming, iterate through the numbers from 1 ~ 100.
	* If the number is divisible by 3, print `Fizz`. 
	* If the number is divisible by 5, print `Buzz`.
	* If the number is divisible by 15, print `FizzBuzz`.
		* Otherwise just print the number.
* To write the above in Python, we do:
```
for n in range(1, 101):
		if n % 15 == 0:
		    print('FizzBuzz')
		else:
		    if n % 3 == 0:
			       print('Fizz')
				 else:
				 			if n % 5 == 0:
										print('Buzz')
							else:
							     print(n)
```
* This would output something like:
```
1
2
Fizz
4
Buzz
Fizz
7
8
```
* It does work, but we can improve it with an elif statement:
```
for n in range(1, 101):
		if n % 15 == 0:
		    print('FizzBuzz')
	 elif n % 3 == 0:
			  print('Fizz')
	 elif n % 5 == 0:
				print('Buzz')
	 else:
			  print(n)
```
* The above outputs the same results, but is much cleaner.
	* `elif` must always be preceded by an `if` statement.
	* The `else` statement at the end is optional.
* Good rule of thumb for `if` statements is the following:
	* `if`
	* `elif`
	* `else`
		* Provides some sort of default value if none of the above matches.
* You can also add another `if` statement as well if you wish:
```
for n in range(1, 101):
		if n % 15 == 0:
		    print('FizzBuzz')
	 elif n % 3 == 0:
			  print('Fizz')
	 elif n % 5 == 0:
				print('Buzz')
	 else:
			  print(n)
		
		if n % 2 == 0:
		    print('It is even!')
```
* `if n % 2 == 0:`
* The problem with the above, is that they can drag on and go for too many lines. There is also a one liner statement as well (Single Line if statements):
```
n = 3
print('Fizz' if n % 3 == 0 else n)
```
* The output of this will be `5`.
* Can then take and set the variable to equal the above output with:
```
fizzBuzz = 'Fizz' if n % 3 == 0 else n
```
* The above in programming is what is known as a ternary operator.
	* A ternary operator takes in a boolean condition, which in this case is `n % 3 == 0`, evaluates it and returns one value if the condition is true `'Fizz'`  and another value if the condition is false: `else n`
		* These are used to run clean code.
		* Be careful of using these improperly.
```
'Fizz' if n % 3 == 0 else 'Buzz' if n % 5 == 0 else n
```
* This will output the following:
```
'Buzz'
```
* More stringing is possible with:
```
'FizzBuzz' if n % 3 == 0 else 'Fizz' if n % 5 == 0 else 'Buzz' if n % 5 == 0 else n
```
* Can also put these in a list like so:
```
[]'FizzBuzz' if n % 3 == 0 else 'Fizz' if n % 5 == 0 else 'Buzz' if n % 5 == 0 else n for n in range (1, 101)]
```