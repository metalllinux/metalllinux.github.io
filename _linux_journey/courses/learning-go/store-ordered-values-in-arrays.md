---
title: "Store Ordered Values In Arrays"
category: "learning-go"
tags: ["learning-go", "store", "ordered", "values", "arrays"]
---

* An array in Go is an ordered collection of values or references.
* It is better to use `slices` than `arrays` to represent ordered collections of values.
* Example of an array is:
```
package main

import "fmt"

func main() {
	// We are going to say that this variable is an array of 3 strings
	var colours [3]string
	colours[0] = "Red"
	colours[1] = "Green"
	colours[2] = "Blue"
	fmt.Println(colours)
}
```
* The output of this then looks like:
```
:!'go' 'run' '/home/myuser/learning-go-2875237/go_learning/store_ordered_values_in_arrays/main.go'  2>&1| tee /tmp/nvim.myuser/2S30Qh/2
[Red Green Blue]
```
* If we want to access one of those values, we can use an array index.
```
package main

import "fmt"

func main() {
	// We are going to say that this variable is an array of 3 strings
	var colours [3]string
	colours[0] = "Red"
	colours[1] = "Green"
	colours[2] = "Blue"
	fmt.Println(colours)
	// The index always starts at 0 and not 1
	fmt.Println(colours[0])
}
```
* The output is like this:
```
:!'go' 'run' '/home/myuser/learning-go-2875237/go_learning/store_ordered_values_in_arrays/main.go'  2>&1| tee /tmp/nvim.myuser/2S30Qh/6                                                                                             
[Red Green Blue]
Red
```
* The `=` operator is used here and not `:=` to assign each value. 
	* This is because the array type has already been declared.
	* Does not have to be inferred.
* You can also declare an array and its values in a single statement.
* Thus the array is output and is listed without the commas:
```
package main

import "fmt"

func main() {
	// We are going to say that this variable is an array of 3 strings
	var colours [3]string
	colours[0] = "Red"
	colours[1] = "Green"
	colours[2] = "Blue"
	fmt.Println(colours)
	// The index always starts at 0 and not 1
	fmt.Println(colours[0])

	var numbers = [5]int{5, 3, 1, 2, 4}
	fmt.Println(numbers)
}
```
* The output for this one is:
```
:!'go' 'run' '/home/myuser/learning-go-2875237/go_learning/store_ordered_values_in_arrays/main.go'  2>&1| tee /tmp/nvim.myuser/2S30Qh/10
[Red Green Blue]
Red
[5 3 1 2 4]
```
* It is possible to find the number of items in an array, with the built-in `len` or length function.
	* This is wrapped around the length identifier.
```
package main

import "fmt"

func main() {
	// We are going to say that this variable is an array of 3 strings
	var colours [3]string
	colours[0] = "Red"
	colours[1] = "Green"
	colours[2] = "Blue"
	fmt.Println(colours)
	// The index always starts at 0 and not 1
	fmt.Println(colours[0])

	var numbers = [5]int{5, 3, 1, 2, 4}
	fmt.Println(numbers)

	fmt.Println("Number of colours", len(colours))
	fmt.Println("Number of numbers", len(numbers))
}
```
* The output here is then:
```
[Red Green Blue]
Red
[5 3 1 2 4]
Number of colours 3
Number of numbers 5
```
* In Go, an array is an object. If you pass it to a function, a copy will be made of the array.
	* Storing data however is all you can do with arrays. You can't easily sort them and you can't add or remove items at runtime. 
		* For these issues, you should package your order data in `slices`, instead of `arrays`.