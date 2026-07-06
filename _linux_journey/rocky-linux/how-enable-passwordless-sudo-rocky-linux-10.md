---
title: "How Enable Passwordless Sudo Rocky Linux 10"
category: "rocky-linux"
tags: ["rocky-linux", "sudo", "passwordless", "security", "rocky"]
---

To allow a user (e.g., `<username>`) to execute sudo commands without being prompted for a password:

1. Create a sudoers override file:
   ```bash
   echo "<username> ALL=(ALL) NOPASSWD: ALL" | sudo tee /etc/sudoers.d/<username>
   ```

2. Set the correct permissions:
   ```bash
   sudo chmod 0440 /etc/sudoers.d/<username>
   ```

3. Verify the configuration:
   ```bash
   sudo systemctl status
   ```
