---
title: "Group Related Values In Structs"
category: "learning-go"
tags: ["learning-go", "group", "related", "values", "structs"]
---

* The `struct` type in Go is a data structure.
* `structs` are simliar in purpose to CS `structs` and Java classes.
* The `struct` can encapsulate both data and methods.
* Unlike Java, Go doesn't have an inheritance model.
	* There is no concept like `super` or `sub` `structs`
* Each structure is independent, with its own fields for data management.
* Optionally its own methods as well.
* A `struct` in Go is a custom type. You can declare the custom types in the same file as the rest of your code.
* To create your own custom type, start with the `type` keyword.
```
package main

import (
	  "fmt"
)

// In the "main" function, we add code to create an instance of that struct.
func main() {
			// Value of "Dog" given to "poodle"
			// The properties are set inside a pair of braces, similar to a constructor in other languages. In this case we are not defining a method, we are calling an object. Pass the values to the object, in the order that they are declared
			poodle := Dog{"Poodle", 10}
		  fmt.Println(poodle)
}
// If the type is given an uppercase initial character, it can be used by other parts of the application. In Go vocab, this has been "exported"
// If you use a lowercase initial character, it is "non-exported" or "private"
// We call this a data structure, by adding the keyword "struct"
type Dog struct {
		// We give the struct a property of "Breed"
		// Just like the name of the type, the property names are either "exported" or "non-exported"
		// Uppercaes means it is exported and the rest of the application can either read or write to those property values
		Breed string
		Weight int
}
```
* The output of the above, shows the string representation of the object:
```
{Poodle 10}
```
* If you get a warning that a fixed type should have a comment or be non-exported:
```
package main

import (
	  "fmt"
)

func main() {
			// Value of "Dog" given, properties set inside the braces. We're defining an object here. Pass the values to the object, in the order that they are declared. 
			poodle := Dog{"Poodle", 10}
		  fmt.Println(poodle)
}
// THE COMMENT WOULD GO HERE, TO REMOVE THE WARNING:
// Dog is a struct
type Dog struct {
		Breed string
		Weight int
}
```
* Once we save the above, the warning is removed and the code still successfully runs.
* If we change `Dog` to a lowercase character and save the changes afterwards, there will be an error, as the `Dog` type is not available.
* To see a struct's field names and values for debugging purposes, use the `printf` function. That would look like the below:
```
package main

import (
	  "fmt"
)

func main() {
			// Value of "Dog" given, properties set inside the braces. We're defining an object here. Pass the values to the object, in the order that they are declared. 
			poodle := Dog{"Poodle", 10}
		  fmt.Println(poodle)
		  fmt.Printf("%+v\n", poodle)
}
// THE COMMENT WOULD GO HERE, TO REMOVE THE WARNING:
// Dog is a struct
type Dog struct {
		Breed string
		Weight int
}
```
* Then when we run the above, we see the following:
```
{Poodle 10}
{Breed:Poodle Weight:10}
```
* We see all of the data from the object.
* Each value of a `struct`, is technically known as a field.
	* Just like classes from other languages.
* We can use String Interpolation like so:
```
package main

import (
	  "fmt"
)

func main() {
			poodle := Dog{"Poodle", 10}
		  fmt.Println(poodle)
		  fmt.Printf("%+v\n", poodle)
		  fmt.Printf("Breed: %v\nWeight: %v\n", poodle.Breed, poodle.Weight)
}
// Dog is a struct
type Dog struct {
		Breed string
		Weight int
}
```
* The result of the above is:
```
Breed: Poodle
Weight: 10
```
* If we want to change the values, we can do that as well with:
```
package main

import (
	  "fmt"
)

func main() {
			poodle := Dog{"Poodle", 10}
		  fmt.Println(poodle)
		  fmt.Printf("%+v\n", poodle)
		  fmt.Printf("Breed: %v\nWeight: %v\n", poodle.Breed, poodle.Weight)
		  poodle.Weight = 9
		  fmt.Printf("Breed: %v\nWeight: %v\n", poodle.Breed, poodle.Weight)

}
// Dog is a struct
type Dog struct {
		Breed string
		Weight int
}
```
* The output would be:
```
Weight: 9
```