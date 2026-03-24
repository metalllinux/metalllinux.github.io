---
title: "My Sed Commands"
category: "editors-and-tools"
tags: ["editors-and-tools", "sed", "commands"]
---

sed 's/"//g'

Removes all " characters from a file

sed 's/ //g'

Deletes all spaces in a file

sed 's/,//g'

Removes all , characters from a file

sed 's/*//g'

Removes all * characters from a file

sudo sed -i 's/<text_1>/<text_2>/g' <file>

Easily change the MARTINI CONTAINER LIMIT (then place this into an ansible command)

Adding `toArray()` at the end of commands:

cat <file>h | sed 's/}})/}}).toArray()/g'

How filter out specific hosts:

sed 's/non-zero return code//g' output.txt | sed 's/ | FAILED | rc=1 >>//g' | sed 's/host[3,4,5,9,11,12,13,17,18,19]//g'

Removing single quote and `-e` from a file:

sed -e "s/'//g" <file>| sed -e 's/-e//g'