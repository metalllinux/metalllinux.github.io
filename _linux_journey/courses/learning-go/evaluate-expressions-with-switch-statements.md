---
title: "Evaluate Expressions With Switch Statements"
category: "learning-go"
tags: ["learning-go", "evaluate", "expressions", "switch", "statements"]
---

* Switch statements are used to evaluate which numbers are generated.
Example code:
```
package main

import (
		 "fmt"
		 "math/rand"
		 "time"
)

func main() {
		// From the "rand" package, we are calling in the "Seed" function and passing in the current time in Unix format.
		rand.Seed(time.Now().Unix())
		// Then we use a function called "Intn" and a ceiling of "7" is passed into it. We add 1 and this provides a value between 1 and 7
		dow := rand.Intn(7) + 1
		fmt.Println("Day", dow)
}
```
* Each time the application is ran, we get a different number. Example output:
```
Day 1
```
* The program's output depends on the milliseconds the computer is currently at. In the Go Playground, the output is always the same.
* Now we evaluate the nubmer that is generated with the `switch` statement:
```
package main

import (
		 "fmt"
		 "math/rand"
		 "time"
)

func main() {
		// From the "rand" package, we are calling in the "Seed" function and passing in the current time in Unix format.
		rand.Seed(time.Now().Unix())
		// Then we use a function called "Intn" and a ceiling of "7" is passed into it. We add 1 and this provides a value between 1 and 7
		dow := rand.Intn(7) + 1
		fmt.Println("Day", dow)
		
		var result string
		switch dow {
				// Just like the if statement, you do not require parenthesis around the expression you are evaluating.
				// We add the cases to the switch statement below:
		case 1:
					result = "It's Sunday!"
		case 2:
					result = "It's Monday!"
		
		default:
					result = "It's some other day!"
    }
	  fmt.Println(result)
}
```
* For example, the above code outputs:
```
Day 1
It's Sunday
```
* In Go, it will execute the code in the case and then jump to the end of the Switch statement. 
* Just like an `if` statement, you can include a statement before the evaluation of your variables.
* An example of that is:
```
switch dow := rand.Intn(7) + 1; dow {

} 
```
* If you prefer to use a C-style flow, where the Break statement is required to prevent things falling through to other cases, you can restore it with Go's fallthrough keyword.
	* If you add `fall through` to any code within a case, if that case is true, you will execute its code and you will also execute the next case as well.
* An example of `fallthrough`:
```
package main

import (
		 "fmt"
		 "math/rand"
		 "time"
)

func main() {
		rand.Seed(time.Now().Unix())
		dow := rand.Intn(7) + 1
		fmt.Println("Day", dow)
		
		var result string
		switch dow {
		case 1:
					result = "It's Sunday!"
					// Adding fallthrough here:
					fallthrough
		case 2:
					result = "It's Monday!"
					// And here
					fallthrough
		default:
					result = "It's some other day!"
    }
	  fmt.Println(result)
}
```
* The only output we would see is `It's some other day!`, that is due to the `fallthrough keyword`.
* 