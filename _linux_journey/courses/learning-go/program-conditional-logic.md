---
title: "Program Conditional Logic"
category: "learning-go"
tags: ["learning-go", "program", "conditional", "logic"]
---

* Go's syntax for the `if` statement, differs from other C-style languages.
* The `if` statement in Go does not require parenthesis around the Boolean condition.
```
package main

import (
		  "fmt"
)

func main() {

			theAnswer := 42
			
			// We now need a string as a result message. We are declaring it, but not assigning it any value.
			var result string 
			
			if theAnswer < 0 {
					result = "Less than zero"
			} else if theAnswer == 0 {
			// Can add more "else if" states if needed to, but if there are no more, we can just go to "else" if none of the other conditions are true
				  result = "Equal to zero"			
			} else {
				   result = "Greater than zero"
			}
			fmt.Println(result)
}
```
* The outcome in this case is:
```
Greater than zero
```
* Regarding braces of code blocks.
	* In other C-style langues, you have the option of placing the beginning brace of a code block, onto the next line.
		* If you do that in Go however, you will receive an error.
* The opening brace has to be on the same line as the proceeding statement:
```
if theAnswer < 0 {
```
* We can also include an initial statement, an exampel of this is:
```
package main

import (
		  "fmt"
)

func main() {

			theAnswer := 42
			
			var result string 
			
			if theAnswer < 0 {
					result = "Less than zero"
			} else if theAnswer == 0 {
				  result = "Equal to zero"			
			} else {
				   result = "Greater than zero"
			}
			fmt.Println(result)
			
			// After the semi colon, we can continue with the rest of the if statement. Here we are initialising values, as part of the if statement
			if x := -42; x < 0 {
						result = "Less than zero"
			} else if x == 0 {
					result = "Equal to zero"
			} else {
					result = "Greater than zero"
			}
			fmt.Println(result)

}
```