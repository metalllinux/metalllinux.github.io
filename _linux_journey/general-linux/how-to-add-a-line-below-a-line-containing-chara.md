---
title: "How To Add A Line Below A Line Containing [] Chara"
category: "general-linux"
tags: ["add", "line", "below", "line", "containing"]
---

`sed -i '/\[.*\]/a\enabled=0' <file_name>`
sed -i performs in-place editing of the file.
/\[.*\]/ matches a line that contains [] characters.
a\ tells sed to append the following text to the matched line.
enabled=0 is the text that will be added on a new line after the matched line.