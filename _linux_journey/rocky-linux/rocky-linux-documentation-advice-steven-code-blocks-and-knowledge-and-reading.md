---
title: "Rocky Linux Documentation Advice from Steven on Code Blocks and Knowledge and Reading Time"
category: "rocky-linux"
tags: ["rocky-linux", "rocky", "linux", "documentation", "advice"]
---

# Rocky Linux Documentation Advice from Steven on Code Blocks and Knowledge and Reading Time

Greetings Howard, and thank you again for your PR for Kickstart on Rocky. I wanted to expand on a few of the changes that I made to your document. One thing that I did was format the entirety of the kickstart options for each version in code blocks (```). Without them, the formatting of those options was jumbled together one right after the other without a LF after each one. Making them a code block formats them in a way that is much more pleasing to the eye and, actually, is more like a kickstart configuration. 

Another thing to help you the next time you write a document (and PLEASE do that! We don't have enough good contributors) is that when you are putting in the "Knowledge" and "Reading Time" options at the top of the document as you've done, in order to have those appear on a separate line, you need to add 2 spaces after the stars in the "Knowledge" line. Otherwise they appear together on the same line, which works, but I'm sure based on the source of your document, that you really wanted them on their own lines. I fixed that up so that it would display correctly.

I use a copy of mkdocs locally installed so that I can actually see how the changes I'm making affect the document. That's very helpful if you are going to be writing more documentation (again, I hope that's the case). 

Anyway, nice job on the document and I hope we receive more from you in the future. 
