---
title: "Scrollback In Screen"
category: "editors-and-tools"
tags: ["editors-and-tools", "scrollback", "screen"]
---

Press Ctrl+A then : and then type

scrollback 10000

to get a 10000 line buffer, for example.

You can also set the default number of scrollback lines by adding

defscrollback 10000

to your ~/.screenrc file.

To scroll (if your terminal doesn't allow you to by default), press Ctrl+A then Esc and then scroll (with the usual Ctrl+F for next page or Ctrl+A for previous page, or just with your mouse wheel / two-fingers). To exit the scrolling mode, just press Esc.

Another tip: Ctrl+A then I shows your current buffer setting.
