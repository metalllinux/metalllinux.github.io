---
title: "Solution Create A Shopping Trolley"
category: "learning-go"
tags: ["learning-go", "solution", "create", "shopping", "trolley"]
---

* We need to calculate the total value of a shopping trolley.
* The trolley consists of 3 items.
	* Each item is an instance of a custom type named `cartItem` 
* The custom type is already declared in the starting code.
	* It is a `struct` and has 3 fields.
		* The `name` (string)
		* The `price` (float64)
		* The `quantity` (an integer)
* When the code is called, three instances of the struct are created, with the required 3 values.
	* Then, the `calculateTotal` function is called.
* Please find the code below:
```
package main

const showExpectedResult = false;
const showHints = false;

type cartItem struct{
		name string
		price float64
		quantity int
}

// calculateTotal() returns the total value of the trolley
func calculateTotal(cart []cartItem) float64 {
		// We declare a total variable and set its type explicitly to `float64`. It is initialised to a value of 0
		var total float64 = 0
		// The cart is then looped through, using the range operator. Each time we go through the loop, we get back two values: the "index" and the "element" within the slice. It is called "item". We do not care about the index, so it is ignored with an `_` character.
		for _, item := range cart {
				// Within the loop, the price is multiplied by the quantity. In Go, when you do a calculation, the two types have to match. The quantity starts off as an integer, so it is converted to a float64
				total += (item.price * float64(item.quantity))
		}
		# Total is returned here.
		return total
}
```
* Test code is the following:
```
var cart []cartItem
var apples = cartItem{"apple", 1.99, 3}
var oranges = cartItem{"orange", 0.99, 8}
var bananas = cartItem{"banana", 0.50, 12}
cart = append{cart, apples, oranges, bananas}
result := calculateTotal(cart)

```
