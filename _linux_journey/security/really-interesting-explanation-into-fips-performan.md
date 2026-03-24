---
title: "Really Interesting Explanation Into Fips Performan"
category: "security"
tags: ["security", "really", "interesting", "explanation", "into"]
---

Why then is getrandom slow in FIPS mode ?
Hard to say without more info, but after looking at the DBRG :spaghetti: I can't imagine it'd ever be fast. When fips=1, the getrandom syscall in CRNG is hijacked to use crypto/rng.c's crypto_devrandom_read() function instead, which then uses the highest-priority DRBG as defined by the order of the drbg_cores array in crypto/drbg.c. Since CONFIG_CRYPTO_DRBG_HMAC=y and HMAC is the highest priority, that means HMAC (SHA512) should be in use. The DRBG (re)seed function, __drbg_seed(), uses a non-blocking call to the CRNG via get_random_bytes() to get some raw entropy that is then mixed by a call to drbg_hmac_update(), which does two HMAC rounds on the same sequence of seed data. And then when the mixed entropy is extracted by a call to drbg_hmac_generate(), it goes through another HMAC pass via drbg_kcapi_hash(). If you HMAC a zillion times, it's secure! :smart:
So the call chain looks something like this:
sys_getrandom
  crypto_devrandom_read
    crypto_rng_get_bytes
      crypto_rng_generate
        drbg_kcapi_random
          drbg_generate_long
            drbg_generate
              drbg_seed //only if reseeding is needed, or explicitly requested with GRND_RANDOM
                drbg_get_random_bytes
                  get_random_bytes
                __drbg_seed
                  drbg_hmac_update
              drbg_kcapi_random
                drbg_generate_long
                  drbg_generate
                    drbg_hmac_generate
OK, aside from the obvious of how much code runs here (with lots of slow SHA512 hashing), why else could it be slow?
Well, if there is any concurrent use of the DRBG by tasks of varying scheduling priority, performance can suffer from the myriad of priority inversions lurking within the DRBG call chain I've written above. There are a lot of mutex locks used in those code paths, and drbg_generate_long() even locks/unlocks a mutex in a loop for each 64 KiB slice of random bytes generated, which can further hurt performance when >64 KiB of random bytes are requested.
Normal mutex locks lack priority inheritance, so all mutex locks utilised by crypto/rng.c and crypto/drbg.c should be converted to RT mutexes (include/linux/rtmutex.h) to fix the priority inversion.
Other than that, this code is just really slow, and is made slower by using the infamously slow crypto API in drbg_kcapi_hash() during the generation step.