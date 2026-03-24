---
title: "If Writing Directly to a File in Warewulf and Why Not to Do it"
category: "rocky-linux"
tags: ["rocky-linux", "writing", "directly", "file", "warewulf"]
---

# If Writing Directly to a File in Warewulf and Why Not to Do it

So if they are writing /etc/passwd directly, they are doing it wrong.  I assume they have a script that is writing out that file from some central management or is warewulf doing it?  Either way the right way to do it is to write the password file in a temp location ( it can even be /etc/passwd.new) and then use an atomic operation like mv to shift it into place.  Writing to a file isn't an atomic operation.

