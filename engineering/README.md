---
owner: engineering
status: active
reviewed: 2026-10-28
review_after: 2026-11-04
---
# Engineering

Engineering owns correctness, reproducibility, compatibility evidence and the
cost of maintaining the system.

The [public skill](https://github.com/agentforge-hq/agentforge) contains the
local deterministic core as a native Go executable; see the
[runtime decision](../decisions/0003-native-go-runtime.md). This public repository contains the company worker
prototype in `scripts/company.py`, its tests, operating configuration and
commercial planning. The separate proprietary [platform](https://github.com/agentforge-hq/platform)
contains the deployed Pixeltable Cloud discovery service and Vercel website.
The [discovery pilot record](discovery-pilot.md) owns implementation evidence and open gates.

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
subsequent Go rewrite are merged. The initial Go port passed 86 native
regression tests, cross-platform CI and all 12 saved lexical smoke cases.
Passing structural checks does not establish better
model routing or completed tasks.

AF-011's controlled duplicate-disable comparison is deferred behind discovery validation.
The [pilot packet](duplicate-pilot.md) owns the raw cases, catalog checks,
evaluator rubric and recovery steps. Keep the rubric outside evaluated prompts.
Leave task outcomes unmeasured until that comparison runs. No Codex setting has
been changed by this pilot.

Review the [v0.1 contract](../product/v0.1-contract-gaps.md) before adding commands.
Treat portability and instruction-pattern findings as review candidates.
Do not edit plugin caches or weaken checks to make a report pass.

The [Devin field follow-up](devin-field-feedback.md) verifies a real filesystem
cleanup and records the resulting batch-storage, root-discovery and help fixes.
Its saved audit counts and restore previews do not establish routing or task lift.
