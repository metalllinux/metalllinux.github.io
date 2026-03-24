---
title: "Converts a string hexadecimal number into an integer decimal"
category: "python-essential-training"
tags: ["python-essential-training", "converting", "hex", "decimal", "challenge"]
---

* Not using the interclass or other Python Conversion Tools.
* Write a function tha take sa string hexadecimal number and convert it to an integer decimal.
```
hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}
    
# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
# Assuming that everything sent into the function is a string
"def hexToDec(hexNum):
# We are going through every character in hexNum and making sure it is something that can be processed.
     for char in hexNum:
     if char not in hexNumbers:
         return None

# There are three cases listed below, 1,2 and 3 character strings
     if len(hexNum) == 3:

# 256 below is the 256th place in a hexadecimal number
# The middle number is then multiplied by 16, because it is in the 16th place.
         return hexNumbers[hexNum[0]] * 256 + hexNumbers[hexNum[1]] * 16 + hexNumbers[hexNum[2]]
# This one is the once place and is added on    
     if len(hexNum) == 2:
         return hexNumbers[hexNum[0]] * 16 + hexNumbers[hexNum[1]]
 
     if len(hexNum) == 1:
         return hexNumbers[hexNum[0]]"

# Test cases for these are:

# 10
hexToDec('A')

# 0
hexToDec('0')

# 27
hexToDec('1B')

# 960
hexToDec('3CQ')

# None
hexToDec('A6G')

# None
hexToDec('ZZTOP')
```
* Another solution to handle hexadecimal strings at any length, is the following:
```
"def hexToDec(hexNum):
# We are going through every character in hexNum and making sure it is something that can be processed.
     for char in hexNum:
     if char not in hexNumbers:
         return None
		 
		 exponent = 0
		 decimalValue = 0
		 # Here, we iterate through the characters backwards
		 for char in hexNum[::-1]:
		 # In each loop, we take the number and multiply it by 16
		 		 decimalValue = decimalValue + hexNumbers[char] * (16**exponent)
			# 1 is added every time we loop through
			# 16 to the zeroth power is 1.
				 exponent = exponent + 1
			
			return decimalValue

# 960
hexToDec('3C0')

# 3932160
hexToDec('3C0000')
```
* If you run into a programming problem, where you are not sure how to do it at first. **Try narrowing the scope**.
	* How do you do it for 1, 2 or 3 characters? Try to find the pattern, get a feel for it and then approach the general case.
* Multiline strings are surround by the following `'''Some string'''`