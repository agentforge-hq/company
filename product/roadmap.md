---
owner: product
status: active
reviewed: 2026-11-08
review_after: 2026-11-15
---
# Roadmap

On November 8, the founder expanded AgentForge's direction to prompts, skills,
and reasoning methods discovered during the work. Source scouting and the
founder's own successful finds feed a reviewed catalog. The product must help
apply a useful approach to the original task and show whether the result improves.

The [expertise discovery PRD](discovery-service-prd.md) defines the proposed v0.2
scope. The [earlier pilot specification](skill-discovery-pilot-spec.md) preserves
the previous stages and AC-01 through AC-12 without changing their outcomes.
The [website](https://lordoftheskill.com/) and shared search service
are deployed previews. The complete October 28 snapshot contains 570 upstream directories from nine
repositories, discovered directly and through a registry. The
[implementation record](../engineering/discovery-pilot.md) separates publication,
relevance, invocation, and task-outcome evidence. Deployment alone passes none
of those gates.

The [earlier capability plan](capability-plan.md) records the skill pilot's
implementation slices. Profiles, constrained search, source-backed fit, canonical
browsing, and guided native adoption are implemented in the pilot. Work items
remain in review while their behavioral and operating acceptance checks are open.

## Next implementation sequence

These are proposed bounded steps. They do not authorize recurring scouts or pass
the existing pilot. The new evaluation uses ED identifiers and a separately
sealed corpus, preserving the old ranker, evaluation material, and failures.

| Priority | Work item and owner | Deliverable |
| --- | --- | --- |
| Review the first version | AF-021, product and founder | Review the PRD's source policy, three task families, adaptation journey, and proposed outcome gates. |
| Build a small reviewed catalog | AF-022, engineering with product review | A bounded importer and queue for founder-saved links, GitHub, and permitted web sources. Review 30 entries across prompts, skills, and methods. Social links can remain link-only. |
| Prove the full interaction | AF-023, engineering with design review | One versioned endpoint for both clients. Demonstrate a prompt, method, and skill from ordinary task through acceptance and application, with rejection and no-match behavior. |
| Decide from measured outcomes | AF-024, product with operations | Separate development and sealed evaluation cases; compare with the ordinary agent and generic reflection. Record relevance, interruptions, actual application, task outcomes, and usage before expanding. |

The first version targets Codex. The website offers the same search and a
task-aware review handoff. X access, broader crawling, personal accounts, and a
second harness follow evidence of need. Upstream authors retain ownership of
their material. Prompt discovery and adaptation remain unimplemented proposals.

## Earlier skill-pilot gates

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

AF-015 now has a local blind review worksheet against the pinned 570-skill
snapshot. It saves portable drafts and validates a separate reviewed successor
without rewriting the original candidate freeze. The product owner still needs
to review and accept the judgments before future final tuning. See the
[workflow and limits](../engineering/discovery-pilot.md#human-review-workflow).

The [ten-task development review](../engineering/discovery-pilot.md#november-1-task-review-and-website-handoff)
and [retrieval diagnosis](../engineering/discovery-pilot.md#november-2-retrieval-diagnosis)
separate keyword-only additions from semantic task mismatches. A semantic-only
admission candidate is rejected because it retains key mismatches and removes
plausible alternatives. Human ratings remain blank. Review the cases for task
fit and unstated platform assumptions, then complete the separate blind
judgments. Keep the frozen ranker and previous failures unchanged. The website
handoff carries the submitted task into its copied review prompt; accepted
activation and original-task improvement still need their own evidence.

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

Prompt editing as a standalone product, third-party repairs, accounts, billing,
a social marketplace, and a larger worker system remain outside v0.2. Adapting
one selected instruction inside the current task is included. Preserve the
original source and distinguish the agent's adaptation from the author's text.

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
