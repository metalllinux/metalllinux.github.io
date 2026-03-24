---
title: "Explore Basic Go Syntax"
category: "learning-go"
tags: ["learning-go", "explore", "basic", "syntax"]
---

* Go is case sensitive.
	* Identifiers such as function, variable and type names have to be spelt exactly.
	* Most variable and package are lower and mixed case.
		* Methods however (functions belonging to types)
		* Fields (variables that are members of types)
			* Both of these frequently have uppercase characters.
	* An initial uppercase character in Go, means the symbol is exported.
		* The equivalent of the keyword `public` in other langues like Java and C#.
	* A lowercase initial character means that the field or method isn't exported and isn't available to the rest of the application.
* Semicolons are not usually needed.
	* Line feed ends a statement - no semicolon is required.
		* No need for semicolons at the end of lines.
	* For example, this is an array in Go:
```
var colours [2]string
colours[0] = "black"
colours[1] = "white"
```
* Semicolons are part of the formal language spec, but not needed to be typed.
	* The `lexer` (software component that parses and analyses the code), adds them during the compilation process.
		* This means that GO is sensitive to whitespace.
			* Including line feeds, tabs and so on.
* The semicolons are added when the statement is complete and the Lexer detects a line feed (end of statement).
	* It therefore means that you cannot always add line feeds freely or break up line statements as you would do in other languages.
		* In certain circumstances, these can be misinterpreted by the Lexer.
* Code blocks are wrapped with braces.
	* This is an example code block:
```
sum := 0
for i := 0; i < 10; i++ {
	 sum += i
}
fmt.Println(sum) //prints '45'
```
* In the above example, a variable name called `sum` is being declared and then looping from 0 to 10. The value is being incrementally added every time. The value is then output using a function `Println` (Print Line). This is a member of a package called `fmt` and the value of `45` is then output.
	* The first brace in the code block, **must** be on the same line as any proceeding statement. Cannot drop the brace to the next blank line.
	* Go has a set of builtin functions, that are always available in your code. No requirement to import anything.
		* The functions are members of a special package called `builtin`.
		* Go compiler assumes that the Go package is always imported.
* Example built-in packages:
	* `len(string)` - returns the length of a string.
	* `panic(error)` - stops execution; displays error message.
	* `recover()` - manages behaviour of a panicking goroutine.
* Can learn more about those packages, as well as other functions and types, at:
* https://golang.org/pkg/builtin