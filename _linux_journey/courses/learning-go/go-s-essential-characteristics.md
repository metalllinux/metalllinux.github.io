---
title: "Go S Essential Characteristics"
category: "learning-go"
tags: ["learning-go", "essential", "characteristics"]
---

* Compiled or Interpreted?
	* Example of Interpreted language is JavaScript.
	* JavaScript source code is read directly in the browser. Then executed at runtime.
	* No pre-compilation step required.
		* Sometimes there is an intermediary format such as bytecode.
		* Typically no precompilation steps that need to be followed.
	* A compiled language is transformed into something specific to an operating system.
		* C and C++ are good examples of compiled languages.
	* Go is compiled and statically typed language.
		* Therefore, its variables have specific types.
		* No need to always specifically declare the types.
		* Always known at compilation time.
		* Can feel like an interpreted language, because you can run a sourcecode file without the need to recompile.
		* In the background, a source file is being created in the background.
		* The compilation tool is also only known as `Go`.
		* Compiled executables are OS specific.
* Applications built with Go have a statically linked run time.
* Run-time component is compiled with the application.
* No external Virtual Machine being used for the compilation.
	* For example with Java, application is compiled into bytecode and the JVM machine can then run that on the OS of choice.
	* Therefore the Runtime
* Go is kind of Object-oriented.
	* Define custom interfaces.
	* Custom types can implement one or more interface .
	* Almost everything is a `type` in Go and every type uses an Interface.
	* Custom types can have member methods.
	* Custom structs (data structures) can have member fields.
		* Similars to classes in C# and Java.
* Go does not support:
	* Type inheritance (no classes)
		* Can't create a `type` and say that will be the super type and then create a subtype which can inherit features from the super type.
	* No Method or operator overloading.
		* Cannot have more than one method in a type that has the same name.
	* No Structured exception handling.
		* C and C# has this.
		* No `try`, `catch` or `finally` keywords.
			* Error objects are returned by functions, which might generate those errors.
* Then you use conditional logic, to examine the error objects.
	* No Implicit numeric conversions. Must explicitly type every variable.
	* Must implicitly type it and say where you are getting the data from.
* If you want to convert a value from one type to another in Go, must be done explicitly, by wrapping the function in a value that wants to be X type.
* The main reason you cannot find these language features in Go, is because a lot of features are common in advanced languages, which ultimately make these languages harder to read and more susceptible to bugs.
* Go was originally designed as a next-generation language for C.
	* This includes Systems Programming, Application Development and so on.
	* Borrows some syntax from C, as well as C++, C#, Java and more.
	* Borrows from Pascal, Modula and Oberon.
* Don't have to do as much typing in Go - characters are very precise.
* 