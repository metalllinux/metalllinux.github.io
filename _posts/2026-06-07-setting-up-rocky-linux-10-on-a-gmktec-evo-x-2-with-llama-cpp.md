---
title: "Setting up Rocky Linux 10 on a GMKtec EVO-X-2 with llama.cpp"
date: 2026-06-07
categories: ai
tags: [ai, llama.cpp, rocky-linux, local-ai, gmktec]
excerpt: "Setting up a local AI inference box using a GMKtec EVO-X-2 mini PC running Rocky Linux 10 and llama.cpp."
---

None of this would have been possible without the brilliant work of [Damen Knight](https://www.damenknight.com/running-frontier-coding-model-mini-pc/). I highly encourage any readers to go through his blog series first before continuing with this post.

I have been wanting to set up a dedicated local AI inference machine for a while now, and I recently picked up a GMKtec EVO-X-2 mini PC for that purpose. The plan is to get Rocky Linux 10 installed on it and then build llama.cpp from source to run local models. This post documents the process, starting with what turned out to be a more frustrating first step than expected.

## Installing Rocky Linux

For reference, the firmware on the machine at the time of installation was as follows:

| Field | Value |
|---|---|
| BIOS Version | EVO-X2 1.11 |
| EC Firmware Version | 1.08 |
| BIOS Build Date and Time | 10/17/2025 17:33:08 |

In the BIOS I also set **Power Mode Select** to **Performance Mode**.

The first task was simply getting Rocky Linux onto the machine. I downloaded the Rocky Linux 10.2 DVD ISO and set about creating a bootable USB stick using a Verbatim 64GB USB3 drive. What followed was a considerably longer exercise in troubleshooting than I anticipated.

The EVO-X-2 was simply unable to read the Verbatim 64GB USB3 memory stick. I verified the drive had been written correctly using multiple tools, but the machine would not recognise it as bootable in any case:

- **`dd`** — the standard go-to on Linux for writing ISOs directly to a block device. The write completed without errors and I verified the flash was successful, but the EVO-X-2 refused to boot from it.
- **[Fedora Media Writer](https://github.com/FedoraQt/MediaWriter)** — a reliable tool I have used successfully with Fedora ISOs in the past. Again, the process completed cleanly and the flash was verified, but the machine would not recognise the stick as bootable.
- **[Rufus](https://rufus.ie/)** — attempted this from a Windows machine as a last resort. Same outcome.
- **[Ventoy](https://www.ventoy.net/)** — tried as a further option, but the EVO-X-2 was unable to find Ventoy either.

### PXE Boot

With USB boot ruled out entirely, I turned to PXE boot. I followed [this guide](https://metalinux.dev/linux-journey/rocky-linux/how-to-set-up-pxe-boot-on-rocky-linux-9-x/) to configure my Beelink machine running Rocky Linux 9 as a PXE server, placing the Rocky Linux 10.2 ISO on it. Back on the EVO-X-2, I configured iPXE via the BIOS to boot via IPv4.

The machine booted successfully from the network. I selected the first option to launch an RDP server — however, this immediately surfaced another problem: the display output on the EVO-X-2 was constantly flickering, making it impossible to continue the setup via the machine itself with a keyboard.

On a separate machine I installed [Remmina](https://remmina.org/) and connected to the EVO-X-2 over RDP. This worked. I was presented with the Anaconda installer running in full graphical mode via Remmina, which allowed me to complete the installation properly — wiping Windows 11 from the primary NVMe drive and installing Rocky Linux 10 in its place. The installation completed successfully.

Installing Rocky Linux 10 on the GMKtec EVO-X-2 was decidedly non-trivial. Between the USB boot failures across four different tools and the display flickering issue that required a remote desktop workaround just to complete the installer, it took considerably more effort than a standard installation. That said, the machine is now up and running with Rocky Linux 10.

## The kernel install

With Rocky Linux 10 installed, the next step was to install a mainline kernel via [ELRepo's kernel-ml](https://elrepo.org/wiki/doku.php?id=kernel-ml). The `kernel-ml` package tracks the mainline stable kernel and is useful for getting up-to-date hardware support on Enterprise Linux distributions.

```bash
sudo dnf install -y elrepo-release
sudo rpm --import https://www.elrepo.org/RPM-GPG-KEY-elrepo.org
sudo dnf --enablerepo=elrepo-kernel install -y kernel-ml
```

Once installed, list the available kernels and set `kernel-ml` as the default using `grubby`:

```bash
$ sudo grubby --info=ALL | grep -E "^kernel|^index"
index=0
kernel="/boot/vmlinuz-7.0.11-1.el10.elrepo.x86_64"
index=1
kernel="/boot/vmlinuz-6.12.0-211.16.1.el10_2.0.1.x86_64"
index=2
kernel="/boot/vmlinuz-0-rescue-f359b732002449e199fc129822382b6d"

$ sudo grubby --set-default /boot/vmlinuz-7.0.11-1.el10.elrepo.x86_64
The default is /boot/loader/entries/f359b732002449e199fc129822382b6d-7.0.11-1.el10.elrepo.x86_64.conf with index 0 and kernel /boot/vmlinuz-7.0.11-1.el10.elrepo.x86_64

$ sudo grubby --default-kernel
/boot/vmlinuz-7.0.11-1.el10.elrepo.x86_64
```

Then reboot for the new kernel to take effect:

```bash
sudo reboot
```

## Thermal power

With the kernel in place, the next step was to configure the thermal power limits for the EVO-X-2's AMD processor using [RyzenAdj](https://github.com/FlyGoat/RyzenAdj). The following command sets the burst power limit to 100W and the thermal target to 88°C:

```bash
$ sudo ryzenadj --fast-limit=100000 --tctl-temp=88
detected compatible ryzen_smu kernel module
Successfully set fast_limit to 100000
Successfully set tctl_temp to 88
```

### Building ryzen_smu

`ryzenadj` depends on the `ryzen_smu` kernel module. To build it, first install `git`:

```bash
sudo dnf install -y git
```

Then install the EPEL repository:

```bash
sudo dnf install -y epel-release
```

Then remove `kernel-ml-headers` to avoid a conflict with the stock `kernel-headers` package that will be pulled in as a dependency of `glibc-devel`:

```bash
sudo dnf remove kernel-ml-headers
```

Then install the required build dependencies:

```bash
sudo dnf --enablerepo=elrepo-kernel install cmake gcc gcc-c++ dkms openssl kernel-ml-devel
```

Clone the module source and install it via DKMS:

```bash
git clone https://github.com/amkillam/ryzen_smu
cd ryzen_smu/ && sudo make dkms-install
cd .. && rm -Rf ./ryzen_smu/
```

### Building RyzenAdj

With `ryzen_smu` in place, the next step is to build `ryzenadj`. First install the required dependency:

```bash
sudo dnf install pciutils-devel
```

Then clone, build, and symlink `ryzenadj`:

```bash
git clone https://github.com/FlyGoat/RyzenAdj.git
cd RyzenAdj
rm -r win32
mkdir build && cd build
cmake -DCMAKE_BUILD_TYPE=Release ..
make
if [ -d ~/.local/bin ]; then ln -s $(readlink -f ryzenadj) ~/.local/bin/ryzenadj && echo "symlinked to ~/.local/bin/ryzenadj"; fi
if [ -d ~/.bin ]; then ln -s $(readlink -f ryzenadj) ~/.bin/ryzenadj && echo "symlinked to ~/.bin/ryzenadj"; fi
sudo mv ./ryzenadj /usr/bin/
sudo restorecon -v /usr/bin/ryzenadj
```

Clean up the build directory:

```bash
cd ~ && rm -Rf ./RyzenAdj
```

### Persisting power limits at boot

The `ryzenadj` command sets limits for the current session only — they reset on reboot. To apply them automatically at every boot, create a systemd service unit:

```bash
sudo tee /etc/systemd/system/ryzenadj.service << 'EOF'
[Unit]
Description=Set RyzenAdj APU power limits
After=systemd-modules-load.service

[Service]
Type=oneshot
ExecStart=/usr/bin/ryzenadj --fast-limit=100000 --tctl-temp=88
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
EOF
```

Reload systemd and enable the service:

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now ryzenadj.service
```

Verify it ran successfully:

```bash
$ sudo systemctl status ryzenadj.service
● ryzenadj.service - Set RyzenAdj APU power limits
     Loaded: loaded (/etc/systemd/system/ryzenadj.service; enabled; preset: disabled)
     Active: active (exited) since ...
    Process: ... ExecStart=/usr/bin/ryzenadj --fast-limit=100000 --tctl-temp=88 (code=exited, status=0/SUCCESS)
```

Then reboot to confirm the limits come up automatically:

```bash
sudo reboot
```

## PyTorch Benchmarking Setup

With RyzenAdj in place and the APU power limits dialled in, the next step was to get a PyTorch benchmarking suite running to measure GPU throughput.

**Note:** `lm-sensors` does not detect any hardware monitoring chips on the EVO-X-2. Running `sensors-detect --auto` against the AMD RYZEN AI MAX+ 395 finds no supported sensors and reports "Sorry, no sensors were detected." Thermal monitoring via `lm-sensors` is not an option on this hardware.

### Installing PyTorch with Vulkan

Unlike ROCm, PyTorch's Vulkan backend on desktop Linux has no prebuilt pip wheel. The Vulkan backend exists in the codebase at [github.com/pytorch/pytorch](https://github.com/pytorch/pytorch) and is functional, but desktop Linux support is not tested in CI and there is no official package distribution for it — a source build is the only path.

Install the Vulkan runtime, headers, and Mesa RADV driver (which provides Vulkan support for the AMD integrated GPU):

```bash
sudo dnf install -y vulkan-loader vulkan-headers vulkan-tools mesa-vulkan-drivers
```

Verify the Vulkan ICD is detected:

```bash
$ vulkaninfo --summary
Instance Version:  1.3.x
GPU id : 0 (AMD Radeon Graphics)
        apiVersion = 1.3.x
        driverVersion = x.x.x
```

The PyTorch Vulkan build requires `glslc` (the GLSL shader compiler) from the [LunarG Vulkan SDK](https://vulkan.lunarg.com/sdk/home#linux). Download and extract it:

```bash
mkdir ~/VulkanSDK && cd ~/VulkanSDK
wget https://sdk.lunarg.com/sdk/download/latest/linux/vulkan_sdk.tar.gz
tar xf vulkan_sdk.tar.gz
```

Source the environment setup script before building — substitute `<version>` with the extracted directory name:

```bash
source ~/VulkanSDK/<version>/setup-env.sh
```

Install build dependencies:

```bash
sudo dnf install -y python3-pip python3-devel cmake git
```

`ninja-build` is not available in the Rocky Linux 10 or EPEL repositories. Install it via pip instead, which is what the PyTorch build system expects anyway:

```bash
python3 -m pip install ninja
```

Clone the PyTorch repository and initialise submodules:

```bash
git clone https://github.com/pytorch/pytorch
cd pytorch
git submodule sync
git submodule update --init --recursive
python3 -m pip install -r requirements.txt
```

Build PyTorch with `USE_VULKAN=1`. This will take a significant amount of time — expect upwards of an hour on this hardware:

```bash
USE_VULKAN=1 USE_CUDA=0 python3 -m pip install --no-build-isolation -v -e .
```

The `-e` flag installs in editable mode, meaning the installed package is a symlink back to the source directory. Once the build is confirmed working, reinstall without it to do a proper install that copies everything into site-packages:

```bash
cd ~/pytorch
USE_VULKAN=1 USE_CUDA=0 python3 -m pip install --no-build-isolation .
```

Then clean up the source and SDK directories:

```bash
cd ~ && rm -rf ~/pytorch ~/VulkanSDK
```

Verify that the Vulkan backend is available once the build completes:

```bash
$ python3 -c "import torch; print(torch.is_vulkan_available())"
True
```

### Running benchmarks safely

The Vulkan backend does not support `torch.compile` at all — Triton/Inductor is not part of the Vulkan codepath. That said, third-party benchmarking scripts may still attempt to call it, so it is worth disabling explicitly before running anything unfamiliar:

```bash
export TORCHDYNAMO_DISABLE=1
python3 benchmark.py
```

A safe baseline benchmark that measures GPU matrix multiply throughput without triggering the CPU+GPU burst. Note that the Vulkan backend has no explicit synchronise API — operations are completed lazily, and `.cpu()` is used here to force each iteration to completion before timing the next:

```python
import os
import time
import torch

os.environ["TORCHDYNAMO_DISABLE"] = "1"

def run_benchmark(size: int = 2048, iterations: int = 50, dtype=torch.float32):
    if torch.is_vulkan_available():
        device = "vulkan"
    else:
        print("Vulkan not available, falling back to CPU")
        device = "cpu"

    print(f"Device: {device}")
    print(f"Matrix size: {size}x{size}, dtype: {dtype}, iterations: {iterations}")

    a = torch.randn(size, size, dtype=dtype).to(device)
    b = torch.randn(size, size, dtype=dtype).to(device)

    def sync(t):
        # Pull result back to CPU to force Vulkan pipeline completion
        return t.cpu() if device == "vulkan" else t

    # Warm-up
    for _ in range(5):
        sync(torch.matmul(a, b))

    start = time.perf_counter()
    for _ in range(iterations):
        sync(torch.matmul(a, b))
    elapsed = time.perf_counter() - start

    tflops = (2 * size ** 3 * iterations) / elapsed / 1e12
    print(f"Elapsed: {elapsed:.2f}s — {tflops:.4f} TFLOPS")

if __name__ == "__main__":
    run_benchmark()
```

Save this as `~/benchmark.py` and run it:

```bash
$ python3 ~/benchmark.py
Device: vulkan
Matrix size: 2048x2048, dtype: torch.float32, iterations: 50
Elapsed: 0.70s — 1.2304 TFLOPS
```

Breaking down what this result means:

**TFLOPS** (Tera Floating Point Operations Per Second) is how many trillion floating point arithmetic operations the system completed each second.

**How the number is calculated:** a 2048×2048 matrix multiply costs approximately 2×2048³ floating point operations. The benchmark ran 50 of those in 0.70 seconds:

```
(2 × 2048³ × 50) / 0.70s / 1,000,000,000,000 = 1.2304 TFLOPS
```

**What it means in context:** the AMD Ryzen AI MAX+ 395's integrated GPU (Radeon 8060S, 40 RDNA3.5 compute units) has a theoretical FP32 peak of roughly 14–15 TFLOPS. The benchmark returns about 8% of that, which sounds low but is expected for two reasons:

1. **The `.cpu()` sync call is inside the timing loop.** Every iteration forces a GPU→CPU round-trip to synchronise results. That host-device latency is baked into the 0.70s elapsed figure — it is measuring GPU compute plus synchronisation overhead per iteration, not pure GPU throughput.

2. **The PyTorch Vulkan backend is experimental.** It has none of the hand-tuned BLAS kernels that ROCm uses. Every matmul goes through a general GLSL compute shader with no architecture-specific optimisation.

1.2304 TFLOPS is not a reflection of what the GPU can do — it is a reflection of what this benchmark methodology measures through this particular backend. What it does confirm is that Vulkan GPU compute is working, tensors are being placed on the GPU, and operations are completing correctly. With RyzenAdj configured at 100W fast limit and 88°C thermal target, the benchmark runs comfortably within the thermal envelope.

## llama.cpp with Vulkan

With the benchmarking setup confirmed, the next step is to install [llama.cpp](https://github.com/ggml-org/llama.cpp) with Vulkan support. Rather than building from source manually, [Nix](https://github.com/NixOS/nix) handles the build and all dependencies cleanly.

### Installing Nix

The standard Nix multi-user installation requires SELinux to be disabled, which conflicts with Rocky Linux's default enforcing configuration. The single-user installation avoids this:

```bash
curl --proto '=https' --tlsv1.2 -L https://nixos.org/nix/install | sh -s -- --no-daemon
```

Source the Nix environment into the current shell, or open a new terminal:

```bash
. ~/.nix-profile/etc/profile.d/nix.sh
```

Add the nixpkgs channel and update it:

```bash
nix-channel --add https://nixos.org/channels/nixpkgs-unstable nixpkgs
nix-channel --update
```

Verify the install:

```bash
$ nix --version
nix (Nix) 2.34.7
```

If the llama.cpp build later fails with a sandbox error, disable Nix sandboxing in the user config:

```bash
mkdir -p ~/.config/nix
echo 'sandbox = false' >> ~/.config/nix/nix.conf
```

### Installing llama.cpp with Vulkan

The `llama-cpp` package in nixpkgs has Vulkan support disabled by default. The expression passed to `nix-env -iE` must be a **function** — `nix-env` always calls it with the default pkgs set. Writing it as `let pkgs = import <nixpkgs> {}; in DERIVATION` produces a derivation directly, which `nix-env` then attempts to call as a function and fails. The correct form is a lambda:

```bash
nix-env -iE 'pkgs: pkgs.llama-cpp.override { vulkanSupport = true; }'
```

Verify the install:

```bash
$ llama-cli --version
```

## Running the API server

llama.cpp ships with `llama-server`, a standalone binary that exposes an OpenAI-compatible HTTP API. Starting it with `--host 0.0.0.0` makes the running model accessible over the network from any machine on the local network, rather than localhost only.

### Downloading a model

llama.cpp works with models in [GGUF format](https://github.com/ggml-org/ggml/blob/master/docs/gguf.md). A broad library is available on [Hugging Face](https://huggingface.co/models?library=gguf). The `huggingface-cli` tool, provided by the `huggingface_hub` package, is the most reliable way to download them:

```bash
python3 -m pip install huggingface_hub
```

Create a directory for models and download a model. [Qwen2.5-Coder-14B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-14B-Instruct-GGUF) in Q4\_K\_M quantisation is a practical choice for a coding assistant on this hardware — approximately 9 GB, fits entirely within the EVO-X-2's unified memory alongside the model weights, and performs well on tool-calling tasks:

```bash
mkdir -p ~/models
huggingface-cli download Qwen/Qwen2.5-Coder-14B-Instruct-GGUF \
  Qwen2.5-Coder-14B-Instruct-Q4_K_M.gguf \
  --local-dir ~/models/
```

### Starting llama-server

With the model in place, start the server. The `--n-gpu-layers 99` flag offloads all model layers to the Vulkan GPU — without it, inference runs on CPU only. The `--alias` sets the model identifier returned by the `/v1/models` endpoint, which the OpenCode client uses to reference the model:

```bash
llama-server \
  --model ~/models/Qwen2.5-Coder-14B-Instruct-Q4_K_M.gguf \
  --alias Qwen2.5-Coder-14B \
  --host 0.0.0.0 \
  --port 8080 \
  --n-gpu-layers 99 \
  --ctx-size 16384
```

Verify the server is healthy:

```bash
$ curl http://localhost:8080/health
{"status":"ok"}
```

Confirm the model is loaded and the alias is set correctly:

```bash
$ curl -s http://localhost:8080/v1/models | python3 -m json.tool
{
    "object": "list",
    "data": [
        {
            "id": "Qwen2.5-Coder-14B",
            ...
        }
    ]
}
```

### Opening the firewall

Rocky Linux uses `firewalld` by default. Open port 8080 to allow inbound connections from other machines on the network:

```bash
sudo firewall-cmd --permanent --add-port=8080/tcp
sudo firewall-cmd --reload
```

Verify the rule is active:

```bash
$ sudo firewall-cmd --list-ports
8080/tcp
```

### Persisting llama-server at boot

The Nix-installed binary lives in `~/.nix-profile/bin/` and runs most cleanly as a user-level systemd service. User services avoid the SELinux context issue that affects system services started from binaries in home directories — there is no need to move the binary or run `restorecon`.

Enable linger so the user service starts at boot without requiring an interactive login session:

```bash
loginctl enable-linger $USER
```

Create the user service directory and unit file. Substitute the correct username in the paths if different:

```bash
mkdir -p ~/.config/systemd/user

tee ~/.config/systemd/user/llama-server.service << 'EOF'
[Unit]
Description=llama.cpp API server
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
ExecStart=/home/howard/.nix-profile/bin/llama-server \
    --model /home/howard/models/Qwen2.5-Coder-14B-Instruct-Q4_K_M.gguf \
    --alias Qwen2.5-Coder-14B \
    --host 0.0.0.0 \
    --port 8080 \
    --n-gpu-layers 99 \
    --ctx-size 16384
Restart=on-failure
RestartSec=5

[Install]
WantedBy=default.target
EOF
```

Reload the user daemon and enable the service:

```bash
systemctl --user daemon-reload
systemctl --user enable --now llama-server.service
```

Verify it is running:

```bash
$ systemctl --user status llama-server.service
● llama-server.service - llama.cpp API server
     Loaded: loaded (/home/howard/.config/systemd/user/llama-server.service; enabled; preset: disabled)
     Active: active (running) since ...
```

Then reboot to confirm the service comes up automatically:

```bash
sudo reboot
```

## Accessing llama-server with OpenCode

The following steps are performed on the client machine — the Rocky Linux 10 laptop running OpenCode. The EVO-X-2's local network IP address is used throughout; substitute the actual address.

### Verifying remote connectivity

Before configuring OpenCode, confirm the server is reachable from the client:

```bash
$ curl http://192.168.1.100:8080/health
{"status":"ok"}
```

### Configuring OpenCode

OpenCode treats llama-server as a custom OpenAI-compatible provider. The global config lives at `~/.config/opencode/opencode.json`. Add the following, substituting the EVO-X-2's IP address. The model ID in the `models` map must match the `--alias` value used when starting llama-server, and the `context` limit must match `--ctx-size`:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "evo-x2": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "EVO-X2 (llama.cpp)",
      "options": {
        "baseURL": "http://192.168.1.100:8080/v1"
      },
      "models": {
        "Qwen2.5-Coder-14B": {
          "name": "Qwen2.5-Coder-14B (EVO-X2)",
          "limit": {
            "context": 16384,
            "output": 8192
          }
        }
      }
    }
  }
}
```

The provider ID (`evo-x2`) is arbitrary — it appears as the provider label in the model picker. Run `/models` within OpenCode to select the `Qwen2.5-Coder-14B (EVO-X2)` entry and switch to inferencing on the EVO-X-2.
