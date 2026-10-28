---
owner: engineering
status: active
reviewed: 2026-10-28
review_after: 2026-11-04
---
# Discovery pilot implementation

The implementation follows the founder-approved [capability plan](../product/capability-plan.md).
The platform remains proprietary. The separate native skill and CLI remain Apache-2.0.

## Implemented behavior

[Platform revision 5f9c64a](https://github.com/agentforge-hq/platform/commit/5f9c64a)
adds source-backed profiles, bounded original author metadata, profile-versioned
immutable rows, explicit tool/setup/account constraints, and grounded shortlist
explanations. The website initially shows three results and exposes prerequisites,
unknown harness support, source excerpts, and paginated canonical browsing.
Known incompatible skills are excluded. The shared endpoint owns ranking for
both website and CLI; it does not execute or repair indexed skills.

The final complete collection has 570 canonical upstream packages from nine repositories:
385 discovered directly through GitHub and 185 through the documented skills.sh
connector. Both paths resolve to pinned upstream GitHub directories. Categories
are Engineering 265, General 211, Design 29, Research 27, Operations 23, and
Writing 15. Two oversized packages are explicitly excluded by policy. This is
bounded pilot coverage, not an index of every skill on the internet.

The final source check completed on October 28 at 22:40 UTC. Its snapshot SHA-256 is
`c7afd9e46459399ccae5fc0c3a7fdec43906c672235e8f24be43f535c0bbd268`.
The extractor is `sections-v2`. A prior rebuild hit three HTTP 429 responses
and was refused; a bounded retry produced the complete snapshot. Local repeat
publication preserved IDs; source withdrawals and failure refusal have targeted
checks. One complete package mirror is an alias of its shorter Microsoft directory; changed files and separate repositories remain distinct. New upstream content added one package, so the count stayed at 570 after removing the mirror. Cloud and observation evidence follow below.

[Native revision 4af8caf](https://github.com/agentforge-hq/agentforge/commit/4af8caf)
guides a selected result through pinned quarantine, complete package-file
verification, promotion review, archive, and restore. Its review fingerprint
binds the selected source, package bytes, destination, harness, and recovery
state. Existing destinations are preserved. Explicit custom roots cannot contain
quarantine. Preparation and promotion execute no supporting scripts.

## Verification and limits

The platform suite passed 78 Python checks against a populated local catalog,
seven gateway checks, TypeScript checking, and a production build. Native tests,
race checking, vet, and six-platform preview builds passed. The real pinned
systematic-debugging package retained all eleven file contents through temporary
promotion and archive/restore. This establishes byte preservation and recovery,
not activation or a safety endorsement. One heuristic finding concerned an
example about tracing secrets through a workflow; it was inspected explicitly.

A fresh Codex CLI 0.165.0-alpha.1.2 session read AgentForge for an ordinary Go CI
request and ran discovery without a skill-specific request. It declined
unsuitable results and continued the original task. A separate fresh trivial
turn made zero commands and zero network searches. These are smoke observations,
not the 50/25/25 reliability evaluation. The CLI's default model was not captured,
so this run cannot establish the model-versioned acceptance gate.

Claude Code 2.1.283 failed authentication before a model call because its OAuth
session could not refresh. OpenCode 1.19.3 has no stored provider credentials; Pi 1.3.0 reports no available
models. No second-harness behavior is established.

The candidate relevance corpus was frozen before final ranking and contains
100 machine-authored requests. Human review remains pending. The ranker was
frozen separately before the held-out run. The untouched local HTTP run completed all 100 cases with no request errors,
one catalog revision (`8b953588fae1f0db`) and ranking `profile-hybrid-v2`.
It found a baseline-approved skill in the top three for 37 of 50 relevant cases,
below the target of 40. It returned candidates for 18 of 25 baseline no-match
cases and five of 25 trivial queries. The larger catalog means no-match labels
need human review; these results do not establish reliable abstention. Ranking
was not tuned using these outcomes. Retrieval scoring does not establish
invocation, accepted adoption, task improvement, or superiority to competitors.

The full PRD gates remain open until their own evidence is reviewed. They are
not replaced by a successful deployment, package checksum, or unit check.

## Deployed service and operating evidence

[lordoftheskill.com](https://lordoftheskill.com) and its www name serve the
existing MoS Vercel project over HTTPS. The previous Vercel name remains
available. The full founder tagline and proprietary platform license remain.
The native [custom-domain preview](https://github.com/agentforge-hq/agentforge/releases/tag/discovery-preview-20261028.3)
is built from revision `1211e82`; its public macOS archive and embedded binary
checksums were verified before the local installation was updated. The previous
local install was archived recoverably outside skill scan roots. A new harness
session is required to refresh its skill discovery index.

The Pixeltable Cloud `app` service registers native query routes for source
pointers, immutable version payloads, and semantic candidates. These routes
associate with `sources` and `skill_versions` in the service specification and
share query builders with the composed public search. The initial custom-only
router had left these table associations empty. Actual Cloud HTTP reads now
return 200, an unauthenticated call returns 401, and the public search key still
receives 403 on refresh. The three captured website example searches retained
their result order and catalog revision. The native queries require the service
key; Vercel continues to expose only search and catalog. See the
[route definitions](https://github.com/agentforge-hq/platform/blob/8360558/app.py).

The initial 570-row Cloud publication completed before its source pointers
changed. A [current-branch refresh](https://github.com/agentforge-hq/platform/actions/runs/40711792603)
then published all 570 pointers with zero new versions and zero withdrawals.
The read key alone receives 403 on refresh. An authenticated old collector
receives 409 before any pointer write. The default-branch collector remains old
until human review and merge; the controlled pilot dispatches the current branch.

The first deployed 100-case retrieval run completed 99 cases and encountered
one 503 during the service rollout. Retrying that case after rollout succeeded.
The original capture remains unchanged, and the combined replay retains all
104 HTTP attempts and four attempt-level errors. Its result agrees with the
initial local candidate score. These diagnostic runs precede the final source
refresh and mirror correction; final-catalog results must name their own revision.

A redacted public availability, freshness-sample and synthetic-search probe
started October 28 at 15:01 UTC. The hourly observation heartbeat is active and
will report gaps and meaningful failures. The collector observes a catalog
sample, not every source. This does not establish 48 completed hours or private
refresh and spending evidence. Reported provider costs can lag and organization
usage must not be attributed wholly to AgentForge. No plan or capacity upgrade
was made.

Pull requests remain open for human review. The proprietary company and platform
licenses remain separate from Apache-2.0 in the native repository.

## Final catalog checkpoint

The final Cloud refresh published 570 canonical packages, created 317 immutable
versions for changed upstream revisions, and withdrew one redundant mirror.
The final catalog revision is `2e1cd1b997b61fed`. The ranker stayed frozen.
A complete local HTTP run against that revision returned 100 valid responses,
with the same diagnostic results: 37 of 50 relevant cases had an approved top-three
match, 18 of 25 baseline no-match cases returned candidates, and five of 25
trivial queries returned matches. Human review and the relevance target remain open.

Native [CI at revision 1211e82](https://github.com/agentforge-hq/agentforge/actions/runs/40782245598)
passed six operating-system/toolchain jobs and the bundle job. The reviewed UI
received a ship disposition; a real typed phone search revealed and focused its
results. The replacement finish reviewer followed an earlier interrupted review.
The design documenter found no new durable rules and preserved the system files.

The [native adoption PR](https://github.com/agentforge-hq/agentforge/pull/6),
[platform PR](https://github.com/agentforge-hq/platform/pull/1), and this company
proposal remain unmerged. The older native search PR #5 had already been merged
before this implementation; its historical CI is not the evidence for the new work.

The earlier diagnostic probes have a long gap. A separate continuous observation
window now starts from its actual first timestamp and requests 49 hourly samples.
The heartbeat checks that collector, records gaps, and reports the result after
48 elapsed hours. Earlier snapshots do not fill missing observations.
