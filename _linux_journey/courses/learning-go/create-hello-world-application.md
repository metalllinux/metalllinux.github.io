---
title: "This is required for each source file"
category: "learning-go"
tags: ["learning-go", "create", "hello", "world", "application"]
---

* The resulting file should be all lowercase.
* `.go` extension is required for all source code files.
* The name of the file before the extension should be all lowercase with no white spaces.
* The code has to be part of the following package and always needs the following at the top:
```
# This is required for each source file
package main
# Required for any packages to be used in the application. If only use one package, can place it all on a single line. The "fmt" package in this case stands for "formatting"
# If using more than one package,
import "fmt"

func main() {
	fmt.Println("vim-go")
}
```
* If adding multiple packages, can wrap the code like the following:
```
package main

import (
     "fmt"
)
```
* `fmt` specifies the formatting package that contains `Println`
* The other requirement for the file to serve as a startup file, is that we also need another function called `main()`
* All functions in Go start with the `func` keyword. The function names start with a lowercase character if they are private to this file or an uppercase character if they are public.
* If using an IDE like VSCode, can use:
```
go run <file.go>
go run .
go build .
```
* Once you run `go build .`, it creates a binary file specifically designed for a particular operating system.