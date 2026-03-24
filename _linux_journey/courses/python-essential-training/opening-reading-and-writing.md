---
title: "Opening, Reading And Writing"
category: "python-essential-training"
tags: ["python-essential-training", "opening", "reading", "writing"]
---

* Sometimes you are given files and you have to read them.
* We need to manage whether we are reading a contents of a file or making changes to it and writing to it.
	* This is due to if two applications are writing to a file at the same time.
* Reading Files. In the example below, the file will be opened in `read` mode.
```
f = open('10_01_file.txt', 'r')
print(f)
```
* The output is a file object:
```
<_io.TextIOWrapper name='10_01_file.txt' mode='r' encoding='UTF-8'>
```
* To get the text inside the file, we do:
```
# This reads the lines of the file one at a time. Every time this is run, a different file is displayed. The file object contains bookmarks of the files it has already read. It is possible to place this in a loop to read all lines of a file, however, we can do:
f.readline()
```
```
# This reads all of the lines of the file. It gets all the lines of the file that have not been read already and places them into a list of strings.
f.readlines()
```
* provides the following output as an example:
```
Complex is better than complicated \n
```
* We can also perform it this way as well:
```
f = open('10_01_file.txt', 'r')
for line in f.readlines():
		 print(line)
```
* All of the lines will be output double spaced.
* That is because each line has a newline character at the end of it.
	* Remember, the `print` statement also includes new lines as well.
* We can remove any leading or separate spaces/white lines with:
```
f = open('10_01_file.txt', 'r')
for line in f.readlines():
		 print(line.strip())
```
* The output for that would be;
```
Beautiful is better than ugly.
Hot is better than not.
etc
```
* Writing Files
* We do this for example with:
```
f = open('10_01_output.txt', 'w')
print(f)
```
* Once the above is ran, a file will be created.
```
f.write('Line 1')
f.write('Line 2')
```
* The output for example is `6.`
* Writing to files is a generally expensive operation. It only writes to the buffer when the buffer becomes full. 
* We can close the file with `f.close()`
* A newline character is not printed between the lines.
	* To add this we can do:
```
f.write('Line 1\n')
f.write('Line 2\n')
```
* If it is the same file that is written to, Python will overwrite the existing data in that file.
* Appending Files
* To continue to add additional data to a file, we can open that file in `append mode`
```
f = open('10_01_output.txt', 'a')
f.write('Line 3\n')
f.write('Line 4\n')
# This releases the file and tells the operating system that all writes have been completed. The files do eventually get closed and there is a process in Python that cleans them up. The behaviour is unpredictable though. It is best practice to close them once done with however.
f.close()
```
* The most common way is to close using the `with` statement.
```
with open('10_01_output.txt', 'a') as f:
    f.write('blah blah\n')
	  f.write('other stuff\n')
```
* As soon as we out-dent the above code block, the above file is closed.
* Running just `f.write('I forgot stuff')` also willl not work. You have to run the `close()` function.