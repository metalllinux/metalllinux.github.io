---
title: "Why Does Openqa Remove An Iso After A Period Of Ti"
category: "general-linux"
tags: ["openqa", "remove", "iso", "after", "period"]
---

The ISO files in that directory are managed as temporary test media by openQA. In openQA’s design, especially in the “factory” context for openSUSE Tumbleweed, ISO images are meant to be ephemeral. The system periodically cleans up files that aren’t tied to active or scheduled test jobs. This automatic removal helps prevent stale or outdated images from cluttering the system and ensures that only up-to-date installation media are used during tests.

To elaborate, openQA is geared toward continuous testing environments where new builds and installation media constantly replace older ones. A built-in housekeeping process checks the ISO directory and purges files that exceed a set retention period. This behaviour isn’t an error—it’s intentional so that disk space isn’t needlessly occupied and tests aren’t inadvertently run against obsolete images.

If you need an ISO to persist beyond this cleanup window (for archival or other purposes), consider storing it outside of the managed directory or adjusting openQA’s configuration (for example, modifying settings in the openQA configuration files, such as openqa.ini, if that’s an option in your deployment).