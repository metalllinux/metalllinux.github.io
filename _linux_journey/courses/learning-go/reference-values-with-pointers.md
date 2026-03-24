---
title: "Reference Values With Pointers"
category: "learning-go"
tags: ["learning-go", "reference", "values", "pointers"]
---

* **pointers** --> variables that store the memory address of another variable.
	* You can declare a pointer with a particular type.
```
package main

import "fmt"

func main() {
	// The variable name is set to "p" for pointer here
	// The *int means that it is a pointer. It is not a value
	// If nothing is assigned, then the variable will be nil
	// It will not contain anything
	var p *int
	fmt.Println("Value of p:", p)
}
```
* Running the above will then generate the following output:
```
:!'go' 'run' '/home/howard/learning-go-2875237/go_learning/reference_values_with_pointers/main.go'  2>&1| tee /tmp/nvim.howard/T2rxr5/2
Value of p: <nil>
```
* However, if we add the asterisk to the variable name like so:
```
package main

import "fmt"

func main() {
	// The variable name is set to "p" for pointer here
	// The *int means that it is a pointer. It is not a value
	// If nothing is assigned, then the variable will be nil
	// It will not contain anything
	var p *int
	fmt.Println("Value of p:", *p)
}
```
* That would then crash the application, as `*p` is pointing to an invalid memory address.
* What happens if we have a pointer that points at a valid variable:
```
package main

import "fmt"

func main() {
	anInt := 42
	// The & character means I am pointing at the memory address of the variable, not its value
	var p = &anInt
	fmt.Println("Value of p:", *p)
}
```
* If we run this code, we can see that the value is correctly `42`:
```
:!'go' 'run' '/home/howard/learning-go-2875237/go_learning/reference_values_with_pointers/main.go'  2>&1| tee /tmp/nvim.howard/T2rxr5/6                                                                                              
Value of p: 42
```
* The reason is that is pointing at the value variable.
* Another example is a floating point value:
```
package main

import "fmt"

func main() {
	anInt := 42
	// The & character means I am pointing at the memory address of the variable, not its value
	var p = &anInt
	fmt.Println("Value of p:", *p)

	value1 := 42.13
	// Here, we are not explicitly declaring the type of pointer1
	// However, because the ampersand is used, we are pointing at the memory address of value1, not the value
	pointer1 := &value1
	// To output that value using the pointer, we use:
	// Again, the asterisk means we are pointing at pointer1 and not another variable
	fmt.Println("Value 1:", *pointer1)
}
```
* Thus the output would be"
```
:!'go' 'run' '/home/howard/learning-go-2875237/go_learning/reference_values_with_pointers/main.go'  2>&1| tee /tmp/nvim.howard/T2rxr5/9
Value of p: 42
Value 1: 42.13
```
* We can then see how this affects the original variable:
```
package main

import "fmt"

func main() {
	anInt := 42
	// The & character means I am pointing at the memory address of the variable, not its value
	var p = &anInt
	fmt.Println("Value of p:", *p)

	value1 := 42.13
	// Here, we are not explicitly declaring the type of pointer1
	// However, because the ampersand is used, we are pointing at the memory address of value1, not the value
	pointer1 := &value1
	// To output that value using the pointer, we use:
	// Again, the asterisk means we are pointing at pointer1 and not another variable
	fmt.Println("Value 1:", *pointer1)

	*pointer1 = *pointer1 / 31
	// This is the first time if I address the pointer
	fmt.Println("Pointer 1:", *pointer1)
	// This is the second time, addressing the value directly
	fmt.Println("Value 1:", value1)
}
```
* Here is the output of the above code:
```
:!'go' 'run' '/home/howard/learning-go-2875237/go_learning/reference_values_with_pointers/main.go'  2>&1| tee /tmp/nvim.howard/T2rxr5/12
Value of p: 42
Value 1: 42.13
Pointer 1: 1.3590322580645162
Value 1: 1.3590322580645162
```
* If you have a variable or something that points to that variable, just change the original variable or the variable that is pointing towards it.
* Unlike in Java, the pointer does not have to point at any particular value initially and you can change it at runtime and it will point from one value to another.