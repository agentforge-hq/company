---
owner: engineering
status: active
reviewed: 2026-10-18
review_after: 2026-10-25
---
# Devin cleanup evidence and product changes

The founder supplied a Devin cleanup report. The saved audit files and cold
storage ledger were also available locally. We inspected them and reran the
same four-root inventory. Redacted counts and source-file checksums are in
[the evidence record](../evidence/devin-cleanup.json). Raw paths, transcripts
and archive contents remain outside the public repository.

| Check | Before | After |
| --- | --- | --- |
| Filesystem skill occurrences | 81 | 38 |
| Unique physical skills | 76 | 36 |
| Index token estimate | 8,556 | 5,260 |
| Duplicate name groups | 4 | 3 |
| Audit read errors | 0 | 0 |

The ledger contains 42 cold-storage transactions and 3 dedupe transactions.
All 45 pass a restore preview, including fingerprint and destination checks.
No actual field restore was applied. A current four-root scan reproduces the
saved after counts.

These were custom-root scans, so they did not profile eager rules. The counts
are filesystem occurrences and byte-based estimates, not an observed Devin
startup catalog or measured prompt-token savings. The field report's 24-principle
merge and warm/cold judgments have not been tested on held-out tasks. They do
not establish that skills unused in one session are obsolete.

## Feedback decisions

| Feedback | Evidence and response |
| --- | --- |
| Normalize mechanical divergence | Keep strict fingerprints. Harness paths and frontmatter can affect execution and permissions. A shared version does not make packages interchangeable. File-level difference summaries remain a later M2 candidate. |
| Bulk cleanup | The CLI previously kept only the last repeated `--skill`. The fix accepts a list, validates all members, and uses one existing transaction. Persistent plan files remain deferred. |
| Automatic roots | Default discovery already exists. It did miss Devin CLI's native global root. The fix adds the documented platform-specific directory and makes default discovery clear in help. |
| Descriptions and token fields | Both saved reports already contain descriptions and nonzero body estimates for every entry. The field is `tokens_estimate`, not `tokens`. Add a JSON field reference and help pointer. |
| Local adoption | No registry registration is needed for a discovered skill directory. A separate adoption command remains deferred. Existing explicit exports require an absent destination and report metadata losses. |
| Archive inspection | Manifests and restore previews already provide an integrity read path. Document their locations. A history command remains a later usability candidate. |
| Multiple dedupe copies | Repeated `--duplicate` already works with one explicit canonical source. Add a visible help example. Do not automatically choose the canonical copy. |
| Home scope | Document `--project "$HOME"` and the inclusion of configured home roots. Custom `--root` inventories exclude configured rule scanning. |
| Path-aware porting | Current exports filter metadata but do not rewrite body paths. Keep target-specific variants until a tested transformation preserves their behavior. |

The root fix follows
[Devin CLI's documented locations](https://docs.devin.ai/cli/extensibility/skills/creating-skills).
Cloud and CLI skill semantics differ. Keep that distinction explicit when
adding future permission or isolation mappings.

## Verification and next evidence

Three new regressions fail against the previous public skill and pass after
the fix. They cover native global-root discovery, batch preview/apply/restore,
and rejection of an invalid batch member before any valid member moves.
The [public skill patch](https://github.com/agentforge-hq/agentforge/pull/3)
passes 89 native tests, local race checks, vet, structural self-lint, metadata
validation and all seven cross-platform CI jobs. Eight extracted native-package
checks pass with an empty executable search path, including a batch archive
and actual restore on isolated fixtures. The patch is installed locally with
the previous installation backed up outside discovery roots.

AF-013 tracks review of that patch. AF-003 and AF-011 still need controlled
task outcomes. Before claiming that the field consolidation preserved useful
behavior, compare representative principle-trigger tasks and inspect the fresh
harness catalog. Test actual restore on an isolated fixture, not by disrupting
the founder's current skill selection. Do not introduce automatic cold storage
from a single session's usage.
