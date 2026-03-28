---
title: "Command Change Any Special Characters To Underscore"
category: "general-linux"
tags: ["command", "change", "any", "special", "characters"]
---

## Basic Usage

Replace any character that isn't alphanumeric, a dot, or a hyphen with an underscore:

```bash
rename -- 's/[^0-9a-zA-Z.-]/_/g' *
```

The `--` prevents filenames starting with `-` from being interpreted as flags.

## Preserving Japanese Characters

To keep kanji, hiragana, katakana, and common Japanese punctuation intact:

```bash
rename -- 's/[^0-9a-zA-Z.\p{Han}\p{Hiragana}\p{Katakana}ー々〜～・「」-]/_/g' *
```

- `\p{Han}` — kanji (漢字)
- `\p{Hiragana}` — hiragana (ひらがな)
- `\p{Katakana}` — katakana (カタカナ)
- `ー々〜～・「」` — common Japanese punctuation (long vowel mark, repeat kanji mark, wave dash, middle dot, brackets)