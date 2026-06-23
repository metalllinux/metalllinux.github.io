---
title: "Running multiple Gemma 4 llama.cpp instances on a GMKtec Evo-X-2"
date: 2026-06-21
categories: ai
tags: [ai, llama.cpp, rocky-linux, local-ai, gmktec evo-x-2, gemma]
excerpt: "Maximizing the utility of a 96GB GMKtec EVO-X-2 by running multiple concurrent llama.cpp instances of Gemma 4 31B with full 128K context."
---

Having successfully set up Rocky Linux 10 and Gemma 4 31B on the GMKtec EVO-X-2, the next question is: how many of these instances can I run simultaneously?

With 96GB of unified memory and the way `llama-server` uses `mmap` to load model weights, multiple processes can share the same physical memory pages for the model weights. This means the primary memory cost for each additional instance is the KV cache for the context window.

For Gemma 4 31B with a 128K context window and Q8_0 KV cache, each instance requires a significant chunk of RAM. On a 96GB system, I can run several instances while maintaining stability.

## Configuration Strategy

To run multiple instances, I need to:
1. Use the same model and mmproj files.
2. Assign a unique port to each server.
3. Assign a unique alias to each model for OpenCode.
4. Create separate systemd user services for each.

## Instance 1 (Port 8081)

This is the base configuration.

```bash
tee ~/.config/systemd/user/llama-server-gemma4-1.service << 'EOF'
[Unit]
Description=llama.cpp API server (Gemma 4 31B - 1)
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
LimitMEMLOCK=infinity
ExecStart=/usr/local/bin/llama-server \
    --model /mnt/data/models/gemma-4-31B-it/gemma-4-31B-it-UD-Q4_K_XL.gguf \
    --mmproj /mnt/data/models/gemma-4-31B-it/mmproj-BF16.gguf \
    --alias gemma-4-31B-it-UD-Q4_K_XL-1 \
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

## Instance 2 (Port 8082)

For the second instance, I increment the port and update the alias.

```bash
tee ~/.config/systemd/user/llama-server-gemma4-2.service << 'EOF'
[Unit]
Description=llama.cpp API server (Gemma 4 31B - 2)
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
LimitMEMLOCK=infinity
ExecStart=/usr/local/bin/llama-server \
    --model /mnt/data/models/gemma-4-31B-it/gemma-4-31B-it-UD-Q4_K_XL.gguf \
    --mmproj /mnt/data/models/gemma-4-31B-it/mmproj-BF16.gguf \
    --alias gemma-4-31B-it-UD-Q4_K_XL-2 \
    --host 0.0.0.0 \
    --port 8082 \
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

## Instance 3 (Port 8083)

For the third instance, I increment the port and update the alias.

```bash
tee ~/.config/systemd/user/llama-server-gemma4-3.service << 'EOF'
[Unit]
Description=llama.cpp API server (Gemma 4 31B - 3)
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
LimitMEMLOCK=infinity
ExecStart=/usr/local/bin/llama-server \
    --model /mnt/data/models/gemma-4-31B-it/gemma-4-31B-it-UD-Q4_K_XL.gguf \
    --mmproj /mnt/data/models/gemma-4-31B-it/mmproj-BF16.gguf \
    --alias gemma-4-31B-it-UD-Q4_K_XL-3 \
    --host 0.0.0.0 \
    --port 8083 \
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

## Scaling and Activation

You can repeat this process for further instances (8084, 8085 etc.), monitoring memory usage with `free -h` and GPU activity with `amdgpu_top` to ensure the system does not swap or crash.

To activate the services:

```bash
systemctl --user daemon-reload
systemctl --user enable --now llama-server-gemma4-1.service
systemctl --user enable --now llama-server-gemma4-2.service
systemctl --user enable --now llama-server-gemma4-3.service
```

## Firewall Configuration

Open all required ports in `firewalld`:

```bash
sudo firewall-cmd --permanent --add-port=8081/tcp
sudo firewall-cmd --permanent --add-port=8082/tcp
sudo firewall-cmd --permanent --add-port=8083/tcp
sudo firewall-cmd --reload
```

## OpenCode Configuration

Update `~/.config/opencode/opencode.json` to include these instances. Using separate provider IDs allows you to easily switch between instances in the model picker. Note that a 10-minute timeout is required to prevent API timeout errors during the initial model warm-up phase.

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "evo-x2-gemma4-1": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "EVO-X2 Gemma 4-1 (llama.cpp)",
      "options": {
        "baseURL": "http://<YOUR_SERVER_IP>:8081/v1",
        "timeout": 600000
      },
      "models": {
        "gemma-4-31B-it-UD-Q4_K_XL-1": {
          "name": "Gemma-4-31B-it-UD-Q4_K_XL-1 (EVO-X2)",
          "limit": {
            "context": 131072,
            "output": 65536
          }
        }
      }
    },
    "evo-x2-gemma4-2": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "EVO-X2 Gemma 4-2 (llama.cpp)",
      "options": {
        "baseURL": "http://<YOUR_SERVER_IP>:8082/v1",
        "timeout": 600000
      },
      "models": {
        "gemma-4-31B-it-UD-Q4_K_XL-2": {
          "name": "Gemma-4-31B-it-UD-Q4_K_XL-2 (EVO-X2)",
          "limit": {
            "context": 131072,
            "output": 65536
          }
        }
      }
    },
    "evo-x2-gemma4-3": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "EVO-X2 Gemma 4-3 (llama.cpp)",
      "options": {
        "baseURL": "http://<YOUR_SERVER_IP>:8083/v1",
        "timeout": 600000
      },
      "models": {
        "gemma-4-31B-it-UD-Q4_K_XL-3": {
          "name": "Gemma-4-31B-it-UD-Q4_K_XL-3 (EVO-X2)",
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

## Caveats

Running three Gemma 4 31B models is possible on my 96GB RAM version of the EVO-X-2. However, the three models combined use up 82GB of the available 90GB that can be provided to the GPU. 

![](/assets/images/gemma-4-models-high-memory-usage.png)

## Model response times

Running a 31B parameter model of this size is slow to initially warm up on the EVO-X-2. For example, asking the model to update my `~/.config/opencode/opencode.json` configuration, took it around 9 minutes to complete the task. 

Once the initial warm-up phase was completed, the response time went down to around 1~2 minutes, which I thought was pretty amazing! 

## Conclusion

By leveraging memory mapping and unique ports, the GMKtec EVO-X-2 becomes a powerful multi-tenant AI server, allowing different tasks or users to have dedicated Gemma 4 instances with their own context windows. Give it a try for yourself! 
