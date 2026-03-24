---
title: "Define And Call Functions"
category: "learning-go"
tags: ["learning-go", "define", "call", "functions"]
---

* Go is organised in packages and packages have functions.
* Every program has a package named `main` and a function named `main`, that always starts at runtime.
* We are able to create our own custom functions and organise them into custom packages.
* Example function is:
```
package main

import {
			"fmt"
}

func main() {
		doSomething()
}

// If you are not returning a value, you do not need anything between the parenthesis and the braces
func doSomething() {
		fmt.Println("Doing something")
}
```
* The above the runs and we see the output as:
```
Doing something
```
* You can pass arguments into a function, declaring each argument with a name and a type.
* If a function returns a value, define the return type after the function's closing parenthesis.
```
package main

import {
			"fmt"
}

func main() {
		doSomething()
		// We call that function in the main function
		sum := addValues(5, 8)
		fmt.Println("The sum is", sum)
}

func doSomething() {
		fmt.Println("Doing something")
}

// The function accepts two values and returns an integer, which is why the "int" type goes after the parenthesis
func addValues(value1 int, value2 int) int {
	  return value1 + value2
}
```
* The output of the above, is that we receive the expected `sum`:
```
Doing something
The sum is 13
```
* If a function receives multiple parameters of the same type, we don't need to declare the type more than once.
```
func addValues(value1, value2 int) int {
		 return value1 + value2
}
```
* The output is the exact same as before:
```
Doing something
The sum is 13
```
* A function can also declare multiple arbitrary values of the same type.
	* To perform this, we declare the parameter name, add three dots and then the type afterwards.
```
package main

import {
			"fmt"
}

func main() {
		doSomething()
		// We call that function in the main function
		sum := addValues(5, 8)
		fmt.Println("The sum is", sum)q
		multiSum := addAllValues(4,7,9)
		fmt.Println("Sum of multiple values:", multiSum)
}

func doSomething() {
		fmt.Println("Doing something")
}

func addValues(value1 int, value2 int) int {
	  return value1 + value2

func addValues(value1, value2 int) int {
		 return value1 + value2
}

// As before, it returns an int
func addAllValues(values ...int) int {
		// We create a variable called "total" and assign its value to zero
		total := 0
		// We then loop through the "values" argument, which is an array
		// "v" is used here for the value. We are looping through the "values" array
		for _, v := range values {
				total += v
		}
		// Total is then returned after the loop
		return total
}
```
* The output of that would be:
```
The sum is 13
Sum of multiple values: 20
```
* Go also allows you to return more than 1 value from a function. We return a comma delimited list of types wrapped in parenthesis.
* To accomplish that, we do:
```
package main

import {
			"fmt"
}

func main() {
		doSomething()
		sum := addValues(5, 8)
		fmt.Println("The sum is", sum)q
		// We add another variable here to receive that second value
		multiSum, multiCount := addAllValues(4,7,9)
		fmt.Println("Sum of multiple values:", multiSum)
		fmt.Println("Count of items, multiCount")
}

func doSomething() {
		fmt.Println("Doing something")
}

func addValues(value1 int, value2 int) int {
	  return value1 + value2

func addValues(value1, value2 int) int {
		 return value1 + value2
}
// Here, we are now returning two integer values
func addAllValues(values ...int) (int, int) {
		total := 0
		for _, v := range values {
				total += v
		}
		// For the second value, we add a comma after the return statement
		// Then we add here to return the length of the values in the array
		return total, len(values)
}
```
* The output of the above is:
```
Count of items 3
```
* With functions, instead of returning the items in a list, you can name the values.