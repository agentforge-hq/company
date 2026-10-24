---
owner: engineering
status: active
reviewed: 2026-10-24
review_after: 2026-10-31
---
# Comparison and managed-copy feedback

The founder reported six problems after using v0.1.0. The
[public skill patch](https://github.com/agentforge-hq/agentforge/pull/4)
addresses the inspection and protection gaps while retaining exact package
identity for cleanup.

| Request | Change and boundary |
| --- | --- |
| Explain a divergent dedupe refusal | Read-only `compare` reports file, executable-bit, link, entry and frontmatter differences. Explicit `--canonical` chooses the reference for a name group and yields preview arguments for eligible exact copies. |
| Explain byte-identical divergence | Report `byte_content_equal` separately from the fingerprint, with the differing field and executable masks. A focused permission-only test reproduces this case. The exact historical humanizer pair is no longer present, so this does not establish the cause of every reported pair. |
| Normalize harness paths | Optional normalization identifies self-path variants and counts remaining line changes. It preserves frontmatter and never changes dedupe eligibility. Normalized equality does not establish equivalent behavior. |
| Protect managed copies | Recognized plugin-cache, built-in and Claude synced paths are marked managed and excluded from cleanup previews. Archive commands reject them through aliases and symlinked parents. Other managed locations still require operator classification. |
| Skip containers during lint | Report containers under `skipped` and lint their discovered child skills. Empty containers produce no scored skill; missing paths and genuine child defects remain errors. |
| Explain lint codes | Every issue includes meaning, actionability and a next action. A reference covers every code. Managed findings point upstream and yield no local pruning suggestion. |

The real Claude synced-container check previously scored zero skills and
reported a missing root skill file. After the fix it discovers nine skills,
marks all nine managed, and reports zero operational errors. It still exits 1
for genuine child findings. That distinction prevents a misleading green result.

Three focused regressions reproduced the container and managed-path defects
before the fix. Further tests reproduced lost management classification
through a symlinked parent and accidental skipping of an existing invalid skill
entry. All pass after repair. The full suite has 105 native tests. The original
Python fingerprint and scan projection remains compatible.

An independent forward check created six fixture occurrences, then exercised
audit, collection lint, comparison and the generated cleanup preview. Only the
exact user-owned copy and alias were proposed; plugin, synced and divergent
copies were rejected. All fixture bytes, modes and links remained unchanged.
The check also prompted an explicit documentation boundary for the exact
`.claude/skills/synced/` layout.

The current patch passed all seven cross-platform CI jobs and built six native
bundles. An extracted macOS ARM64 bundle passed ten checks with an empty
executable search path, including fixture dedupe and restore. That build was
activated locally on October 24 after preserving and checking the previous
package in a full backup. Installed version, comparison help and self-lint
checks pass. The skill PR remains open for human review.

Private raw outputs remain outside Git. The evidence proves tested inspection
and protection behavior, not better routing or task quality. AF-011's fresh
session comparison and principle-consolidation fidelity checks remain open.
