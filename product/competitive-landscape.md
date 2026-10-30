---
owner: product
status: active
reviewed: 2026-10-27
review_after: 2026-11-10
---
# Skill discovery competitors

AgentForge's proposed advantage is helping a person complete an ordinary task
with a useful capability they did not know existed. That advantage remains a
hypothesis. Existing products already offer task discovery, semantic search,
conversational installation, and skill evaluation.

This October 27 review covers the direct alternatives below and several adjacent
systems. It is a bounded review of first-party documentation, public interfaces,
and selected source files. It is not an exhaustive census or a comparative
runtime benchmark. A documented feature means its publisher describes it. It
does not establish successful behavior in a particular harness.

## Direct alternatives

| Product | What the reviewed source establishes | Implication for AgentForge |
| --- | --- | --- |
| [SkillsMP](https://skillsmp.com/) | A broad directory, category and occupation filters, and agent connection through API and MCP. Its [changelog](https://skillsmp.com/changelog) says the former Cloudflare semantic search was retired and current public search uses keywords and filters. Its [API documentation](https://skillsmp.com/docs/api) describes the supported interface. | Compare ordinary-task relevance against a substantial directory. An API or connection button is already available elsewhere. The public search description does not establish what private pilots can do. |
| [Vercel skills.sh](https://skills.sh/) and [find-skills](https://github.com/vercel-labs/skills/blob/main/skills/find-skills/SKILL.md) | The discovery skill covers ordinary requests about how to do a task or use a specialized capability. It searches, presents candidates, and offers installation. Recommendation rules include install counts, source reputation, and stars. | A meta-skill that finds other skills from an ordinary request already exists. Compare relevance and completed adoption. Popularity alone does not prove task suitability. |
| [agentskill.sh /learn](https://agentskill.sh/install) | Search, preview, installation, and management inside a conversation. The publisher also describes project-based recommendations, content hashes, and update checks. | Conversational adoption overlaps directly with our journey. Test activation in each harness. The page advertises mid-conversation use but also requires a restart or new session for initial setup. |
| [Hugging Face hf-discover](https://github.com/huggingface/hf-discover) | Semantic search with CLI, REST, and MCP access. Its ARD client can search one catalog or follow federated catalogs. It returns skills and MCP resources. | Natural-language search and federation already exist. Evaluate this as a baseline and possible connector before inventing another federation protocol. |
| [ClawHub](https://github.com/openclaw/clawhub) | OpenClaw's registry documents vector search, inspection, installation, updates, versions, and pinned installs. Owners can rename or merge their own duplicate listings with redirects. | Semantic retrieval, provenance, and canonicalization operations are established features. Owned-listing merges do not establish automatic deduplication of unrelated upstream forks. |
| [SkillKit](https://www.skillkit.sh/docs) | Cross-harness installation and translation, stack-based recommendations, and runtime discovery through local REST or MCP. | Recommendations and cross-harness management overlap both our original local tool and the discovery service. Compatibility claims need observed tests. |
| [Tessl](https://tessl.io/registry) | A searchable, versioned registry publishes quality and impact scores, evaluation-scenario counts, and security-scan results. It describes evaluation on publication. | Evaluation is already a competitive offering. Inspect its methodology before claiming differentiation. Its uplift and security results are publisher claims we have not reproduced. |
| [Skillstore](https://skillstore.io/) | Task-description search and curated task packs, with audit information and installation commands. | Task-first positioning and assembling several skills for a job are already present. Measure whether our recommendation helps the original job. |
| [Tencent SkillHub](https://github.com/Tencent/skillhub/blob/main/README_EN.md) | Public APIs, an official discovery skill, TRACE evaluation, organization libraries, and a DeepSeek Harness plugin for in-chat search, details, and installation. Its catalog combines synced and locally published skills. | Harness discovery and evaluation have regional and ecosystem-specific competitors. Published certification claims are not independent safety evidence. |
| [SkillHub.fyi](https://docs.skillhub.fyi/docs) | Private registries with content-hashed versions and mutable tags. Documentation describes one local store, per-agent symlinks, and search across owned registries, skills.sh, and GitHub. | Team distribution and cross-registry search are existing products. This is separate from Tencent SkillHub. |
| [skills.md](https://skills.md/docs/skills) | Hosted search and inspection through its CLI, followed by quoting and running hosted skills. | Discovery can lead to hosted execution. AgentForge's current scope ends at finding and adopting upstream skills. |

## Additional directories and review limits

| Product | Evidence and boundary |
| --- | --- |
| [Playbooks](https://playbooks.com/skills/inclusionai/aworld/search) | A listing exposes the upstream directory, skill contents, and a Playbooks install command. Several index and category routes were unavailable, so ranking and runtime discovery remain unverified. A listed third-party skill does not establish the platform's own search behavior. |
| [LobeHub](https://lobehub.com/agent) | Its agent marketplace offers browsing and workspace adoption. An [official example](https://lobehub.com/agent-mbti) links a skills marketplace install path. The skills index returned HTTP 403, so skill-search behavior is partially reviewed. Agent listings are not a comparable count of standalone skills. |
| [SkillHub.space](https://docs.skillhub.space/) | Documentation describes an OpenClaw registry and a CLI for search, install, publishing, and validation. Quality claims are untested. This is separate from the two SkillHub services above. |
| [Skill Marketplace](https://www.skill-marketplace.com/) | Its public description covers source aggregation, full-text search, filters, and validation. Collection and verification counts are self-reported. It is another distinct service using the SkillHub name. |
| [SkillsMD.dev](https://skillsmd.dev/) | The public directory describes browsing, installation, sharing, and usage rankings. Retrieval and installation behavior are untested. It is separate from skills.md. |

Native features can replace part of our product. Google's
[Agent Registry](https://docs.cloud.google.com/agent-registry/search-agents-and-tools)
documents keyword and semantic discovery across registered agents, skills, and
MCP resources. It addresses governed organization resources rather than an
internet-wide public catalog. Microsoft's
[Agent Framework skill providers](https://learn.microsoft.com/en-us/agent-framework/agents/skills)
cover resource loading and aggregation, including an experimental MCP source.
These are adjacent integration systems, not equivalent public marketplaces.
The [Agent Skills specification](https://agentskills.io/) defines a package
format. It does not establish registry quality or automatic invocation.

## What we have measured

The deployed AgentForge [catalog endpoint](https://agentforge-five-sandy.vercel.app/api/v1/catalog)
returned 90 entries from six repositories on October 27. The
[implementation](https://github.com/agentforge-hq/platform) contains hybrid
retrieval and one endpoint for the website and native client. This confirms a
working preview with a small catalog. It does not prove broad coverage,
superior relevance, or reliable automatic discovery.

An earlier single-query comparison used "Make my writing sound like me".
AgentForge returned writing-related skills and SkillsMP returned less relevant
items in that request. This was an exploratory observation with different
catalogs, not a benchmark. It cannot support a general superiority claim.
None of the other competing clients was installed or tested in a fresh harness
session during this review.

Directory counts can include mirrors, forks, versions, agent profiles, generated
skills, and MCP servers. They are not comparable units of unique usable skills.
A checksum establishes content identity, not safety. A security badge records
the publisher's reported assessment, not an independent guarantee.

## Product decisions and evidence needed

The founder accepted these priorities on October 27. The [roadmap](roadmap.md)
orders them. The [PRD](discovery-service-prd.md#11-release-sequence-and-acceptance)
defines the existing pilot gates.

1. Expand canonical coverage. Resolve listings to upstream directories and
   revisions. Track aliases, forks, requirements, and freshness. Report task-family
   coverage as well as counts. Prefer documented feeds, APIs, and federation.
   Verify access terms, limits, and identity mapping before choosing a connector.
2. Freeze a representative evaluation. Separate development cases from held-out
   ordinary requests, ambiguous tasks, no-match requests, and trivial messages.
   Compare with lexical retrieval and accessible competing discovery paths.
   Record catalog differences, revisions, latency, and access limits. Human
   reviewers judge suitability with source requirements visible and provider
   identity hidden where practical.
3. Prove discovery and adoption in fresh sessions. Measure search calls, visible
   recommendations, rejection, accepted loading, and original-task completion
   separately. Start with Codex, then repeat in a second harness before claiming
   cross-harness reliability. Use matched inputs and model settings for task
   comparisons with and without discovery.

The numerical gates remain proposed targets. Retrieval success alone does not
demonstrate better completed tasks. Task results and user effort must justify
the interruptions, latency, and setup discovery introduces.

If tests show no useful advantage over existing paths, narrow the product, use an
upstream registry, or improve an integration. "One Skill" remains our product
promise. Exclusivity and superior performance remain unproved.
