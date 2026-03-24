---
title: "Linux Add A Prefix String To Beginning Of Each L"
category: "general-linux"
tags: ["linux", "add", "prefix", "string", "beginning"]
---

[Skip to main content](#content)

[Stack Overflow](https://stackoverflow.com)

1.  [About](https://stackoverflow.co/)
2.  [Products](#)
3.  [OverflowAI](https://stackoverflow.co/teams/ai/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=top-nav-bar&utm_content=overflowai)

3.  [Log in](https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f2099471%2fadd-a-prefix-string-to-beginning-of-each-line)
4.  [Sign up](https://stackoverflow.com/users/signup?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f2099471%2fadd-a-prefix-string-to-beginning-of-each-line)

1.  1.  [Home](https://stackoverflow.com/)
    2.  <a id="nav-questions"></a>[Questions](https://stackoverflow.com/questions)
    3.  [Tags](https://stackoverflow.com/tags)
    
    5.  <a id="nav-users"></a>[Users](https://stackoverflow.com/users)
    6.  <a id="nav-companies"></a>[Companies](https://stackoverflow.com/jobs/companies?so_medium=stackoverflow&so_source=SiteNav)
    7.  Labs
    8.  <a id="nav-labs-jobs"></a>[Jobs](https://stackoverflow.com/jobs?source=so-left-nav)
    9.  <a id="nav-labs-discussions"></a>[Discussions](https://stackoverflow.com/beta/discussions)
    10. Collectives
        
    11. Communities for your favourite technologies. [Explore all Collectives](https://stackoverflow.com/collectives-all)
        
2.  Teams
    
    <img width="129" height="22" src="../_resources/teams-promo_774f180b8a094d2eb52a3710565242e2-1.htm"/>
    
    Ask questions, find answers and collaborate at work with Stack Overflow for Teams.
    
    [Explore Teams](https://stackoverflow.co/teams/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=side-bar&utm_content=explore-teams) [Create a free Team](https://stackoverflowteams.com/teams/create/free/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=side-bar&utm_content=explore-teams)
    

# [Add a prefix string to beginning of each line](https://stackoverflow.com/questions/2099471/add-a-prefix-string-to-beginning-of-each-line)

[Ask Question](https://stackoverflow.com/questions/ask)

Asked 14 years, 5 months ago

Modified [4 days ago](https://stackoverflow.com/questions/2099471/?lastactivity "2024-07-05 10:20:57Z")

Viewed 547k times

461

[](https://stackoverflow.com/posts/2099471/timeline)

I have a file as below:

```
line1
line2
line3
```

And I want to get:

```
prefixline1
prefixline2
prefixline3
```

I could write a Ruby script, but it is better if I do not need to.

`prefix` will contain `/`. It is a path, `/opt/workdir/` for example.

- [linux](https://stackoverflow.com/questions/tagged/linux "show questions tagged 'linux'")
- [scripting](https://stackoverflow.com/questions/tagged/scripting "show questions tagged 'scripting'")
- [text-processing](https://stackoverflow.com/questions/tagged/text-processing "show questions tagged 'text-processing'")

[Share](https://stackoverflow.com/q/2099471 "Short permalink to this question")

[Improve this question](https://stackoverflow.com/posts/2099471/edit)

[edited Jun 28, 2018 at 14:33](https://stackoverflow.com/posts/2099471/revisions "show all edits to this post")

<img width="32" height="32" src="../_resources/U0oyt_d358948b160a4e21880a4667c73c648f-1.htm"/>](https://stackoverflow.com/users/3266847/benjamin-w)

[Benjamin W.](https://stackoverflow.com/users/3266847/benjamin-w)

50k

1919 gold badges

122122 silver badges

124124 bronze badges

asked Jan 20, 2010 at 6:36

<img width="32" height="32" src="../_resources/6cak4_fd2d1f82128946f9a3a3e6709ec8b78e-1.htm"/>](https://stackoverflow.com/users/115722/pierrotlefou)

[pierrotlefou](https://stackoverflow.com/users/115722/pierrotlefou)

40.4k

3939 gold badges

138138 silver badges

175175 bronze badges

[Add a comment](# "Use comments to ask for more information or suggest improvements. Avoid answering questions in comments.")

<a id="tab-top"></a>

## 19 Answers

Sorted by:

<a id="2099478"></a>

710

[](https://stackoverflow.com/posts/2099478/timeline)

```
# If you want to edit the file in-place
sed -i -e 's/^/prefix/' file

# If you want to create a new file
sed -e 's/^/prefix/' file > file.new
```

If `prefix` contains `/`, you can use any other character not in `prefix`, or escape the `/`, so the `sed` command becomes

```
's#^#/opt/workdir#'
# or
's/^/\/opt\/workdir/'
```

[Share](https://stackoverflow.com/a/2099478 "Short permalink to this answer")

[Improve this answer](https://stackoverflow.com/posts/2099478/edit)

[edited Oct 25, 2018 at 22:35](https://stackoverflow.com/posts/2099478/revisions "show all edits to this post")

[![PhysicalChemist's user avatar](https://graph.facebook.com/735415084/picture?type=large)](https://stackoverflow.com/users/3767980/physicalchemist)

[PhysicalChemist](https://stackoverflow.com/users/3767980/physicalchemist)

550

55 silver badges

1414 bronze badges

answered Jan 20, 2010 at 6:38

<img width="32" height="32" src="../_resources/4ecd473d46f300f81636ee7034c358e2_7723b4aa0499456fa-1.png"/>](https://stackoverflow.com/users/226621/alok-singhal)

[Alok Singhal](https://stackoverflow.com/users/226621/alok-singhal)

95.2k

2121 gold badges

127127 silver badges

158158 bronze badges

- 1
    
    @benjamin, I had already upvoted your answer, however, I prefer `sed` for lightweight tasks such as this. If "prefix" is known, it's very easy to pick a character not from "prefix".
    
    – [Alok Singhal](https://stackoverflow.com/users/226621/alok-singhal "95,233 reputation")
    
    [Commented Jan 20, 2010 at 6:56](#comment2033181_2099478)
    
- 7
    
    Don't forget you can also use `sed` in a pipeline, e.g. `foo | sed -e 's/^/x /' | bar`.
    
    – [Mattie](https://stackoverflow.com/users/722332/mattie "21,040 reputation")
    
    [Commented Mar 13, 2014 at 18:11](#comment34034248_2099478)
    
- 1
    
    @Dataman cool. Another way would be `sed -e '2,$s/^/prefix/'`.
    
    – [Alok Singhal](https://stackoverflow.com/users/226621/alok-singhal "95,233 reputation")
    
    [Commented Oct 21, 2014 at 13:57](#comment41610987_2099478)
    
- 1
    
    @BinChen escape the `/` like `\/` (in single-quoted strings) or `\\/` (in double-quoted strings)
    
    – user6516765
    
    [Commented Mar 28, 2017 at 5:23](#comment73206555_2099478)
    
- 11
    
    Use `sed -e 's/$/postfix/' file` if you want to add string to the end of each line.
    
    – [Brian](https://stackoverflow.com/users/1408347/brian "13,170 reputation")
    
    [Commented Jun 29, 2017 at 7:54](#comment76618632_2099478)
    

[Show **16** more comments](# "Expand to show all comments on this post")

<a id="2099492"></a>

159

[](https://stackoverflow.com/posts/2099492/timeline)

```
awk '$0="prefix"$0' file > new_file
```

In awk the [default](https://stackoverflow.com/a/20263611/32453) action is `'{print $0}'` (i.e. print the whole line), so the above is equivalent to:

```
awk '{print "prefix"$0}' file > new_file
```

With Perl (in place replacement):

```
perl -pi 's/^/prefix/' file
```

[Share](https://stackoverflow.com/a/2099492 "Short permalink to this answer")

[Improve this answer](https://stackoverflow.com/posts/2099492/edit)

[edited Dec 21, 2023 at 17:55](https://stackoverflow.com/posts/2099492/revisions "show all edits to this post")

<img width="32" height="32" src="../_resources/cb0388d1c21590c716f03bed19bd36be_a2c9d62bdbfc437cb-1.png"/>](https://stackoverflow.com/users/7123660/benjamin-loison)

[Benjamin Loison](https://stackoverflow.com/users/7123660/benjamin-loison)

5,462

44 gold badges

1818 silver badges

3737 bronze badges

answered Jan 20, 2010 at 6:41

<img width="32" height="32" src="../_resources/5143bb3f979be36f8508d2605b215a4d_b0930d488525424ab-1.png"/>](https://stackoverflow.com/users/134713/vijay)

[Vijay](https://stackoverflow.com/users/134713/vijay)

66.7k

9090 gold badges

234234 silver badges

325325 bronze badges

- 9
    
    With a pipe/stream or variable: `prtinf "$VARIABLE\n" | awk '$0="prefix"$0'`
    
    – [ThorSummoner](https://stackoverflow.com/users/1695680/thorsummoner "17,651 reputation")
    
    [Commented Feb 25, 2015 at 18:20](#comment45739803_2099492)
    
- 5
    
    With a large file (12 G), `awk` reports `awk: out of memory in readrec 1 source line number 1`, but the solution with `sed` completes successfully.
    
    – [jrm](https://stackoverflow.com/users/1050694/jrm "727 reputation")
    
    [Commented Jul 6, 2017 at 16:04](#comment76883014_2099492)
    
- 1
    
    This is the best answer, with AWK it Worked right off the bat without having to annoyingly deal with escaping regex special characters
    
    – [Maximo Migliari](https://stackoverflow.com/users/2755684/maximo-migliari "109 reputation")
    
    [Commented Jan 6, 2022 at 21:50](#comment124828451_2099492)
    
- With "normal files" split into lines awk shouldn't run out of memory...
    
    – [rogerdpack](https://stackoverflow.com/users/32453/rogerdpack "65,459 reputation")
    
    [Commented Feb 2, 2022 at 19:07](#comment125445793_2099492)
    

[Add a comment](# "Use comments to ask for more information or suggest improvements. Avoid comments like “+1” or “thanks”.")

<a id="12662819"></a>

34

[](https://stackoverflow.com/posts/12662819/timeline)

You can use Vim in Ex mode:

```
ex -sc '%s/^/prefix/|x' file
```

1.  `%` select all lines
    
2.  `s` replace
    
3.  `x` save and close
    

[Share](https://stackoverflow.com/a/12662819 "Short permalink to this answer")

[Improve this answer](https://stackoverflow.com/posts/12662819/edit)

[edited Nov 5, 2016 at 14:30](https://stackoverflow.com/posts/12662819/revisions "show all edits to this post")

answered Sep 30, 2012 at 16:18

<img width="32" height="32" src="../_resources/5ec9c21c8d54825b04def7a41998d18d_7e78dd5fa1244f008-1.png"/>](https://stackoverflow.com/users/1002260/zombo)

[Zombo](https://stackoverflow.com/users/1002260/zombo)

1

- 1
    
    For me, I just open the file in vim and type `:%s/^/prefix/`, since this strategy ends up being useful in many situations
    
    – [Frank Bryce](https://stackoverflow.com/users/3960399/frank-bryce "8,348 reputation")
    
    [Commented Feb 2, 2017 at 16:35](#comment71190832_12662819)
    

[Add a comment](# "Use comments to ask for more information or suggest improvements. Avoid comments like “+1” or “thanks”.")

<a id="28571517"></a>

31

[](https://stackoverflow.com/posts/28571517/timeline)

If your prefix is a bit complicated, just put it in a variable:

```
prefix=path/to/file/
```

Then, you pass that variable and let awk deal with it:

```
awk -v prefix="$prefix" '{print prefix $0}' input_file.txt
```

[Share](https://stackoverflow.com/a/28571517 "Short permalink to this answer")

[Improve this answer](https://stackoverflow.com/posts/28571517/edit)

[edited Dec 21, 2023 at 17:55](https://stackoverflow.com/posts/28571517/revisions "show all edits to this post")

<img width="32" height="32" src="../_resources/cb0388d1c21590c716f03bed19bd36be_a2c9d62bdbfc437cb-1.png"/>](https://stackoverflow.com/users/7123660/benjamin-loison)

[Benjamin Loison](https://stackoverflow.com/users/7123660/benjamin-loison)

5,462

44 gold badges

1818 silver badges

3737 bronze badges

answered Feb 17, 2015 at 21:35

<img width="32" height="32" src="../_resources/lSDag_fecbc1e71a32475eab8c6a8161a9a755-1.htm"/>](https://stackoverflow.com/users/2030962/melka)

[Melka](https://stackoverflow.com/users/2030962/melka)

521

55 silver badges

1212 bronze badges

[Add a comment](# "Use comments to ask for more information or suggest improvements. Avoid comments like “+1” or “thanks”.")

<a id="55759796"></a>

21

[](https://stackoverflow.com/posts/55759796/timeline)

Here is a oneliner solution using the [`ts`](https://manpages.ubuntu.com/manpages/focal/en/man1/ts.1.html) command from moreutils

```
$ cat file | ts prefix
```

And how it's derived step by step:

```
# Step 1. create the file

$ cat file
line1
line2
line3
```

```
# Step 2. add prefix to the beginning of each line

$ cat file | ts prefix
prefix line1
prefix line2
prefix line3
```

Note that the prefix will be space separated from the content

[Share](https://stackoverflow.com/a/55759796 "Short permalink to this answer")

[Improve this answer](https://stackoverflow.com/posts/55759796/edit)

[edited Jan 23 at 0:12](https://stackoverflow.com/posts/55759796/revisions "show all edits to this post")

<img width="32" height="32" src="../_resources/U4QjP_bff5e853bfe34f308a1975aa62bf88a5-1.htm"/>](https://stackoverflow.com/users/6320039/ulysse-bn)

[Ulysse BN](https://stackoverflow.com/users/6320039/ulysse-bn)

11k

77 gold badges

6060 silver badges

9090 bronze badges

answered Apr 19, 2019 at 9:41

<img width="32" height="32" src="../_resources/fa3e69633759c95e3e7e2139f0c7cb26_456f30adbf0c41599-1.png"/>](https://stackoverflow.com/users/4602592/btwiuse)

[btwiuse](https://stackoverflow.com/users/4602592/btwiuse)

2,871

11 gold badge

2727 silver badges

3333 bronze badges

- 6
    
    'ts' is not installed by default on many Linux distros. Also, downvoting because the trailing "tr -d ' '" in this answer will remove all spaces from the lines, not just the space that was added by 'ts'
    
    – [Tim Bird](https://stackoverflow.com/users/757965/tim-bird "1,114 reputation")
    
    [Commented May 13, 2020 at 17:21](#comment109277881_55759796)
    

[Add a comment](# "Use comments to ask for more information or suggest improvements. Avoid comments like “+1” or “thanks”.")

<a id="20528931"></a>

13

[](https://stackoverflow.com/posts/20528931/timeline)

If you have Perl:

```
perl -pe 's/^/PREFIX/' input.file
```

[Share](https://stackoverflow.com/a/20528931 "Short permalink to this answer")

[Improve this answer](https://stackoverflow.com/posts/20528931/edit)

[edited Dec 21, 2023 at 17:55](https://stackoverflow.com/posts/20528931/revisions "show all edits to this post")

<img width="32" height="32" src="../_resources/cb0388d1c21590c716f03bed19bd36be_a2c9d62bdbfc437cb-1.png"/>](https://stackoverflow.com/users/7123660/benjamin-loison)

[Benjamin Loison](https://stackoverflow.com/users/7123660/benjamin-loison)

5,462

44 gold badges

1818 silver badges

3737 bronze badges

answered Dec 11, 2013 at 20:08

<img width="32" height="32" src="../_resources/837b193bb43ef1dd3fb31ddae1b791b0_90043abf11e54b3d9-1.jpg"/>](https://stackoverflow.com/users/654269/majid-azimi)

[Majid Azimi](https://stackoverflow.com/users/654269/majid-azimi)

5,725

1313 gold badges

6565 silver badges

117117 bronze badges

[Add a comment](# "Use comments to ask for more information or suggest improvements. Avoid comments like “+1” or “thanks”.")

<a id="61036878"></a>

8

[](https://stackoverflow.com/posts/61036878/timeline)

Using & (the whole part of the input that was matched by the pattern”):

```
cat in.txt | sed -e "s/.*/prefix&/" > out.txt
```

OR using back references:

```
cat in.txt | sed -e "s/\(.*\)/prefix\1/" > out.txt
```

[Share](https://stackoverflow.com/a/61036878 "Short permalink to this answer")

[Improve this answer](https://stackoverflow.com/posts/61036878/edit)

[edited Dec 21, 2023 at 17:55](https://stackoverflow.com/posts/61036878/revisions "show all edits to this post")

<img width="32" height="32" src="../_resources/cb0388d1c21590c716f03bed19bd36be_a2c9d62bdbfc437cb-1.png"/>](https://stackoverflow.com/users/7123660/benjamin-loison)

[Benjamin Loison](https://stackoverflow.com/users/7123660/benjamin-loison)

5,462

44 gold badges

1818 silver badges

3737 bronze badges

answered Apr 5, 2020 at 1:15

<img width="32" height="32" src="../_resources/photo_5ad5414d487d4a0d8778ce05c0064125-1.png"/>](https://stackoverflow.com/users/13160840/ark25)

[Ark25](https://stackoverflow.com/users/13160840/ark25)

109

11 silver badge

33 bronze badges

[Add a comment](# "Use comments to ask for more information or suggest improvements. Avoid comments like “+1” or “thanks”.")

<a id="2099581"></a>

6

[](https://stackoverflow.com/posts/2099581/timeline)

Using the shell:

```
#!/bin/bash
prefix="something"
file="file"
while read -r line
do
 echo "${prefix}$line"
done <$file > newfile
mv newfile $file
```

[Share](https://stackoverflow.com/a/2099581 "Short permalink to this answer")

[Improve this answer](https://stackoverflow.com/posts/2099581/edit)

[edited Dec 21, 2023 at 17:56](https://stackoverflow.com/posts/2099581/revisions "show all edits to this post")

<img width="32" height="32" src="../_resources/cb0388d1c21590c716f03bed19bd36be_a2c9d62bdbfc437cb-1.png"/>](https://stackoverflow.com/users/7123660/benjamin-loison)

[Benjamin Loison](https://stackoverflow.com/users/7123660/benjamin-loison)

5,462

44 gold badges

1818 silver badges

3737 bronze badges

answered Jan 20, 2010 at 7:05

<img width="32" height="32" src="../_resources/c2618d986361c695497c1a875ea8da01_332c58c0638a47b38-1.png"/>](https://stackoverflow.com/users/131527/ghostdog74)

[ghostdog74](https://stackoverflow.com/users/131527/ghostdog74)

337k

5858 gold badges

260260 silver badges

348348 bronze badges

[Add a comment](# "Use comments to ask for more information or suggest improvements. Avoid comments like “+1” or “thanks”.")

<a id="22261254"></a>

5

[](https://stackoverflow.com/posts/22261254/timeline)

While I don't think pierr had this concern, I needed a solution that would not delay output from the live "tail" of a file, since I wanted to monitor several alert logs simultaneously, prefixing each line with the name of its respective log.

Unfortunately, sed, cut, etc. introduced too much buffering and kept me from seeing the most current lines. Steven Penny's suggestion to use the `-s` option of `nl` was intriguing, and testing proved that it did not introduce the unwanted buffering that concerned me.

There were a couple of problems with using `nl`, though, related to the desire to strip out the unwanted line numbers (even if you don't care about the aesthetics of it, there may be cases where using the extra columns would be undesirable). First, using "cut" to strip out the numbers re-introduces the buffering problem, so it wrecks the solution. Second, using "-w1" doesn't help, since this does NOT restrict the line number to a single column - it just gets wider as more digits are needed.

It isn't pretty if you want to capture this elsewhere, but since that's exactly what I didn't need to do (everything was being written to log files already, I just wanted to watch several at once in real time), the best way to lose the line numbers and have only my prefix was to start the `-s` string with a carriage return (CR or ^M or Ctrl-M). So for example:

```
#!/bin/ksh

# Monitor the widget, framas, and dweezil
# log files until the operator hits <enter>
# to end monitoring.

PGRP=$$

for LOGFILE in widget framas dweezil
do
(
    tail -f $LOGFILE 2>&1 |
    nl -s"^M${LOGFILE}>  "
) &
sleep 1
done

read KILLEM

kill -- -${PGRP}
```

[Share](https://stackoverflow.com/a/22261254 "Short permalink to this answer")

[Improve this answer](https://stackoverflow.com/posts/22261254/edit)

[edited Dec 21, 2023 at 17:56](https://stackoverflow.com/posts/22261254/revisions "show all edits to this post")

<img width="32" height="32" src="../_resources/cb0388d1c21590c716f03bed19bd36be_a2c9d62bdbfc437cb-1.png"/>](https://stackoverflow.com/users/7123660/benjamin-loison)

[Benjamin Loison](https://stackoverflow.com/users/7123660/benjamin-loison)

5,462

44 gold badges

1818 silver badges

3737 bronze badges

answered Mar 7, 2014 at 21:44

<img width="32" height="32" src="../_resources/84cbbaef5bb2b82715938c274b53f11d_770db969ea9e4a01a-1.png"/>](https://stackoverflow.com/users/3394513/scriptguy)

[ScriptGuy](https://stackoverflow.com/users/3394513/scriptguy)

51

11 silver badge

11 bronze badge

- 3
    
    use the `-u` option to sed to avoid the buffering.
    
    – [Bryan Larsen](https://stackoverflow.com/users/91365/bryan-larsen "9,716 reputation")
    
    [Commented Mar 7, 2014 at 21:48](#comment33812752_22261254)
    
- 2
    
    Buffering can be turned off with unbuffer/stdbuf, see [unix.stackexchange.com/q/25372/6205](http://unix.stackexchange.com/q/25372/6205)
    
    – [myroslav](https://stackoverflow.com/users/38592/myroslav "3,753 reputation")
    
    [Commented Jun 4, 2015 at 19:15](#comment49367718_22261254)
    

[Add a comment](# "Use comments to ask for more information or suggest improvements. Avoid comments like “+1” or “thanks”.")

<a id="51085519"></a>

4

[](https://stackoverflow.com/posts/51085519/timeline)

Using ed:

```
ed infile <<'EOE'
,s/^/prefix/
wq
EOE
```

This substitutes, for each line (`,`), the beginning of the line (`^`) with `prefix`. `wq` saves and exits.

If the replacement string contains a slash, we can use a different delimiter for `s` instead:

```
ed infile <<'EOE'
,s#^#/opt/workdir/#
wq
EOE
```

I've quoted the here-doc delimiter `EOE` ("end of ed") to prevent parameter expansion. In this example, it would work unquoted as well, but it's good practice to prevent surprises if you ever have a `$` in your ed script.

[Share](https://stackoverflow.com/a/51085519 "Short permalink to this answer")

[Improve this answer](https://stackoverflow.com/posts/51085519/edit)

answered Jun 28, 2018 at 14:32

<img width="32" height="32" src="../_resources/U0oyt_d358948b160a4e21880a4667c73c648f-1.htm"/>](https://stackoverflow.com/users/3266847/benjamin-w)

[Benjamin W.](https://stackoverflow.com/users/3266847/benjamin-w)

50k

1919 gold badges

122122 silver badges

124124 bronze badges

[Add a comment](# "Use comments to ask for more information or suggest improvements. Avoid comments like “+1” or “thanks”.")

<a id="36037014"></a>

3

[](https://stackoverflow.com/posts/36037014/timeline)

Here's a wrapped up example using the `sed` approach from [this answer](https://stackoverflow.com/a/2099478/26510):

```
$ cat /path/to/some/file | prefix_lines "WOW: "

WOW: some text
WOW: another line
WOW: more text
```

### prefix_lines

```
function show_help()
{
  IT=$(CAT <<EOF
    Usage: PREFIX {FILE}

    e.g.

    cat /path/to/file | prefix_lines "WOW: "

      WOW: some text
      WOW: another line
      WOW: more text
  )
  echo "$IT"
  exit
}

# Require a prefix
if [ -z "$1" ]
then
  show_help
fi

# Check if input is from stdin or a file
FILE=$2
if [ -z "$2" ]
then
  # If no stdin exists
  if [ -t 0 ]; then
    show_help
  fi
  FILE=/dev/stdin
fi

# Now prefix the output
PREFIX=$1
sed -e "s/^/$PREFIX/" $FILE
```

[Share](https://stackoverflow.com/a/36037014 "Short permalink to this answer")

[Improve this answer](https://stackoverflow.com/posts/36037014/edit)

[edited Dec 21, 2023 at 17:57](https://stackoverflow.com/posts/36037014/revisions "show all edits to this post")

<img width="32" height="32" src="../_resources/cb0388d1c21590c716f03bed19bd36be_a2c9d62bdbfc437cb-1.png"/>](https://stackoverflow.com/users/7123660/benjamin-loison)

[Benjamin Loison](https://stackoverflow.com/users/7123660/benjamin-loison)

5,462

44 gold badges

1818 silver badges

3737 bronze badges

answered Mar 16, 2016 at 13:24

<img width="32" height="32" src="../_resources/25ee9a1b9f5a16feb1432882a9ef2f06_86811b81a7cf4c8b8-1.png"/>](https://stackoverflow.com/users/26510/brad-parks)

[Brad Parks](https://stackoverflow.com/users/26510/brad-parks)

69.9k

6666 gold badges

277277 silver badges

360360 bronze badges

- 2
    
    This will not work if `PREFIX` contains any characters special to sed like a slash.
    
    – [josch](https://stackoverflow.com/users/784669/josch "6,986 reputation")
    
    [Commented Jan 3, 2017 at 11:57](#comment70091917_36037014)
    
- Good point... If you find you use slash alot, you could use a different delimiter with the sed part, [as detailed here](http://stackoverflow.com/a/16790859/26510), which would allow you to use it in searches. Other special sed chars can be put in by escaping with a slash, e.g `prefix_lines \*`
    
    – [Brad Parks](https://stackoverflow.com/users/26510/brad-parks "69,944 reputation")
    
    [Commented Jan 3, 2017 at 13:19](#comment70095063_36037014)
    

[Add a comment](# "Use comments to ask for more information or suggest improvements. Avoid comments like “+1” or “thanks”.")

<a id="61154149"></a>

3

[](https://stackoverflow.com/posts/61154149/timeline)

1.  You can also achieve this using the backreference technique
    
    ```
    sed -i.bak 's/\(.*\)/prefix\1/' foo.txt
    ```
    
2.  You can also use with awk like this
    
    ```
    awk '{print "prefix"$0}' foo.txt > tmp && mv tmp foo.txt
    ```
    

[Share](https://stackoverflow.com/a/61154149 "Short permalink to this answer")

[Improve this answer](https://stackoverflow.com/posts/61154149/edit)

[edited Dec 21, 2023 at 17:58](https://stackoverflow.com/posts/61154149/revisions "show all edits to this post")

<img width="32" height="32" src="../_resources/cb0388d1c21590c716f03bed19bd36be_a2c9d62bdbfc437cb-1.png"/>](https://stackoverflow.com/users/7123660/benjamin-loison)

[Benjamin Loison](https://stackoverflow.com/users/7123660/benjamin-loison)

5,462

44 gold badges

1818 silver badges

3737 bronze badges

answered Apr 11, 2020 at 8:44

<img width="32" height="32" src="../_resources/d22bcc8c0ded10ae5e370d27b543c495_f2c8d5b7e1be49778-1.png"/>](https://stackoverflow.com/users/6341379/k-vishwanath)

[k_vishwanath](https://stackoverflow.com/users/6341379/k-vishwanath)

1,536

33 gold badges

2121 silver badges

3232 bronze badges

[Add a comment](# "Use comments to ask for more information or suggest improvements. Avoid comments like “+1” or “thanks”.")

<a id="66743774"></a>

2

[](https://stackoverflow.com/posts/66743774/timeline)

Using [Pythonise](https://github.com/CZ-NIC/pz) (`pz`):

```
pz '"preix"+s' <filename
```

[Share](https://stackoverflow.com/a/66743774 "Short permalink to this answer")

[Improve this answer](https://stackoverflow.com/posts/66743774/edit)

answered Mar 22, 2021 at 9:56

<img width="32" height="32" src="../_resources/GBgbz_ee432f57ef554a3689d4ce7ed390c418-1.htm"/>](https://stackoverflow.com/users/2556118/hans-ginzel)

[Hans Ginzel](https://stackoverflow.com/users/2556118/hans-ginzel)

8,581

44 gold badges

2525 silver badges

2222 bronze badges

[Add a comment](# "Use comments to ask for more information or suggest improvements. Avoid comments like “+1” or “thanks”.")

<a id="70664014"></a>

2

[](https://stackoverflow.com/posts/70664014/timeline)

You can do it using **AWK**

```
echo example| awk '{print "prefix"$0}'
```

or

```
awk '{print "prefix"$0}' file.txt > output.txt
```

For suffix: `awk '{print $0"suffix"}'`

For prefix and suffix: `awk '{print "prefix"$0"suffix"}'`

[Share](https://stackoverflow.com/a/70664014 "Short permalink to this answer")

[Improve this answer](https://stackoverflow.com/posts/70664014/edit)

[edited Dec 21, 2023 at 17:59](https://stackoverflow.com/posts/70664014/revisions "show all edits to this post")

<img width="32" height="32" src="../_resources/cb0388d1c21590c716f03bed19bd36be_a2c9d62bdbfc437cb-1.png"/>](https://stackoverflow.com/users/7123660/benjamin-loison)

[Benjamin Loison](https://stackoverflow.com/users/7123660/benjamin-loison)

5,462

44 gold badges

1818 silver badges

3737 bronze badges

answered Jan 11, 2022 at 8:57

<img width="32" height="32" src="../_resources/LNObS_41cc8e36b60e425380da343d24c3ca66-1.htm"/>](https://stackoverflow.com/users/16510338/rauf)

[Rauf](https://stackoverflow.com/users/16510338/rauf)

117

11 silver badge

66 bronze badges

[Add a comment](# "Use comments to ask for more information or suggest improvements. Avoid comments like “+1” or “thanks”.")

<a id="67150187"></a>

1

[](https://stackoverflow.com/posts/67150187/timeline)

Simple solution using a for loop on the command line with bash:

```
for i in $(cat yourfile.txt); do echo "prefix$i"; done
```

Save the output to a file:

```
for i in $(cat yourfile.txt); do echo "prefix$i"; done > yourfilewithprefixes.txt
```

[Share](https://stackoverflow.com/a/67150187 "Short permalink to this answer")

[Improve this answer](https://stackoverflow.com/posts/67150187/edit)

[edited Dec 21, 2023 at 17:58](https://stackoverflow.com/posts/67150187/revisions "show all edits to this post")

<img width="32" height="32" src="../_resources/cb0388d1c21590c716f03bed19bd36be_a2c9d62bdbfc437cb-1.png"/>](https://stackoverflow.com/users/7123660/benjamin-loison)

[Benjamin Loison](https://stackoverflow.com/users/7123660/benjamin-loison)

5,462

44 gold badges

1818 silver badges

3737 bronze badges

answered Apr 18, 2021 at 15:19

<img width="32" height="32" src="../_resources/bc5d3852fcdaab0c1af328ad03ad7f9c_64fdfef9098143369-1.png"/>](https://stackoverflow.com/users/6352735/michael)

[Michael](https://stackoverflow.com/users/6352735/michael)

829

11 gold badge

1010 silver badges

2424 bronze badges

[Add a comment](# "Use comments to ask for more information or suggest improvements. Avoid comments like “+1” or “thanks”.")

<a id="65241100"></a>

1

[](https://stackoverflow.com/posts/65241100/timeline)

If you need to prepend a text at the beginning of each line that has a certain string, try following. In the following example, I am adding # at the beginning of each line that has the word "rock" in it.

```
sed -i -e 's/^.*rock.*/#&/' file_name
```

[Share](https://stackoverflow.com/a/65241100 "Short permalink to this answer")

[Improve this answer](https://stackoverflow.com/posts/65241100/edit)

[edited Dec 21, 2023 at 17:59](https://stackoverflow.com/posts/65241100/revisions "show all edits to this post")

<img width="32" height="32" src="../_resources/cb0388d1c21590c716f03bed19bd36be_a2c9d62bdbfc437cb-1.png"/>](https://stackoverflow.com/users/7123660/benjamin-loison)

[Benjamin Loison](https://stackoverflow.com/users/7123660/benjamin-loison)

5,462

44 gold badges

1818 silver badges

3737 bronze badges

answered Dec 10, 2020 at 19:31

<img width="32" height="32" src="../_resources/5ff13eb73b4fc9e02441a94e3fb2fd72_73b277991d0b466e8-1.png"/>](https://stackoverflow.com/users/1392873/mandroid)

[mandroid](https://stackoverflow.com/users/1392873/mandroid)

189

22 silver badges

55 bronze badges

[Add a comment](# "Use comments to ask for more information or suggest improvements. Avoid comments like “+1” or “thanks”.")

<a id="55755560"></a>

0

[](https://stackoverflow.com/posts/55755560/timeline)

For people on BSD/OSX systems there's utility called `lam`, short for laminate. `lam -s prefix file` will do what you want. I use it in pipelines, eg:

`find -type f -exec lam -s "{}: " "{}" \; | fzf`

...which will find all files, exec lam on each of them, giving each file a prefix of its own filename. (And pump the output to fzf for searching.)

[Share](https://stackoverflow.com/a/55755560 "Short permalink to this answer")

[Improve this answer](https://stackoverflow.com/posts/55755560/edit)

[edited Dec 15, 2019 at 18:15](https://stackoverflow.com/posts/55755560/revisions "show all edits to this post")

answered Apr 19, 2019 at 1:36

<img width="32" height="32" src="../_resources/aaa5d5b9b73e271b471187d6eac6b1d1_b47862e91bf44772a-1.png"/>](https://stackoverflow.com/users/5682988/ray)

[Ray](https://stackoverflow.com/users/5682988/ray)

11

33 bronze badges

- You're right, it appears this is a BSD only command. POSIX replaced it with paste, but paste doesn't have the feature of adding a full separator string. I'll update my answer.
    
    – [Ray](https://stackoverflow.com/users/5682988/ray "11 reputation")
    
    [Commented Dec 15, 2019 at 18:14](#comment104889597_55755560)
    

[Add a comment](# "Use comments to ask for more information or suggest improvements. Avoid comments like “+1” or “thanks”.")

<a id="78710911"></a>

0

[](https://stackoverflow.com/posts/78710911/timeline)

Another alternative (`sponge` is optional):

```
$ cat file | xargs -I{} echo 'prefix-{}-suffix' | sponge file
```

Example:

```
$ seq 1 10 | xargs -I{} echo 'prefix-{}-suffix'
prefix-1-suffix
prefix-2-suffix
prefix-3-suffix
prefix-4-suffix
prefix-5-suffix
prefix-6-suffix
prefix-7-suffix
prefix-8-suffix
prefix-9-suffix
prefix-10-suffix
```

[Share](https://stackoverflow.com/a/78710911 "Short permalink to this answer")

[Improve this answer](https://stackoverflow.com/posts/78710911/edit)

answered Jul 5 at 10:20

<img width="32" height="32" src="../_resources/1f6e4accc90e26815f84983432f727b9_850db5e6c2ab42f4b-1.jpg"/>](https://stackoverflow.com/users/1054458/fark)

[FarK](https://stackoverflow.com/users/1054458/fark)

606

11 gold badge

55 silver badges

1717 bronze badges

[Add a comment](# "Use comments to ask for more information or suggest improvements. Avoid comments like “+1” or “thanks”.")

<a id="64771618"></a>

\-1

[](https://stackoverflow.com/posts/64771618/timeline)

```
SETLOCAL ENABLEDELAYEDEXPANSION

YourPrefix=blabla

YourPath=C:\path

for /f "tokens=*" %%a in (!YourPath!\longfile.csv)     do (echo !YourPrefix!%%a) >> !YourPath!\Archive\output.csv
```

[Share](https://stackoverflow.com/a/64771618 "Short permalink to this answer")

[Improve this answer](https://stackoverflow.com/posts/64771618/edit)

[edited Dec 21, 2023 at 18:00](https://stackoverflow.com/posts/64771618/revisions "show all edits to this post")

<img width="32" height="32" src="../_resources/cb0388d1c21590c716f03bed19bd36be_a2c9d62bdbfc437cb-1.png"/>](https://stackoverflow.com/users/7123660/benjamin-loison)

[Benjamin Loison](https://stackoverflow.com/users/7123660/benjamin-loison)

5,462

44 gold badges

1818 silver badges

3737 bronze badges

answered Nov 10, 2020 at 15:15

<img width="32" height="32" src="../_resources/2a7d465888b6ccbb42eb796adb4819a3_b0734d27a6cf4193b-1.png"/>](https://stackoverflow.com/users/6719006/pietervnk)

[pietervnk](https://stackoverflow.com/users/6719006/pietervnk)

107

44 bronze badges

- 1
    
    Please add some explanation to your answer such that others can learn from it
    
    – [Nico Haase](https://stackoverflow.com/users/1116230/nico-haase "11,938 reputation")
    
    [Commented Nov 10, 2020 at 16:15](#comment114523694_64771618)
    
- 1
    
    Please don't post only code as an answer, but also provide an explanation of what your code does and how it solves the problem of the question. Answers with an explanation are usually more helpful and of better quality, and are more likely to attract upvotes.
    
    – [Yagiz Degirmenci](https://stackoverflow.com/users/13161155/yagiz-degirmenci "19,431 reputation")
    
    [Commented Nov 10, 2020 at 17:03](#comment114525030_64771618)
    
- If you were looking for an answer in a knowledgebase, trying to solve an issue, do you think this answer would be helpful? Not so much.
    
    – [Trenton McKinney](https://stackoverflow.com/users/7758804/trenton-mckinney "61,003 reputation")
    
    [Commented Nov 10, 2020 at 23:33](#comment114533588_64771618)
    
- Thank you for your interest in contributing to the Stack Overflow community. This question already has quite a few answers—including one that has been extensively validated by the community. Are you certain your approach hasn’t been given previously? **If so, it would be useful to explain how your approach is different, under what circumstances your approach might be preferred, and/or why you think the previous answers aren’t sufficient.** Can you kindly [edit](https://stackoverflow.com/posts/64771618/edit) your answer to offer an explanation?
    
    – [Jeremy Caney](https://stackoverflow.com/users/3025856/jeremy-caney "7,425 reputation")
    
    [Commented Dec 22, 2023 at 0:08](#comment136984640_64771618)
    

[Add a comment](# "Use comments to ask for more information or suggest improvements. Avoid comments like “+1” or “thanks”.")

**[Highly active question](https://stackoverflow.com/help/privileges/protect-questions)**. Earn 10 reputation (not counting the [association bonus](https://meta.stackexchange.com/questions/141648/what-is-the-association-bonus-and-how-does-it-work)) in order to answer this question. The reputation requirement helps protect this question from spam and non-answer activity.

## 

Not the answer you're looking for? Browse other questions tagged

- [linux](https://stackoverflow.com/questions/tagged/linux "show questions tagged 'linux'")
- [scripting](https://stackoverflow.com/questions/tagged/scripting "show questions tagged 'scripting'")
- [text-processing](https://stackoverflow.com/questions/tagged/text-processing "show questions tagged 'text-processing'")

or [ask your own question](https://stackoverflow.com/questions/ask).

- Featured on Meta
- [We spent a sprint addressing your requests — here’s how it went](https://meta.stackexchange.com/questions/401060/we-spent-a-sprint-addressing-your-requests-here-s-how-it-went?cb=1)
    
- [Upcoming initiatives on Stack Overflow and across the Stack Exchange network...](https://meta.stackexchange.com/questions/401061/upcoming-initiatives-on-stack-overflow-and-across-the-stack-exchange-network-ju?cb=1 "Upcoming initiatives on Stack Overflow and across the Stack Exchange network (July 2024)")
    
- [What makes a homepage useful for logged-in users](https://meta.stackoverflow.com/questions/430779/what-makes-a-homepage-useful-for-logged-in-users?cb=1)
    

#### Linked

[0](https://stackoverflow.com/q/24018937?lq=1 "Question score (upvotes - downvotes)")[Add a sentence in each line of a file with sed](https://stackoverflow.com/questions/24018937/add-a-sentence-in-each-line-of-a-file-with-sed?noredirect=1&lq=1)

[0](https://stackoverflow.com/q/31040652?lq=1 "Question score (upvotes - downvotes)")[how to add text (shell var.) in the first place in each line using sed](https://stackoverflow.com/questions/31040652/how-to-add-text-shell-var-in-the-first-place-in-each-line-using-sed?noredirect=1&lq=1)

[0](https://stackoverflow.com/q/75093727?lq=1 "Question score (upvotes - downvotes)")[Print string variable that stores the output of a command in Bash](https://stackoverflow.com/questions/75093727/print-string-variable-that-stores-the-output-of-a-command-in-bash?noredirect=1&lq=1)

[\-1](https://stackoverflow.com/q/56721707?lq=1 "Question score (upvotes - downvotes)")[How can I concatenate pipeline string into file](https://stackoverflow.com/questions/56721707/how-can-i-concatenate-pipeline-string-into-file?noredirect=1&lq=1)

[\-1](https://stackoverflow.com/q/52639579?lq=1 "Question score (upvotes - downvotes)")[Adding a command at the beginning of every line using bash command](https://stackoverflow.com/questions/52639579/adding-a-command-at-the-beginning-of-every-line-using-bash-command?noredirect=1&lq=1)

[\-1](https://stackoverflow.com/q/51085032?lq=1 "Question score (upvotes - downvotes)")[Add string at the beginning of each line with the name of the file](https://stackoverflow.com/questions/51085032/add-string-at-the-beginning-of-each-line-with-the-name-of-the-file?noredirect=1&lq=1)

[\-2](https://stackoverflow.com/q/31820209?lq=1 "Question score (upvotes - downvotes)")[How can I add text to a text file using Bash or Python](https://stackoverflow.com/questions/31820209/how-can-i-add-text-to-a-text-file-using-bash-or-python?noredirect=1&lq=1)

[205](https://stackoverflow.com/q/4787413?lq=1 "Question score (upvotes - downvotes)")[Rename Files and Directories (Add Prefix)](https://stackoverflow.com/questions/4787413/rename-files-and-directories-add-prefix?noredirect=1&lq=1)

[193](https://stackoverflow.com/q/16790793?lq=1 "Question score (upvotes - downvotes)")[How to insert strings containing slashes with sed?](https://stackoverflow.com/questions/16790793/how-to-insert-strings-containing-slashes-with-sed?noredirect=1&lq=1)

[45](https://stackoverflow.com/q/20262869?lq=1 "Question score (upvotes - downvotes)")[Why does "1" in awk print the current line?](https://stackoverflow.com/questions/20262869/why-does-1-in-awk-print-the-current-line?noredirect=1&lq=1)

[See more linked questions](https://stackoverflow.com/questions/linked/2099471?lq=1)

#### Related

[22](https://stackoverflow.com/q/16991035?rq=3 "Question score (upvotes - downvotes)")[Add suffix to each line with shell script](https://stackoverflow.com/questions/16991035/add-suffix-to-each-line-with-shell-script?rq=3)

[16](https://stackoverflow.com/q/19831827?rq=3 "Question score (upvotes - downvotes)")[Add prefix to every line in text in bash](https://stackoverflow.com/questions/19831827/add-prefix-to-every-line-in-text-in-bash?rq=3)

[0](https://stackoverflow.com/q/23811279?rq=3 "Question score (upvotes - downvotes)")[How to add a prefix for each line according to a line field](https://stackoverflow.com/questions/23811279/how-to-add-a-prefix-for-each-line-according-to-a-line-field?rq=3)

[3](https://stackoverflow.com/q/29178216?rq=3 "Question score (upvotes - downvotes)")[Add prefix to each line of output with sed](https://stackoverflow.com/questions/29178216/add-prefix-to-each-line-of-output-with-sed?rq=3)

[2](https://stackoverflow.com/q/31471952?rq=3 "Question score (upvotes - downvotes)")[Add prefix to every line shell](https://stackoverflow.com/questions/31471952/add-prefix-to-every-line-shell?rq=3)

[0](https://stackoverflow.com/q/31822871?rq=3 "Question score (upvotes - downvotes)")[bash script to add prefix to line.](https://stackoverflow.com/questions/31822871/bash-script-to-add-prefix-to-line?rq=3)

[1](https://stackoverflow.com/q/34857907?rq=3 "Question score (upvotes - downvotes)")[Add input lines subset to prefix shell script output](https://stackoverflow.com/questions/34857907/add-input-lines-subset-to-prefix-shell-script-output?rq=3)

[1](https://stackoverflow.com/q/34983928?rq=3 "Question score (upvotes - downvotes)")[Add a prefix to beginning of each line depending on its size](https://stackoverflow.com/questions/34983928/add-a-prefix-to-beginning-of-each-line-depending-on-its-size?rq=3)

[1](https://stackoverflow.com/q/44578797?rq=3 "Question score (upvotes - downvotes)")[Linux Bash: add prefix to lines if match the condition](https://stackoverflow.com/questions/44578797/linux-bash-add-prefix-to-lines-if-match-the-condition?rq=3)

[0](https://stackoverflow.com/q/45571474?rq=3 "Question score (upvotes - downvotes)")[Add prefix to a line from the line before it in shell](https://stackoverflow.com/questions/45571474/add-prefix-to-a-line-from-the-line-before-it-in-shell?rq=3)

#### [Hot Network Questions](https://stackexchange.com/questions?tab=hot)

- [Can I change a 12 speed eagle cassete to a 9 speed CUES cassete?](https://bicycles.stackexchange.com/questions/94807/can-i-change-a-12-speed-eagle-cassete-to-a-9-speed-cues-cassete)
- [Real-life problems involving solving triangles](https://matheducators.stackexchange.com/questions/27943/real-life-problems-involving-solving-triangles)
- [What scientifically plausible apocalypse scenario, if any, meets my criteria?](https://worldbuilding.stackexchange.com/questions/259835/what-scientifically-plausible-apocalypse-scenario-if-any-meets-my-criteria)
- [Can non-admins create new domain on local DNS from a client computer?](https://serverfault.com/questions/1162234/can-non-admins-create-new-domain-on-local-dns-from-a-client-computer)
- [ArXiv submission on hold for 11 days. Should I inquire via moderation support or wait longer?](https://academia.stackexchange.com/questions/212097/arxiv-submission-on-hold-for-11-days-should-i-inquire-via-moderation-support-or)
- [Keyboard Ping Pong](https://codegolf.stackexchange.com/questions/274018/keyboard-ping-pong)
- [Did any other European leader praise China for its peace initiatives since the outbreak of the Ukraine war?](https://politics.stackexchange.com/questions/88225/did-any-other-european-leader-praise-china-for-its-peace-initiatives-since-the-o)
- [How to turn a sum into an integral?](https://physics.stackexchange.com/questions/820861/how-to-turn-a-sum-into-an-integral)
- [Are you radical enough to solve this SURDOKU?](https://puzzling.stackexchange.com/questions/127358/are-you-radical-enough-to-solve-this-surdoku)
- [The centre of gravity of a triangle on a parabola lies on the axis of symmetry](https://math.stackexchange.com/questions/4943872/the-centre-of-gravity-of-a-triangle-on-a-parabola-lies-on-the-axis-of-symmetry)
- [Why is this transformer placed on rails?](https://electronics.stackexchange.com/questions/718877/why-is-this-transformer-placed-on-rails)
- [Is prescreening not detrimental for paid surveys?](https://stats.stackexchange.com/questions/650734/is-prescreening-not-detrimental-for-paid-surveys)
- [Why does Macbeth well deserve his name?](https://literature.stackexchange.com/questions/27357/why-does-macbeth-well-deserve-his-name)
- [Go the Distance](https://puzzling.stackexchange.com/questions/127361/go-the-distance)
- [Using grout that had hardened in the bag](https://diy.stackexchange.com/questions/303060/using-grout-that-had-hardened-in-the-bag)
- [Is this a Hadamard matrix?](https://codegolf.stackexchange.com/questions/273990/is-this-a-hadamard-matrix)
- [Alternatives to iterrow loops in python pandas dataframes](https://codereview.stackexchange.com/questions/292885/alternatives-to-iterrow-loops-in-python-pandas-dataframes)
- [Car stalls when coming to a stop except when in neutral](https://mechanics.stackexchange.com/questions/97277/car-stalls-when-coming-to-a-stop-except-when-in-neutral)
- [Efficient proof of Bessel's correction](https://stats.stackexchange.com/questions/650702/efficient-proof-of-bessels-correction)
- [Schreier-Sims algorithm for solving Rubik's cube](https://mathoverflow.net/questions/474711/schreier-sims-algorithm-for-solving-rubiks-cube)
- [Does accreditation matter in Computer Science (UK)?](https://academia.stackexchange.com/questions/212087/does-accreditation-matter-in-computer-science-uk)
- [Could a Black Market exist in a cashless society (digital currency)?](https://worldbuilding.stackexchange.com/questions/259851/could-a-black-market-exist-in-a-cashless-society-digital-currency)
- [When, if ever, is bribery legal?](https://law.stackexchange.com/questions/103753/when-if-ever-is-bribery-legal)
- [Coping with consequences of a dog bite before buying a puppy](https://parenting.stackexchange.com/questions/44236/coping-with-consequences-of-a-dog-bite-before-buying-a-puppy)

[Question feed](https://stackoverflow.com/feeds/question/2099471 "Feed of this question and its answers")

[](https://stackoverflow.com)

##### [Stack Overflow](https://stackoverflow.com)

- [Questions](https://stackoverflow.com/questions)
- [Help](https://stackoverflow.com/help)
- [Chat](https://chat.stackoverflow.com/?tab=site&host=stackoverflow.com)

##### [Products](https://stackoverflow.co/)

- [Teams](https://stackoverflow.co/teams/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=footer&utm_content=teams)
- [Advertising](https://stackoverflow.co/advertising/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=footer&utm_content=advertising)
- [Collectives](https://stackoverflow.co/collectives/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=footer&utm_content=collectives)
- [Talent](https://stackoverflow.co/advertising/employer-branding/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=footer&utm_content=talent)

##### [Company](https://stackoverflow.co/)

- [About](https://stackoverflow.co/)
- [Press](https://stackoverflow.co/company/press/)
- [Work Here](https://stackoverflow.co/company/work-here/)
- [Legal](https://stackoverflow.com/legal)
- [Privacy Policy](https://stackoverflow.com/legal/privacy-policy)
- [Terms of Service](https://stackoverflow.com/legal/terms-of-service/public)
- [Contact Us](https://stackoverflow.com/contact)

- [Cookie Policy](https://stackoverflow.com/legal/cookie-policy)

##### [Stack Exchange Network](https://stackexchange.com)

- [Technology](https://stackexchange.com/sites#technology)
- [Culture & recreation](https://stackexchange.com/sites#culturerecreation)
- [Life & arts](https://stackexchange.com/sites#lifearts)
- [Science](https://stackexchange.com/sites#science)
- [Professional](https://stackexchange.com/sites#professional)
- [Business](https://stackexchange.com/sites#business)
- [API](https://api.stackexchange.com/)
- [Data](https://data.stackexchange.com/)

- [Blog](https://stackoverflow.blog?blb=1)
- [Facebook](https://www.facebook.com/officialstackoverflow/)
- [Twitter](https://twitter.com/stackoverflow)
- [LinkedIn](https://linkedin.com/company/stack-overflow)
- [Instagram](https://www.instagram.com/thestackoverflow)

Site design / logo © 2024 Stack Exchange Inc; user contributions licensed under [CC BY-SA](https://stackoverflow.com/help/licensing). <a id="svnrev"></a>rev 2024.7.9.12232