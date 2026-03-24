---
title: "Diff Command"
category: "general-linux"
tags: ["diff", "command"]
---

* https://www.geeksforgeeks.org/diff-command-linux-examples/

In the world of Linux, managing and comparing files is a common task for system administrators and developers alike. The ability to compare files line by line is crucial for identifying differences, debugging code, and ensuring the integrity of data. One powerful tool that facilitates this process is the `diff` command. In this article, we will explore how to use the `diff` command to compare files line by line in Linux.

Table of Content

- [Basic Syntax of diff Command](#basic-syntax-of-diff-command)
- [Options Available in diff Command](#options-available-in-diff-command)
- [Pratical Implementaion of How to compare files line by line in Linux? :](#pratical-implementaion-of-how-to-compare-files-line-by-line-in-linux-)
- [Comparing Two Files](#comparing-two-files)
- [Deleting a Line in Files using diff Command](#deleting-a-line-in-files-using-diff-command)
- [Viewing Differences in Context Mode](#viewing-differences-in-context-mode)
- [Viewing Differences in Unified Mode](#viewing-differences-in-unified-mode)
- [Case-Insensitive Comparing between Files](#caseinsensitive-comparing-between-files)
- [Displaying diff Version](#displaying-diff-version)

## Understanding the diff Command

diff stands for ****difference**** .The `diff` command is a versatile utility that is pre-installed on most Linux distributions. Its primary purpose is to compare the contents of two files and display the differences between them. The command provides a comprehensive way to highlight changes, additions, and deletions in a clear and readable format.

This command is used to display the differences in the files by comparing the files line by line. Unlike its fellow members, [cmp](https://www.geeksforgeeks.org/cmp-command-linux-examples/) and [comm](https://www.geeksforgeeks.org/comm-command-linux-examples/), it tells us which lines in one file have is to be changed to make the two files identical. 

The important thing to remember is that ****diff**** uses certain ****special symbols**** and ****instructions**** that are required to make two files identical. It tells you the instructions on how to change the first file to make it match the second file. 

## Basic Syntax of diff Command

The basic syntax of the `diff` command is as follows:

diff \[OPTION\]... FILE1 FILE2

Here, \`**`` FILE1` ``** and \`**`` FILE2` ``** are the two files you want to compare.

The \`**`` OPTION` ``** flag allows you to customize the behavior of the \`**`` diff` ``** command.

## Options Available in diff Command

| Option | Description |
| --- | --- |
| `-c` or `--context` | Output differences in context mode |
| `-u` or `--unified` | Output differences in unified mode (more concise) |
| `-i` or `--ignore-case` | Perform a case-insensitive comparison |
| –ignore-all-space | Ignore whitespace when comparing lines |
| –brief | Output only whether files differ, no details |
| –recursive | Recursively compare directories |
| `-y` or `--side-by-side` | Display the output in a side-by-side format |

## Pratical Implementaion of How to compare files line by line in Linux? :

## ****Comparing Two Files****

Compare files line by line in Linux.

Lets say we have two files with names ****a.txt**** and ****b.txt**** containing 5 Indian states.  

cat a.txt
cat b.txt

![displaying content of files using cat command](../_resources/2024-01-29_17-17_500b4f49fbe5472b8fe7346b84268c8a-1.png)

displaying content of files using cat command

Now, applying diff command without any option we get the following output:

diff a.txt b.txt

![comparing file line by line in linux](../_resources/2024-01-29_17-55_10bfb6b170a749448c6b12de359dcab3-1.png)

comparing file line by line in linux

Let’s take a look at what this output means. The first line of the ****diff**** output will contain:  

- Line numbers corresponding to the first file,
- A special symbol and
- Line numbers corresponding to the second file.

Like in our case, ****0a1**** which means ****after**** lines 0(at the very beginning of file) you have to add ****Tamil Nadu**** to match the second file line number 1. It then tells us what those lines are in each file preceded by the symbol:  

- Lines preceded by a ****<**** are lines from the first file.
- Lines preceded by ****\>**** are lines from the second file.
- Next line contains ****2,3c3**** which means from line 2 to line 3 in the first file needs to be changed to match line number 3 in the second file. It then tells us those lines with the above symbols.
- The three dashes ****(“—“)**** merely separate the lines of file 1 and file 2.

As a summary to make both the files identical, first add **Tamil Nadu** in the first file at very beginning to match line 1 of second file after that change line 2 and 3 of first file i.e. **Uttar Pradesh** and **Kolkata** with line 3 of second file i.e. **Andhra Pradesh**. After that change line 5 of first file i.e. **Jammu and Kashmir** with line 5 of second file i.e. **Uttar Pradesh**. 

## Deleting a Line in Files using diff Command

Consider the scenario where `diff` indicates the need to delete a line. Given two files, `a.txt` and `b.txt`:

![displaying content of files using cat command](../_resources/2024-01-29_18-02_5f2023cd5f7545308809825a8176e4c9-1.png)

displaying content of files using cat command

diff a.txt b.txt

![Deleting a Line in File](../_resources/2024-01-29_18-04_d1ce431a3a0e40f5b5a85f924f6757d8-1.png)

Deleting a Line in File

Here above output ****3d2**** means delete line 3rd of first file i.e. **Telangana** so that both the files ****sync up**** at line 2. 

## Viewing Differences in Context Mode

To view differences in context mode, use the ****\-c**** option. Lets try to understand this with example, we have two files ****file1.txt**** and ****file2.txt****: 

![displaying content of files using cat command](../_resources/2024-01-29_18-12_3895e07063cc4f56ad4b3fdcb47b188a-1.png)

displaying content of files using cat command

diff -c file1.txt file2.txt

![Viewing difference in context mode](../_resources/2024-01-29_18-17_ef21333228a74016a34a890b05d3cd5d-1.png)

Viewing difference in context mode

In the above output:

- The first file is denoted by \`**`` ***` ``**, and the second file is denoted by \`**`` ---` ``**.
- The line with \`**`` ***************` ``** serves as a separator.
- The first two lines provide information about file 1 and file 2, displaying the file name, modification date, and modification time.
- Following that, three asterisks \`**`` ***` ``** are followed by a line range from the first file (lines 1 through 4). Four asterisks \`**`` ****` ``** come next. The contents of the first file are then displayed with specific indicators:
    - If a line is unchanged, it is prefixed by two spaces.
    - If a line needs to be changed, it is prefixed by a symbol and a space. The symbols indicate:
        - **`` `+` ``**: A line in the second file to be added to the first file for identical results.
        - **`` `-` ``**: A line in the first file to be deleted for identical results.
- Three dashes \`**`` ---` ``** are followed by a line range from the second file (lines 1 through 4), separated by a comma. Four dashes \`**`` ----` ``** follow, and the contents of the second file are displayed.

## Viewing Differences in Unified Mode

To view differences in unified mode, use the ****\-u**** option. It is similar to context mode but it ****doesn’t display any redundant information**** or it shows the information in concise form. 

![displaying content of files using cat command](../_resources/2024-01-29_18-12_3895e07063cc4f56ad4b3fdcb47b188a-1.png)

displaying content of files using cat command

diff -u file1.txt file2.txt  

![Viewing difference in Unified mode](../_resources/2024-01-29_18-25_0444e3f10975470bbdc8e3784b9bfb51-1.png)

Viewing difference in Unified mode

In the above output:

- The first file is indicated by \`**`` ---` ``**, and the second file is indicated by \`**`` +++` ``**.
- The first two lines provide information about file 1 and file 2, including the modification date and time.
- After that, \`**`@@ -1`**`` `,` ``**`` 4 +1` ``**`` ,` ``**`` 4 @@` ``** denotes the line range for both files. In this case, it represents lines 1 through 4 in both files.
- The subsequent lines represent the contents of the files with specific indicators:
    - Unchanged lines are displayed without any prefix.
    - Lines in the first file to be deleted are prefixed with `-`.
    - Lines in the second file to be added are prefixed with `+`.

In this example, the output indicates that to make both files identical, the lines containing “mv” and “comm” need to be deleted from the first file (`file1.txt`), and the lines containing “diff” and “comm” need to be added to it.

## Case-Insensitive Comparing between Files

By default, \`**`` diff` ``** is case-sensitive. To perform a case-insensitive comparison, use the \`**`` -i` ``** option:

![displaying content of files using cat command](../_resources/2024-01-29_18-49_bbb69a646f69438d9f8acbad74711575-1.png)

displaying content of files using cat command

The `diff` command is then used to compare these files with the `-i` option, which makes the comparison case-insensitive.

diff -i file1.txt file2.txt

![case-insensitive Comparing](../_resources/2024-01-29_18-54_51d53ed02a104f2ca50c7e5884dd9304-1.png)

case-insensitive Comparing

- `2d1`: This indicates a change in line 2 of the first file (`file1.txt`). The `d` stands for delete, and it says to delete line 2 from the first file.
    - `< mv`: This line signifies the content of the line to be deleted. In this case, it is “mv.”
- `3a3`: This indicates an addition in line 3 of the first file (`file1.txt`). The `a` stands for add, and it says to add a line at position 3.
    - `> diff`: This line represents the content to be added. In this case, it is “diff.”

In summary, the output tells us that to make both files identical (ignoring case), we need to delete the line containing “mv” from the first file (`file1.txt`) and add the line “diff” at the same position. The `diff` command, with the `-i` option, allows for a case-insensitive comparison, making it consider “mv” and “MV” as the same during the analysis.

## Displaying `diff` Version

To check the version of \`**`` diff` ``** installed on your system, use the \`**`` --version` ``** option:

diff --version

![Displaying version of diff command](../_resources/2024-01-30_10-54_a995e867b0884989afdcfd9b46e90765-1.png)

Displaying version of diff command

This command provides information about the version, licensing, and authors of the \`**`` diff` ``** utility.

## Frequently Asked Question on diff Command – FAQs

### How do I use the `diff` command to compare two files line by line in Linux?

> To compare two files line by line using the `diff` command, simply use the following syntax:
> 
> diff file1.txt file2.txt
> 
> This command will display the differences between the two files, highlighting additions, deletions, and modifications.

### Can I ignore whitespace differences while comparing files with the `diff` command?

> Yes, the `diff` command provides the `-w` or `--ignore-all-space` option to ignore whitespace differences. For example:
> 
> diff -w file1.txt file2.txt
> 
> This is particularly useful when comparing code files where changes in indentation or spacing are not significant.

### How can I create a patch file using the `diff` command?

> To create a patch file representing the differences between two files, use the `-u` option and redirect the output to a file:
> 
> diff -u file1.txt file2.txt > mypatch.patch
> 
> The generated patch file can be applied later to synchronize another file with the changes.

### What is the unified format in `diff` output, and how is it different from the context format?

> The unified format (\`**`` -u` ``** option) in \`**`` diff` ``** output provides a more concise and readable representation of differences compared to the context format (\`**`` -c` ``** option). It displays changes in a more compact form, making it easier to understand modifications between files.

### How do I recursively compare two directories in Linux using the `diff` command?

> To recursively compare two directories and their contents, use the \`**`` -r` ``** or \`**`` --recursive` ``** option with the `diff` command:
> 
> diff -r directory1/ directory2/
> 
> This command compares all files in the specified directories and provides detailed information about the differences.

## Conclusion

In the Linux world, comparing files is a common task for system administrators and developers. The \`**`diff`** command is a handy tool that helps in this process. This article explores how to use \`**`` diff` ``** to compare files line by line in Linux. It covers the basic syntax, important options like context mode and unified mode, and practical applications such as creating patch files and recursively comparing directories. Whether you’re debugging code or ensuring file integrity, understanding and mastering the \`**`` diff` ``** 

command is essential for efficient file management in Linux.

Here's a complete roadmap for you to become a developer: **Learn DSA -> Master Frontend/Backend/Full Stack -> Build Projects -> Keep Applying to Jobs**  
And why go anywhere else when our [DSA to Development: Coding Guide](https://www.geeksforgeeks.org/courses/dsa-to-development-coding-guide?utm_source=geeksforgeeks&utm_medium=article_bottom_text_default&utm_campaign=courses) helps you do this in a single program! <a id="docs-internal-guid-25c00b00-7fff-3831-e51c-8560d58bf776"></a>Apply now to our [DSA to Development Program](https://www.geeksforgeeks.org/courses/dsa-to-development-coding-guide?utm_source=geeksforgeeks&utm_medium=article_bottom_text_default&utm_campaign=courses) and our counsellors will connect with you for further guidance & support.

  

Like Article

Suggest improvement

<a id="discussion_message"></a>Share your thoughts in the comments

### Please Login to comment...