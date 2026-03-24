---
title: "What to Do When you Have an Article for Rocky Linux Docs and It Affects All Three Versions of Rocky Linux"
category: "rocky-linux"
tags: ["rocky-linux", "when", "article", "rocky", "linux"]
---

# What to Do When you Have an Article for Rocky Linux Docs and It Affects All Three Versions of Rocky Linux

Good day everyone and Happy Holidays wherever you are!

I had a question please about the multiple versions of the Rocky Linux Documentation website.

I see there are three different branches, 10 latest, 9 and 8 and that makes perfect sense related to each major Rocky Linux version.

I am currently writing an article on how to create a kickstart file for Rocky Linux. I want to cover all current latest versions (10.1, 9.7 and 8.10) of Rocky Linux in the article and the changes that would need to be made in the kickstart file per version.

Should I create three separate versions of the article and then create three different PRs? One article that covers 8.10, one for 9.7 and one for 10.1 respectfully? Or should I create the one article that covers all Rocky Linux versions?

Thanks ever so much for taking the time to look at my question and the Rocky Linux Docs really are an excellent resource!

Wale's Response:

@Howard   - 1st off - THANK YOU  :rockyheart: 

Either approach is fine. But:
I'll recommend that you start of creating one for latest Rocky Linux v10.
You can drop subtle in the doc/guide for RL 10 that calls out the specific differences as they affect Rl 9 and RL8. And if the differences are too many - we can consider separate docs for RL 8 & 9.
please start with RL-10 for now :-)

My response:

Thank YOU @wale !

That's excellent and exactly the advice I was looking for thank you! Okay, I'll create the one article for Rocky Linux 10 and if there are minor differences that affect Rocky Linux 9 and 8, I will call those out in the same article.

