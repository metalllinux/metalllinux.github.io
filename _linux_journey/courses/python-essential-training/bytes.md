---
title: "Bytes"
category: "python-essential-training"
tags: ["python-essential-training", "bytes"]
---

* This is a Python Byte Object
	* Common behind the scenes.
	* These are used as data is passed into a program.
	* Rarely manipulated or modified directly.
	* Byte Objects are a sequence of data.
		* 101010101010111
* Byte Object Common Uses:
	* Streaming files.
	* Transmitting text without knowing the encoding.
	* Often used "under the hood" in Python.
* To create a bytes object, we use:
```
bytes(4)
```
* Output is `b'\x00\x00\x00\x00'`
	* The command creates an empty Bytes Object.
	* The above output is 4 bytes long.
		* Followed by `x` and then two hexadecimal base 16 numbers.
			* Two hexadecimal numbers is 256 possibilities.
			* Same as 2 to the power of 8 or 8 bits.
				* There are 8 bites to a byte.
					* The `b` above is to differentiate it from a regular string.
* To create a bytes object with data inside of it.
```
smileyBytes = bytes('EYE_ROLL', 'utf-8')
smileyBytes
```
Outputs: `b'\xf0\z4t\x11\x65'` for example.
		* Need to tell Python what Type the bytes object is, so it can find and isolate the data.
			* Emojis are encoded in utf-8.
				* UTF-8 --> Unicode Transformation Format.
* How do you take a bytes object and represent it as a string again? Need the `decode` function.
	* `smileyBytes.decode('utf-8')`
		* Then the output the EYE_ROLL emoji.
* Bytes Objects are immutable, like tuples.
	* If we want byte data that we can modify, we use a Byte Array.
```
smileyBytes = bytearray('EYE_ROLL', 'utf-8')
smileyBytes
```
* Outputs `bytearray(b'\xf0\x9f\x99\x84')`
	* Can modify a specific value, using the String Slice Notation.
	* To get hexadecimal 85, we use the `int` library.
```
# Uses base 16.
smileyBytes[3] = int('85', 16)
```
* Then we run `smileyBytes.decode('utf-8')` and receive a SHRUG emoji.