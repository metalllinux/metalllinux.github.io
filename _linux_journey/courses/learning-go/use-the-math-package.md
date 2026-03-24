---
title: "Use The Math Package"
category: "learning-go"
tags: ["learning-go", "math", "package"]
---

```
package main

import (
			"fmt"
)

func main() {
		//Go compiler recognises these and then implicitly sets the types of the variables to int
		i1, i2, i3 := 12, 45, 68
		// We now add the values together:
		intSum := i1 + i2 + i3
		fmt.Println("Integer sum:", intSum)
}
```
* When you want to declare more than 1 variable of the same type, you can do it all in a single statement.
* The output of `intSum` above would be 125.
* To add floating numbers together, we can perform the following:
```
package main

import (
			"fmt"
)

func main() {
		//Go compiler recognises these and then implicitly sets the types of the variables to int
		i1, i2, i3 := 12, 45, 68
		// We now add the values together:
		intSum := i1 + i2 + i3
		fmt.Println("Integer sum:", intSum)
		
		f1, f2, f3 := 23.5, 65.1, 76.3
		floatSum := f1 + f2 + f3
		fmt.Println("Float sum:", floatSum)
}
```
* Running the above would output the following:
```
Float sum: 164.8999999999998
```
* We see the above, because floating values in Go are stored in binary. Therefore simple mathematical operations don't always provide the precision you expect.
	* The `math/big` package can help accomplish this.
* We can make this more precise with the `math` package:
```
package main

import (
			"fmt"
			"math"
)

func main() {
		//Go compiler recognises these and then implicitly sets the types of the variables to int
		i1, i2, i3 := 12, 45, 68
		// We now add the values together:
		intSum := i1 + i2 + i3
		fmt.Println("Integer sum:", intSum)
		
		f1, f2, f3 := 23.5, 65.1, 76.3
		floatSum := f1 + f2 + f3
		fmt.Println("Float sum:", floatSum)

		//We reassign the value of floatSum like below. We are not using the := operator, because the floatSum variable in this case has already been initialised.
		floatSum = math.Round(floatSum)
    fmt.Println("The sum is now", floatSum)
}
```
* Running the above then shows the `floatSum` as `165` and rounds to an integer.
* We however want to round to the nearest 2 decimals.
```
package main

import (
			"fmt"
			"math"
)

func main() {
		//Go compiler recognises these and then implicitly sets the types of the variables to int
		i1, i2, i3 := 12, 45, 68
		// We now add the values together:
		intSum := i1 + i2 + i3
		fmt.Println("Integer sum:", intSum)
		
		f1, f2, f3 := 23.5, 65.1, 76.3
		floatSum := f1 + f2 + f3
		fmt.Println("Float sum:", floatSum)

		//We reassign the value of floatSum like below. We are not using the := operator, because the floatSum variable in this case has already been initialised.
		floatSum = math.Round(floatSum*100) / 100
    fmt.Println("The sum is now", floatSum)
}
```
* The output we then see is the expected of `164.9`.
* Another tool from the `math` package with useful constants.
```
package main

import (
			"fmt"
			"math"
)

func main() {
		//Go compiler recognises these and then implicitly sets the types of the variables to int
		i1, i2, i3 := 12, 45, 68
		// We now add the values together:
		intSum := i1 + i2 + i3
		fmt.Println("Integer sum:", intSum)
		
		f1, f2, f3 := 23.5, 65.1, 76.3
		floatSum := f1 + f2 + f3
		fmt.Println("Float sum:", floatSum)

		//We reassign the value of floatSum like below. We are not using the := operator, because the floatSum variable in this case has already been initialised.
		floatSum = math.Round(floatSum*100) / 100
    fmt.Println("The sum is now", floatSum)
	
	  circleRadius := 15.5
	  // The "circleRadius * 2" is the diameter. The constant is "math.Pi"
	  circumference := circleRadius * 2 * math.Pi
	  // We now need to do formatting on the number with:
	  // The %.2f is a floating number with two digits after the decimal
	  fmt.Printf("Circumference: %.2f", circumference)
}
```
* The output code would then output the following:
```
Circumference: 97.39
```