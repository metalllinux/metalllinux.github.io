---
title: "Explore Go S Variable Types"
category: "learning-go"
tags: ["learning-go", "explore", "variable", "types"]
---

* Store data in memory with Go using variables.
* Go is a statically typed language.
* All variables have assigned types.
	* Once the type is assigned, it cannot be changed afterwards.
* Can set types for each variable either explicitly (naming the variable type in the declaration) or implicitly (allow the compiler to infer the type, based on the value you initially assign). 
* Go comes with a set of built-in data types.
	* You are able to define your own data types, but in particular these are the ones that are always available.
	* Boolean Values - `bool`
		* Only two values - `true` or `false`
	* String Type - `string`
		* This contains a series of characters.
	* Integers
		* Come in a variety of flavours. Fixed integer types are:
```
uint8
uint16
uint32
uint64
int8
int16
int32
int64
```
* Integers either declare an unsigned or assigned integer.
* The numeric value in the name is the number of bits.
	* That affects the range or the highest and lowest values that can be assigned.
	* Aliases can be used instead of full type names
```
byte
uint
int
uintptr
```
* `int` and unsigned int (`uint`) reflect either 32 or 64 bit values, depending on the OS.
	* 64 bit OS would be int64 and uint64
	* For 32 bit (or the Go Playground), those then become 32 bit values.
* Other numeric types:
	* `float32`
	* `float64`
		* Numeric values again represent number of bits for storage and represent the range that is available.
* Complex numbers:
	* `complex64`
	* `complex128`
	* A complex number contains two parts (real numbers and imaginary numbers)
* Built-in types called `Data collections`:
* `Arrays`
* `Slices`
* `Maps`
* `Structs`
	* Arrays and Slices manage order data collections. Maps and Structs manage aggregations of values.
* Other types that deal with Language Organisation"
	* `Functions`
	* `Interfaces`
	* `Channels`
* In Go, a function is a `type`, which is why you can take a function and that pass that into another function as an argument.
* Interfaces and Channels are also `type`s in Go.
* Data Management:
	* `Pointers`
		* These are reference variables, that point to an address in memory, to refer to another value.