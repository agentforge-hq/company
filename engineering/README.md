---
owner: engineering
status: active
reviewed: 2026-10-18
review_after: 2026-10-25
---
# Engineering

Engineering owns correctness, reproducibility, compatibility evidence and the
cost of maintaining the system.

The [public skill](https://github.com/agentforge-hq/agentforge) contains the
local deterministic core as a native Go executable; see the
[runtime decision](../decisions/0003-native-go-runtime.md). This public repository contains the company worker
prototype in `scripts/company.py`, its tests, operating configuration and
commercial planning. A hosted commercial service has not been built.

Read [the roadmap](../product/roadmap.md), [contract gaps](../product/v0.1-contract-gaps.md)
and [worker design](company-workers.md) before proposing architecture changes.

For each change, state the observed failure, smallest mechanism, affected
guarantees and verification. Preserve user files, permissions and source
provenance. Do not weaken a skill to conceal a product bug. Optional external
services stay outside the zero-dependency local core.

The engineering worker proposes documentation changes within `engineering/`.
It may describe a code change and its tests as a handoff; this prototype does
not grant model output direct write access to executable code or CI policy.
Implementation follows a reviewed engineering task in a separate branch.

Run the company checks with `python3.11 -S -m unittest discover -s tests -v`.
Keep repository history, CI logs and review artifacts free of credentials,
personal data and confidential third-party material. Before a live provider
pilot, review data scope and cost limits with the founder.

## Audit reliability and cleanup pilot

The first dogfood audit exposed problems in AgentForge's measurements. The
[reliability patch](https://github.com/agentforge-hq/agentforge/pull/1) corrects
Codex built-in coverage, false dependency errors and weak lexical matches. Its
local activation and verification are recorded in
[release verification](../evidence/release-verification.json). The patch and
subsequent Go rewrite are merged. The installed Go skill passes 86 native
regression tests, cross-platform CI and all 12 saved lexical smoke cases.
Passing structural checks does not establish better
model routing or completed tasks.

Next, capture a fresh Codex baseline, then test disabling one duplicate
`humanizer` entry for Codex while retaining the universal copy and all files.
Back up the setting, restart the harness and verify the new catalog. Compare
the same rewrite, skill-creation, audit and unrelated arithmetic tasks with
fixed inputs and model settings. Record selected skill paths, fact preservation
and task completion; restore the setting if outcomes regress. Keep plugin
caches and eager project rules intact during this first pilot. No configuration
change or fresh-session performance improvement has been verified yet.

The native audit reproduces 124 filesystem candidates, a 12,188-token index
proxy and a 3,253-token eager-rule proxy. The saved 41-entry session catalog
still has four review findings: two uppercase plugin names, one plugin directory
name mismatch and one remote-execution pattern. These are review candidates,
not proof that those skills fail or are malicious. Do not edit plugin caches or
weaken checks simply to make this report pass.

Resolve the [v0.1 contract](../product/v0.1-contract-gaps.md) before expanding
the command surface. The next behavioral priority is AF-011's controlled
duplicate-disable pilot. If a fresh-session comparison is unavailable, prepare
its raw cases and recovery steps; leave its outcome unmeasured.
The [pilot packet](duplicate-pilot.md) contains those cases, evaluator checks and
recovery steps. Keep the rubric separate from evaluated prompts.
