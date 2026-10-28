---
owner: product
status: active
reviewed: 2026-10-27
review_after: 2026-11-03
---
# Roadmap

The founder accepted the discovery-first product direction and the next
priorities on October 27. AgentForge should connect an ordinary request to a
useful capability and help the agent apply it to the original task. The
[competitive review](competitive-landscape.md) shows that discovery skills,
semantic registries, and conversational installation already exist. Our
advantage must come from measured usefulness.

The [discovery service PRD](discovery-service-prd.md) defines the pilot gates.
The [website](https://agentforge-five-sandy.vercel.app/) and shared search service
are deployed previews. The public catalog returned 90 entries from six
repositories on October 27. Deployment does not establish that the coverage,
relevance, invocation, or task-outcome gates have passed.

The [capability plan](capability-plan.md) specifies proposed functionality and
implementation slices. Source-backed profiles precede broader indexing. Search
and local-adoption improvements each have an owned work item and acceptance
check. These additions remain planned.

## Active priorities

| Priority | Owner | Outcome | Exit evidence |
| --- | --- | --- | --- |
| P1: canonical coverage, AF-014 | Engineering | Broader task coverage with upstream identities, revision pins, aliases, and actual freshness | PRD stage B: at least 500 distinct directories from two source kinds. Record repeat ingestion, changes, removal, extraction failure, and duplicate or fork handling. Publish coverage by task family. |
| P2: representative relevance, AF-015 | Product | Know whether ordinary requests find a useful capability | Freeze the PRD's 100 human-reviewed prompts before final tuning. At least 40 of 50 relevant requests have an approved top-three result. Report no-match behavior and comparisons with lexical retrieval and accessible competing paths. |
| P3: reliable discovery and adoption, AF-016 | Product and engineering | An ordinary request triggers useful discovery and accepted skills help the original task | In fresh sessions, at least 45 of 50 relevant requests trigger discovery. At most 2 of 25 no-match tasks prompt an inappropriate recommendation. No trivial message triggers a recommendation or search. Record rejection, revision-pinned loading, activation limits, and matched task outcomes separately. |
| P4: controlled pilot, AF-017 | Operations and product | Operate and describe the service according to observed evidence | Complete the PRD's parity, installation, failure, security, latency, cost, and 48-hour operating checks. Record a launch decision with unmet gates visible. |

P2 uses a frozen P1 catalog revision. Evaluation cases can be prepared while
coverage expands. Start P3 installation and invocation checks in Codex.
Repeat the journey in a second harness before claiming cross-harness reliability.
The thresholds above are targets, not achieved measurements.

## Completed foundations and open review

The public skill and company repositories exist with separate licenses. The
[native Go runtime](../decisions/0003-native-go-runtime.md) is merged. The
platform, preview bundles, and website are available for inspection. Product
direction is accepted, while the complete PRD remains a release specification
with open acceptance work. AF-002 retains the review of scope and contract gaps.

The founder-owned [vision](../vision.md) still describes the earlier maintenance
thesis. Aligning that document is a founder review item. This roadmap records
the accepted product priorities without treating old vision wording as a
prerequisite to discovery work.

## Deferred work

Local audit and recovery commands remain available. The maintenance repair,
maintenance-specific design walkthrough, duplicate-disable pilot, and team
maintenance offering are deferred behind discovery validation. Their evidence
remains in the [work queue](../.company/work-items.json),
[contract review](v0.1-contract-gaps.md), and
[Devin follow-up](../engineering/devin-field-feedback.md).

Do not add authoring tools, repair third-party skills, accounts, billing, a
social marketplace, or a larger worker system to satisfy the discovery pilot.
Upstream authors maintain their own skills.

## Company operating experiments

The company workspace remains a public record of organizational design and
operating experiments under its proprietary license. Public walkthroughs must
distinguish accepted plans from observed outcomes.

The function-worker prototype produces proposals. Its xAI pilot and recurring
document work remain separate from the product service's refresh jobs. Do not
infer a consumer Grok desktop automation API or activate workers without the
configured data scope and budget.

Review the roadmap after the coverage evaluation, held-out relevance run,
fresh-session tests, or material competitor change. Replace failed proposals
with a documented decision rather than leaving conflicting plans active.
