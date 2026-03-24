---
title: "What is the difference between git rm --cached and git reset ?"
category: "editors-and-tools"
tags: ["editors-and-tools", "difference", "between", "git", "cached"]
---

# What is the difference between git rm --cached and git reset <file>?

Asked 9 years, 6 months ago
Modified 1 year, 10 months ago
Viewed 113k times
41

According to the git rm documentation,

--cached
Use this option to unstage and remove paths only from the index.    
Working tree files, whether modified or not, will be left alone.
But according to this resource unstaging a file is done with

git reset HEAD <file>
What is the difference? Is there one?

git
Share
Improve this question
Follow
asked Jun 23, 2016 at 20:27
sakurashinken's user avatar
sakurashinken
4,11088 gold badges4141 silver badges7575 bronze badges
git reset can be used to go back on the tree, for instance if you want to go two commits back you can do git reset HEAD~2. – 
Jezor
 CommentedJun 23, 2016 at 20:30
6
If there is no <file> in HEAD, then both command equivalent. If there is <file> in HEAD, then git reset HEAD <file> will unstage file, while git rm --cached <file> will stage file for removal. – 
user4003407
 CommentedJun 23, 2016 at 20:45
Add a comment
3 Answers
Sorted by:

Highest score (default)
57

With git rm --cached you stage a file for removal, but you don't remove it from the working dir. The file will then be shown as untracked.

Take a test drive

git init test_repo
cd test_repo

touch test
git add test
git commit -m 'Added file test'

git rm --cached test

git status
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        deleted:    test      <---- staged for removal

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        test              <-- still in the working dir
With git reset <file> you can unstage a file. In the example above you might want to use git reset test to unstage the removal.

git reset test
git status
On branch master
nothing to commit, working directory clean
Share
Improve this answer
Follow
edited Mar 13, 2024 at 16:14
Monica Granbois's user avatar
Monica Granbois
8,25211 gold badge2020 silver badges1818 bronze badges
answered Jun 23, 2016 at 21:12
René Link's user avatar
René Link
52k1515 gold badges119119 silver badges152152 bronze badges
Sign up to request clarification or add additional context in comments.

Comments

23

The command with flag git rm --cached removes the file from the index but leaves it in the working directory. This indicates to git that you don't want to track the file any more.

On the other hand, the command git reset HEAD <file> leaves the file as a tracked file in the index, but the modifications cached in the index are lost. This has the effect as if the file in cache had been over written by the file in HEAD (while the working tree file is untouched).

Share
Improve this answer
Follow
edited Oct 5, 2021 at 14:00
Kris Stern's user avatar
Kris Stern
1,39022 gold badges1818 silver badges2727 bronze badges
answered Jun 23, 2016 at 20:59
Gregg's user avatar
Gregg
2,68211 gold badge1414 silver badges2222 bronze badges
Comments

6

clear cache full by this:

git rm -r --cached .
Share
Improve this answer
Follow
edited Jan 23, 2024 at 7:28
answered Dec 23, 2022 at 7:50
hgiahuyy's user avatar
hgiahuyy
31833 silver badges6
