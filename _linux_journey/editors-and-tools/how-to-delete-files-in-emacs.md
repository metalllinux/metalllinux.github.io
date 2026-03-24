---
title: "How to Delete Files in Emacs"
category: "editors-and-tools"
tags: ["editors-and-tools", "delete", "files", "emacs"]
---

# How to Delete Files in Emacs

In Emacs' Dired mode, you can delete a file by following these steps:

1. Open Dired by running `M-x dired` and navigating to the directory containing the file.
2. Move the cursor to the file you want to delete.
3. Press `d` to mark the file for deletion.
4. If you want to delete multiple files, mark them individually using `d`.
5. Once all files are marked, press `x` to execute the deletion.

Emacs will ask for confirmation before permanently removing the files. If you want to bypass the confirmation prompt, use `D` instead of `d` to delete the file immediately.
