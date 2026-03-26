---
title: "Manage Ordered Values In Slices"
category: "learning-go"
tags: ["learning-go", "manage", "ordered", "values", "slices"]
---

* A `slice` in Go is an abstraction layer, which sits on top of an array.
* When a slice is declared, the runtime allocates the required memory and creates the array in the background.
	* The slice is returned however.
* Like arrays, all items in a slice are of the same time.
	* Unlike arrays, they are re-sizeable.
	* They can also be sorted easily.
```
package main

import "fmt"

func main() {
	// This variable is being explicitly declared with 3 items
	// The reason this is an array and NOT a slice, is that a set number of items were provided
	// var colours = [3]string{"Red", "Green", "Blue"}
	// If the number is removed like so, then it becomes a slice, that means you can add and remove items, sort it and more
	var colours = []string{"Red", "Green", "Blue"}
	fmt.Println(colours)
	// append() is a built-in function we are calling here
	colours = append(colours, "Purple")
	fmt.Println(colours)
}
```
* The output of this one is:
```
:!'go' 'run' '/home/myuser/learning-go-2875237/go_learning/manage_ordered_values_in_slices/main.go'  2>&1| tee /tmp/nvim.myuser/lBEKZJ/8
[Red Green Blue]
[Red Green Blue Purple]
```
* To remove an item, perform the following steps:
```
package main

import "fmt"

func main() {
	// This variable is being explicitly declared with 3 items
	// The reason this is an array and NOT a slice, is that a set number of items were provided
	// var colours = [3]string{"Red", "Green", "Blue"}
	// If the number is removed like so, then it becomes a slice, that means you can add and remove items, sort it and more
	var colours = []string{"Red", "Green", "Blue"}
	fmt.Println(colours)
	// append() is a built-in function we are calling here
	colours = append(colours, "Purple")
	fmt.Println(colours)
	
	// To remove an item from the slice, we perform the following:
	// The range is saying we start the array with an item in index one and then retrieve all of the other data up till the end of the slice.
	// If you leave out the starting number, it defaults to zero.
	colours = append(colours[1:len(colours)])
	fmt.Println(colours)
}
```
* Once we run the above, we will observe the following:
```
:!'go' 'run' '/home/myuser/learning-go-2875237/go_learning/manage_ordered_values_in_slices/main.go'  2>&1| tee /tmp/nvim.myuser/lBEKZJ/8
[Red Green Blue]
[Red Green Blue Purple]
[Green Blue Purple]
```
* To delete the last item in the array, we can perform:
```
package main

import "fmt"

func main() {
	// This variable is being explicitly declared with 3 items
	// The reason this is an array and NOT a slice, is that a set number of items were provided
	// var colours = [3]string{"Red", "Green", "Blue"}
	// If the number is removed like so, then it becomes a slice, that means you can add and remove items, sort it and more
	var colours = []string{"Red", "Green", "Blue"}
	fmt.Println(colours)
	// append() is a built-in function we are calling here
	colours = append(colours, "Purple")
	fmt.Println(colours)
	
	// To remove an item from the slice, we perform the following:
	// The range is saying we start the array with an item in index one and then retrieve all of the other data up till the end of the slice.
	// If you leave out the starting number, it defaults to zero.
	colours = append(colours[1:len(colours)])
	fmt.Println(colours)
	
	//To delete the last item in the array, we can perform:
	colours = append(colours[:len(colours)-1])
	fmt.Println(colours)

}
```
* You can also declare a slice of a type and an initial size with the built-in make function.
	* `make` takes 3 arguments:
		* The type of the slice's items.
		* The initial length.
		* Optional capacity that caps the number of items, that the slice can contain.
* An example of the above declaration is below:
```
package main

import "fmt"

func main() {
	// This variable is being explicitly declared with 3 items
	// The reason this is an array and NOT a slice, is that a set number of items were provided
	// var colours = [3]string{"Red", "Green", "Blue"}
	// If the number is removed like so, then it becomes a slice, that means you can add and remove items, sort it and more
	var colours = []string{"Red", "Green", "Blue"}
	fmt.Println(colours)
	// append() is a built-in function we are calling here
	colours = append(colours, "Purple")
	fmt.Println(colours)
	
	// To remove an item from the slice, we perform the following:
	// The range is saying we start the array with an item in index one and then retrieve all of the other data up till the end of the slice.
	// If you leave out the starting number, it defaults to zero.
	colours = append(colours[1:len(colours)])
	fmt.Println(colours)
	
	//To deleete the last item in the array, we can perform:
	colours = append(colours[:len(colours)-1])
	fmt.Println(colours)
	
	// The type below is an array of ints
	// The initial size is 5 and has a max cap of 5 
	numbers := make([]int, 5, 5) 
	// The first item is created with number 0
	numbers[0] = 134
	numbers[1] = 72
	numbers[2] = 32
	numbers[3] = 12
	numbers[4] = 156
	fmt.Println(numbers)
	// Once we run the code, we see the result below:
}
```
* The result of the above code would look like:
```
[134 72 32 12 156]
```
* If you perform the following, you can add more numbers (removing the cap at the end):
```
	numbers := make([]int, 5) 
```
* To add further numbers, we then do:
```
package main

import "fmt"

func main() {
	// This variable is being explicitly declared with 3 items
	// The reason this is an array and NOT a slice, is that a set number of items were provided
	// var colours = [3]string{"Red", "Green", "Blue"}
	// If the number is removed like so, then it becomes a slice, that means you can add and remove items, sort it and more
	var colours = []string{"Red", "Green", "Blue"}
	fmt.Println(colours)
	// append() is a built-in function we are calling here
	colours = append(colours, "Purple")
	fmt.Println(colours)
	
	// To remove an item from the slice, we perform the following:
	// The range is saying we start the array with an item in index one and then retrieve all of the other data up till the end of the slice.
	// If you leave out the starting number, it defaults to zero.
	colours = append(colours[1:len(colours)])
	fmt.Println(colours)
	
	//To deleete the last item in the array, we can perform:
	colours = append(colours[:len(colours)-1])
	fmt.Println(colours)
	
	// The type below is an array of ints
	// The initial size is 5 and has a max cap of 5 
	numbers := make([]int, 5) 
	// The first item is created with number 0
	numbers[0] = 134
	numbers[1] = 72
	numbers[2] = 32
	numbers[3] = 12
	numbers[4] = 156
	fmt.Println(numbers)
	
	// To add further numbers, we perform the following:
	
	numbers = append(numbers, 235)
	fmt.Println(numbers)
}
```
* Running this, we then see that the number `235` has been successfully added:
```
[134 72 32 12 156 235]
```
* Can also sort a slice using the `sort` package. We need to add this to the `import` statement:
```
package main

import (
     "fmt"
	   "sort"
)

func main() {
	// This variable is being explicitly declared with 3 items
	// The reason this is an array and NOT a slice, is that a set number of items were provided
	// var colours = [3]string{"Red", "Green", "Blue"}
	// If the number is removed like so, then it becomes a slice, that means you can add and remove items, sort it and more
	var colours = []string{"Red", "Green", "Blue"}
	fmt.Println(colours)
	// append() is a built-in function we are calling here
	colours = append(colours, "Purple")
	fmt.Println(colours)
	
	// To remove an item from the slice, we perform the following:
	// The range is saying we start the array with an item in index one and then retrieve all of the other data up till the end of the slice.
	// If you leave out the starting number, it defaults to zero.
	colours = append(colours[1:len(colours)])
	fmt.Println(colours)
	
	//To deleete the last item in the array, we can perform:
	colours = append(colours[:len(colours)-1])
	fmt.Println(colours)
	
	// The type below is an array of ints
	// The initial size is 5 and has a max cap of 5 
	numbers := make([]int, 5) 
	// The first item is created with number 0
	numbers[0] = 134
	numbers[1] = 72
	numbers[2] = 32
	numbers[3] = 12
	numbers[4] = 156
	fmt.Println(numbers)
	
	// To add further numbers, we perform the following:
	
	numbers = append(numbers, 235)
	fmt.Println(numbers)

  // To sort the numbers, we do:
  sort.Ints(numbers)
  fmt.Println(numbers)
}
```
* The result then looks like:
```
[12 32 72 134 156 235]
```
* More information about sorting techniques, is available via the documentation from the sort package.
	* This includes sorting slices of structures, by a structure's member values and sort your own user defined data collections.
* 