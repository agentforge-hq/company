---
owner: engineering
status: active
reviewed: 2026-10-18
review_after: 2026-11-01
---
# 0003: Ship the local skill as a native Go executable

The founder authorized rewriting the public AgentForge skill in Go during v0.1.
The binding requirement is a local tool that can run on a developer machine or
agent VM without provisioning a language runtime or external packages.

Keep the skill format: a compact `SKILL.md`, conditional references and a
bundled helper under `scripts/`. Replace the five Python entrypoints with one
Go executable containing audit, lint, sync, discover and drift commands.
Use only Go's standard library and embed default configuration.

Python was easier to iterate and supplied full Python AST checks, but required
a suitable interpreter at installation. Go adds a build and distribution step
and larger platform-specific artifacts. It provides a direct native installation
without a separate runtime. A Rust rewrite would add another migration without
evidence that it solves a remaining v0.1 constraint.

## Compatibility and verification

Retain preview-first management, strict fingerprints, quarantine review,
transaction journals, no-overwrite recovery and explicit lossy exports.
Python-created cold-storage journals remain restorable. Go syntax checks use
the Go AST. Python compatibility checks inspect literal flags and balanced
tokens; full Python syntax is explicitly unverified. Inspected scripts never
run as part of linting.

The [merged rewrite](https://github.com/agentforge-hq/agentforge/pull/2)
passes 86 native tests, local race checks and
[CI on Linux, macOS and Windows](https://github.com/agentforge-hq/agentforge/actions/runs/39161034567)
with Go 1.23 and 1.27. The build produces checksummed amd64 and arm64 bundles
for each OS; building a target does not establish that every target was executed.
An extracted macOS arm64 bundle passed version, audit and self-lint checks with
an empty executable search path. The previous local installation is backed up
outside discovery roots.

These results establish the tested portability and recovery boundaries. They
do not establish faster execution, better model routing or improved user tasks.
Revisit packaging if clean-machine installation fails or supported environments
cannot execute native binaries. Revisit Python validation if real missed syntax
errors make the current disclosed boundary insufficient.

This decision covers the Apache-2.0 public skill. The separate company worker
prototype remains Python and proprietary under [LICENSE](../LICENSE).
