---
title: "For"
category: "python-essential-training"
tags: ["python-essential-training"]
---

* Typical syntax is the following:
```
myList = [1,2,3,4]
for item in myList:
    print(item)
```
* All the statement covered in `while` loops, can also be used in `for` loops as well.
* If you want to write a `stub` for a `for` loop and then come back to it later, we can use `pass`.
```
animalLookup = {
     'a': ['aardvark', 'antelope'],
	   'b': ['bear'],
	   'c': ['cat'],
	   'd': ['dog'],
}

for letter, animals in animalLookup.items():
    pass
```
* Also possible to skip the rest of the loop with a `continue` statement.
```
for letter, animals in animalLookup.items():
    if len(animals) > 1:
	       continue
		 print(f'Only one animal! {animals[0]}')
```
* This would output:
```
Only one animal! bear
Only one animal! cat
Only one animal! dog
```
* Can also use a `break` statement with:
```
for letter, animals in animalLookup.items():
    if len(animals) > 1:
		    print(f'Found {len(animals)} animals: {animals}')
			  break
```
* Outputs:
```
Found 2 animals: ['aardvark', 'antelope']
```
* If there were two or more instances of animals in the list, it stops after the first one.
* There is also the `break else` statement or more formally the `for else` statement.
* Example for finding Prime Numbers (computers do this for cryptography and security).
* Example below is finding all the primes between 2 and 100:
```
for number in range (2, 100):
    for factor in range(2, int(number ** 0.5) + 1):
	       if number % factor == 0:
		         break
# The else statement will only be called, if a break did not happen in the previous loop
		 else:
		     print(f'{number} is prime!')
```
* `number` is the one we are testing for Primality.
* Then we want to loop through all the potential factors.
	* `** 0.5` is the square root of the number
	* The number goes to the one halfth exponent.
		* If we don't find a factor by that point, we know the number is prime.
* We can use the module (`%`) to check if it is evenly divisible.
* Will then output:
```
2 is prime!
3 is prime!
5 is prime!
```
* and so on
* `break` - `else` pattern can also be used in a `while` loop as well.
* Sometimes you will see Python code similar to this:
```
for number in range (2, 100):
    found_factors = False
    for factor in range(2, int(number ** 0.5) + 1):
	       if number % factor == 0:
		         found_factor = True
# The else statement will only be called, if a break did not happen in the previous loop
		 if not found_factors:
		     print(f'{number} is prime!')
```
* The output will still be the same and it is a lot more code required. The previous line is much for `Pythonic`