---
title: "Create Loops With For Statements"
category: "learning-go"
tags: ["learning-go", "create", "loops", "statements"]
---

* There is in `while` statement in Go.
	* You can do the same thing with extended versions of `for` statement syntax.
* The most common `for` statement has a three part declaration.
* As an example, we are starting off with the following array:
```
package main

import {
		 "fmt"
}

func main() {
			colours := []string{"Red", "Green", "Blue"}
			fmt.Println(colours)
}
```
* Running the above will output the following:
```
[Red Green Blue]
```
* Now we add the `for` block with a 3 part declaration:
```
package main

import {
		 "fmt"
}

func main() {
			colours := []string{"Red", "Green", "Blue"}
			fmt.Println(colours)
			// The "i" is known as a "counter" variable
			// We compare the counter variable to the length of the array
			for i := 0; i < len(colours); i++ {
			    // We now output the colour value at the index position in the array
					fmt.Println(colours[i])
			}
}
```
* This then prints out each item from the array onto its own line:
```
[Red Green Blue]
Red
Green
Blue
```
* We can also assign the `counter` varialbe using the `range` keyword - it is more concise and more readable.
```
package main

import {
		 "fmt"
}

func main() {
			colours := []string{"Red", "Green", "Blue"}
			fmt.Println(colours)

			for i := 0; i < len(colours); i++ {
					fmt.Println(colours[i])
			}
			// This results in setting "i" to the index position each time through the loop. We do not need to explicitly reset the "counter" variable and it is done for us.
			for i := range colours {
					fmt.Println(colours[i])
			}
}
```
* This outputs the exactl same result as previously shown above.
* We can also do a `for each` loop.
	* In the next example, we perform that in a comma delimited list.
```
package main

import {
		 "fmt"
}

func main() {
			colours := []string{"Red", "Green", "Blue"}
			fmt.Println(colours)

			for i := 0; i < len(colours); i++ {
					fmt.Println(colours[i])
			}

			for i := range colours {
					fmt.Println(colours[i])
			}
			// The first variable will be the index and the second will be the associated value
			// If you need the value, you can ignore the index by using an underscore character
			// Colour is the variable that contains the current value
			for _, colour := range colours {
					fmt.Println(colour)
			}
}
```
* Once again, we see the exact same results as before:
```
[Red Green Blue]
Red
Green
Blue
```
* Many languages have a `while` keyword that allows you to loop until a boolean expression returns true.
	* Go implements these with the `for` keyword.
	* Instead of a counter variable or range, we declare a boolean condition.
```
package main

import {
		 "fmt"
}

func main() {
			colours := []string{"Red", "Green", "Blue"}
			fmt.Println(colours)

			for i := 0; i < len(colours); i++ {
					fmt.Println(colours[i])
			}

			for i := range colours {
					fmt.Println(colours[i])
			}

			for _, colour := range colours {
					fmt.Println(colour)
			}
			
			value := 1
			for value < 10 {
					fmt.Println("Value:", value)
					value++
			}
}
```
* The output of that one is counting from 1 to 9:
```
Value: 1
Value: 2
Value: 3
Value: 4
Value: 5
Value: 6
Value: 7
Value: 8
Value: 9
```
* The `break` and `continue` statements work similarly to other C style language .
	* `break` means jumping to the end of the current code block.
		* Works for `for` and `switch` statements.
	* `continue` means start back at the beginning of the code block.
	* The `goto` statement with label is also available.
		* You can add labels to the code and jump to the label with a `goto` or `break` statement.
* An example of that is:
```
package main

import {
		 "fmt"
}

func main() {
			colours := []string{"Red", "Green", "Blue"}
			fmt.Println(colours)

			for i := 0; i < len(colours); i++ {
					fmt.Println(colours[i])
			}

			for i := range colours {
					fmt.Println(colours[i])
			}

			for _, colour := range colours {
					fmt.Println(colour)
			}
			
			value := 1
			for value < 10 {
					fmt.Println("Value:", value)
					value++
			}
			
			sum := 1
			for sum < 1000 {
					// We add sum to sum here:
					sum += sum
					fmt.Println("Sum:", sum)
			}
}
```
* Once the `sum` code is ran, it will keep running until `sum` exceeds 1000.
```
Sum: 4
~
Sum: 1024
```
* If we want `sum` to jump out when it hits 200:
```
package main

import {
		 "fmt"
}

func main() {
			colours := []string{"Red", "Green", "Blue"}
			fmt.Println(colours)

			for i := 0; i < len(colours); i++ {
					fmt.Println(colours[i])
			}

			for i := range colours {
					fmt.Println(colours[i])
			}

			for _, colour := range colours {
					fmt.Println(colour)
			}
			
			value := 1
			for value < 10 {
					fmt.Println("Value:", value)
					value++
			}
			
			sum := 1
			for sum < 1000 {
					sum += sum
					fmt.Println("Sum:", sum)
					if sum > 200 {
							goto theEnd
					}
			}
			// We place a label outside of the code block.
			
			theEnd : fmt.Println("End of program") 
}
```
* Now we only keep looping, until we hit the condition of `200`:
```
Sum: 128
Sum: 256
End of program
```
* Go adds features to the `for` statement to make it concise and readable. 