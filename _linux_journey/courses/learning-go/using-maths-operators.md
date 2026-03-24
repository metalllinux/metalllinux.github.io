---
title: "Using Maths Operators"
category: "learning-go"
tags: ["learning-go", "maths", "operators"]
---

* Numeric types don't implicitly convert.
	* Cannot take an integer value and then add it to a floating value without conversion. An example of this is the below code:
```
var anInt int = 5
var aFloat float64 = 42
sum := anInt + aFloat
fmt.Printf("Sum: %v, Type: %T\n", sum, sum)
```
* In the above code, one variable is an integer and the other is a float and we attempt to add these together using `sum`.
* However, this results in an error, causing the application to crash.
```
// invalid operation: anInt + aFloat
// (mismatched types int and float64)
```
* To correctly add the values, one has to match the type of the other.
* We do this by wrapping the value in a function, that has the same name as the target type.
```
var anInt int = 5
var aFloat float64 = 42
// Here we convert the integer to a float64 value, before the two values are added together. The operation will be successful and the result seen
sum := float64(anInt) + aFloat
fmt.Printf("Sum: %v, Type: %T\n", sum, sum)
```
* This will output:
```
// Sum: 47, Type: float64
```
* For mathematical operations that go beyond simple operators, we should inspect the `math` package:
```
import "math"

var aFloat = 3.14159
// The value is rounded, using the Round function from the math package. It rounds to the nearest integer
var rounded = math.Round(aFloat)
fmt.Printf("Original: %v, Rounded: %v\n", aFloat, rounded)
```
* The output would be:
```
Original 3.14159, Rounded: 3
```
* There are also `constants` in the `math` package. We can also replace `pi` with the `constant` `math.pi`