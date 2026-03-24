---
title: "Encoding Ascii Art Solution"
category: "python-essential-training"
tags: ["python-essential-training", "encoding", "ascii", "art", "solution"]
---

* If you encode a string multiple times, such as like with `AAAAABBBBAAA` as a list of Tuples for example. This is called `Run Length Encoding` in Computer Science.
	* You run along the string and record the character and count as you go along.
	* Useful for compressing data that does not have a lot of variation in it or has long stretches of the same character over and over again.
* For the challenge, two functions have to be written:
	* `encodeString` --> Take in the string and encode it into a list of Tuples.
	* `decodeString` --> Takes in the list of Tuples and returns the original string afterwards.
```
{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "6a6c3649",
   "metadata": {},
   "source": [
    "## ASCII Art Encoding",
    "",
    "Write a function \"encodeString\" that will encode a string like 'AAAAABBBBAAA' as a list of tuples: [('A', 5), ('B', 4), ('A', 3)] meaning that the string has \"5 A's, followed by 4 B's, followed by 3 A's\"",
    "",
    "Then use that function to compress a string containing \"ASCII Art\" (https://en.wikipedia.org/wiki/ASCII_art)",
    "",
    "Write a corresponding function \"decodeString\" that will take in a list of tuples and print the original string."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7777d38e",
   "metadata": {},
   "outputs": [],
   "source": [
 # stringVal is the item we want to loop through
    "def encodeString(stringVal):",
# During the looping we keep track of three things
    "    encodedList = []",
# This is so we know when the string has changed. If the current character does not meet the previous character, we know we have to stop and add something to the encoded list. The prevChar also starts as the first character in the string, therefore we never detect a change whilst still on the first character
    "    prevChar = stringVal[0]",
# count starts at zero and keeps track of how many characters we have gone through without seeing any change
    "    count = 0",

    "    for char in stringVal:",
# If the previous character is not equal to the current character, we have seen a change
    "        if prevChar != char:",
# When we detect a change, we add that previous character and count to our list.
    "            encodedList.append((prevChar, count))",
# count is set back to zero
    "            count = 0",
    "        prevChar = char",
# We keep looping through afterwards
    "        count = count + 1",
    "    ",
# Once we reach the end of our string, we record the last few characters and we append a new Tuple
    "    encodedList.append((prevChar, count))",
# Ultimately this is then returned from the function
    "    return encodedList",
    "",
    "def decodeString(encodedList):",
    "    decodedStr = ''",
# We go through each item in the list
    "    for item in encodedList:",
# We multiply the count by the character within it. Count is `item[1]` and the character is `item[0]`. When you multiple a string by a number, the string is multiplied X amount of times
    "        decodedStr = decodedStr + item[0] * item[1]",
    "    return decodedStr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "bb768c53",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('A', 5), ('B', 4), ('C', 3)]"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Test encodeString function",
    "encodeString('AAAAABBBBCCC')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "706659bd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'AAAAABBBBCCC'"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Test decodeString function",
    "decodeString([('A', 5), ('B', 4), ('C', 3)])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "3eee6256",
   "metadata": {},
   "outputs": [],
   "source": [
    "art = '''",
    "",
    "                                                                                ",
    "                                                                                ",
    "                               %%%%%%%%%%%%%%%%%%%                              ",
    "                        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                       ",
    "                    %%%%%%%%                         %%%%%%%%                   ",
    "                %%%%%%%                                   %%%%%%                ",
    "              %%%%%%                                         %%%%%%             ",
    "           %%%%%%                                               %%%%%           ",
    "          %%%%%                                                   %%%%%         ",
    "        %%%%%                                                       %%%%%       ",
    "       %%%%                 %%%%%              %%%%%                  %%%%      ",
    "      %%%%                 %%%%%%%            %%%%%%%                  %%%%     ",
    "     %%%%                  %%%%%%%            %%%%%%%                   %%%%    ",
    "    %%%%                   %%%%%%%            %%%%%%%                    %%%%   ",
    "    %%%%                    %%%%%              %%%%%                     %%%%   ",
    "   %%%%                                                                   %%%%  ",
    "   %%%%                                                                   %%%%  ",
    "   %%%%                                                                   %%%%  ",
    "   %%%%                                                      %%%%        %%%%   ",
    "    %%%%       %%%%%%                                        %%%%%       %%%%   ",
    "    %%%%         %%%%                                       %%%%        %%%%    ",
    "     %%%%         %%%%                                     %%%%         %%%%    ",
    "      %%%%         %%%%%                                  %%%%         %%%%     ",
    "       %%%%%         %%%%%                             %%%%%         %%%%%      ",
    "        %%%%%          %%%%%%                        %%%%%          %%%%        ",
    "          %%%%%           %%%%%%%               %%%%%%%           %%%%%         ",
    "            %%%%%             %%%%%%%%%%%%%%%%%%%%%             %%%%%           ",
    "              %%%%%%%                                        %%%%%              ",
    "                 %%%%%%%                                 %%%%%%%                ",
    "                     %%%%%%%%%                     %%%%%%%%%                    ",
    "                          %%%%%%%%%%%%%%%%%%%%%%%%%%%%%                         ",
    "                                   %%%%%%%%%%%%                                 ",
    "                                                                                ",
    "                                                                                 ",
    "",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "dec27033",
   "metadata": {},
   "outputs": [],
   "source": [
    "encodedString = encodeString(art)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "942d4ff8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "",
      "",
      "                                                                                ",
      "                                                                                ",
      "                               %%%%%%%%%%%%%%%%%%%                              ",
      "                        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                       ",
      "                    %%%%%%%%                         %%%%%%%%                   ",
      "                %%%%%%%                                   %%%%%%                ",
      "              %%%%%%                                         %%%%%%             ",
      "           %%%%%%                                               %%%%%           ",
      "          %%%%%                                                   %%%%%         ",
      "        %%%%%                                                       %%%%%       ",
      "       %%%%                 %%%%%              %%%%%                  %%%%      ",
      "      %%%%                 %%%%%%%            %%%%%%%                  %%%%     ",
      "     %%%%                  %%%%%%%            %%%%%%%                   %%%%    ",
      "    %%%%                   %%%%%%%            %%%%%%%                    %%%%   ",
      "    %%%%                    %%%%%              %%%%%                     %%%%   ",
      "   %%%%                                                                   %%%%  ",
      "   %%%%                                                                   %%%%  ",
      "   %%%%                                                                   %%%%  ",
      "   %%%%                                                      %%%%        %%%%   ",
      "    %%%%       %%%%%%                                        %%%%%       %%%%   ",
      "    %%%%         %%%%                                       %%%%        %%%%    ",
      "     %%%%         %%%%                                     %%%%         %%%%    ",
      "      %%%%         %%%%%                                  %%%%         %%%%     ",
      "       %%%%%         %%%%%                             %%%%%         %%%%%      ",
      "        %%%%%          %%%%%%                        %%%%%          %%%%        ",
      "          %%%%%           %%%%%%%               %%%%%%%           %%%%%         ",
      "            %%%%%             %%%%%%%%%%%%%%%%%%%%%             %%%%%           ",
      "              %%%%%%%                                        %%%%%              ",
      "                 %%%%%%%                                 %%%%%%%                ",
      "                     %%%%%%%%%                     %%%%%%%%%                    ",
      "                          %%%%%%%%%%%%%%%%%%%%%%%%%%%%%                         ",
      "                                   %%%%%%%%%%%%                                 ",
      "                                                                                ",
      "                                                                                 ",
      "",
      ""
     ]
    }
   ],
   "source": [
    "print(decodeString(encodedString))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e1485f53",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

```