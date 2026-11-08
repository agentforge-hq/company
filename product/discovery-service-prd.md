---
owner: product
status: draft
reviewed: 2026-11-08
review_after: 2026-11-15
---
# AgentForge expertise discovery PRD

AgentForge helps an agent discover useful prompts, skills, and reasoning methods
while a person works. It identifies a missing approach, explains how that approach
could help the current task, and offers to apply it. The person should not need
the expert vocabulary, the name of a skill, or a separate search session.

The founder requested this direction on November 8. This document defines the
first expertise-discovery pilot, called v0.2 here to distinguish it from the
existing local tool and skill-search preview. The scope and numerical gates below
are proposals. Prompt discovery, web scouting, and adaptation are not shipped
capabilities. The existing [website](https://lordoftheskill.com/) and skill-search
service are foundations. Their [implementation record](../engineering/discovery-pilot.md)
does not establish the broader product's usefulness.

The [earlier pilot specification](skill-discovery-pilot-spec.md) preserves its
acceptance criteria. Its frozen ranker, evaluation cases, failures, and open human
review remain intact. The [roadmap](roadmap.md) separates that work from this pilot.

## 1. Problem, beneficiary, and outcome

People can describe a desired result without knowing which investigation,
question, constraint, or workflow would produce it. A repository of prompts is
useful when someone knows what to look for. AgentForge must also help when they
do not recognize the missing expertise.

The first cohort is builders working in Codex on software diagnosis, product
experience, and written analysis. These are three bounded task families for
testing the idea. Broad professional coverage remains a longer-term goal.

Success is a better completed task with acceptable user effort. Record discovery,
suggestion, acceptance, actual application, and outcome separately. Downloads,
more elaborate prompts, and a growing catalog are insufficient outcome measures.
The hypothesis fails if suggestions add interruptions without improving the work,
or if a generic instruction to question assumptions performs just as well.

## 2. What the first version includes

One installed AgentForge skill and its Go client connect to the existing cloud
service. A single-page website searches the same catalog and shows source details.
The pilot adds three kinds of reusable material:

| Kind | What the person receives | Application |
| --- | --- | --- |
| Prompt | A bounded instruction with its required inputs, expected output, and limits | The agent offers an adaptation for the current task and uses it after acceptance. |
| Skill | An upstream package with instructions and possibly supporting resources | The existing inspection and revision-pinned adoption flow applies. |
| Method | A short procedure or set of questions, such as generating competing explanations and testing what would distinguish them | The agent explains the procedure in ordinary language and applies the accepted steps. |

A method can be packaged as a prompt or skill. Store its canonical source once
and link alternate forms. Do not fill a shortlist with the same approach three
times. Use `kind` for the primary application form and tags for the reasoning
technique. A technical name such as "abductive reasoning" is optional metadata,
not vocabulary the user must learn.

Start with 30 human-reviewed entries, assigned to one primary task family each,
ten per family, including at least eight prompts, eight skills, and four methods
across the set. These are proposed scope bounds, not quality claims.
Select skills from the existing catalog and add
prompts and methods from sources with sufficient reuse rights. The wider skill
catalog remains searchable through the existing preview. It does not become
approved for automatic v0.2 suggestions merely by being indexed.

The pilot includes bounded scouting, an operator review queue, provenance,
contextual retrieval, a suggestion inside the conversation, and a private outcome
record. It excludes a prompt editor product, public submissions, accounts,
payments, social rankings, arbitrary autonomous browsing, hosted task execution,
and automatic rewriting of third-party material. No new paid connector or plan
upgrade is part of this scope.

## 3. Discovery during the work

The following is an illustrative interaction, not a test result:

> User: Make this onboarding better.
>
> AgentForge: A first-time-user walkthrough could reveal missing steps before
> we change the screens. I found a method for following one person through one
> task. Want me to use it on this flow?

After acceptance, the agent retains the original objective and applies the
selected method. It can adapt a prompt to the task without claiming the adapted
wording came from the source author.

1. At the start of a substantive task, the harness considers whether a useful
   approach is missing. The person does not need to ask for prompt discovery.
2. The agent sends a short task summary and optional bounded context to discovery.
   Local files, transcripts, private paths, and the installed-skill inventory stay
   local. Setup explains the disclosure of task-derived text and its embedding.
3. Retrieval returns at most three eligible candidates. The harness compares them
   with the current work, available capabilities, and explicit constraints.
4. The agent normally offers one approach, with an alternative only when there
   is a meaningful choice. It states the contribution, required inputs, source,
   and material limitation. Similar vocabulary alone is not a reason to suggest.
5. The person accepts, edits the proposed approach, or declines. Existing explicit
   authorization can cover its use. A decline resumes the task and suppresses the
   same approach for that task. A selection is not permission to run downloaded
   code, send messages, purchase access, or disclose additional data.
6. Accepted prompts and methods are adapted by the current harness model, without
   a separate AgentForge model call.
   Preserve the user's objective and constraints, show the proposed instruction,
   and keep its source version and adaptation distinct. Missing essential inputs
   cause one focused clarification rather than an invented requirement.
   If the adaptation changes the agreed scope, show that change before using it.
7. For a skill, inspect the pinned package and use the supported activation path.
   State any new-session requirement and carry the original task into the handoff.
   Installing files is not proof that the skill influenced the current session.

The local integration can reconsider discovery when the goal or constraint
materially changes, or when an observed failure suggests a different approach.
Ordinary follow-ups, every edit, and every model response do not trigger searches.
Allow at most one automatic search at task start and one reconsideration per task
in the pilot. Explicit requests may search again. Keep this state local and offer
at most one visible suggestion message per search. An unresolved suggestion is
never replaced with a stream of alternatives.

If existing instructions cover the approach, continue without a recommendation.
If a source is unsuitable, no result is a valid outcome. An outage must leave the
original work able to continue. Dynamic discovery through a skill is a behavior
to demonstrate in fresh Codex sessions, not a guarantee that all harnesses invoke
it on every relevant turn.

An illustrative diagnostic method could ask for three plausible explanations,
the observation that would distinguish them, and the cheapest next test. Its
value would be measured against premature commitment to one cause. The pilot
does not assume that adding this instruction improves every task.

## 4. Scout sources and review what was found

Source collection has two entry paths: the founder saves something promising,
or a bounded scout finds a candidate. Both enter the same review queue.

| Source | First-version collection | Later expansion |
| --- | --- | --- |
| GitHub | Reuse canonical repository discovery. Add allowlisted prompt collections and method documents, pinned to commits and file locations. | Expand repositories using reviewed search queries and source-quality evidence. |
| Author websites and documentation | Fetch selected public pages or feeds after checking their permitted access. Extract a candidate with its author, location, retrieval time, and content digest. | Bounded link discovery within approved domains, then more domains after review. |
| X/Twitter and other social sources | Save a post URL, author, and the founder's note. Follow a linked canonical repository or page when available. Unsupported access leaves a link-only candidate. | A supported connector after access, retention rules, budget, and deletion handling are verified. |
| Founder-supplied material | Import a URL or text the founder is authorized to provide, with optional context about where it helped. | Opt-in personal or team collections after the shared pilot proves useful. |

The first importer is an operator command and a reviewable queue file, not an
admin website. The founder can mark "worth testing" or "worked for me", add the
task category, model if known, outcome, and failure conditions, and keep the note
private. A bookmark without outcome evidence remains an endorsement, not a test.
Only a separately approved public summary enters the shared catalog.

The scout follows: discover, resolve source, extract, deduplicate, inspect rights
and content, review applicability, then publish an immutable version. Unreviewed
finds remain outside automatic suggestions. Exact copies can share a source;
adaptations and materially different variants retain their lineage and identity.

Start each manual scout run with at most 10 seed sources, 100 fetches, 2 MiB per
document, and one level of outbound links on approved domains. These are initial
engineering bounds; source-specific limits can be lower. Reject private-network
destinations and unsafe redirects, bound extraction, and execute no fetched code.
Respect access rules and rate limits. Preserve retry cursors and distinguish
failure from removal. Enable daily runs only after two manual runs prove useful
and stay within the approved usage. Existing skill refresh jobs keep their
separate operating policy.

GitHub documents conditional requests and rate-limit backoff in its
[REST API guidance](https://docs.github.com/en/rest/using-the-rest-api/best-practices-for-using-the-rest-api).
X documents [post-search endpoints](https://docs.x.com/x-api/posts/search/introduction)
with differing access requirements. These establish possible collection paths;
they do not establish that AgentForge has access or redistribution permission.
No general X crawler is a dependency for the pilot.

## 5. Evidence, rights, and freshness

Every published entry needs its source, author when available, canonical identity,
immutable version or captured content digest, last check, intended outcome,
requirements, exclusions, ordinary-task examples, and primary application kind.
Record the model or environment used in an example when known. Unknowns remain
visible. Generated examples are indexing aids and never count as independent
evidence of effectiveness.

Keep evidence as separate records rather than one quality badge:

| Evidence | What it establishes |
| --- | --- |
| Author claim | The author says it helps. Preserve the claim and attribution. |
| Curator endorsement | A named reviewer found it worth testing, with a reason. |
| Reported use | Someone reports an outcome in a stated task and environment. |
| Observed trial | A retained test records the inputs, version, model, rubric, result, and failures. |

The founder's judgment helps prioritize review. It does not automatically raise
an item above a more suitable candidate or establish that it works for everyone.
Likes, reposts, and stars may help scouting; they are not effectiveness scores.

Store and serve reusable content only when the recorded rights permit it.
Unknown rights permit a source link and allowed metadata, not a full prompt copy,
embedding of restricted text, or an adapted copy presented as original. Preserve
attribution when adapting. Treat source text as untrusted material during both
extraction and use; it cannot change application rules or authorize tools.

Recheck the pilot's published sources daily once manual operation is validated.
Publish a new version only after extraction, rights review, and applicability
review succeed. A failure retains the previous complete version with its real
check date. Confirmed withdrawal removes the item from new suggestions and
detail delivery at the next successful publication. Retain identifiers and safe
audit metadata as permitted; do not promise to retain deleted source text forever.
Effectiveness evidence stays attached to the version tested. It does not transfer
automatically to a changed prompt or model.

## 6. Retrieval and adaptation

Use hybrid lexical and semantic retrieval over purpose, expected output,
requirements, exclusions, and ordinary-language examples. Query the reviewed
v0.2 publication set. Filter known incompatibility and missing mandatory
requirements before forming the bounded shortlist. Group copies and alternate
forms of the same approach. Unknown requirements must remain explicit.

The retrieval experiment must distinguish topical similarity from task fit.
The previous [semantic-admission experiment](../engineering/discovery-pilot.md#november-2-retrieval-diagnosis)
retained semantic mismatches and removed plausible alternatives. Requiring a
semantic match alone is not an accepted suitability rule.

The cloud returns sourced metadata and match evidence. The harness decides
whether a candidate adds something to the current work and adapts the chosen
instruction. The first version does not add a cloud model call to rewrite every
query or synthesize a custom prompt. If no item fits, the harness continues the
task normally. Generic reasoning can be part of its normal work; it must not be
represented as a retrieved or tested source.

Adaptation preserves the original objective, explicit constraints, and required
inputs. Record which parts were sourced and which the agent changed. Do not
silently add a platform dependency or turn a request to analyze into a request
to act. Prompt length and sophisticated terminology are not ranking objectives.

## 7. Website and shared service

The landing page keeps the founder's tagline and the question "What are you
trying to do?". Explain that AgentForge can suggest a useful prompt, skill, or
method. Keep installation prominent. Results show the contribution to the task,
kind, source, requirements, evidence, and last check. An optional kind filter
helps exploration; knowing a kind is not required for a search.

Use "Review this approach" for prompts and methods and retain the skill's
inspection action. The review view shows permitted content and a task-aware
handoff, preserving source identity, version, and user constraints. Copying that
handoff is not activation. The website does not upload a local conversation or
claim to install into an unrelated agent. Preserve keyboard, mobile, loading,
no-match, error, and stale-response behavior. Queries stay out of URLs and
analytics by default.

The proposed shared contract is `POST /api/v2/discover`. It is a future version,
not a live endpoint. Keep `POST /api/v1/search`, its clients, and its frozen
ranking behavior unchanged during development. Define v0.2 in OpenAPI before
implementation and update website and Go-client parity fixtures together.

| Contract part | Required behavior |
| --- | --- |
| Request | `query` up to 2,048 UTF-8 bytes, optional `harness`, optional `kind` filter, and `limit` from 1 to 3. Optional `context` contains a stage, desired output, and concise explicit constraints. The complete JSON body is capped at 8 KiB and rejects unknown fields. No raw files, transcript, secrets, or local paths. |
| Candidate | Stable `capability_id`, kind, title, purpose, expected contribution, prerequisites, exclusions, source and version, evidence summaries, rights, and permitted next action. Unknown compatibility is visible. No executable commands taken from unreviewed descriptions. |
| Envelope | Ordered candidates, `matches` or `no_match`, catalog revision, ranking version, retrieval mode, and request ID. Scores are diagnostics, not probabilities of success. |
| Detail | A version-pinned read returns only reviewed content permitted for delivery. Revalidate publication and withdrawal at read time; unknown rights return source metadata only. Skills retain package review before adoption. |
| Failure | Distinguish no match, rate limiting, timeout, and unavailable service. Keep an 8-second public request deadline and no automatic interactive retry. A lexical fallback requires its own evaluated fit rule and a visible retrieval-mode label. |

Search performs no crawl, adoption, or query-history write. Both clients must
receive identical candidates and metadata for the same request, catalog revision,
and ranker. Display explanations and local adaptation can differ because the
harness has more task context; server ranking cannot depend on client identity.
Application and forwarding logs exclude raw queries and request bodies. Keep
request IDs, timing, retrieval mode, and catalog revision for diagnosis. Outcome
evidence is an explicit private pilot record, with separate approval for any
public examples.

## 8. Pixeltable and implementation boundaries

Keep Pixeltable Cloud as the catalog, computed-enrichment, embedding-index, and
query service. Reuse the existing fixed Vercel forwarding path with server-held
credentials. Browsers and distributed skills receive no Cloud credentials.

The proposed data model extends the existing implementation:

| Record | Purpose |
| --- | --- |
| Source and scout run | Acquisition method, canonical location, access and rights decisions, crawl cursor, bounded-run counts, actual check time, and errors. |
| Capability version | Immutable source version, kind, permitted content, source metadata, derived applicability fields, extraction version, and linked alternate forms. |
| Evidence | Author claims, curator notes, and trial results tied to a capability version, environment, visibility, and reviewer. Private notes are excluded from public queries and embeddings. |
| Published search document | Reviewed purpose and examples with lexical fields and the Pixeltable embedding index; publication points only to complete approved versions. |

Reuse `sources` and `skill_versions` where compatible. Keep the existing rows and
publication path readable; choose the additive schema migration after a small
fixture proves prompt, method, and skill behavior. No separate vector database or
search cluster is needed for the pilot. Preserve source metadata separately from
inferred fields, and version any enrichment model or extraction change.

The platform repository owns collection, serving, shared contracts, and the
website. The native repository owns the Go client and discovery skill. The
company repository owns this product specification and the pilot decision.
The native skill and CLI remain Apache-2.0. Original platform and company code
and documents remain proprietary. Upstream licenses remain separate.

Existing MoS Vercel and Pixeltable usage authorization applies. No new paid access
or plan change is implied. Record bounded collection and search usage; uncertain
organization-level spend must not become a claim of AgentForge-only cost.

## 9. Pilot evaluation and stop conditions

Use separate development tasks for catalog curation, prompt adaptation, and
ranking changes. Product prepares and seals a new human-reviewed v0.2 evaluation
before final tuning. The ranking author cannot inspect the held-out tasks or
judgments. Do not reuse the old held-out outcomes as development examples. Freeze
catalog, ranker, instructions, model, harness settings, and rubrics for the run.

The proposed release checks below are not achieved results:

| ID | Check |
| --- | --- |
| ED-01: source readiness | All 30 entries have required provenance, rights, applicability, exclusions, two ordinary-task examples, and a human review. Exercise changed content, duplicate forms, withdrawal, and failed fetch. Personal endorsements remain distinct from tests. |
| ED-02: relevance | On 60 new held-out requests, use 30 relevant tasks, ten per family, 15 substantive no-match tasks, and 15 trivial messages. At least 24 of 30 relevant tasks have a human-approved result in the top three. At most one no-match task receives an unsuitable visible suggestion. No trivial message causes a search or suggestion. |
| ED-03: timely discovery | At least 27 of the 30 relevant tasks trigger discovery in fresh Codex sessions without naming AgentForge. Additional disjoint fixtures cover changed goals, a useful approach already present, failure-triggered reconsideration, rejection, and the per-task search limit. Search and visible suggestion counts are separate. |
| ED-04: application | Six separately recorded accepted sessions, two per kind, preserve the task and source version, demonstrate application, and capture the result. Include one rejection and one new-session skill handoff as separate checks. Unknown activation is not a pass. |
| ED-05: outcome | Compare three conditions on 12 held-out relevant tasks, four per family: ordinary agent, agent with a generic instruction to question assumptions, and AgentForge discovery. Keep inputs, model, tools, settings, and run budget matched. A human reviewer blind to condition scores accuracy, usefulness, constraint adherence, and required rework. AgentForge must win at least eight paired tasks against each control, with no critical regression. Report ties, failures, added time, suggestions, and user interventions. This is a pilot decision threshold, not proof of general superiority. |
| ED-06: operation | Both clients pass parity, privacy, mobile, keyboard, no-match, timeout, and rate-limit checks. Two bounded scout runs retain failures and budgets. A new bounded observation of the changed path records latency, availability, freshness, and attributable usage before release; the earlier 48-hour report does not certify new routes. |

For ED-06, propose 25 hourly observations over at least 24 actual hours, with no
gap over 75 minutes and all scheduled discovery requests succeeding. Record
retry-free latency separately from a bounded, uncached development check of
100 searches at one request per second, with a proposed p95 at most two seconds.
This measures a small pilot, not production capacity. A usage report without
verifiable AgentForge attribution is unavailable, and the usage gate remains
open. Confirm resource limits before running these checks; this PRD schedules
no new monitoring or paid workload.

Choose the 12 outcome tasks and task-specific rubrics before inspecting results.
Predeclare win, tie, and critical-regression rules, and randomize the order of
outputs shown to the reviewer. Labels refer to the frozen v0.2 publication set.
Use one predeclared run per condition and retain failed runs. For this controlled
comparison, an evaluator accepts the first suggestion when present; no suggestion
or failed application still counts as that condition's result. This measures
assisted usefulness under an acceptance policy. The six separately accepted
sessions record voluntary acceptance and cannot establish broad adoption demand.

If retrieval improves but outcomes do not, investigate applicability and the
adaptation before expanding the catalog. If generic reflection matches the
benefit, reconsider whether retrieval adds enough value. A failed held-out gate
stays failed. Further development requires new cases and a separately frozen
evaluation, with earlier failures retained. Product and the founder decide
whether the evidence supports a wider pilot.

## 10. Build sequence

| Step | Owner | Deliverable |
| --- | --- | --- |
| 1. Review the scope | Product and founder | Review this v0.2 proposal, the three task families, evidence policy, and evaluation bounds. No existing acceptance gate is marked passed. |
| 2. Seed and inspect | Product and engineering | Import founder-saved links and selected GitHub or web material into the bounded queue. Review the first 30 entries and develop disjoint example tasks. |
| 3. Prove one complete journey | Engineering and design | Ship the versioned fixture-backed contract, then a prompt, a method, and a skill through contextual search, explanation, acceptance, and application in Codex and the website handoff. |
| 4. Evaluate before expanding | Product and operations | Run the sealed relevance and matched-outcome checks, inspect operating usage, and record a release or stop decision. Broader crawling follows demonstrated useful additions. |

The [work queue](../.company/work-items.json) tracks this proposal separately from
the existing pilot. A second harness, supported social APIs, wider web scouting,
personal libraries, and learned personalization are later decisions based on
observed need. Continuous source refresh maintains the index; upstream authors
continue to own and maintain their prompts and skills.
