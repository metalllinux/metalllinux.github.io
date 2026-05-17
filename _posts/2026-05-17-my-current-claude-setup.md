---
title: "My Current Claude Setup"
date: 2026-05-17
categories: ai
tags: [ai, claude, emacs, workflow, plugins]
---

I have been using Claude daily for Linux troubleshooting and open-source work for a while now, so I wanted to document my current setup. Here is what I am running.

- **[Doom Emacs](https://github.com/doomemacs/doomemacs)** as my primary editor. Doom is a fast, opinionated Emacs configuration framework that gives you a modern editing experience out of the box.

- **[claudemacs](https://github.com/cpoile/claudemacs)** for integrating Claude Code directly into Emacs. This lets me interact with Claude without leaving my editor, keeping everything in one workflow.

- **[Claude Code](https://code.claude.com/docs/en/overview)** as the core CLI tool that powers my AI-assisted workflows. It handles everything from code generation to research to ticket analysis.

- **Skills** for specialised research and accuracy. I have custom skills for in-depth Linux and kernel research (`linux-research`, `kernel-research`) that pull from upstream sources, vendor documentation, and package repositories. I also have a `double-check-for-accuracy` skill that forces Claude to verify its own claims against primary sources before presenting them, catching errors before they reach customers.

- **[Sub-agents](https://code.claude.com/docs/en/sub-agents)** for programming and development. Sub-agents let Claude delegate specialised tasks to separate agent instances, each with their own tools and context. I use them for parallel code exploration, independent fact-checking, and product-specific analysis.

- **[Auto-mode](https://code.claude.com/docs/en/auto-mode-config)** to reduce the amount of prompting necessary. Auto-mode allows Claude to execute tool calls without requiring manual approval for each one, which dramatically speeds up multi-step workflows like sosreport analysis or kernel research.

- **Opus 4.6 as the executor model with Opus 4.7 as the [advisor](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool)**. I observed regressions in Opus 4.7 (long-context retrieval issues, tokeniser inconsistencies), so I run 4.6 as the primary model and use 4.7 exclusively as an independent reviewer. The advisor receives the full conversation transcript and challenges every claim before I commit to a response. This two-model setup provides higher accuracy than either model alone.

- **Plugins** for extended functionality:
  - [context-mode](https://github.com/mksglu/context-mode) processes large command outputs (logs, sosreports, kernel dumps) outside the main context window, so raw data does not consume valuable conversation space. Only a printed summary enters the context.
  - [claude-hud](https://github.com/jarrodwatts/claude-hud) provides a real-time status line showing model info, token usage, and session state directly in the terminal.

- **[Remote Control](https://code.claude.com/docs/en/remote-control)** to connect from my mobile device. This lets me monitor and interact with running Claude Code sessions remotely, so I can check on long-running tasks or provide input from my phone without needing to be at my desk.

- **[Goal Mode](https://code.claude.com/docs/en/goal)** to ensure Claude keeps working on a task until it is 100% complete. Goal mode prevents Claude from stopping prematurely or asking unnecessary clarifying questions mid-task. It stays focused on the objective until the work is fully done.

This setup has been refined over months of daily use on enterprise Linux support tickets. The combination of Emacs as the interface, Claude Code as the engine, and the advisor pattern for accuracy checking gives me a workflow where I can move fast without sacrificing correctness.
