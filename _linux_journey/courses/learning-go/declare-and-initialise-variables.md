---
title: "Declare And Initialise Variables"
category: "learning-go"
tags: ["learning-go", "declare", "initialise", "variables"]
---

* Cannot change variable types at runtime, because the types are static.
* With Go's syntax, cannot set types either explicitly or implicitly.
* An example of setting a variable name explicitly:
```
package main

import (
	"fmt"
)

func main() {

	var aString string = "This is Go!"

	fmt.Println(aString)
}
```
* Can find out the type of the variable that is used, by using the `Printf` function.
```
package main

import (
	"fmt"
)

func main() {

	var aString string = "This is Go!"
	fmt.Println(aString)
	fmt.Printf("The variable's type is %T")
}
```
* The `%T` is know as a `verb` or a `placeholder`. This will output the following:
```
:!'go' 'run' '/home/howard/learning-go-2875237/practice/main.go'  2>&1| tee /tmp/nvim.howard/MVnh52/3
This is Go!
The variable's type is string
```
* If we then run the following, it will be concatenated to the previous output:
```
package main

import (
	"fmt"
)

func main() {

	var aString string = "This is Go!"
	fmt.Println(aString)
	fmt.Printf("The variable's type is %T", aString)

	var anInteger int = 42
	fmt.Println(anInteger)
}
```
* This looks like:
```
:!'go' 'run' '/home/howard/learning-go-2875237/practice/main.go'  2>&1| tee /tmp/nvim.howard/MVnh52/5                                                                                                                               
This is Go!
The variable's type is string42
```
* Therefore, need to add a line feed (new line), like so:
```
package main

import (
	"fmt"
)

func main() {

	var aString string = "This is Go!"
	fmt.Println(aString)
	fmt.Printf("The variable's type is %T\n", aString)

	var anInteger int = 42
	fmt.Println(anInteger)
}
```
* This then outputs:
```
:!'go' 'run' '/home/howard/learning-go-2875237/practice/main.go'  2>&1| tee /tmp/nvim.howard/MVnh52/8
This is Go!
The variable's type is string
42
```
* Running the following shows that the default value is `0`:
```
package main

import (
	"fmt"
)

func main() {

	var aString string = "This is Go!"
	fmt.Println(aString)
	fmt.Printf("The variable's type is %T\n", aString)

	var anInteger int = 42
	fmt.Println(anInteger)

	var defaultInt int
	fmt.Println(defaultInt)
}
```
* This outputs the following:
```
:!'go' 'run' '/home/howard/learning-go-2875237/practice/main.go'  2>&1| tee /tmp/nvim.howard/rnzMUc/3
This is Go!
The variable's type is string
42
0
```
* Again, for Explicit Typing, we have to say this is the variable and this is its type.
* For Implicit Typing, these are inferred based on initial values that are assigned to them.
```
package main

import (
	"fmt"
)

func main() {

	var aString string = "This is Go!"
	fmt.Println(aString)
	fmt.Printf("The variable's type is %T\n", aString)

	var anInteger int = 42
	fmt.Println(anInteger)

	var defaultInt int
	fmt.Println(defaultInt)

	var anotherString = "This is another string"
	fmt.Println(anotherString)
	fmt.Printf("The variable's type is %T\n", anotherString)
}
```
* This then outputs:
```
:!'go' 'run' '/home/howard/learning-go-2875237/practice/main.go'  2>&1| tee /tmp/nvim.howard/rnzMUc/6                                                                                                                                
This is Go!
The variable's type is string
42
0
This is another string
The variable's type is string
```
* Another style to initialise variables, is using an operator called `:=`. An example is:
```
package main

import (
	"fmt"
)

func main() {

	var aString string = "This is Go!"
	fmt.Println(aString)
	fmt.Printf("The variable's type is %T\n", aString)

	var anInteger int = 42
	fmt.Println(anInteger)

	var defaultInt int
	fmt.Println(defaultInt)

	var anotherString = "This is another string"
	fmt.Println(anotherString)
	fmt.Printf("The variable's type is %T\n", anotherString)

	var anotherInt = 53
	fmt.Println(anotherInt)
	fmt.Printf("The variable's type is %T\n", anotherInt)

	myString := "This is also a string"
	fmt.Println(myString)
	fmt.Printf("The variable's type is %T\n", myString)
}
```
* The `:=` operator only works for variables inside of functions.
	* If you declare variables outside of functions, you must use the `var` keyword.
	* This is also true for another variable type, called a `constant`.
	* `constant`'s can be declared outside of functions.
* An example of using `const`
	* The type can be either explicit or implicit.
```
package main

import (
	"fmt"
)

const aConst int = 64

func main() {

	var aString string = "This is Go!"
	fmt.Println(aString)
	fmt.Printf("The variable's type is %T\n", aString)

	var anInteger int = 42
	fmt.Println(anInteger)

	var defaultInt int
	fmt.Println(defaultInt)

	var anotherString = "This is another string"
	fmt.Println(anotherString)
	fmt.Printf("The variable's type is %T\n", anotherString)

	var anotherInt = 53
	fmt.Println(anotherInt)
	fmt.Printf("The variable's type is %T\n", anotherInt)

	myString := "This is also a string"
	fmt.Println(myString)
	fmt.Printf("The variable's type is %T\n", myString)
}
```
* The above constant is available to any function within the file. For example, an uppercase initial character would make it public. 
* To check the contents of a `constant`, we can add the line like so:
```
package main

import (
	"fmt"
)

const aConst int = 64

func main() {

	var aString string = "This is Go!"
	fmt.Println(aString)
	fmt.Printf("The variable's type is %T\n", aString)

	var anInteger int = 42
	fmt.Println(anInteger)

	var defaultInt int
	fmt.Println(defaultInt)

	var anotherString = "This is another string"
	fmt.Println(anotherString)
	fmt.Printf("The variable's type is %T\n", anotherString)

	var anotherInt = 53
	fmt.Println(anotherInt)
	fmt.Printf("The variable's type is %T\n", anotherInt)

	myString := "This is also a string"
	fmt.Println(myString)
	fmt.Printf("The variable's type is %T\n", myString)

	fmt.Println(aConst)
	fmt.Printf("The variable's type is %T\n", aConst)
}
```
* The output would then be:
```
:!'go' 'run' '/home/howard/learning-go-2875237/practice/main.go'  2>&1| tee /tmp/nvim.howard/rnzMUc/12
[No write since last change]
This is Go!
The variable's type is string
42
0
This is another string
The variable's type is string
53
The variable's type is int
This is also a string
The variable's type is string
64
The variable's type is int
```