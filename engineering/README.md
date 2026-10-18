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
local deterministic core. This private repository contains the company worker
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

Run the private checks with `python3.11 -S -m unittest discover -s tests -v`.
Keep public release artifacts free of private company context and test fixtures
containing personal data. Before a live provider pilot, review data scope and
cost limits with the founder.
