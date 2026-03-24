---
title: "Command Line Arguments"
category: "python-essential-training"
tags: ["python-essential-training", "command", "line", "arguments"]
---

* Can pass in multiple command line arguments after running something like `python example.py`
* The command line arguments can be one of two types:
	* A single character, for instance `-h` for help.
		* If you run this, it usually prints out documentation about the program, with available commands.
		* They can also take values, for example `-i` for input, as an example: `python example.py -i somefile.txt`
			* argparse is a good way to check these.
* `argparse` provides an ArgumentParser class. This allows you to create an object and this object keeps track of all of the arguments that the program accepts.
```
from argparse import ArgumentParser 

parser = ArgumentParser()

# This parser is called `--output`. Since it is a full word, you need two dashes in front of it as per programming convention
parser.add_argument('--output', '-o', required=True, help='The destination file for the output of this program')
parser.add_argument('--text', '-t', required=True, help='The text to write to the file')

parser.add_argument('--output')

args = parser.parse_args()

with open(args.output, 'w') as f:
    f.write(args.text+'\n')

print(f'Wrote "{args.text}" to file "{args.output}"')
```
* We can provide an example filename like so:
```
python 11_1_writefile.py --output somefile.txt
```
* How do we get the value `somefile.txt`?
```
# The `args` here is the object, that has all of the attributes tied to it
args = parser.parser_args()
```
* We can then access the file like so:
```
print(args.output)
```
* Then when you run `python 11_1_writefile.py --output somefile.txt
` you see `somefile.txt` printed.
* To make the keyword required, we can add:
```
parser.add_argument('--output', required=True)
```
* Another useful keyword argument is `help`, that being. It provides some `help` text to the user, which lets them know what the command does.
```
parser.add_argument('--output', required=True, help='The destination file for the output of this program')
```
* Then when you run the program, you see:
```
python 11_1_writefile.py -h

usage: 11_1_writefile.py [-h] --output OUTPUT

options:
	-h, --help show this help message and exit
	--output OUTPUT The destination file for the output of this program
```
* If we also run the Python file without the arguments, we get an error:
```
python 11_1_writefile.py
~~~
the following arguments are required: --output
```
* We can add further arguments, such as with `-o`:
```
parser.add_argument('--output', '-o', required=True, help='The destination file for the output of this program')
```
* We can add another argument called `text` with:
```
parser.add_argument('--output', '-o', required=True, help='The destination file for the output of this program')
parser.add_argument('--text', '-t', required=True, help='The text to write to the file')
```
* To write to a new file, we do:
```
with open(args.output, 'w') as f:
    f.write(args.text+'\n')

# Add a line to inform the user the program has run successfully
print(f'Wrote "{args.text}" to file "{args.output}"')
```
* A newline character is added to the top of the text, to keep the lines clean.
* We can now write to the file with the following:
```
python 11_1_writefile.py -o somefile.txt -t "some text to write to the file"
```
* The output is then:
```
Wrote "some text to write to the file" to file "somefile.txt"
```
* Every time you have a value with spaes inside of it, you need to place quotes around the string.