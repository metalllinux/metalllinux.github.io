---
title: "How to Move Files in Emacs"
category: "editors-and-tools"
tags: ["editors-and-tools", "move", "files", "emacs"]
---

# How to Move Files in Emacs

To move files in Emacs, you can use **Dired mode** (Emacs' built-in file manager), which makes it straightforward. Here's how:

---

### ✅ **Steps to Move a File Using Dired:**

1. **Open Dired**
   Press: `C-x d` (that’s `Ctrl + x`, then `d`)
   Then enter the directory path where your file is located and press `RET`.

2. **Mark the File(s) to Move**
   Move the cursor to the file you want to move, then press `m` to mark it.
   (You can mark multiple files if needed.)

3. **Copy or Rename (Move)**

   * To **move**, press `R` (`Shift + r`) — stands for **Rename**.
   * You'll be prompted for a destination. Enter the full path, or just the target directory.

     * If the destination is a directory, the file(s) will be moved there.
     * If it's a filename, the file will be renamed/moved accordingly.

4. **Confirm**
   Press `y` to confirm the move.

---

### 🧠 Notes:

* Emacs uses "Rename" (`R`) to move files — it renames the file, possibly to a different directory.
* If you just want to copy (not move), use `C` in Dired mode instead of `R`.

---
