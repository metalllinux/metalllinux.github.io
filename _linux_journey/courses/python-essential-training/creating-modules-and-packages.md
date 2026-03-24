---
title: "Takes in a number and decides whether or not that number is prime."
category: "python-essential-training"
tags: ["python-essential-training", "creating", "modules", "packages"]
---

* No real such concept as a `library` in Python, it is just code that has been imported from somewhere else.
	* For Python libraries, these are usually referencing modules or packages.
* A module is a Python file.
* Instructor's file is primes.py, which is listed below:
```
def isPrime(n, foundPrimes=None):
    foundPrimes = range(2, int(n**0.5)) if foundPrimes is None else foundPrimes
    for factor in foundPrimes:
         # Takes in a number and decides whether or not that number is prime.
		     if n % factor == 0:
            return False
    return True

# This returns a list of primes, up to the number selected above
def listPrimes(max):
    foundPrimes = []
    for n in range(2, max):
        if isPrime(n, foundPrimes):
            foundPrimes.append(n)
    return foundPrimes

```
* useModule.py:
```
import primes

# The isPrime function decides whether or not 5 (in this case) is prime
print(primes.isPrime(5))
```
* Running `python useModule.py` will output `true`, because 5 is prime.
* We can also rewrite the `import` statement to not import the whole primes module.
```
from primes import listPrimes

# Now we can call the function directly, rather than saying `prime.listPrimes`
print(listPrimes(100))
```
* The above when running `python useModule.py` will list all of the numbers up to 100.
* A package is a collection of modules (all related and bundled up into a single package).
* You can have a package such as `numbers` and inside are the modules `factors.py` and `primes.py`
* For example, we have `factors.py`
* Inside is:
```
def getFactors(n):
		return [facotr for factor in range(1, n+1) if n % factor == 0]
```
* The returns a list of all the primes for the number that you pass in.
* `primes.py` is the same module used previously in the course, but inside the `numbers.py` package instead .
* `primes.py` in full:
```
def isPrime(n, foundPrimes=None):
    foundPrimes = range(2, int(n**0.5)) if foundPrimes is None else foundPrimes
    for factor in foundPrimes:
        if n % factor == 0:
            return False
    return True

def listPrimes(max):
    foundPrimes = []
    for n in range(2, max):
        if isPrime(n, foundPrimes):
            foundPrimes.append(n)
    return foundPrimes

```
* In the package, there is also an important file called `__init__.py`
	* This file will be blank and it is to tell Python that it is a package and not a random collection of python files in a folder.
* Then we can do the following and create `usePackage.py`
```
# numbers is the package and factors is the module and importing the function getFactors
from numbers.factors import getFactors

print(getFactors(100))
```
* If we then run the Python code, we get `python usePackage.py`. If we run that,  we get all the primes up to 100.
* If you don't have the `__init__.py` file, the program will error with `'numbers' is not a package` 
* The modules are also closely related to each other in a package, so for example we can rewrite the `primes.py` code:
```
from numbers.factors import getFactors

def isPrime(n, foundPrimes=None):
		# Prime numbers have exactly 2 factors, hence they equal to 2
    return len(getFactors()) == 2

def listPrimes(max):
    foundPrimes = []
    for n in range(2, max):
        if isPrime(n, foundPrimes):
            foundPrimes.append(n)
    return foundPrimes

```
* There is a built-in Python variable called `name` We can go to the module `primes.py` and add the following line:
```
from numbers.factors import getFactors

def isPrime(n, foundPrimes=None):
		# Prime numbers have exactly 2 factors, hence they equal to 2
    return len(getFactors()) == 2

def listPrimes(max):
    foundPrimes = []
    for n in range(2, max):
        if isPrime(n, foundPrimes):
            foundPrimes.append(n)
    return foundPrimes

print(f'primes.py module name is {__name__}')

```
* If you then run `primes.py` directly from the command line, you receive `python primes.py`:
```
primes.py module name is __main__
```
* `main` is the default module name for the "main" piece of code you are running.
* If you run `python useModule.py` you receive `primes.py module name is primes`, but just running `python primes.py`, you get `primes.py module name is __main__`. 
* We can also add code to the `__init__.py` file, For example:
```
print(f'name in __init__.py is {__name__}')
```
* Then in `factors.py`, we can add:
```
def getFactors(n):
		return [facotr for factor in range(1, n+1) if n % factor == 0]

print(f'name in factors.py is {__name__}')
```
* Running `python usePackage.py`, we receive:
```
name in __init__.py is numbers
name in factors.py is numbers.factor
```
* With the `__NAME__` variable, we can take advantage of this, by creating code that will only be ran, if your module is called directly, versus being imported.
* We can also add helper text if our users become confused, such as:
```
from numbers.factors import getFactors

def isPrime(n, foundPrimes=None):
		# Prime numbers have exactly 2 factors, hence they equal to 2
    return len(getFactors()) == 2

def listPrimes(max):
    foundPrimes = []
    for n in range(2, max):
        if isPrime(n, foundPrimes):
            foundPrimes.append(n)
    return foundPrimes

print(f'primes.py module name is {__name__}')

# We can add helper text if the user gets confused

if __name__ == '__main__':
		print('This is a module! Please import using:\nimport primes')
```
* After that if you run `python primes.py`, it will output the above helper text. 
```
primes.py module name is __main__
This is a module! Please import using:
import primes
```
* If you run `python useModule.py`, the above would then not print out.
* 