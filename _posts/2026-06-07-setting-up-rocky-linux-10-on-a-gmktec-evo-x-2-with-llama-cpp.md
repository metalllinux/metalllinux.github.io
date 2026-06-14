---
title: "Setting up Rocky Linux 10 on a GMKtec EVO-X-2 with llama.cpp"
date: 2026-06-07
categories: ai
tags: [ai, llama.cpp, rocky-linux, local-ai, gmktec]
excerpt: "Setting up a local AI inference box using a GMKtec EVO-X-2 mini PC running Rocky Linux 10 and llama.cpp."
---

None of this would have been possible without the brilliant work of [Damen Knight](https://www.damenknight.com/running-frontier-coding-model-mini-pc/). I highly encourage any readers to go through his blog series first before continuing with this post.

I had been wanting to set up a dedicated local AI inference machine for a while, and I recently picked up a GMKtec EVO-X-2 mini PC for that purpose. The plan was to get Rocky Linux 10 installed on it and then build llama.cpp from source to run local models.

This post documents the process, starting with what turned out to be a more frustrating first step than expected.

## Installing Rocky Linux

For reference, the firmware on the machine at the time of installation was as follows:

| Field | Value |
|---|---|
| BIOS Version | EVO-X2 1.11 |
| EC Firmware Version | 1.08 |
| BIOS Build Date and Time | 10/17/2025 17:33:08 |

In the BIOS I also set **Power Mode Select** to **Performance Mode**.

Two additional BIOS changes were required before installing the OS.

Under **GFX Configuration**, I set **iGPU Configuration** to **[UMA_SPECIFIED]** and **UMA Frame buffer Size** to **[1G]**. The default carves out 64 GB as dedicated VRAM the OS cannot see or use for anything else. On a unified memory system the GPU accesses system RAM at the same bandwidth through GTT, which stands for Graphics Translation Table, so the carveout is wasted capacity.

Setting the frame buffer to 1 GB leaves the full remaining pool available for both system and GPU workloads, including model weights.

Note: BIOS 1.12 raised the minimum to 2 GB; BIOS 1.11 still allows 1 GB.

Under **CPU Configuration**, I set **IOMMU(AMD-Vi)** to **[Disabled]**. Disabling IOMMU at the hardware level produces a measurable improvement in inference throughput. Disabling it here makes the `amd_iommu=off` kernel parameter redundant, though including it is harmless.

The first task was simply getting Rocky Linux onto the machine. I downloaded the Rocky Linux 10.2 DVD ISO and set about creating a bootable USB stick using a Verbatim 64GB USB3 drive. What followed was a considerably longer exercise in troubleshooting than I anticipated.

The EVO-X-2 was simply unable to read the Verbatim 64GB USB3 memory stick. I verified the drive had been written correctly using multiple tools, but the machine would not recognise it as bootable in any case. These were some of the tools I used to create a bootable Rocky Linux 10.2 USB:

- **[`dd`](https://rockyman.org/10.2/coreutils-common/man1/dd.1.html)** - the standard go-to on Linux for writing ISOs directly to a block device. The write completed without errors and I verified the flash was successful, but the EVO-X-2 refused to boot from it.
- **[Fedora Media Writer](https://github.com/FedoraQt/MediaWriter)** - a reliable tool I had used successfully with multiple distributions' ISOs, not just Fedora. Again, the process completed cleanly and the flash was verified, but the machine would not recognise the stick as bootable.
- **[Rufus](https://rufus.ie/)** - attempted this from a Windows machine as a last resort. Same outcome.
- **[Ventoy](https://www.ventoy.net/)** - tried as a further option, but the EVO-X-2 was unable to find Ventoy either.

### PXE Boot

With USB boot ruled out entirely, I turned to PXE boot. I followed [this guide](https://metalinux.dev/linux-journey/rocky-linux/how-to-set-up-pxe-boot-on-rocky-linux-9-x/) to configure my Beelink machine, that was running Rocky Linux 9, into a PXE server, placing the Rocky Linux 10.2 ISO on it. Back on the EVO-X-2, I configured iPXE via the BIOS to boot via IPv4.

The machine booted successfully from the network. I selected the first option to launch an RDP server. I was observing severe screen flicker on my Dell 4K monitor via DisplayPort (this happens occasionally from my testing), so the RDP server option was the simplest way to install Rocky Linux 10.

On a separate machine I installed [Remmina](https://remmina.org/) and connected to the EVO-X-2 over RDP. This worked. I was presented with the Anaconda installer running in full graphical mode via Remmina, which allowed me to complete the installation properly - wiping Windows 11 from the primary NVMe drive and installing Rocky Linux 10 in its place. The installation completed successfully.

Installing Rocky Linux 10 on the GMKtec EVO-X-2 was decidedly non-trivial. Between the USB boot failures across four different tools and the display flickering issue that required a remote desktop workaround just to complete the installer, it took considerably more effort than a standard installation. That said, the machine is now up and running with Rocky Linux 10 and I couldn't be happier! I now have rock-solid stability for my AI workloads!

## The kernel install

With Rocky Linux 10 installed, the next step was to install a mainline kernel via [ELRepo's kernel-ml](https://elrepo.org/wiki/doku.php?id=kernel-ml). The `kernel-ml` package tracks the mainline stable kernel and is useful for getting up-to-date hardware support on Enterprise Linux distributions.

```bash
sudo dnf install -y elrepo-release
sudo rpm --import https://www.elrepo.org/RPM-GPG-KEY-elrepo.org
sudo dnf --enablerepo=elrepo-kernel install -y kernel-ml
```

Once installed, I listed the available kernels and set `kernel-ml` as the default using `grubby`:

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

I then rebooted for the new kernel to take effect:

```bash
sudo reboot
```

### Kernel parameters for unified memory and IOMMU

With the mainline kernel in place, I set additional kernel parameters to maximise the GTT memory pool and disable IOMMU. These had to be applied at boot via `grubby` - runtime changes have no effect:

```bash
sudo grubby --update-kernel=DEFAULT \
  --args="amd_iommu=off amdgpu.gttsize=90112 ttm.pages_limit=23068672 ttm.page_pool_size=23068672 amdgpu.no_system_mem_limit=1"
```

What each parameter does:

- **`amd_iommu=off`** - fully disables IOMMU. This produced an improvement in generation speed and GTT was also bumped from 112 GiB to 124 GiB in the same change.
- **`amdgpu.gttsize=90112`** - sets GTT to 88 GiB (90112 MiB), making that memory available for GPU workloads.
- **`ttm.pages_limit=23068672`** and **`ttm.page_pool_size=23068672`** - must match the GTT size. Without these, the TTM subsystem silently caps usable GPU memory to roughly half the configured GTT regardless of what the kernel reports - GPU compute only sees ~44 GiB even with 88 GiB configured.
- **`amdgpu.no_system_mem_limit=1`** - disables the SVM resident memory cap.

I verified the parameters were saved to the default kernel entry before rebooting:

```bash
$ sudo grubby --info=DEFAULT | grep args
args="ro ... amd_iommu=off amdgpu.gttsize=90112 ttm.pages_limit=23068672 ttm.page_pool_size=23068672 amdgpu.no_system_mem_limit=1"
```

I then rebooted for the parameters to take effect:

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

`ryzenadj` depends on the `ryzen_smu` kernel module. To build it, I first installed `git`:

```bash
sudo dnf install -y git
```

I then installed the EPEL repository:

```bash
sudo dnf install -y epel-release
```

I then removed `kernel-ml-headers` to avoid a conflict with the stock `kernel-headers` package that would be pulled in as a dependency of `glibc-devel`:

```bash
sudo dnf remove kernel-ml-headers
```

I then installed the required build dependencies:

```bash
sudo dnf --enablerepo=elrepo-kernel install cmake gcc gcc-c++ dkms openssl kernel-ml-devel
```

I cloned the module source and installed it via DKMS:

```bash
git clone https://github.com/amkillam/ryzen_smu
cd ryzen_smu/ && sudo make dkms-install
cd .. && rm -Rf ./ryzen_smu/
```

### Building RyzenAdj

With `ryzen_smu` in place, the next step was to build `ryzenadj`. I first installed the required dependency:

```bash
sudo dnf install pciutils-devel
```

I then cloned, built, and symlinked `ryzenadj`:

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

I cleaned up the build directory:

```bash
cd ~ && rm -Rf ./RyzenAdj
```

### Persisting power limits at boot

The `ryzenadj` command sets limits for the current session only and which reset upon a reboot. To apply them automatically at every boot, I created a systemd service unit:

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

I reloaded systemd and enabled the service:

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now ryzenadj.service
```

I verified it ran successfully:

```bash
$ sudo systemctl status ryzenadj.service
● ryzenadj.service - Set RyzenAdj APU power limits
     Loaded: loaded (/etc/systemd/system/ryzenadj.service; enabled; preset: disabled)
     Active: active (exited) since ...
    Process: ... ExecStart=/usr/bin/ryzenadj --fast-limit=100000 --tctl-temp=88 (code=exited, status=0/SUCCESS)
```

I then rebooted to confirm the limits came up automatically:

```bash
sudo reboot
```

After coming back up, I verified the service had started automatically:

```bash
$ sudo systemctl status ryzenadj.service
● ryzenadj.service - Set RyzenAdj APU power limits
     Loaded: loaded (/etc/systemd/system/ryzenadj.service; enabled; preset: disabled)
     Active: active (exited) since ...
```

I then confirmed the limits were in effect by running `ryzenadj --info` and checking the `fast_limit` and `tctl_temp` values in the output:

```bash
$ sudo ryzenadj --info
...
stapm_limit:           100.000 W
...
fast_limit:            100.000 W
...
tctl_temp:              88.000 °C
...
```

## PyTorch Benchmarking Setup

With RyzenAdj in place and the APU power limits dialled in, the next step was to get a PyTorch benchmarking suite running to measure GPU throughput.

Note: `lm-sensors` does not detect any hardware monitoring chips on the EVO-X-2. Running `sensors-detect --auto` as `root` or a user with `sudo` privileges against the AMD RYZEN AI MAX+ 395 finds no supported sensors and reports "Sorry, no sensors were detected." Thermal monitoring via `lm-sensors` is not an option from my testing on this hardware.

### Installing PyTorch with Vulkan

Unlike ROCm, PyTorch's Vulkan backend on Linux has no prebuilt pip wheel. The Vulkan backend exists in the codebase at [github.com/pytorch/pytorch](https://github.com/pytorch/pytorch) and is functional, but Linux support is not tested in CI and there is no official package distribution for it - a source build is the only path.

I installed the Vulkan runtime, headers, and Mesa RADV driver (which provides Vulkan support for the AMD integrated GPU):

```bash
sudo dnf install -y vulkan-loader vulkan-headers vulkan-tools mesa-vulkan-drivers
```

I verified the Vulkan ICD was detected:

```bash
$ vulkaninfo --summary
Instance Version:  1.3.x
GPU id : 0 (AMD Radeon Graphics)
        apiVersion = 1.3.x
        driverVersion = x.x.x
```

The PyTorch Vulkan build required `glslc` (the GLSL shader compiler) from the [LunarG Vulkan SDK](https://vulkan.lunarg.com/sdk/home#linux). I downloaded and extracted it:

```bash
mkdir ~/VulkanSDK && cd ~/VulkanSDK
wget https://sdk.lunarg.com/sdk/download/latest/linux/vulkan_sdk.tar.gz
tar xf vulkan_sdk.tar.gz
```

I sourced the environment setup script before building - substituting `<version>` with the extracted directory name:

```bash
source ~/VulkanSDK/<version>/setup-env.sh
```

I installed build dependencies:

```bash
sudo dnf install -y python3-pip python3-devel cmake git
```

`ninja-build` was not available in the Rocky Linux 10 or EPEL repositories. I installed it via pip instead, which is what the PyTorch build system expects anyway:

```bash
python3 -m pip install ninja
```

I cloned the PyTorch repository and initialised submodules:

```bash
git clone https://github.com/pytorch/pytorch
cd pytorch
git submodule sync
git submodule update --init --recursive
python3 -m pip install -r requirements.txt
```

I built PyTorch with `USE_VULKAN=1`. This took a significant amount of time - upwards of an hour on this hardware:

```bash
USE_VULKAN=1 USE_CUDA=0 python3 -m pip install --no-build-isolation -v -e .
```

The `-e` flag installs in editable mode, meaning the installed package is a symlink back to the source directory. Once the build was confirmed working, I reinstalled without it to do a proper install that copies everything into site-packages:

```bash
cd ~/pytorch
USE_VULKAN=1 USE_CUDA=0 python3 -m pip install --no-build-isolation .
```

I then cleaned up the source and SDK directories:

```bash
cd ~ && rm -rf ~/pytorch ~/VulkanSDK
```

I verified that the Vulkan backend was available once the build completed:

```bash
$ python3 -c "import torch; print(torch.is_vulkan_available())"
True
```

### Running benchmarks safely

The Vulkan backend does not support `torch.compile` at all - Triton/Inductor is not part of the Vulkan codepath. That said, third-party benchmarking scripts could still attempt to call it, so it was worth disabling explicitly before running anything unfamiliar:

```bash
export TORCHDYNAMO_DISABLE=1
python3 benchmark.py
```

A safe baseline benchmark measured GPU matrix multiply throughput without triggering the CPU+GPU burst. The Vulkan backend has no explicit synchronise API - operations are completed lazily, and `.cpu()` was used here to force each iteration to completion before timing the next:

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

I saved this as `~/benchmark.py` and ran it:

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

**What it means in context:** the AMD Ryzen AI MAX+ 395's integrated GPU (Radeon 8060S, 40 RDNA3.5 compute units) has a theoretical FP32 peak of roughly 14–15 TFLOPS. The benchmark returned about 8% of that, which sounds low but was expected for two reasons:

1. **The `.cpu()` sync call is inside the timing loop.** Every iteration forces a GPU→CPU round-trip to synchronise results. That host-device latency is baked into the 0.70s elapsed figure - it is measuring GPU compute plus synchronisation overhead per iteration, not pure GPU throughput.

2. **The PyTorch Vulkan backend is experimental.** It has none of the hand-tuned BLAS kernels that ROCm uses. Every matmul goes through a general GLSL compute shader with no architecture-specific optimisation.

1.2304 TFLOPS was not a reflection of what the GPU can do - it was a reflection of what this benchmark methodology measures through this particular backend. What it did confirm was that Vulkan GPU compute was working, tensors were being placed on the GPU, and operations were completing correctly. With RyzenAdj configured at 100W fast limit and 88°C thermal target, the benchmark ran comfortably within the thermal envelope.

## llama.cpp with Vulkan

With the benchmarking setup confirmed, the next step was to build [llama.cpp](https://github.com/ggml-org/llama.cpp) from source with Vulkan support. The Nix binary cache serves a pre-built llama-cpp binary without Vulkan enabled - `ldd` on the installed binary confirms no Vulkan libraries are linked, and `llama-server --list-devices` returns an empty list regardless of the `vulkanSupport` override. A source build was required.

### Build dependencies

The build tools from the ryzenadj steps were already in place. One additional system package was needed:

```bash
sudo dnf install -y vulkan-loader-devel
```

The llama.cpp Vulkan build also required `glslc` and `SPIRV-Headers`. Neither was available in Rocky Linux 10's BaseOS, AppStream, or EPEL repositories. I installed both permanently to `/usr/local` - `cmake --build` re-runs the configure step on each invocation, so these dependencies needed to be available system-wide, not from a temporary environment.

I installed `glslc` from the LunarG Vulkan SDK:

```bash
mkdir ~/VulkanSDK && cd ~/VulkanSDK
curl -LO https://sdk.lunarg.com/sdk/download/latest/linux/vulkan_sdk.tar.gz
tar xf vulkan_sdk.tar.gz
sudo install -m 755 $(find ~/VulkanSDK -name glslc -type f | head -1) /usr/local/bin/glslc
sudo restorecon -v /usr/local/bin/glslc
cd ~ && rm -rf ~/VulkanSDK
```

I installed `SPIRV-Headers` from source - it is header-only and installs in seconds:

```bash
git clone https://github.com/KhronosGroup/SPIRV-Headers.git
cd SPIRV-Headers
cmake -B build -DCMAKE_INSTALL_PREFIX=/usr/local
sudo cmake --install build
cd ~ && rm -rf SPIRV-Headers
```

I verified `glslc` was on the path:

```bash
$ glslc --version
shaderc v2026.2 v2026.2
```

### Building llama.cpp

I cloned the repository and configured the build. With `glslc` and `SPIRV-Headers` installed to `/usr/local`, no `CMAKE_PREFIX_PATH` override was needed:

```bash
cd ~
git clone https://github.com/ggml-org/llama.cpp
cd llama.cpp
cmake -B build \
  -DGGML_VULKAN=ON \
  -DGGML_NATIVE=OFF \
  -DCMAKE_C_FLAGS='-march=znver5' \
  -DCMAKE_CXX_FLAGS='-march=znver5' \
  -DGGML_AVX512=ON \
  -DGGML_AVX512_VBMI=ON \
  -DGGML_AVX512_VNNI=ON \
  -DGGML_AVX512_BF16=ON \
  -DGGML_LTO=ON \
  -DCMAKE_BUILD_TYPE=Release
```

Flag explanations:

- **`-DGGML_NATIVE=OFF` with `-march=znver5`** - disables GCC's auto-detection of CPU features and targets Zen 5 explicitly. Rocky Linux 10 ships GCC 14 which supports `znver5`. Using an explicit target is cleaner than auto-detection and avoids any edge cases with feature probing.
- **`-DGGML_AVX512=ON` / `VBMI` / `VNNI` / `BF16`** - enables AVX-512 SIMD extensions for CPU-side tensor operations (prompt processing, KV cache operations). The Ryzen AI MAX+ 395 supports all four. These flags apply regardless of GPU backend - Vulkan handles the GPU path; AVX-512 accelerates the CPU path.
- **`-DGGML_LTO=ON`** - enables link-time optimisation, allowing the linker to inline and optimise across translation unit boundaries.

The following flags from ROCm/HIP builds are **not applicable** with Vulkan and must be omitted: `-DGGML_HIP=ON`, `-DAMDGPU_TARGETS=gfx1151`, `-DGGML_HIP_ROCWMMA_FATTN=ON`, `-DGGML_CUDA_FA_ALL_QUANTS=ON`.

I built using all available CPU cores:

```bash
cmake --build build --config Release --parallel $(nproc)
```

I verified that Vulkan device detection was working before installing:

```bash
$ ./build/bin/llama-server --list-devices
Available devices:
  Vulkan0: Radeon 8060S Graphics (RADV GFX1151) (91136 MiB, 90974 MiB free)
```

The 91136 MiB figure (~89 GiB) confirmed the full unified memory pool was correctly exposed - the kernel GTT parameters and BIOS UMA configuration from earlier in this guide had worked as intended.

I installed the binaries and restored the SELinux context:

```bash
sudo cmake --install build --prefix /usr/local
sudo restorecon -Rv /usr/local/bin/
```

The cmake install placed shared libraries under `/usr/local/lib64/`, which is not in Rocky Linux's default ldconfig search paths. I added it and updated the cache:

```bash
echo "/usr/local/lib64" | sudo tee /etc/ld.so.conf.d/usrlocal.conf
sudo ldconfig
```

As my shell had previously resolved `llama-server` to a different path (from an earlier Nix install), I cleared the cached lookup:

```bash
hash -r
```

I cleaned up the build directory:

```bash
cd ~ && rm -rf llama.cpp
```

## Secondary NVMe storage

The EVO-X-2 has two M.2 slots. A second NVMe drive dedicated to model storage kept the OS drive uncluttered and gave model I/O its own bandwidth - relevant when a 14B Q4 model is 9 GB and larger models exceed 50 GB.

### Formatting the drive

The secondary drive appeared as `/dev/nvme1n1`. I verified it was visible before proceeding:

```bash
$ lsblk /dev/nvme1n1
```

XFS was the right choice for model storage for two reasons. First, it is the default filesystem on Rocky Linux - the kernel module, tooling, and `xfsprogs` are all first-class on this platform. Second, XFS was designed for high-throughput large file workloads, which is exactly what llama-server produces: sequential reads of multi-gigabyte files with no random access pattern. Its extent-based allocation avoids the fragmentation that accumulates with repeated large file writes and reads, and its allocation group architecture handles parallel metadata operations cleanly.

The drive had been previously used in another Linux system - `lsblk` showed existing LVM volumes beneath it (e.g. `rl-root`, `rl-swap`, `rl-home`). Rocky Linux had auto-activated these LVM volume groups at boot, which held the device open and caused `mkfs.xfs` to fail with `Device or resource busy`. I deactivated the old volume group first - substituting the actual VG name shown in the `lsblk` output:

```bash
sudo vgchange -an rl
```

I formatted the drive:

```bash
sudo mkfs.xfs -f /dev/nvme1n1
```

### Mounting the drive

I created the mount point:

```bash
sudo mkdir -p /mnt/data
```

I retrieved the filesystem UUID - fstab entries should reference UUID rather than the device path, since NVMe device names can change across reboots if drives are added or removed:

```bash
$ sudo blkid /dev/nvme1n1
/dev/nvme1n1: UUID="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx" BLOCK_SIZE="512" TYPE="xfs"
```

I added the entry to `/etc/fstab`, substituting the UUID from the `blkid` output:

```bash
sudo tee -a /etc/fstab << 'EOF'
UUID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx  /mnt/data  xfs  noatime,allocsize=64m,nofail  0 2
EOF
```

The mount options chosen:

- **`noatime`** - disables updating the file access timestamp on reads. Without it, every model load generates a metadata write to the NVMe alongside the actual read. On a drive used almost exclusively for large sequential reads this is pure overhead - write amplification with no benefit.
- **`allocsize=64m`** - sets the speculative preallocation size for new file extents to 64 MB. When writing large files such as multi-gigabyte GGUF downloads, XFS preallocates disk space in larger contiguous chunks, reducing fragmentation and the number of extent tree updates committed during the write. The result is a less fragmented file that reads back faster.
- **`nofail`** - the system boots normally if the drive is absent or fails to mount. Without this, a missing secondary drive drops Rocky Linux into emergency mode on boot.

I verified the fstab entry mounted correctly:

```bash
sudo mount -a
$ df -h /mnt/data
Filesystem      Size  Used Avail Use% Mounted on
/dev/nvme1n1    1.9T   18G  1.9T   1% /mnt/data
```

### Setting up the models directory

I gave the current user ownership of the mount so models could be downloaded without `sudo`:

```bash
sudo chown $USER:$USER /mnt/data
mkdir -p /mnt/data/models
```

## Running the API server

llama.cpp ships with `llama-server`, a standalone binary that exposes an OpenAI-compatible HTTP API. Starting it with `--host 0.0.0.0` made the running model accessible over the network from any machine on the local network, rather than localhost only.

### Downloading a model

llama.cpp works with models in [GGUF format](https://github.com/ggml-org/ggml/blob/master/docs/gguf.md). A broad library is available on [Hugging Face](https://huggingface.co/models?library=gguf). The `hf` CLI tool, provided by the `huggingface_hub` package, is the most reliable way to download them. I installed the latest version:

```bash
python3 -m pip install -U huggingface_hub
```

pip reported a dependency conflict warning after installation - this was a false alarm. `huggingface_hub` upgrades `click`; `spin` is a NumPy build tool with no relevance here. The `Successfully installed` line at the end confirmed `hf` was ready to use.

Note: `huggingface-cli` was deprecated in `huggingface_hub` 1.19.0 and replaced with `hf`. If you see a warning saying `huggingface-cli` is no longer supported, upgrade the package as above and use `hf` in its place.

I logged in to my Hugging Face account before downloading, to avoid the stricter anonymous rate limits that HuggingFace applies to large downloads - worthwhile given this model is approximately 46 GiB:

```bash
hf auth login
```

I downloaded the model to the NVMe drive. [Qwen3-Coder-Next](https://huggingface.co/unsloth/Qwen3-Coder-Next-GGUF) in Q4\_K\_M quantisation is the model this guide targets - an 80B parameter Mixture-of-Experts model built for coding agents. The MoE architecture means only around 3B parameters are active per token rather than the full 80B, which is what makes the hardware viable: the GPU streams only the active expert weights each token, not the entire model. The Q4\_K\_M quantisation is a single 48.5 GiB file, well within the EVO-X-2's 96 GB pool and leaving headroom for a 65K context window. [Unsloth](https://huggingface.co/unsloth) also provide a `UD-Q4_K_M` variant (49.3 GiB) using their Dynamic 2.0 quantisation, which they benchmark as higher accuracy at the same bit-width - either will work on this hardware:

```bash
hf download unsloth/Qwen3-Coder-Next-GGUF \
  Qwen3-Coder-Next-Q4_K_M.gguf \
  --local-dir /mnt/data/models/Qwen3-Coder-Next/
```

### Starting llama-server

With the model in place, I started the server. The `--n-gpu-layers 99` flag offloads all model layers to the Vulkan GPU - without it, inference runs on CPU only. The `--alias` sets the model identifier returned by the `/v1/models` endpoint, which the OpenCode client uses to reference the model:

```bash
llama-server \
  --model /mnt/data/models/Qwen3-Coder-Next/Qwen3-Coder-Next-Q4_K_M.gguf \
  --alias Qwen3-Coder-Next \
  --host 0.0.0.0 \
  --port 8080 \
  --n-gpu-layers 99 \
  -fa on \
  --parallel 1 \
  -t 32 -tb 32 \
  -ub 2048 \
  -ctk q8_0 -ctv q8_0 \
  --mlock \
  -c 65536
```

Flag explanations:

- **`-fa on`** - enables flash attention, reducing KV cache memory and speeding up attention computation.
- **`--parallel 1`** - single request slot; all available memory is dedicated to one user rather than split across parallel slots.
- **`-t 32 -tb 32`** - uses all 32 CPU cores for both inference and batch processing.
- **`-ub 2048`** - sets the micro-batch size to 2048, improving GPU utilisation during prompt processing.
- **`-ctk q8_0 -ctv q8_0`** - quantises the KV cache to Q8_0, approximately halving its memory footprint compared to f16 with minimal quality loss.
- **`--mlock`** - pins the model weights in RAM, preventing the OS from paging them out.
- **`-c 65536`** - 65K token context window.

I verified the server was healthy:

```bash
$ curl http://localhost:8080/health
{"status":"ok"}
```

I confirmed the model was loaded and the alias was set correctly:

```bash
$ curl -s http://localhost:8080/v1/models | python3 -m json.tool
```

```json
{
    "models": [
        {
            "name": "Qwen3-Coder-Next",
            "model": "Qwen3-Coder-Next",
            "modified_at": "",
            "size": "",
            "digest": "",
            "type": "model",
            "description": "",
            "tags": [
                ""
            ],
            "capabilities": [
                "completion"
            ],
            "parameters": "",
            "details": {
                "parent_model": "",
                "format": "gguf",
                "family": "",
                "families": [
                    ""
                ],
                "parameter_size": "",
                "quantization_level": ""
            }
        }
    ],
    "object": "list",
    "data": [
        {
            "id": "Qwen3-Coder-Next",
            "aliases": [
                "Qwen3-Coder-Next"
            ],
            "tags": [],
            "object": "model",
            "created": 1781247411,
            "owned_by": "llamacpp",
            "meta": {
                "vocab_type": 2,
                "n_vocab": 151936,
                "n_ctx": 65536,
                "n_ctx_train": 262144,
                "n_embd": 2048,
                "n_params": 79674391296,
                "size": 48522331136
            }
        }
    ]
}
```

### Opening the firewall

Rocky Linux uses `firewalld` by default. I opened port 8080 to allow inbound connections from other machines on the network:

```bash
sudo firewall-cmd --permanent --add-port=8080/tcp
sudo firewall-cmd --reload
```

I verified the rule was active:

```bash
$ sudo firewall-cmd --list-ports
8080/tcp
```

### Persisting llama-server at boot

The `llama-server` binary installed to `/usr/local/bin/` ran most cleanly as a user-level systemd service. User services avoided the SELinux context issue that affects system services started from binaries in home directories - there was no need to move the binary or run `restorecon`.

I enabled linger so the user service would start at boot without requiring an interactive login session:

```bash
loginctl enable-linger $USER
```

I created the user service directory and unit file:

```bash
mkdir -p ~/.config/systemd/user

tee ~/.config/systemd/user/llama-server.service << 'EOF'
[Unit]
Description=llama.cpp API server
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
LimitMEMLOCK=infinity
ExecStart=/usr/local/bin/llama-server \
    --model /mnt/data/models/Qwen3-Coder-Next/Qwen3-Coder-Next-Q4_K_M.gguf \
    --alias Qwen3-Coder-Next \
    --host 0.0.0.0 \
    --port 8080 \
    --n-gpu-layers 99 \
    -fa on \
    --parallel 1 \
    -t 32 -tb 32 \
    -ub 2048 \
    -ctk q8_0 -ctv q8_0 \
    --mlock \
    -c 65536
Restart=on-failure
RestartSec=5

[Install]
WantedBy=default.target
EOF
```

I reloaded the user daemon and enabled the service:

```bash
systemctl --user daemon-reload
systemctl --user enable --now llama-server.service
```

I verified it was running:

```bash
$ systemctl --user status llama-server.service
● llama-server.service - llama.cpp API server
     Loaded: loaded (/home/howard/.config/systemd/user/llama-server.service; enabled; preset: disabled)
     Active: active (running) since ...
```

Two warnings appeared in the journal output - neither was fatal, but one required attention:

- **`failed to mlock ... Try increasing RLIMIT_MEMLOCK`** - the `--mlock` flag could not pin the model in RAM because the memlock limit was too low. `LimitMEMLOCK=infinity` in the user service unit alone was not sufficient: the user systemd manager (`systemd --user`) inherits its own memlock ceiling from the system, and a user service cannot exceed what its manager was given. The fix was a system-level override that raised the limit for the entire user@1000 manager, which then applied to all services it spawned. I found my UID first:

  ```bash
  $ id -u
  1000
  ```

  I created the override, substituting the UID if different from 1000:

  ```bash
  sudo mkdir -p /etc/systemd/system/user@1000.service.d/
  sudo tee /etc/systemd/system/user@1000.service.d/limits.conf << 'EOF'
  [Service]
  LimitMEMLOCK=infinity
  EOF
  sudo systemctl daemon-reload
  ```

  A reboot was required. Reloading the system daemon updates the config on disk but does not restart the running `user@1000.service` process - it had been started before the override existed and still held the old limits. All child processes, including llama-server, inherited those old limits until the user manager itself restarted at next boot:

  ```bash
  sudo reboot
  ```

  After coming back up, I confirmed the limit had been applied to the user manager before starting the service:

  ```bash
  $ systemctl show user@1000.service | grep LimitMEMLOCK
  LimitMEMLOCK=infinity
  ```

- **`control-looking token: 128247 '</s>' was not control-type`** - a tokenizer metadata quirk in Qwen3-Coder-Next where the EOS token is not classified as control-type despite its appearance. llama.cpp flags it as a warning but it has no effect on inference quality or output. No action needed.

I then rebooted to confirm the service came up automatically:

```bash
sudo reboot
```

## Accessing llama-server with OpenCode

The following steps were performed on the client machine - the Rocky Linux 10 laptop running OpenCode. The EVO-X-2's local network IP address was used throughout; substitute the actual address.

### Verifying remote connectivity

Before configuring OpenCode, I confirmed the server was reachable from the client:

```bash
$ curl http://<YOUR_SERVER_IP>:8080/health
{"status":"ok"}
```

### Configuring OpenCode

OpenCode treats llama-server as a custom OpenAI-compatible provider. The global config lives at `~/.config/opencode/opencode.json`. I added the following, substituting the EVO-X-2's IP address. The model ID in the `models` map must match the `--alias` value used when starting llama-server, and the `context` limit must match `--ctx-size`:

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
          "name": "Qwen3-Coder-Next (EVO-X2)",
          "limit": {
            "context": 65536,
            "output": 32768
          }
        }
      }
    }
  }
}
```

The provider ID (`evo-x2`) is arbitrary - it appears as the provider label in the model picker. I ran `/models` within OpenCode to select the `Qwen3-Coder-Next (EVO-X2)` entry and switch to inferencing on the EVO-X-2.

## Monitoring GPU usage

### amdgpu_top

`amdgpu_top` provides a detailed TUI showing compute utilisation, memory bandwidth, power consumption, and per-process GPU activity. It was not available in EPEL or the Rocky Linux AppStream and BaseOS repositories. I installed the RPM directly from the [GitHub releases page](https://github.com/Umio-Yasuno/amdgpu_top/releases):

```bash
sudo dnf install -y https://github.com/Umio-Yasuno/amdgpu_top/releases/download/v0.11.5/amdgpu_top-0.11.5-1.x86_64.rpm
```

I then ran:

```bash
amdgpu_top
```

### Confirming GPU layer offload

Rocky Linux 10 does not enable the persistent journal by default. Without it, `journalctl --user` reports `No journal files were found`. I enabled it first:

```bash
sudo mkdir -p /var/log/journal
sudo systemd-tmpfiles --create --prefix /var/log/journal
sudo systemctl restart systemd-journald
```

I then logged out and back in - the user journal socket is only created for new login sessions after journald restarts.

When llama-server started, I confirmed that GPU offloading was active by tailing the service log:

```bash
$ journalctl --user -u llama-server.service -f
```

I looked for the following line during startup:

```
llm_load_tensors: offloaded 95/95 layers to GPU
```

If the count shows 0 layers offloaded, `--n-gpu-layers 99` is not taking effect via Vulkan.

### Temperature

As noted earlier, `lm-sensors` does not detect any hardware monitoring chips on the EVO-X-2. Two alternatives work on this hardware.

`ryzenadj` was already installed from earlier in this guide. Its `--info` flag prints live thermal data including the tctl temperature:

```bash
$ sudo ryzenadj --info
```

I could alternatively read directly from the hwmon sysfs interface:

```bash
watch -n 1 'paste /sys/class/hwmon/hwmon*/name /sys/class/hwmon/hwmon*/temp1_input'
```

Running this during inference produced output similar to the following:

```
acpitz  r8169_0_c100:00 amdgpu  k10temp 75000   64000   54000   79250
```

The format is all sensor names followed by all temperatures in millidegrees Celsius - divide by 1000 for °C. The four sensors present on the EVO-X-2 are:

| Sensor | Example (millideg) | °C | Description |
|---|---|---|---|
| `acpitz` | 75000 | 75.0 | ACPI thermal zone |
| `r8169_0_c100:00` | 64000 | 64.0 | Realtek NIC |
| `amdgpu` | 54000 | 54.0 | GPU die temperature |
| `k10temp` | 79250 | 79.25 | AMD CPU Tctl - the value ryzenadj limits to 88°C |
