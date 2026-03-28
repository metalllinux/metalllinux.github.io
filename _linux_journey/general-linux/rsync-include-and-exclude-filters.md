---
title: "Rsync Include and Exclude Filters"
category: "general-linux"
tags: ["rsync", "include", "exclude", "filters", "backup"]
---

## Overview

Rsync's `--include` and `--exclude` options let you selectively transfer files based on pattern matching. Rules are evaluated in order from first to last, and the first matching rule wins. This makes rule ordering critical.

## Basic Syntax

```bash
rsync -avP \
  --include='PATTERN' \
  --exclude='PATTERN' \
  /source/directory/ /destination/directory/
```

- `--include='PATTERN'` — transfer files matching this pattern
- `--exclude='PATTERN'` — skip files matching this pattern
- Rules are evaluated **top to bottom**; first match wins

## Using `**` for Recursive Matching

The `**` wildcard matches any path component, including subdirectories. This is especially useful when your files are nested at unknown depths.

| Pattern | Matches |
|---------|---------|
| `*` | Any filename in the current directory |
| `**` | Any file at any depth |
| `*.m2ts` | All `.m2ts` files in the current directory |
| `**/*.m2ts` | All `.m2ts` files at any depth |
| `**/reports-monday**` | Any file containing `reports-monday` at any depth |

## Selective Transfer with Include/Exclude

The most common pattern is to include specific files and exclude everything else:

```bash
rsync -avP \
  --include='**/*-monday*' \
  --include='**/*-special-edition*' \
  --include='**/*-weekly-summary*' \
  --include='**/*-highlights*' \
  --exclude='*' \
  /source/directory/ /destination/directory/
```

This transfers only files matching the four include patterns and ignores everything else.

### How Rule Order Works

```bash
rsync -avP \
  --include='**/*-monday*'         \  # 1. Include monday files
  --include='**/*-weekly-summary*' \  # 2. Include weekly summaries
  --exclude='*'                    \  # 3. Exclude everything else
  /source/directory/ /destination/directory/
```

A file is checked against rule 1 first. If it matches, it is included. If not, it moves to rule 2, and so on. The final `--exclude='*'` acts as a catch-all to reject anything not previously matched.

## Practical Example: One File Per Category Per Week

Suppose you have a directory of daily recordings and you only want to transfer one episode per show per week, plus all special editions:

```
/recordings/
├── 2025-02-17-show-a-monday.m2ts
├── 2025-02-18-show-a-tuesday.m2ts
├── 2025-02-19-show-a-wednesday.m2ts
├── 2025-02-17-show-b-episode-12.m2ts
├── 2025-02-18-show-c-episode-45.m2ts
├── 2025-02-17-show-a-special-edition.m2ts
└── 2025-02-20-unrelated-program.m2ts
```

To transfer only Monday episodes of Show A, all of Show B, all of Show C, and all special editions:

```bash
rsync -avP \
  --include='**/*show-a-monday*' \
  --include='**/*show-a-special-edition*' \
  --include='**/*show-b*' \
  --include='**/*show-c*' \
  --exclude='*' \
  /recordings/ /backup/recordings/
```

This results in transferring:
- `2025-02-17-show-a-monday.m2ts` (matched by rule 1)
- `2025-02-17-show-a-special-edition.m2ts` (matched by rule 2)
- `2025-02-17-show-b-episode-12.m2ts` (matched by rule 3)
- `2025-02-18-show-c-episode-45.m2ts` (matched by rule 4)

While skipping:
- `2025-02-18-show-a-tuesday.m2ts` (excluded by catch-all)
- `2025-02-19-show-a-wednesday.m2ts` (excluded by catch-all)
- `2025-02-20-unrelated-program.m2ts` (excluded by catch-all)

## Using Filter Files

For complex rule sets, store filters in a file:

```bash
# filters.txt
+ **/*show-a-monday*
+ **/*show-a-special-edition*
+ **/*show-b*
+ **/*show-c*
- *
```

Then reference it with `--filter`:

```bash
rsync -avP --filter='merge filters.txt' /recordings/ /backup/recordings/
```

In filter files, `+` means include and `-` means exclude.

## Dry Run

Always preview what will be transferred before committing:

```bash
rsync -avP --dry-run \
  --include='**/*show-a-monday*' \
  --exclude='*' \
  /recordings/ /backup/recordings/
```

The `--dry-run` flag shows what rsync *would* do without actually copying any files.

## Common Pitfalls

- **Rule order matters** — an early `--exclude='*'` will block all subsequent includes
- **Trailing slash on source** — `/source/` copies contents; `/source` copies the directory itself
- **Single `*` vs `**`** — use `**` when files may be nested in subdirectories
- **Quoting patterns** — always single-quote patterns to prevent shell glob expansion
