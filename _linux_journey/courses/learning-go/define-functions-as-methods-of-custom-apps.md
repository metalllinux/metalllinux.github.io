---
title: "Define Functions As Methods Of Custom Apps"
category: "learning-go"
tags: ["learning-go", "define", "functions", "methods", "custom"]
---

* You can attach functions to custom types in Go.
	* They are then referred to as `methods`.
* In Go, a method is a member of a type.
* In the below example, we will attach a method to the struct.
```
package main

import (
	  "fmt"
)

func main() {
			// We pass in a sound of Woof
			poodle := Dog{"Poodle", 10, "Woof!"}
		  fmt.Println(poodle)
		  fmt.Printf("%+v\n", poodle)
		  fmt.Printf("Breed: %v\nWeight: %v\n", poodle.Breed, poodle.Weight)
		  poodle.Weight = 9
		  fmt.Printf("Breed: %v\nWeight: %v\n", poodle.Breed, poodle.Weight)
			
			// In the main function, we call the function "Speak":
			poodle.Speak()
}
// Dog is a struct
type Dog struct {
		Breed string
		Weight int
		// We add a new field called `sound`:
		Sound string
}

// Here, we create a custom method
// Before we put in the name of the function, we pass in the receiver. The identity for the receive is "d" in this case and the type is "Dog"
// We typically need a comment, before all exported functions. An exported function is public to the rest of the application 
// The comment has a required format: start with double forward slashes. You need the function name + "is" and then any characters after that are fine
// Speak is how the dog speaks
func (d Dog) Speak() {
			// Within the function, we can reference the "Dog" object with the identifier
		 fmt.Println(d.Sound)
}
```
* Once we run the above code, we receive:
```
{Poodle 10 Woof!}
{Breed:Poodle Weight:10 Sound:Woof!}
Breed: Poodle
Weight: 10
Woof!
```
* You can also change the exported / public fields of an object and then call the method again:
```
package main

import (
	  "fmt"
)

func main() {
			poodle := Dog{"Poodle", 10, "Woof!"}
		  fmt.Println(poodle)
		  fmt.Printf("%+v\n", poodle)
		  fmt.Printf("Breed: %v\nWeight: %v\n", poodle.Breed, poodle.Weight)
		  poodle.Weight = 9
		  fmt.Printf("Breed: %v\nWeight: %v\n", poodle.Breed, poodle.Weight)
			
			poodle.Speak()
			// We set poodle.Sound here:
			poodle.Sound() = "Arf!"
			poodle.Speak()
}
type Dog struct {
		Breed string
		Weight int
		// We add a new field called `sound`:
		Sound string
}
// Speak is how the dog speaks
func (d Dog) Speak() {
			// Within the function, we can reference the "Dog" object with the identifier
		 fmt.Println(d.Sound)
}
```
* The code then outputs:
```
{Poodle 10 Woof!}
{Breed:Poodle Weight:10 Sound:Woof!}
Breed: Poodle
Weight: 10
Woof!
Arf!
```
* Go does not support Method overrides and each method has to have a unique name. 
* Like all functions, methods can return values.
	* We declare the type assigned to the method.
```
package main

import (
	  "fmt"
)

func main() {
			poodle := Dog{"Poodle", 10, "Woof!"}
		  fmt.Println(poodle)
		  fmt.Printf("%+v\n", poodle)
		  fmt.Printf("Breed: %v\nWeight: %v\n", poodle.Breed, poodle.Weight)
		  poodle.Weight = 9
		  fmt.Printf("Breed: %v\nWeight: %v\n", poodle.Breed, poodle.Weight)
			
			poodle.Speak()
			poodle.Sound() = "Arf!"
			poodle.Speak()
			poodle.SpeakThreeTimes()
}
type Dog struct {
		Breed string
		Weight int
		// We add a new field called `sound`:
		Sound string
}
// Speak is how the dog speaks
func (d Dog) Speak() {
		 fmt.Println(d.Sound)
}

// We call this one 3 times:
// We need to pass in the receiver (d Dog)
// SpeakThreeTimes is how the dog speaks loudly
func (d Dog) SpeakThreeTimes(){
		// We reassign the value of the sound field
		d.Sound = fmt.Sprintf("%v %v %v", d.Sound, d.Sound, d.Sound)
		fmt.Println(d.Sound)
		
}
```
* The output is that the dog barks three times:
```
Arf! Arf! Arf!
```
* If we call the `poodle.SpeakThreeTimes()` function multiple times however.
	* The dog only ever barks 3 times, not matter how often we write the function.
* When you pass in the dog object as the receiver, a copy is made of it. It is not a reference. If you want it to be a reference, then use pointers.
* When we modify the `Sound` field, we are not modifying the one that was create in the `main` function.