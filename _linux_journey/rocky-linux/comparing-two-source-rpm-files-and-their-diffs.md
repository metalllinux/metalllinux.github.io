---
title: "1. Extract the Changelogs Directly from the SRPMs"
category: "rocky-linux"
tags: ["rocky-linux", "comparing", "two", "source", "rpm"]
---

From AI 
Below is one effective approach to diffing the commits (or, more precisely, the changelog entries and patches) in two OpenSSL source RPMs:

### 1\. Extract the Changelogs Directly from the SRPMs

Many SRPMs embed the commit history (or at least the packaging changelog) in the `%changelog` section of the spec file. You can quickly extract these using the RPM query option:

bash

```
rpm -qp --changelog openssl1.src.rpm > changelog1.txt
rpm -qp --changelog openssl2.src.rpm > changelog2.txt
```

Then compare them with a standard diff tool:

bash

```
diff -u changelog1.txt changelog2.txt
```

This will list all differences in the recorded changelog entries between the two packages. If those changelogs reflect the commits (or patches) you’re interested in, this can be a fast solution.

### 2\. Extract the Contents of Each SRPM

Sometimes you might want to see more than just the changelog differences—for example, how the patch files differ that were applied to the original source. To do that, unpack the SRPMs into separate directories using `rpm2cpio` with `cpio`:

bash

```
mkdir openssl1 && cd openssl1
rpm2cpio ../openssl1.src.rpm | cpio -idmv
cd ..

mkdir openssl2 && cd openssl2
rpm2cpio ../openssl2.src.rpm | cpio -idmv
cd ..
```

Once extracted, you’ll have the spec file, patch files, and the upstream source archives. You can then:

- **Diff the Spec Files:**
    
    bash
    
    ```
    diff -u openssl1/openssl.spec openssl2/openssl.spec
    ```
    
    The spec file’s `%changelog` section usually shows the commit-like entries (from the packager’s perspective).
    
- **Diff the Patch Files:** If the SRPMs include patches (often named `openssl-fix-XYZ.patch` or similar), you can compare each corresponding patch to see what was added, removed, or altered:
    
    bash
    
    ```
    diff -u openssl1/patches/patchfile.patch openssl2/patches/patchfile.patch
    ```
    

This method lets you examine more granular changes beyond just the changelog.

### 3\. Use an Advanced Diff Tool

For a comprehensive report, consider using . It’s a tool designed to deeply compare complex archive formats—including RPMs—by recursively unpacking and diffing them:

bash

```
diffoscope openssl1.src.rpm openssl2.src.rpm
```

This approach compares every aspect of the two SRPMs, revealing differences in embedded files, metadata, and changelogs. It’s especially useful if you’re unsure where the differences lie.

### Additional Considerations

- **Understanding “Commits” in an SRPM:** Remember that source RPMs are typically built from a snapshot of the upstream source code with additional packaging patches. The “commits” you see in the changelog often reflect packaging decisions rather than VCS commits from the upstream project (unless the upstream commit history is embedded separately).
    
- **Reconstructing a Git Repository (Optional):** If your goal is to work with an actual commit history (for instance, if the SRPM was built from a Git repository), you could:
    
    - Extract the patch series from the SRPM.
        
    - Create a new Git repository.
        
    - Apply the patches sequentially as commits.
        
    
    Once that’s done for both SRPMs, you could then use Git’s powerful diffing capabilities (such as `git log` or `git diff`) to compare the commit graphs. This approach requires additional scripting and is more involved but can be very insightful if you have the necessary context.