---
title: "Recursively Replace Spaces with Underscores and Make All Characters Lowercase"
category: "editors-and-tools"
tags: ["editors-and-tools", "recursively", "make", "all", "directories"]
---

# Recursively Replace Spaces with Underscores and Make All Characters Lowercase
```
find . -depth | while IFS= read -r file; do
    new="$(dirname "$file")/$(basename "$file" | tr '[:upper:]' '[:lower:]' | tr ' ' '_')"
    if [ "$file" != "$new" ]; then
        echo "Renaming: $file -> $new"
        mv "$file" "$new"
    fi
done
```
