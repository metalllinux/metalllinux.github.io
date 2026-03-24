---
title: "Encodes as a list of (char, count) tuples"
category: "python-essential-training"
tags: ["python-essential-training", "ascii", "art", "compression", "solution"]
---

* Three basic types of data compression.
* `encodeFile` needs to call `encodeString`
* `decodeFile` needs to call `decodeString`

```
import os

import json

# Encodes as a list of (char, count) tuples
    def encodeString(stringVal):
        encodedList = []
        prevChar = None
        count = 0
        for char in stringVal:
            if prevChar != char and prevChar is not None:
                encodedList.append((prevChar, count))
                count = 0
            prevChar = char
            count = count + 1
        encodedList.append((prevChar, count))
        return encodedList
    
    def decodeString(encodedList):
        decodedStr = ''
        for item in encodedList:
            try:
                decodedStr = decodedStr + item[0] * item[1]
            except:
                print(item)
        return decodedStr

def encodeFile(filename, newFilename):
        with open(filename) as f:
            data = encodeString(f.read())
    		# We grab the JSON blob from above and is then written to a file like below
        with open(newFilename, 'w') as f:
            f.write(json.dumps(data))
    
    
    def decodeFile(filename):
        with open(filename) as f:
            data = f.read()
        return decodeString(json.loads(data))
		
print(f'Original file size: {os.path.getsize(\10_04_challenge_art.txt\)}'),

# This takes in a new file name
encodeFile('10_04_challenge_art.txt', '10_04_challenge_art_encoded.txt')

print(f'New file size: {os.path.getsize(\10_04_challenge_art_encoded.txt\)}')
    print(decodeFile('10_04_challenge_art_encoded.txt'))
```
* Running the above will then output:
```
Original file size: 2757
New file size: 2441
Outputs the ASCII art below.
```
* Keep in mind the characters that are in a JSON file, commas, apostrophes, brackets etc all take up space.
* To further improve the compression, we can do:
```
# [('A', 1), ('B', 80), ('C', 10)]
# This outputs | ~ | ~ in that pattern instead
    # becomes A|1~B|80~C|10
    def encodeFile(filename, newFilename):
        with open(filename) as f:
            data = encodeString(f.read())
    
        data = [f'{char}|{count}' for char, count in data]
        
        with open(newFilename, 'w') as f:
            f.write('~'.join(data))
    
    # The decoder then splits the data and puts it into pairs
    def decodeFile(filename):
        with open(filename) as f:
            data = f.read()
            
        pairs = data.split('~')
        pairs = [p.split('|') for p in pairs]
				 # This is the stage where it is placed into pairs
        pairs = [(p[0], int(p[1])) for p in pairs]
        return decodeString(pairs)
```
* Running that, we then get:
```
Original file size: 2757
New file size: 1007
Outputs the ASCII art below.
```
* Even more improved solution than the last.
* You can store any integer up to 255 in a single byte (or single character's worth of data) of data.
```
def encodeFile(filename, newFilename):
        with open(filename) as f:
            data = encodeString(f.read())
        output = bytearray()
        for item in data:
            # Character byte
            output.extend(bytes(item[0], 'utf-8'))
            # Integer count byte
            output.extend(item[1].to_bytes(1, 'big'))
        with open(newFilename, 'wb') as binary_file:
            # Write bytes to file
            binary_file.write(output)
			
def decodeFile(filename):
				with open(filename, 'rb') as f:
					data = f.read()
					# Split data into pairs 
					bytePairs = [data[i:i+2] for i in range(0, len(data), 2)]
					encodedList = []
					for bytePair in bytePairs:
						encodedList.append((bytePair[:1].decode('utf-8'), int.from_bytes(bytePair[1:], 'big')))
					return decodeString(encodedList)

print(f'Original file size: {os.path.getsize(\10_04_challenge_art.txt\)}'),
encodeFile('10_04_challenge_art.txt', '10_04_challenge_art_encoded.aa')

print(f'New file size: {os.path.getsize(\10_04_challenge_art_encoded.aa\)}')
print(decodeFile('10_04_challenge_art_encoded.aa'))
```
* The above outputs the file at `466` bytes.