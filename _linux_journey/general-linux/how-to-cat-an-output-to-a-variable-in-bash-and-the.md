---
title: "How To Cat An Output To A Variable In Bash And The"
category: "general-linux"
tags: ["cat", "output", "variable", "bash"]
---

* Firstly add the output to the variable:
```
<VARIABLE_NAME_1>=$(cat <FILE_1>)
```
* Then create the second variable:
```
<VARIABLE_NAME_2>=$(cat <FILE_2>)
```
* Check the contents of the variable with `echo "$<VARIABLE_NAME>"`
* Show the variables side-by-side like so:
```
diff <(echo "$VARIABLE_1") <("echo $VARIABLE_2")
```
* Else if the above does not work, output each variable into a file and compare them that way:
```
echo "$VARIABLE_1" > temp1
echo "$VARIABLE_2" > temp2
```