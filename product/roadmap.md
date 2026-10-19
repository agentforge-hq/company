---
owner: product
status: draft
reviewed: 2026-10-18
review_after: 2026-10-25
---
# Roadmap

The sequence below is driven by evidence gates. Timing is a planning assumption,
not a release promise. The detailed queue is in [work-items.json](../.company/work-items.json).

| Milestone | State | Outcome | Exit evidence |
| --- | --- | --- | --- |
| M0: publish and establish ownership | Complete | Public Apache-2.0 skill and public company workspace under the chosen organization | Both repositories exist with verified visibility; tests pass; owners and links are correct |
| M1: reconcile the v0.1 contract | In review | Review the proposed smaller contract alongside the merged native Go implementation | Each gap has an owner and an implement, reject or milestone-specific defer decision accepted in review |
| M2: prove useful maintenance | Planned | Dogfood audit, selected deduplication and one real drift repair | Redacted before/after reports, explicit authorization for file moves, regression checks and user acceptance from distinct tasks |
| M3: test task outcomes | Planned | Compare maintained skills with baselines on representative jobs | Reproducible cases, actual task results, failure analysis and a clear distinction between structural scores and skill lift |
| M4: validate a team offering | Planned | Learn which recurring maintenance job teams will adopt or pay for | Customer evidence, selected job, willingness-to-pay test and a bounded service specification |
| M5: pilot function workers | Prototype prepared | Product, engineering, design, marketing and operations produce useful proposals | Approved provider budget and data scope; manual runs accepted by reviewers; no unexplained or unauthorized edits |
| M6: schedule proven recurring work | Deferred | Recurring document/skill maintenance with visible ownership and cost | Manual pilot establishes a recurring need; stop conditions, provider spend controls, review path and rollback are tested |

## Next work

1. M0 is complete; [release verification](../evidence/release-verification.json) records repository visibility and passing CI.
2. Review [the v0.1 contract](v0.1-contract-gaps.md). The
   [native Go rewrite](../decisions/0003-native-go-runtime.md) is merged and
   installed locally, with a full backup and passing platform checks. Do not rename an internal
   heuristic to imply a published benchmark, or encode unverified harness flags.
3. Run AF-011's fresh-session duplicate-disable comparison, then one demonstrated
   drift repair under AF-003. Preserve the minimal evidence needed to assess
   outcomes. Avoid publishing machine inventories that expose private paths.

## Candidate later products

A registry, command-line installer, read-only cloud bridge and GitHub App
(working name: Friday Skill Healer) remain options from the source brief.
Choose among them after M2–M4 evidence. Hosted benchmarks and model-change
regressions may become useful when a verified task suite exists.

The company workspace is also a public record of our organizational design and
operating experiments. Share accepted changes and evidence-backed lessons from
the work as part of product distribution; track this in the marketing queue.

## Worker pilot

The initial prototype uses one explicitly selected role per invocation and
returns proposals plus handoff requests. It does not claim that consumer Grok
desktop sessions can be scheduled or coordinated through an undocumented API.
Workers use the documented xAI API only after activation. Product turns accepted
handoffs into queue items; operations checks dependencies and stale documents.

## Review and retirement

Review the roadmap after a meaningful dogfood result, a validated harness change
or a customer discovery result. Move obsolete proposals to a decision record
with the reason, rather than leaving competing plans active indefinitely.
