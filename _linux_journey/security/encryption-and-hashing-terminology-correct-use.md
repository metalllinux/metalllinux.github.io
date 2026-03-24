---
title: "Encryption and Hashing Terminology Correct Use"
category: "security"
tags: ["security", "encryption", "hashing", "terminology", "correct"]
---

# Encryption and Hashing Terminology Correct Use

Let's not call this "encryption" because it's hashing and not encryption. Let's not call these hashes SHA-512 because they're actually sha512crypt (a higher-level algorithm building upon SHA-512 and having very different properties as a result, making it much more suitable for password hashing than raw SHA-512 was).
"Encryption" is something they may setup separately, like you say with LUKS, but also it won't help against data leaks from the live server, whereas ensuring no old cached stuff stays in there will partially mitigate those (only data seen from the moment of compromise may leak).
