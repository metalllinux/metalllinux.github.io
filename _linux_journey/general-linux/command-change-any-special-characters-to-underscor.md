---
title: "Command Change Any Special Characters To Underscore"
category: "general-linux"
tags: ["command", "change", "any", "special", "characters"]
---

## Basic Usage (Perl rename)

If you have Perl's `rename` (aka `prename`) installed, replace any character that isn't alphanumeric, a dot, or a hyphen with an underscore:

```bash
rename -- 's/[^0-9a-zA-Z.-]/_/g' *
```

The `--` prevents filenames starting with `-` from being interpreted as flags.

**Note:** On many distros (e.g. Rocky Linux, Fedora), the default `rename` is from `util-linux` and does **not** support Perl regex. Check with `rename --version`. If you see `util-linux`, use the for loop approach below instead, or install `prename`.

## For Loop Approach (No Perl rename Required)

This works on any system with `perl` installed, regardless of which `rename` you have:

```bash
for f in /path/to/files/*; do
  dir=$(dirname "$f")
  base=$(basename "$f")
  newname=$(echo "$base" | perl -CSD -pe 's/[^0-9a-zA-Z.-]/_/g')
  [ "$base" != "$newname" ] && mv "$dir/$base" "$dir/$newname"
done
```

## Preserving Japanese Characters

To keep kanji, hiragana, katakana, and common Japanese punctuation intact:

```bash
for f in /path/to/files/*; do
  dir=$(dirname "$f")
  base=$(basename "$f")
  newname=$(echo "$base" | perl -CSD -pe 's/[^0-9a-zA-Z.\p{Han}\p{Hiragana}\p{Katakana}ー々〜～・「」-]/_/g')
  [ "$base" != "$newname" ] && mv "$dir/$base" "$dir/$newname"
done
```

- `-CSD` — tells Perl to handle UTF-8 on stdin, stdout, and default layers
- `\p{Han}` — kanji (漢字)
- `\p{Hiragana}` — hiragana (ひらがな)
- `\p{Katakana}` — katakana (カタカナ)
- `ー々〜～・「」` — common Japanese punctuation (long vowel mark, repeat kanji mark, wave dash, middle dot, brackets)

With Perl's `rename` the equivalent command is:

```bash
rename -- 's/[^0-9a-zA-Z.\p{Han}\p{Hiragana}\p{Katakana}ー々〜～・「」-]/_/g' *
```