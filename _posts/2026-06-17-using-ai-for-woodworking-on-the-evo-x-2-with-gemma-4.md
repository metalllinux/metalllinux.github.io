---
title: "Using AI for Woodworking on the EVO-X-2"
date: 2026-07-03
categories: ai
tags: [ai, llama.cpp, rocky-linux, local-ai, gmktec evo-x-2, woodworking, gemma]
excerpt: "Running Google's Gemma 4 31B locally on the GMKtec EVO-X-2 to assist with woodworking projects — from timber selection and joinery planning to finish schedules and cut lists."
---

In my [previous post](/ai/2026/06/07/setting-up-rocky-linux-10-on-a-gmktec-evo-x-2-with-llama-cpp.html) I got Rocky Linux 10 running on the GMKtec EVO-X-2 with llama.cpp and full Vulkan GPU offload, serving Qwen3-Coder-Next as a local coding assistant via OpenCode. One of the things I mentioned wanting to explore was using the machine to help plan and research woodworking projects and here we are!

## Using Gemma 4 for woodworking

With the model running and wired into OpenCode, I started putting it to use on some actual woodworking problems.

### Case Study: Upgrading the Nintendo Switch Game Shelf

I decided to test Gemma 4's ability to handle specific dimensions and cultural context by asking it to help me upgrade my [Nintendo Switch game shelf](https://metalinux.dev/woodwork/nintendo-switch-game-shelf/). I wanted to add a sliding door that slides outwards, similar to a Japanese sliding door, including a lock.

**The Prompt:**
"I want to upgrade my game shelf (43 cm wide x 40.4 cm tall) using a piece of wood (3 cm thick) to add a sliding door that slides outwards, like a Japanese sliding door. I need a lock as well. Please provide instructions and a shopping list for a Japanese hardware store, including the Japanese terms for the items."

**Gemma 4's Response:**
"To create a Japanese-inspired sliding door (similar to a *Shoji* or *Fusuma* style) for your game shelf, you'll want to implement a track system that allows the door to glide horizontally. Given your wood thickness of 3 cm, we will focus on a sturdy, surface-mounted track approach.

#### Technical Plan
- **Shelf Dimensions**: 43 cm (W) x 40.4 cm (H)
- **Door Material**: 3 cm thick wood
- **Mechanism**: Top and bottom sliding rails

#### Step-by-Step Instructions
1. **Dimensioning the Door**: Cut your wood to approximately 44 cm x 41 cm. This provides a slight overlap (overhang) on the edges to prevent gaps and ensure the 'outward' sliding feel.
2. **Installing the Tracks**: 
   - Purchase two U-shaped aluminum channels. 
   - Mount one channel to the top edge of the shelf and one to the bottom.
   - Since you want it to slide 'outwards', mount the tracks so they are flush with the front face of the shelf.
3. **Fitting the Door**: Insert the door into the channels. If the fit is too tight, sand the edges of the wood slightly.
4. **Adding the Lock**: Install a sliding bolt lock (*Suraido boruto*) to keep the door secure. Mount the bolt mechanism on the inner face of the sliding door, approximately 5-10 cm from the top edge for easy access. Then, fix the corresponding catch (the receiver) to the inner side wall of the shelf. When the door is closed, the bolt should slide horizontally into the catch, locking the door firmly against the shelf frame.

#### Shopping List for a Japanese Hardware Store (ホームセンター - Hōmu Sentā)
To get the right parts, you can use these terms:

| English | Japanese (Kanji/Kana) | Romaji |
| :--- | :--- | :--- |
| Sliding Rail / U-Channel | アルミ製Uチャンネル / スライドレール | *Arumi-sei U-channeru / Suraido reiru* |
| Wood Screws | 木ねじ | *Kineji* |
| Sliding Bolt Lock | スライドボルト / かんぬき | *Suraido boruto / Kannuki* |
| Sandpaper | 紙やすり | *Kamiyasuri* |
| Wood Glue | 木工用ボンド | *Mokkō-yō bondo* |
| Right Angle Square | 直角定規 | *Chokkaku jōgi* |"

## The Final Product

![sam-1-game-shelf-woodworking-on-the-evo-x-2-with-gemma-4-1](/assets/images/sam-1-game-shelf-woodworking-on-the-evo-x-2-with-gemma-4-1.jpg)
![sam-1-game-shelf-woodworking-on-the-evo-x-2-with-gemma-4-2](/assets/images/sam-1-game-shelf-woodworking-on-the-evo-x-2-with-gemma-4-2.jpg)
![sam-1-game-shelf-woodworking-on-the-evo-x-2-with-gemma-4-3](/assets/images/sam-1-game-shelf-woodworking-on-the-evo-x-2-with-gemma-4-3.jpg)

## The Aftermath

While an AI can help guide you with skills such as woodworking that you're not necessarily familiar with, you still as a human need to practice practically with the tools (AI DEFINITELY CAN'T HELP YOU WITH THIS). I have not much experience at all with drills, nail sizes, hammering in nails, drilling pilot holes, figuring out how best to drill in screws, placement of locks / pieces of metal and so on. The AI can only guide you (show you the door) to those things; it is you who must walk through it. As Morpheus says in *The Matrix*: "I can only show you the door. You're the one who has to walk through it."

## Conclusion

I am happy with the end result and while the AI helped guide me, I still need more practical experience with using the tools themselves and figuring out how best to put things together, which an AI cannot teach you.
