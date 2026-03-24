---
title: "✅ Step-by-step Working Solution"
category: "general-linux"
tags: ["downloading", "specific", "packages", "repo"]
---

To download all `.NET` packages from the **"Rocky Linux 9.2 CIQ Long Term Support (x86_64-debug)"** repository using `dnf`, follow these steps:

### ✅ Step-by-step Working Solution

1. **List all available packages in the target repo that match `dotnet`:**

   ```bash
   dnf --disablerepo="*" --enablerepo="ciq-debug" list available | grep dotnet
   ```

   > Replace `ciq-debug` with the actual repo ID of the "Rocky Linux 9.2 CIQ Long Term Support (x86_64-debug)" repo. You can find it using:
   >
   > ```bash
   > dnf repolist all
   > ```

2. **Download all matching packages (without installing):**

   ```bash
   sudo dnf --disablerepo="*" --enablerepo="ciq-debug" download $(dnf --disablerepo="*" --enablerepo="ciq-debug" list available | grep dotnet | awk '{print $1}')
   ```

   This command:
   - Lists all available packages in the repo.
   - Filters for those with `dotnet` in the name.
   - Extracts the package names.
   - Downloads them using `dnf download`.

---

### 🧪 Optional: Verify the Repo ID

If you're unsure of the exact repo ID, run:

```bash
dnf repolist all | grep -i ciq
```

Look for something like `ciq-debug` or similar.