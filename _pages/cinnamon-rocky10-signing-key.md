---
title: "Cinnamon for Rocky Linux 10 GPG Signing Key"
layout: single
permalink: /linux-journey/cinnamon-rocky10-signing-key/
author_profile: true
sidebar:
  nav: "linux-journey"
header:
  overlay_image: /assets/images/metalinux-2.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
---

This page is the canonical out-of-band anchor for the GPG key that signs the [Cinnamon for Rocky Linux 10](https://github.com/metalllinux/cinnamon-for-rocky10) repository. The "Verifying the release" section in the repository's INSTALL.md and the "Signing and release verification" section in its README.md both direct you to compare the fingerprint of the key shipped in the repository against the value published here before you trust the key. The key file in the repository is not an independent source of trust, and this page is the reference that makes the comparison meaningful.

## Fingerprint

```
1689676AF4D4F6FEC142B4429C0A8912FDA02785
```

## User ID

```
metallinux Cinnamon for Rocky Linux (repo signing) <repo-signing@metalinux.dev>
```

## Public key

The full armored public key, verbatim from `keys/cinnamon-rocky10-public.asc` in the repository:

```
-----BEGIN PGP PUBLIC KEY BLOCK-----

mQINBGqxAfQBEADXao51rU74woZr+MwDL8WOBP7cfPanGqf0rLHY16F8hs7ez9hP
0Izl2cx39piT68eg+VMI7HpgmYjzQwoFXq+4PRFd1RZDm8z8+0TdRFxf92tuK/eS
KwKSNQWuXbIqmyGMQSodihqL8eL3GZn40HrdllW470T3wXm102rqYNeklNxkfDR5
nRMrsL4SEDJb4oTKgijfQyvAmBAWHv+DQW8FY8/UCHrs5+izoVx8YsXF0Ss1MQdQ
B5wMPd1IdZx3rGmEU1mnnyww1U9Zdk7J3U4bU2qxkTwB4Dzg4M8Jen/O8As9vw27
VzJj/B7V8FektogyQX8kCdIZv8J7rC9PXgAYuuE0q4z//KvHx5Wt+03oWIYgSvl+
lAK+ERyKHpVrQIr2s/LiA4+o+ewusz7qVUoHp0uXbChgLQJE+vnM8gS+4LFB7z67
SLbLXG5IgDguN4pP7EVc3m10DO9/PXxhbxSrpHm3lhNdLsP5BCtAPgM3E6Pn43kC
9gQ/iEvfKzwndztSU/33CTjTcrxSth9GDLqwYkGXfqdeQmGamoJtAIhvVUklWeIY
PqI4L+9vCfBGncPbG3FLm9+vijEWkGdQ7ysP/EEhCDKVf5y2fvJ7Af+enRyeTN4t
UPTTh1U+xTRZTS3TATkaQD4za+3/aLm/VAwM2VD7zDSZ0GjZXYaOD66wIwARAQAB
tE9tZXRhbGxpbnV4IENpbm5hbW9uIGZvciBSb2NreSBMaW51eCAocmVwbyBzaWdu
aW5nKSA8cmVwby1zaWduaW5nQG1ldGFsaW51eC5kZXY+iQJRBBMBCAA7FiEEFoln
avTU9v7BQrRCnAqJEv2gJ4UFAmqxAfQCGwMFCwkIBwICIgIGFQoJCAsCBBYCAwEC
HgcCF4AACgkQnAqJEv2gJ4VGKw/9GFgGiDBYVjy3zriaHvBSq84VXH9ucBAC6lS6
cpfBVRIB7RHlwZ1gtA3lH7upc0vI1euB74maCaNwFAQUC1WfCibu3CPfBupPwB15
U3wB26y5k2h0BKq8QKzN/QBL3J9kDT9HX/h4PXrZwG3hYd0jHMUA8kMaK5/yoIEu
D9iRCUpcQTfLR8ydFmKD4gEoF9VN+jWqQ2UZaEQiOdeFyAPTifteot5qhchSfnwL
wpkR0MiNtBRaKesaVymCdH7+d3JIGoYmDatWd+V2t2rGIouJSIGLFOOtFMIHaEoe
JpQJ5TFB0GNNU8o1/1Fqs7uGPwADThDBGd+DWW4bqKTEKAgjSgT3OdnZbIFyU+lo
vTNUkNgYgcpZi7TbB4QJ3NtckcT55av9DBpoMQvSQrCGYe2qJDAqZmnXChVYJKbw
yy9fck7wamOzegexhBESlHiD3IBEIm9M5kV9AbIyojJN81hlYxRX5bD1MBnFxsGI
+VVLUFelmdQCQdE5254LwogpQXTeluGKYXm0o9PCxPIrHMwu8RC8v8l6fM8orEV7
ZLA4AItsEeIiLLk18vwBVqWBsGVHYz9VdHCV5q6kN6yQNu03RxjJsTRTk6twWCmg
HHoQahOq/XG3UOZvb8huWAmmyxliMON5rocgpRMT80EZRHZdu0oS49T1Q2o8oh32
J/hFmu8=
=f2of
-----END PGP PUBLIC KEY BLOCK-----
```

## How to verify

Ask GPG to print the fingerprint of the key file shipped in the repository. This reads the file only and does not import anything into a keyring.

```
gpg --show-keys keys/cinnamon-rocky10-public.asc
```

GPG prints the key block with the fingerprint, in groups of four hex digits, on the line following the `pub` line. Compare that value, ignoring the spaces, character by character, against the fingerprint published at the top of this page. If the two match, the key in your copy of the repository is the legitimate signing key for the Cinnamon for Rocky Linux 10 repository. If they do not match, do not import the key into your rpm keyring, and treat the repository contents as untrusted until you can establish where the key in your copy came from.
