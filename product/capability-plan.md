---
owner: product
status: active
reviewed: 2026-10-30
review_after: 2026-11-06
---
# Capabilities for the discovery pilot

AgentForge should help someone describe a task, discover useful expertise, and
bring a suitable skill into the agent's work. The person should not need a skill
name or knowledge of the technique that would help.

The founder authorized this functional scope. The
[implementation record](../engineering/discovery-pilot.md) separates shipped
mechanisms, measured smoke checks, and unestablished release gates. The
[competitive review](competitive-landscape.md) records alternatives and its limits.

## Implementation state

Source-backed profiles, canonical GitHub and registry discovery, constraints,
grounded shortlists, evidence details, paginated browsing, and guided native
quarantine/promotion are implemented in the preview branches. The native preview
is available for six operating-system/CPU combinations. Broader coverage is a
570-directory complete snapshot from nine repositories and two source kinds.

The next constraint is measured relevance and task usefulness. A frozen
machine-authored candidate set exists, but its human-review gate is pending.
Bounded Codex diagnostics cover ordinary discovery, trivial skipping, transport
recovery, and non-repetition after a candidate mention. They do not establish
reliable invocation or accepted activation. Claude Code authentication currently
prevents the second-harness test.
The elapsed [operating observation](../engineering/discovery-pilot.md#completed-operating-observation)
is complete, with a retained freshness lapse and unavailable spending attribution.
AC-12 and matched task improvement remain unestablished.

## Required user capabilities

| Capability | Behavior to build | Observable acceptance |
| --- | --- | --- |
| Discover from an ordinary task | The installed skill searches for a new substantive job without requiring the person to request a skill. It stays quiet on trivial turns and respects rejection within the session. | Fresh-session AC-04 measures search calls and visible recommendations separately. An outage leaves the original task able to continue. |
| Find the useful technique | Match the goal, intended output, and explicit constraints against capabilities, examples, requirements, and exclusions. A request can succeed without sharing the skill's name or terminology. | Held-out terminology-free requests, ambiguous tasks, and no-match cases pass the PRD relevance gates. A broad lexical match alone is insufficient. |
| Understand each recommendation | Offer a short list, normally one to three, with a source-backed explanation of what each skill helps accomplish, what it requires, and what remains unknown. | Every fit explanation refers to metadata or a source excerpt from the returned revision. Do not display a ranking score as a probability of success. |
| Choose between real alternatives | Resolve mirrors and listings to an upstream skill directory. Show one upstream skill with its variants where appropriate, retaining meaningful forks and harness-specific requirements. | Two registries pointing to the same upstream directory do not consume two recommendation slots. Divergent forks remain distinguishable. |
| Know whether it is usable here | Show tools, credentials, runtime, license status, and compatibility evidence. Separate declared, inferred, tested, unknown, and incompatible states. | Known-incompatible candidates are excluded for the selected harness. Unknown support remains visible and is never relabeled tested. Optional environment constraints contain no files, secrets, or private paths. |
| Inspect and adopt a pinned version | Offer source inspection, package review, and a guided path through existing quarantine and promotion. Detect an existing local install and explain activation in the current harness. | Accepted adoption uses the returned revision and supporting files. A mismatch requires renewed inspection. Existing installations are preserved, and rollback or removal is available. A restart requirement is explicit. |
| Rely on current source information | Refresh registered sources, discover additional sources through bounded connectors, and expose actual last-check times. Preserve the previous complete revision on refresh failure. | Changed sources update without duplicate identities. Confirmed withdrawals stop appearing as adoptable results. Temporary fetch errors do not imply deletion. |

Search uses only a short task goal and the declared harness by default. The local
client can compare results with installed skills without uploading the person's
skill inventory. Additional environment constraints are explicit caller input.
The service must abstain when no candidate fits. It can request one clarification
when missing information changes the choice, without interrupting every task.

## Capability profiles make these behaviors possible

Each profile needs a purpose, intended outputs, suitable tasks, unsuitable tasks,
representative ordinary-language examples, prerequisites, and source evidence.
Identity includes the upstream repository and directory. Revision and file
digests identify the reviewed package, including supporting resources.

Preserve the author's metadata separately from AgentForge's derived fields.
Every derived field records its source revision and extraction version. Missing
requirements are unknown, not evidence that a skill needs no tools or accounts.
Generated examples used in retrieval are not held-out evaluation prompts.

Start with author-provided sections and reviewed extraction rules. Compare any
model-assisted enrichment with that baseline before adding provider cost or a
new dependency. Enrichment belongs in the indexing path. A search request should
not require a large model to reread the entire catalog.

## What the website and installed skill provide

Any public contract change updates the OpenAPI definition, parity fixtures, and
both clients in the same slice. Both clients use the same ranking. The website supports
ordinary-task search, a concise recommendation list, source and requirement
inspection, and an AgentForge installation prompt. Shareable skill detail URLs
are useful after canonical identities and profiles are stable. Browsing can
offer additional results without forcing the agent to read a long list.

The installed skill adds task-triggered search and local adoption. A cloud-only
chat with no supported local tool access receives a transparent handoff rather
than an installation-success claim. First establish the whole journey in Codex,
then repeat it in a second harness. No undocumented hook is a dependency.

The API remains the common integration. A thin MCP adapter or ARD-compatible
catalog can follow when a specific integration requires it. These adapters must
reuse the same catalog and query behavior. They do not justify another ranker,
database, or public execution service.

## Build sequence

| Slice | Work items | Deliverable and limit |
| --- | --- | --- |
| A: source meaning and canonical coverage | AF-018, AF-014 | Source-backed capability profiles, upstream identity mapping, and a documented registry connector. Review extraction across the existing task families, then reach the PRD's 500-directory, two-source-kind pilot gate. |
| B: useful recommendations | AF-019, AF-015 | Constraint-aware matching, grounded fit explanations, and calibrated abstention through the existing endpoint. Prepare development cases and freeze the separate 100-prompt release set before final tuning. Evaluate after the ranker is frozen. |
| C: discovery through adoption | AF-020, AF-016 | A guided local inspection and adoption path using existing native commands. Record rejection, pinned loading, activation limitations, and matched original-task outcomes in fresh sessions. |
| D: operating evidence | AF-017 | Complete parity, failure, privacy, latency, cost, and refresh checks, including the 48-hour observation, before the target release claim. |

AF-015 dependencies gate the final evaluation run, not prompt preparation. Product
starts that preparation while the catalog and search improve. AF-019 cannot
complete final tuning until product freezes the held-out set. Do not tune
on held-out judgments. Compare the same catalog revision across both clients.
When comparing another product, record its different catalog and access limits.

## Later capabilities and deliberate exclusions

After the pilot establishes usefulness, consider opt-in outcome feedback tied to
the selected source revision and harness. Distinguish a click, installation,
successful activation, and a useful completed task. Do not silently collect raw
queries or transcripts, or let one unverified rating directly change ranking.

Private team catalogs, organization policies, curated task packs, and MCP or ARD
distribution are later candidates with a demonstrated user need. Pricing and a
paid offering remain hypotheses.

Skill editing, autonomous upstream repairs, a social feed, public star rankings,
billing, hosted task execution, and multi-agent company workers are outside this
pilot. An index listing or static scan must not become a universal safety badge.
The original authors maintain their skills.

## Why this scope follows the competitor evidence

[Vercel find-skills](https://github.com/vercel-labs/skills/blob/main/skills/find-skills/SKILL.md)
already covers ordinary-task discovery and installation.
[hf-discover](https://github.com/huggingface/hf-discover) provides semantic and
federated discovery. [Tessl](https://tessl.io/registry) publishes skill evaluation
results. These documented capabilities establish alternatives, not comparative
performance in our target tasks.

Reuse the existing service, embedding index, and native review tools. The new
work must establish better task suitability and successful adoption. If matched
task tests do not show useful improvement over existing discovery or no
discovery, reduce the scope or use an upstream service instead of accumulating
features. The retained PRD gates measure a pilot; they do not prove superiority.
