---
title: "!/usr/bin/env bash"
category: "editors-and-tools"
tags: ["editors-and-tools", "script", "make", "all", "files"]
---

#!/usr/bin/env bash
set -euo pipefail

# Usage: ./run.sh [TARGET_DIR]
TARGET_DIR="${1:-.}"

shopt -s globstar nullglob

# Normalise filename: lowercase, replace spaces with underscores, remove special chars except . _ -
normalize_name() {
  local name="$1"
  local base ext newbase

  if [[ "$name" == *.* ]]; then
    base="${name%.*}"
    ext=".${name##*.}"
  else
    base="$name"
    ext=""
  fi

  # lowercase
  newbase="$(printf '%s' "$base" | tr '[:upper:]' '[:lower:]')"
  # replace spaces with underscores
  newbase="${newbase// /_}"
  # remove any characters except a-z0-9._- (keep underscore and hyphen)
  newbase="$(printf '%s' "$newbase" | sed 's/[^a-z0-9._-]//g')"

  printf '%s%s' "$newbase" "$ext"
}

# Iterate files recursively under TARGET_DIR
while IFS= read -r -d '' file; do
  [[ -f "$file" ]] || continue

  filename="$(basename "$file")"

  # get modification time in format YYYY-MM (GNU stat)
  mod_ym="$(stat -c %y "$file" | cut -d' ' -f1 | awk -F- '{printf "%s-%02d", $1, $2}')"

  target_dir="$TARGET_DIR/$mod_ym"
  mkdir -p "$target_dir"

  newname="$(normalize_name "$filename")"

  # ensure unique filename in target directory
  dest="$target_dir/$newname"
  if [[ -e "$dest" ]]; then
    base="${newname%.*}"
    ext=""
    if [[ "$newname" == *.* ]]; then
      ext=".${newname##*.}"
    fi
    counter=1
    while [[ -e "$target_dir/${base}_$counter${ext}" ]]; do
      ((counter++))
    done
    dest="$target_dir/${base}_$counter${ext}"
  fi

  mv -n "$file" "$dest"
done < <(find "$TARGET_DIR" -type f -print0)

echo "Done."
