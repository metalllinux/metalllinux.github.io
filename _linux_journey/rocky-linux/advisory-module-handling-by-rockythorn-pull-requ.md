---
title: "Navigation Menu"
category: "rocky-linux"
tags: ["rocky-linux", "advisory", "module", "handling", "rockythorn"]
---

[Skip to content](#start-of-content)

## Navigation Menu

[](https://github.com/)

- [resf](https://github.com/resf) /
    
- [distro-tools](https://github.com/resf/distro-tools)

<a id="copilot-chat-header-button"></a>[](https://github.com/copilot)

<a id="icon-button-47ceb287-3586-4901-802d-0de17768f5c1"></a>[](https://github.com/issues)<a id="icon-button-5d9631c6-c016-4e03-9f24-b8d0763a5eec"></a>[](https://github.com/pulls)

<a id="AppHeader-notifications-button"></a>[](https://github.com/notifications)

- <a id="code-tab"></a>[Code](https://github.com/resf/distro-tools)
- <a id="issues-tab"></a>[Issues <a id="issues-repo-tab-count"></a>4](https://github.com/resf/distro-tools/issues)
- <a id="pull-requests-tab"></a>[Pull requests <a id="pull-requests-repo-tab-count"></a>1](https://github.com/resf/distro-tools/pulls)
- <a id="actions-tab"></a>[Actions](https://github.com/resf/distro-tools/actions)
- <a id="projects-tab"></a>[Projects](https://github.com/resf/distro-tools/projects)
- <a id="security-tab"></a>[Security](https://github.com/resf/distro-tools/security)
- <a id="insights-tab"></a>[Insights](https://github.com/resf/distro-tools/pulse)

Code

# Advisory module handling #39

Merged

[nazunalika](https://github.com/nazunalika) merged 4 commits into [resf:main](https://github.com/resf/distro-tools/tree/main "resf/distro-tools:main")

 from [rockythorn:advisory-module-handling](https://github.com/rockythorn/distro-tools/tree/advisory-module-handling "rockythorn/distro-tools:advisory-module-handling")

Apr 9, 2025

<a id="diffstat"></a>+68 −44

[Conversation <a id="conversation_tab_counter"></a>1](https://github.com/resf/distro-tools/pull/39) [Commits <a id="commits_tab_counter"></a>4](https://github.com/resf/distro-tools/pull/39/commits) [Checks <a id="checks_tab_counter"></a>0](https://github.com/resf/distro-tools/pull/39/checks) [Files changed <a id="files_tab_counter"></a>2](https://github.com/resf/distro-tools/pull/39/files)

## Conversation

<img width="40" height="40" src="../_resources/191179323_s_60_v_4_6e9e76ab5edd4cc1bbd09954cfa3d7b.jpg"/>](https://github.com/rockythorn)

Contributor

### 

**[rockythorn](https://github.com/rockythorn)** commented <a id="issue-2973415637-permalink"></a>[Apr 5, 2025](#issue-2973415637)

# Changes

The level changes introduced in this PR are to properly add all matching module streams to the cloned Rocky advisories. Previously the "cleaned" versions of package nvrs would remove the module stream information which led to the cloned advisories not containing all appropriate module streams.

### `repomd.py`

- Return both the "cleaned" and "raw" versions of a package name from the `clean_nvra_pkg1 and` clean_vra\` functions.

### `rh_matcher_activities.py`

- `clone_advisory()`: Add some code comments
- `process_repomd()`:
    - add the raw package versions to the `raw_package_map` dictionary with the key being the "cleaned" nvr and the value being a list of all matching "raw" nvrs.
    - Use the "raw" package name as the value for the `nvra_alias` dictionary.

# Testing

In my local setup for Apollo I compared the advisories generated with main and the advisories generated with these changes in place. There were no Rocky advisories removed and advisories with modules generally saw an increase in the number of linked packages. Having spot checked a number of them I saw that we now included multiple module streams which led to the increased number of associated packages.

```
(.venv) [mrthorn@rocky-mobile distro-tools]$ python3 -m pytest apollo/tests --ignore node_modules --ignore .venv --ignore-glob "bazel-*" -v
/home/mrthorn/resf/distro-tools/.venv/lib64/python3.9/site-packages/pytest_asyncio/plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
======================================================= test session starts ========================================================
platform linux -- Python 3.9.21, pytest-8.3.5, pluggy-1.5.0 -- /home/mrthorn/resf/distro-tools/.venv/bin/python3
cachedir: .pytest_cache
rootdir: /home/mrthorn/resf/distro-tools
plugins: mock-3.14.0, asyncio-0.26.0
asyncio: mode=strict, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 11 items

apollo/tests/publishing_tools/test_apollo_tree.py::test_scan_path_valid_structure PASSED                                     [  9%]
apollo/tests/publishing_tools/test_apollo_tree.py::test_scan_path_multiple_formats PASSED                                    [ 18%]
apollo/tests/publishing_tools/test_apollo_tree.py::test_scan_path_valid_structure_arch_first PASSED                          [ 27%]
apollo/tests/publishing_tools/test_apollo_tree.py::test_fetch_updateinfo_from_apollo_live SKIPPED (Skipping test_fetch_u...) [ 36%]
apollo/tests/publishing_tools/test_apollo_tree.py::test_fetch_updateinfo_from_apollo_live_no_updateinfo SKIPPED (Skippin...) [ 45%]
apollo/tests/publishing_tools/test_apollo_tree.py::test_fetch_updateinfo_from_apollo_mock PASSED                             [ 54%]
apollo/tests/publishing_tools/test_apollo_tree.py::test_gzip_updateinfo PASSED                                               [ 63%]
apollo/tests/publishing_tools/test_apollo_tree.py::test_write_updateinfo_to_file PASSED                                      [ 72%]
apollo/tests/publishing_tools/test_apollo_tree.py::test_update_repomd_xml PASSED                                             [ 81%]
apollo/tests/publishing_tools/test_apollo_tree.py::test_run_apollo_tree PASSED                                               [ 90%]
apollo/tests/publishing_tools/test_apollo_tree.py::test_run_apollo_tree_arch_in_product PASSED                               [100%]

=================================================== 9 passed, 2 skipped in 0.08s ===================================================
```

Sam Thornton added 4 commits [April 1, 2025 16:15](#commits-pushed-6e842d3)

`[Fix: include module all module stream builds for advisories](https://github.com/resf/distro-tools/pull/39/commits/6e842d38045972f4c5a15c4998ecdbb58ceb3719 "Fix: include module all module stream builds for advisories")`

`[6e842d3](https://github.com/resf/distro-tools/pull/39/commits/6e842d38045972f4c5a15c4998ecdbb58ceb3719)`

`[update to dist compare logic](https://github.com/resf/distro-tools/pull/39/commits/3be0a9758fdd9f274901d9ed66cd177aea760222 "update to dist compare logic")`

`[3be0a97](https://github.com/resf/distro-tools/pull/39/commits/3be0a9758fdd9f274901d9ed66cd177aea760222)`

`[remove dist comparison](https://github.com/resf/distro-tools/pull/39/commits/1f5bce942134fdea69de4de8518f914db998ba49 "remove dist comparison")`

`[1f5bce9](https://github.com/resf/distro-tools/pull/39/commits/1f5bce942134fdea69de4de8518f914db998ba49)`

`[Cleaning up prior to PR](https://github.com/resf/distro-tools/pull/39/commits/980d686f27ea14fa81be38f53a62b65e6c414181 "Cleaning up prior to PR")`

`[980d686](https://github.com/resf/distro-tools/pull/39/commits/980d686f27ea14fa81be38f53a62b65e6c414181)`

<img width="40" height="40" src="../_resources/191179323_s_80_u_0e167a8c49f3180_5a1f5733971a4b1c8.jpg"/>](https://github.com/rockythorn)

Contributor Author

### 

**[rockythorn](https://github.com/rockythorn)** commented <a id="issuecomment-2779859691-permalink"></a>[Apr 5, 2025](#issuecomment-2779859691)

<div class="joplin-table-wrapper"><table class="d-block user-select-contain" data-paste-markdown-skip=""><tbody class="d-block"><tr class="d-block"><td class="d-block comment-body markdown-body  js-comment-body"><p dir="auto">The advisory that triggered this fix is: <a href="https://errata.build.resf.org/RLSA-2024:10219" rel="nofollow">https://errata.build.resf.org/RLSA-2024:10219</a></p><p dir="auto">The live advisory only contains reference to a single module stream:</p><div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate" style="font-family: ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace;"><code class="notranslate">perl-App-cpanminus-0:1.7044-6.module+el8.10.0+1886+1635aa55.src.rpm
perl-CPAN-DistnameInfo-0:0.12-13.module+el8.10.0+1616+0d20cc68.src.rpm
perl-CPAN-Meta-Check-0:0.014-6.module+el8.10.0+1890+1072d5cf.src.rpm
perl-File-pushd-0:1.014-6.module+el8.10.0+1890+1072d5cf.src.rpm
perl-Module-CPANfile-0:1.1002-7.module+el8.10.0+1890+1072d5cf.src.rpm
perl-Parse-PMFile-0:0.41-7.module+el8.10.0+1890+1072d5cf.src.rpm
perl-String-ShellQuote-0:1.04-24.module+el8.10.0+1890+1072d5cf.src.rpm
</code></pre><div class="zeroclipboard-container position-absolute right-0 top-0"><clipboard-copy aria-label="Copy" class="ClipboardButton btn js-clipboard-copy m-2 p-0" data-copy-feedback="Copied!" data-tooltip-direction="w" value="perl-App-cpanminus-0:1.7044-6.module+el8.10.0+1886+1635aa55.src.rpm
perl-CPAN-DistnameInfo-0:0.12-13.module+el8.10.0+1616+0d20cc68.src.rpm
perl-CPAN-Meta-Check-0:0.014-6.module+el8.10.0+1890+1072d5cf.src.rpm
perl-File-pushd-0:1.014-6.module+el8.10.0+1890+1072d5cf.src.rpm
perl-Module-CPANfile-0:1.1002-7.module+el8.10.0+1890+1072d5cf.src.rpm
perl-Parse-PMFile-0:0.41-7.module+el8.10.0+1890+1072d5cf.src.rpm
perl-String-ShellQuote-0:1.04-24.module+el8.10.0+1890+1072d5cf.src.rpm" tabindex="0" role="button"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon m-2 joplin-clipper-svg-77" style="width: 16px; height: 16px;"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg></clipboard-copy></div></div><p dir="auto">After the fix we get all of the module streams that should have this fix:</p><div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate" style="font-family: ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace;"><code class="notranslate"> perl-App-cpanminus-0:1.7044-6.module+el8.10.0+1886+1635aa55.src.rpm
 perl-App-cpanminus-0:1.7044-6.module+el8.10.0+1886+1e729698.src.rpm
 perl-App-cpanminus-0:1.7044-6.module+el8.10.0+1886+95a09097.src.rpm
 perl-App-cpanminus-0:1.7044-6.module+el8.10.0+1886+c31d99b8.src.rpm
 perl-CPAN-DistnameInfo-0:0.12-13.module+el8.10.0+1616+0d20cc68.src.rpm
 perl-CPAN-DistnameInfo-0:0.12-13.module+el8.10.0+1890+1072d5cf.src.rpm
 perl-CPAN-DistnameInfo-0:0.12-13.module+el8.10.0+1890+281b551b.src.rpm
 perl-CPAN-DistnameInfo-0:0.12-13.module+el8.10.0+1890+318cbfb5.src.rpm
 perl-CPAN-DistnameInfo-0:0.12-13.module+el8.6.0+878+f93dfff7.src.rpm
 perl-CPAN-DistnameInfo-0:0.12-13.module+el8.9.0+1491+219f8fe7.src.rpm
 perl-CPAN-DistnameInfo-0:0.12-13.module+el8.9.0+1491+3507a112.src.rpm
 perl-CPAN-DistnameInfo-0:0.12-13.module+el8.9.0+1491+a1bcd037.src.rpm
 perl-CPAN-Meta-Check-0:0.014-6.module+el8.10.0+1890+1072d5cf.src.rpm
 perl-CPAN-Meta-Check-0:0.014-6.module+el8.10.0+1890+281b551b.src.rpm
 perl-CPAN-Meta-Check-0:0.014-6.module+el8.10.0+1890+318cbfb5.src.rpm
 perl-CPAN-Meta-Check-0:0.014-6.module+el8.10.0+1890+372c0e22.src.rpm
 perl-CPAN-Meta-Check-0:0.014-6.module+el8.9.0+1491+19eb7ac4.src.rpm
 perl-CPAN-Meta-Check-0:0.014-6.module+el8.9.0+1491+219f8fe7.src.rpm
 perl-CPAN-Meta-Check-0:0.014-6.module+el8.9.0+1491+3507a112.src.rpm
 perl-CPAN-Meta-Check-0:0.014-6.module+el8.9.0+1491+a1bcd037.src.rpm
 perl-File-pushd-0:1.014-6.module+el8.10.0+1890+1072d5cf.src.rpm
 perl-File-pushd-0:1.014-6.module+el8.10.0+1890+281b551b.src.rpm
 perl-File-pushd-0:1.014-6.module+el8.10.0+1890+318cbfb5.src.rpm
 perl-File-pushd-0:1.014-6.module+el8.10.0+1890+372c0e22.src.rpm
 perl-File-pushd-0:1.014-6.module+el8.9.0+1491+19eb7ac4.src.rpm
 perl-File-pushd-0:1.014-6.module+el8.9.0+1491+219f8fe7.src.rpm
 perl-File-pushd-0:1.014-6.module+el8.9.0+1491+3507a112.src.rpm
 perl-File-pushd-0:1.014-6.module+el8.9.0+1491+a1bcd037.src.rpm
 perl-Module-CPANfile-0:1.1002-7.module+el8.10.0+1890+1072d5cf.src.rpm
 perl-Module-CPANfile-0:1.1002-7.module+el8.10.0+1890+281b551b.src.rpm
 perl-Module-CPANfile-0:1.1002-7.module+el8.10.0+1890+318cbfb5.src.rpm
 perl-Module-CPANfile-0:1.1002-7.module+el8.10.0+1890+372c0e22.src.rpm
 perl-Module-CPANfile-0:1.1002-7.module+el8.9.0+1491+19eb7ac4.src.rpm
 perl-Module-CPANfile-0:1.1002-7.module+el8.9.0+1491+219f8fe7.src.rpm
 perl-Module-CPANfile-0:1.1002-7.module+el8.9.0+1491+3507a112.src.rpm
 perl-Module-CPANfile-0:1.1002-7.module+el8.9.0+1491+a1bcd037.src.rpm
 perl-Parse-PMFile-0:0.41-7.module+el8.10.0+1890+1072d5cf.src.rpm
 perl-Parse-PMFile-0:0.41-7.module+el8.10.0+1890+281b551b.src.rpm
 perl-Parse-PMFile-0:0.41-7.module+el8.10.0+1890+318cbfb5.src.rpm
 perl-Parse-PMFile-0:0.41-7.module+el8.10.0+1890+372c0e22.src.rpm
 perl-Parse-PMFile-0:0.41-7.module+el8.9.0+1491+19eb7ac4.src.rpm
 perl-Parse-PMFile-0:0.41-7.module+el8.9.0+1491+219f8fe7.src.rpm
 perl-Parse-PMFile-0:0.41-7.module+el8.9.0+1491+3507a112.src.rpm
 perl-Parse-PMFile-0:0.41-7.module+el8.9.0+1491+a1bcd037.src.rpm
 perl-String-ShellQuote-0:1.04-24.module+el8.10.0+1890+1072d5cf.src.rpm
 perl-String-ShellQuote-0:1.04-24.module+el8.10.0+1890+281b551b.src.rpm
 perl-String-ShellQuote-0:1.04-24.module+el8.10.0+1890+318cbfb5.src.rpm
 perl-String-ShellQuote-0:1.04-24.module+el8.10.0+1890+372c0e22.src.rpm
 perl-String-ShellQuote-0:1.04-24.module+el8.9.0+1491+19eb7ac4.src.rpm
 perl-String-ShellQuote-0:1.04-24.module+el8.9.0+1491+219f8fe7.src.rpm
 perl-String-ShellQuote-0:1.04-24.module+el8.9.0+1491+3507a112.src.rpm
 perl-String-ShellQuote-0:1.04-24.module+el8.9.0+1491+a1bcd037.src.rpm
</code></pre><div class="zeroclipboard-container position-absolute right-0 top-0"><clipboard-copy aria-label="Copy" class="ClipboardButton btn js-clipboard-copy m-2 p-0" data-copy-feedback="Copied!" data-tooltip-direction="w" value=" perl-App-cpanminus-0:1.7044-6.module+el8.10.0+1886+1635aa55.src.rpm
 perl-App-cpanminus-0:1.7044-6.module+el8.10.0+1886+1e729698.src.rpm
 perl-App-cpanminus-0:1.7044-6.module+el8.10.0+1886+95a09097.src.rpm
 perl-App-cpanminus-0:1.7044-6.module+el8.10.0+1886+c31d99b8.src.rpm
 perl-CPAN-DistnameInfo-0:0.12-13.module+el8.10.0+1616+0d20cc68.src.rpm
 perl-CPAN-DistnameInfo-0:0.12-13.module+el8.10.0+1890+1072d5cf.src.rpm
 perl-CPAN-DistnameInfo-0:0.12-13.module+el8.10.0+1890+281b551b.src.rpm
 perl-CPAN-DistnameInfo-0:0.12-13.module+el8.10.0+1890+318cbfb5.src.rpm
 perl-CPAN-DistnameInfo-0:0.12-13.module+el8.6.0+878+f93dfff7.src.rpm
 perl-CPAN-DistnameInfo-0:0.12-13.module+el8.9.0+1491+219f8fe7.src.rpm
 perl-CPAN-DistnameInfo-0:0.12-13.module+el8.9.0+1491+3507a112.src.rpm
 perl-CPAN-DistnameInfo-0:0.12-13.module+el8.9.0+1491+a1bcd037.src.rpm
 perl-CPAN-Meta-Check-0:0.014-6.module+el8.10.0+1890+1072d5cf.src.rpm
 perl-CPAN-Meta-Check-0:0.014-6.module+el8.10.0+1890+281b551b.src.rpm
 perl-CPAN-Meta-Check-0:0.014-6.module+el8.10.0+1890+318cbfb5.src.rpm
 perl-CPAN-Meta-Check-0:0.014-6.module+el8.10.0+1890+372c0e22.src.rpm
 perl-CPAN-Meta-Check-0:0.014-6.module+el8.9.0+1491+19eb7ac4.src.rpm
 perl-CPAN-Meta-Check-0:0.014-6.module+el8.9.0+1491+219f8fe7.src.rpm
 perl-CPAN-Meta-Check-0:0.014-6.module+el8.9.0+1491+3507a112.src.rpm
 perl-CPAN-Meta-Check-0:0.014-6.module+el8.9.0+1491+a1bcd037.src.rpm
 perl-File-pushd-0:1.014-6.module+el8.10.0+1890+1072d5cf.src.rpm
 perl-File-pushd-0:1.014-6.module+el8.10.0+1890+281b551b.src.rpm
 perl-File-pushd-0:1.014-6.module+el8.10.0+1890+318cbfb5.src.rpm
 perl-File-pushd-0:1.014-6.module+el8.10.0+1890+372c0e22.src.rpm
 perl-File-pushd-0:1.014-6.module+el8.9.0+1491+19eb7ac4.src.rpm
 perl-File-pushd-0:1.014-6.module+el8.9.0+1491+219f8fe7.src.rpm
 perl-File-pushd-0:1.014-6.module+el8.9.0+1491+3507a112.src.rpm
 perl-File-pushd-0:1.014-6.module+el8.9.0+1491+a1bcd037.src.rpm
 perl-Module-CPANfile-0:1.1002-7.module+el8.10.0+1890+1072d5cf.src.rpm
 perl-Module-CPANfile-0:1.1002-7.module+el8.10.0+1890+281b551b.src.rpm
 perl-Module-CPANfile-0:1.1002-7.module+el8.10.0+1890+318cbfb5.src.rpm
 perl-Module-CPANfile-0:1.1002-7.module+el8.10.0+1890+372c0e22.src.rpm
 perl-Module-CPANfile-0:1.1002-7.module+el8.9.0+1491+19eb7ac4.src.rpm
 perl-Module-CPANfile-0:1.1002-7.module+el8.9.0+1491+219f8fe7.src.rpm
 perl-Module-CPANfile-0:1.1002-7.module+el8.9.0+1491+3507a112.src.rpm
 perl-Module-CPANfile-0:1.1002-7.module+el8.9.0+1491+a1bcd037.src.rpm
 perl-Parse-PMFile-0:0.41-7.module+el8.10.0+1890+1072d5cf.src.rpm
 perl-Parse-PMFile-0:0.41-7.module+el8.10.0+1890+281b551b.src.rpm
 perl-Parse-PMFile-0:0.41-7.module+el8.10.0+1890+318cbfb5.src.rpm
 perl-Parse-PMFile-0:0.41-7.module+el8.10.0+1890+372c0e22.src.rpm
 perl-Parse-PMFile-0:0.41-7.module+el8.9.0+1491+19eb7ac4.src.rpm
 perl-Parse-PMFile-0:0.41-7.module+el8.9.0+1491+219f8fe7.src.rpm
 perl-Parse-PMFile-0:0.41-7.module+el8.9.0+1491+3507a112.src.rpm
 perl-Parse-PMFile-0:0.41-7.module+el8.9.0+1491+a1bcd037.src.rpm
 perl-String-ShellQuote-0:1.04-24.module+el8.10.0+1890+1072d5cf.src.rpm
 perl-String-ShellQuote-0:1.04-24.module+el8.10.0+1890+281b551b.src.rpm
 perl-String-ShellQuote-0:1.04-24.module+el8.10.0+1890+318cbfb5.src.rpm
 perl-String-ShellQuote-0:1.04-24.module+el8.10.0+1890+372c0e22.src.rpm
 perl-String-ShellQuote-0:1.04-24.module+el8.9.0+1491+19eb7ac4.src.rpm
 perl-String-ShellQuote-0:1.04-24.module+el8.9.0+1491+219f8fe7.src.rpm
 perl-String-ShellQuote-0:1.04-24.module+el8.9.0+1491+3507a112.src.rpm
 perl-String-ShellQuote-0:1.04-24.module+el8.9.0+1491+a1bcd037.src.rpm" tabindex="0" role="button"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon m-2 joplin-clipper-svg-79" style="width: 16px; height: 16px;"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg></clipboard-copy></div></div></td></tr></tbody></table></div>

<img width="40" height="40" src="../_resources/143631742_s_60_v_4_3af05629e2c441fe8ddc88adbb6403a.png"/>](https://github.com/jason-rodri)

**[jason-rodri](https://github.com/jason-rodri)** approved these changes <a id="pullrequestreview-2744527427-permalink"></a>[Apr 5, 2025](#pullrequestreview-2744527427)

[View reviewed changes](https://github.com/resf/distro-tools/pull/39/files/980d686f27ea14fa81be38f53a62b65e6c414181)

<img width="20" height="20" src="../_resources/680198_s_40_v_4_73444649d04d4ef4b499dd1baf90e105.jpg"/>](https://github.com/NeilHanlon)[NeilHanlon](https://github.com/NeilHanlon) self-assigned this [Apr 7, 2025](#event-17154098178)

<img width="40" height="40" src="../_resources/11469736_s_60_v_4_050f782d35ce4bd594e86113b36b1de1.jpg"/>](https://github.com/nazunalika)

**[nazunalika](https://github.com/nazunalika)** approved these changes <a id="pullrequestreview-2750900190-permalink"></a>[Apr 9, 2025](#pullrequestreview-2750900190)

[View reviewed changes](https://github.com/resf/distro-tools/pull/39/files/980d686f27ea14fa81be38f53a62b65e6c414181)

<img width="20" height="20" src="../_resources/11469736_s_40_v_4_cb9ae0d73d1c476bbdf5cf35fdd48bbf.jpg"/>](https://github.com/nazunalika)[nazunalika](https://github.com/nazunalika) merged commit [`07e21af`](https://github.com/resf/distro-tools/commit/07e21af9be11bef225cf87729113dc9c1844e5b5) into resf:main [Apr 9, 2025](https://github.com/resf/distro-tools/pull/39#event-17175474328)

<img width="20" height="20" src="../_resources/191179323_s_40_u_0e167a8c49f3180_12867a1cb99547db9.jpg"/>](https://github.com/rockythorn)[rockythorn](https://github.com/rockythorn) mentioned this pull request [Apr 9, 2025](#ref-issue-1679115165)

[Apollo: Potential bug in module version parsing #8](https://github.com/resf/distro-tools/issues/8)

Open

## Merge info

### Pull request successfully merged and closed

You're all set — the branch has been merged.

<img width="40" height="40" src="../_resources/87049949_s_80_v_4_fb525131b07146ed9e3410ccf102b967.png"/>](https://github.com/metalllinux)

#### Add a comment

Comment

* * *

* * *

Add your comment here...

[Markdown is supported](https://docs.github.com/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

Remember, contributions to this repository should follow our <ins>GitHub Community Guidelines</ins>.

**ProTip!** Add [.patch](https://github.com/resf/distro-tools/pull/39.patch) or [.diff](https://github.com/resf/distro-tools/pull/39.diff) to the end of URLs for Git’s plaintext views.

Reviewers

 <img width="20" height="20" src="../_resources/11469736_s_40_v_4_cb9ae0d73d1c476bbdf5cf35fdd48bbf.jpg"/>](https://github.com/nazunalika)[nazunalika](https://github.com/nazunalika)<a id="review-status-nazunalika"></a>[](https://github.com/resf/distro-tools/pull/39/files/980d686f27ea14fa81be38f53a62b65e6c414181)

<img width="20" height="20" src="../_resources/143631742_s_40_v_4_0167969a737d4ad9982e31d4fd65df2.png"/>](https://github.com/jason-rodri)[jason-rodri](https://github.com/jason-rodri)<a id="review-status-jason-rodri"></a>[](https://github.com/resf/distro-tools/pull/39/files/980d686f27ea14fa81be38f53a62b65e6c414181)

Assignees

 <img width="20" height="20" src="../_resources/680198_s_40_v_4_73444649d04d4ef4b499dd1baf90e105.jpg"/>](https://github.com/NeilHanlon)[NeilHanlon](https://github.com/NeilHanlon)

Labels

None yet

Projects

None yet

Milestone

No milestone

Development

Successfully merging this pull request may close these issues.

None yet

You’re not receiving notifications from this thread.

4 participants

 <img width="26" height="26" src="../_resources/191179323_s_52_v_4_8a2cbbd261d946c09a064f46ca14943.jpg"/>](https://github.com/rockythorn)<img width="26" height="26" src="../_resources/11469736_s_52_v_4_4ce8dbf2046944198b52d5b49b19019a.jpg"/>](https://github.com/nazunalika)<img width="26" height="26" src="../_resources/143631742_s_52_v_4_725fb7043b874c71900e04523d501fa.png"/>](https://github.com/jason-rodri)<img width="26" height="26" src="../_resources/680198_s_52_v_4_b5a24b455f8c457590c6ede88ba2e5e3.jpg"/>](https://github.com/NeilHanlon) 

## Footer

[](https://github.com "GitHub")© 2025 GitHub, Inc.

### Footer navigation

- [Terms](https://docs.github.com/site-policy/github-terms/github-terms-of-service)
- [Privacy](https://docs.github.com/site-policy/privacy-policies/github-privacy-statement)
- [Security](https://github.com/security)
- [Status](https://www.githubstatus.com/)
- [Docs](https://docs.github.com/)
- [Contact](https://support.github.com?tags=dotcom-footer)