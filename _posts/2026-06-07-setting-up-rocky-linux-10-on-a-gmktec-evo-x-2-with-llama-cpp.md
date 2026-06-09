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
```

Clean up the build directory:

```bash
cd ~ && rm -Rf ./RyzenAdj
```

Then reboot:

```bash
sudo reboot
```

## PyTorch Benchmarking Setup

With RyzenAdj in place and the APU power limits dialled in, the next step was to get a PyTorch benchmarking suite running to measure GPU throughput. What followed was a series of full hard power-off events that required some investigation to understand.

### The hard shutdown problem

The system started dying during benchmark runs — not locking up, not crashing to a kernel panic, but fully powering off with no warning and nothing in the logs. It happened repeatedly: kick off a benchmark, machine cuts out.

Setting up thermal monitoring at five-second intervals showed exactly what was happening:

```
19:00:07  Tctl=71°C   pwr=92W    ← normal inference
19:00:12  Tctl=91°C   pwr=165W   ← torch.compile spike
19:00:22  Tctl=93°C   pwr=164W   ← approaching TjMax (100°C)
19:00:27  Tctl=61°C   pwr=30W    ← thermal shutdown
```

`torch.compile` triggers Triton/Inductor kernel compilation, which simultaneously pegs all 32 CPU cores and the GPU. On a UMA APU where the CPU and GPU share one thermal envelope inside a mini PC chassis, that produces a 165W power spike — well past the 120W PPT Fast limit and far beyond what the cooler can handle. The firmware thermal protection cuts power entirely. No graceful shutdown, just off.

Normal LLM inference is completely stable: 73–75W, 76–80°C, runs all day. The problem is specifically mixed CPU+GPU burst workloads. `torch.compile` is the most consistent trigger, but anything that simultaneously saturates the CPU and GPU can cause the same outcome on this hardware.

### Setting up thermal monitoring

Before running any benchmarks, set up continuous thermal monitoring. Install `lm-sensors`:

```bash
sudo dnf install -y lm_sensors
sudo sensors-detect --auto
```

Then create a monitoring script that logs temperature and package power at five-second intervals:

```bash
cat > ~/thermal-monitor.sh << 'EOF'
#!/usr/bin/env bash
LOG="${1:-thermal.log}"
echo "Logging to $LOG — Ctrl+C to stop"
while true; do
    TCTL=$(sensors 2>/dev/null | awk '/^Tctl:/ {gsub(/[+°C]/,"",$2); print $2}')
    PWR_RAW=$(cat /sys/class/hwmon/hwmon*/power1_average 2>/dev/null | sort -n | tail -1)
    if [ -n "$PWR_RAW" ]; then
        PWR_W=$(awk "BEGIN {printf \"%.0f\", $PWR_RAW / 1000000}")W
    else
        PWR_W=N/A
    fi
    printf '%s  Tctl=%-6s pwr=%s\n' "$(date '+%H:%M:%S')" "${TCTL}°C" "$PWR_W" | tee -a "$LOG"
    sleep 5
done
EOF
chmod +x ~/thermal-monitor.sh
```

Run it in a separate terminal before starting any benchmark:

```bash
~/thermal-monitor.sh benchmark-run-1.log
```

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
sudo dnf install -y python3-pip python3-devel cmake ninja-build git
```

Clone the PyTorch repository and initialise submodules:

```bash
git clone https://github.com/pytorch/pytorch
cd pytorch
git submodule sync
git submodule update --init --recursive
pip3 install -r requirements.txt
```

Build PyTorch with `USE_VULKAN=1`. This will take a significant amount of time — expect upwards of an hour on this hardware:

```bash
USE_VULKAN=1 USE_CUDA=0 pip3 install --no-build-isolation -v -e .
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

    a = torch.randn(size, size, dtype=dtype)
    b = torch.randn(size, size, dtype=dtype)

    if device == "vulkan":
        a = a.vulkan()
        b = b.vulkan()

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

Save this as `~/benchmark.py` and run it with the thermal monitor active in a separate terminal:

```bash
$ python3 ~/benchmark.py
Device: vulkan
Matrix size: 2048x2048, dtype: torch.float32, iterations: 50
Elapsed: ...
```

Note that the TFLOPS figure here includes the overhead of the `.cpu()` synchronisation call on each iteration — on a UMA APU where CPU and GPU share the same physical memory the transfer cost is minimal, but it is worth bearing in mind when comparing figures against other backends. With RyzenAdj configured at 100W fast limit and 88°C thermal target, the benchmark runs comfortably within the thermal envelope. Any reading consistently approaching 90°C is worth stopping to investigate.
