---
title: "Using AI for Woodworking on the EVO-X-2 with Gemma 4"
date: 2026-06-17
categories: ai
tags: [ai, llama.cpp, rocky-linux, local-ai, gmktec evo-x-2, woodworking, gemma]
excerpt: "Running Google's Gemma 4 31B locally on the GMKtec EVO-X-2 to assist with woodworking projects — from timber selection and joinery planning to finish schedules and cut lists."
---

In my [previous post](/ai/2026/06/07/setting-up-rocky-linux-10-on-a-gmktec-evo-x-2-with-llama-cpp.html) I got Rocky Linux 10 running on the GMKtec EVO-X-2 with llama.cpp and full Vulkan GPU offload, serving Qwen3-Coder-Next as a local coding assistant via OpenCode. One of the things I mentioned wanting to explore was using the machine to help plan and research woodworking projects.

This post covers doing exactly that — swapping in Google's [Gemma 4 31B](https://huggingface.co/unsloth/gemma-4-31B-it-GGUF) as a second model on the same server and wiring it up in OpenCode for woodworking conversations. The llama.cpp installation and all the kernel and power configuration from the previous guide remain in place; this post only covers the new model.

## Why Gemma 4 31B

[Gemma 4](https://ai.google.dev/gemma/docs/gemma4) is Google DeepMind's fourth-generation open model family, released in April 2026. The 31B variant is a dense transformer with a 128K token context window and native multimodal support and it can accept both text and images in the same conversation.

That last point is genuinely useful for woodworking. Being able to drop a photo of a rough board, a joinery problem, or a reference piece and discuss it directly in the same context window changes the workflow considerably compared to a text-only model.

At Q4\_K\_M quantisation the 31B model is approximately 19 GB, which is a fraction of the EVO-X-2's 96 GB pool — and runs with full GPU offload on the Vulkan backend, leaving ample headroom for a generous context window.

[Unsloth](https://huggingface.co/unsloth) provide the quantised GGUF files and benchmark their Dynamic 2.0 variants (`UD-*`) as higher accuracy at the same bit-width. The `UD-Q4_K_XL` file is the recommended pick for this hardware. It has better accuracy than standard Q4\_K\_M with negligible size difference, and well within the memory budget.

## Downloading Gemma 4 

The `hf` CLI from the previous guide should already be installed and authenticated. If not, install and log in first:

```bash
python3 -m pip install -U huggingface_hub
git config --global credential.helper store
hf auth login
```

I created a directory for the model on my secondary NVMe drive. 

```bash
mkdir -p /mnt/data/models/gemma-4-31B-it/
sudo chown $USER:$USER /mnt/data/models/gemma-4-31B-it/
```

I downloaded the `UD-Q4_K_XL` quantisation:

```bash
hf download unsloth/gemma-4-31B-it-GGUF \
  gemma-4-31B-it-UD-Q4_K_XL.gguf \
  --local-dir /mnt/data/models/gemma-4-31B-it/
```

Gemma 4 is a multimodal model. To enable image input alongside text, the multimodal projector file is required as well:

```bash
hf download unsloth/gemma-4-31B-it-GGUF \
  mmproj-BF16.gguf \
  --local-dir /mnt/data/models/gemma-4-31B-it/
```

I verified both files were present before proceeding:

```bash
$ ls -lh /mnt/data/models/gemma-4-31B-it/
total 20G
-rw-r--r--. 1 howard howard  20G Jun 17 10:42 gemma-4-31B-it-UD-Q4_K_XL.gguf
-rw-r--r--. 1 howard howard 1.6G Jun 17 10:51 mmproj-BF16.gguf
```

## Starting llama-server with Gemma 4

The server flags are largely the same as in the previous guide. Two differences are worth noting:

- **`--mmproj`** — points to the multimodal projector file to enable image input.
- **`-c 131072`** — sets a 128K token context window, matching Gemma 4's full training context.

The `--alias` value must match exactly what OpenCode will reference in its configuration:

```bash
llama-server \
  --model /mnt/data/models/gemma-4-31B-it/gemma-4-31B-it-UD-Q4_K_XL.gguf \
  --mmproj /mnt/data/models/gemma-4-31B-it/mmproj-BF16.gguf \
  --alias gemma-4-31B-it-UD-Q4_K_XL \
  --host 0.0.0.0 \
  --port 8081 \
  --n-gpu-layers 99 \
  -fa on \
  --parallel 1 \
  -t 32 -tb 32 \
  -ub 2048 \
  -ctk q8_0 -ctv q8_0 \
  --mlock \
  -c 131072
```

I used port 8081 to avoid conflicting with the Qwen3-Coder-Next server already running on 8080.

I verified the server was healthy:

```bash
$ curl http://localhost:8081/health
{"status":"ok"}
```

I confirmed the model alias was set correctly:

```bash
$ curl -s http://localhost:8081/v1/models | python3 -m json.tool
```

```json
{
    "object": "list",
    "data": [
        {
            "id": "gemma-4-31B-it-UD-Q4_K_XL",
            "aliases": [
                "gemma-4-31B-it-UD-Q4_K_XL"
            ],
            "object": "model",
            "created": 1750111200,
            "owned_by": "llamacpp"
        }
    ]
}
```

### Persisting the Gemma 4 server at boot

Note: if you do not want multiple llama-server instances running at the same time, disable any existing service before enabling this one:

```bash
systemctl --user disable --now llama-server.service
```

I created a second user service unit for the Gemma 4 server alongside the existing Qwen3-Coder-Next unit:

```bash
tee ~/.config/systemd/user/llama-server-gemma4.service << 'EOF'
[Unit]
Description=llama.cpp API server (Gemma 4 31B)
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
LimitMEMLOCK=infinity
ExecStart=/usr/local/bin/llama-server \
    --model /mnt/data/models/gemma-4-31B-it/gemma-4-31B-it-UD-Q4_K_XL.gguf \
    --mmproj /mnt/data/models/gemma-4-31B-it/mmproj-BF16.gguf \
    --alias gemma-4-31B-it-UD-Q4_K_XL \
    --host 0.0.0.0 \
    --port 8081 \
    --n-gpu-layers 99 \
    -fa on \
    --parallel 1 \
    -t 32 -tb 32 \
    -ub 2048 \
    -ctk q8_0 -ctv q8_0 \
    --mlock \
    -c 131072
Restart=on-failure
RestartSec=5

[Install]
WantedBy=default.target
EOF
```

I reloaded the user daemon and enabled the service:

```bash
systemctl --user daemon-reload
systemctl --user enable --now llama-server-gemma4.service
```

I verified it was running:

```bash
$ systemctl --user status llama-server-gemma4.service
● llama-server-gemma4.service - llama.cpp API server (Gemma 4 31B)
     Loaded: loaded (/home/howard/.config/systemd/user/llama-server-gemma4.service; enabled; preset: disabled)
     Active: active (running) since ...
```

The `LimitMEMLOCK=infinity` override applied in the previous guide to `/etc/systemd/system/user@1000.service.d/limits.conf` covers all user services, so no additional system configuration was needed here.

### Opening the firewall

Port 8081 also needs to be opened in firewalld to allow inbound connections from other machines on the network:

```bash
sudo firewall-cmd --permanent --add-port=8081/tcp
sudo firewall-cmd --reload
```

I verified the rule was active:

```bash
$ sudo firewall-cmd --list-ports
8080/tcp 8081/tcp
```

## Configuring OpenCode

OpenCode supports multiple custom providers simultaneously. I added the Gemma 4 server as a second entry alongside the existing `evo-x2` provider in `~/.config/opencode/opencode.json`.

The model ID in the `models` map must match the `--alias` value exactly, and the `context` limit must match `-c`:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "evo-x2": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "EVO-X2 (llama.cpp)",
      "options": {
        "baseURL": "http://<YOUR_SERVER_IP>:8080/v1"
      },
      "models": {
        "Qwen3-Coder-Next": {
          "name": "Qwen3-Coder-Next-Q4_K_M (EVO-X2)",
          "limit": {
            "context": 65536,
            "output": 32768
          }
        }
      }
    },
    "evo-x2-gemma4": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "EVO-X2 Gemma 4 (llama.cpp)",
      "options": {
        "baseURL": "http://<YOUR_SERVER_IP>:8081/v1"
      },
      "models": {
        "gemma-4-31B-it-UD-Q4_K_XL": {
          "name": "Gemma-4-31B-it-UD-Q4_K_XL (EVO-X2)",
          "limit": {
            "context": 131072,
            "output": 65536
          }
        }
      }
    }
  }
}
```

I ran `/models` within OpenCode and selected `Gemma-4-31B-it-UD-Q4_K_XL (EVO-X2)` from the picker to switch over to the Gemma 4 server.

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



