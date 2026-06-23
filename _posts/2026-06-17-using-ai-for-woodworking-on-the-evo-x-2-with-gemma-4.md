---
title: "Using AI for Woodworking on the EVO-X-2 with Gemma 4"
date: 2026-06-17
categories: ai
tags: [ai, llama.cpp, rocky-linux, local-ai, gmktec evo-x-2, woodworking, gemma]
excerpt: "Running Google's Gemma 4 31B locally on the GMKtec EVO-X-2 to assist with woodworking projects — from timber selection and joinery planning to finish schedules and cut lists."
---

In my [previous post](/ai/2026/06/07/setting-up-rocky-linux-10-on-a-gmktec-evo-x-2-with-llama-cpp.html) I got Rocky Linux 10 running on the GMKtec EVO-X-2 with llama.cpp and full Vulkan GPU offload, serving Qwen3-Coder-Next as a local coding assistant via OpenCode. One of the things I mentioned wanting to explore was using the machine to help plan and research woodworking projects.

## Why Gemma 4 31B

[Gemma 4](https://ai.google.dev/gemma/docs/gemma4) is Google DeepMind's fourth-generation open model family, released in April 2026. The 31B variant is a dense transformer with a 128K token context window and native multimodal support and it can accept both text and images in the same conversation.

That last point is genuinely useful for woodworking. Being able to drop a photo of a rough board, a joinery problem, or a reference piece and discuss it directly in the same context window changes the workflow considerably compared to a text-only model.

At Q4\_K\_M quantisation the 31B model is approximately 19 GB, which is a fraction of the EVO-X-2's 96 GB pool — and runs with full GPU offload on the Vulkan backend, leaving ample headroom for a generous context window.

My Gemma 4 setup is documented [here](/ai/2026/06/21/running-multiple-gemma-4-llama-cpp-instances-on-a-gmktec-evo-x-2.html).

## Using Gemma 4 for woodworking

With the model running and wired into OpenCode, I started putting it to use on some actual woodworking problems.

### Case Study: Upgrading the Game Shelf

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
4. **Adding the Lock**: Install a sliding bolt lock on the inner side of the door, securing it to the side wall of the shelf.

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



