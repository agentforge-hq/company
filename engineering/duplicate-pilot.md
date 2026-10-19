---
owner: engineering
status: draft
reviewed: 2026-10-18
review_after: 2026-10-25
---
# One duplicate, fresh-session comparison

AF-011 tests whether one fewer humanizer entry improves or preserves useful
work. The [raw cases](../evidence/duplicate-pilot/cases.json) are synthetic,
reproducible inputs. No new-session outcomes have been measured, and no setting
has been changed.

## Setup

1. Keep this rubric and previous audit conclusions out of evaluated chats.
   Give each fresh chat only its case prompt, raw input and fixture location.
   Use the same model, effort, available tools and project instructions in both
   conditions. Run each case in its own fresh chat; do not reuse this chat.
2. Prepare an isolated workspace outside harness discovery roots. Under
   `fixture-skills`, create `report-one/SKILL.md` and `report-two/SKILL.md`
   with identical contents:

   ```markdown
   ---
   name: report-fixture
   description: Summarize supplied project status notes when preparing a weekly report.
   ---
   Verify the supplied facts and report missing inputs.
   ```

   Create no executable
   files. Preserve identical fixture bytes and a clean output directory for
   each condition. The duplicate names are intentional test data.
3. Capture a baseline catalog showing both humanizer paths. Record the complete
   selected paths and available catalog, model settings, raw outputs, file
   changes and tool use. Count inspected instruction bytes separately from
   claimed prompt tokens; do not infer actual token usage from the file proxy.
4. Recheck that the universal and legacy humanizer contents still match. The
   prior audit found an executable-mode difference in a helper; strict
   fingerprints therefore correctly reported divergence. This pilot retains
   all files and does not treat them as safely deletable identical trees.
5. After the baseline, back up Codex configuration and verify the currently
   documented per-path disable setting. Disable only the legacy Codex
   humanizer path, retaining the universal copy and every file. Restart the
   harness, then verify one fewer humanizer catalog entry before running the
   same cases. Do not apply this setting based solely on an old documentation
   snapshot or a filesystem inventory.

## Evaluator rubric

| Case | Selection and outcome to inspect |
| --- | --- |
| Rewrite | An appropriate writing skill is selected. Preserve the date, time zone, 12 invited, 7 confirmed, proposed/unapproved $19 monthly price and no-upload claim. Add no facts. |
| Audit | AgentForge reports two same-name identical fixture copies, distinguishes filesystem exposure from observed loading, and changes no files or settings. |
| Create skill | Skill creation guidance is used, the requested skill validates, and it does not introduce publishing or unrelated audit work. |
| Arithmetic | The answer is 391, without loading an unrelated workflow. |

Record actual selected paths; do not count a predicted lexical match as model
selection. A missing task result, altered fact, new unauthorized change or
unexplained loss of necessary capability is a regression. If it occurs, restore
the saved configuration, restart and verify the baseline catalog. If unrelated
settings changed meanwhile, revert only the pilot edit rather than overwriting
those changes with the full backup.

Retain the treatment only after catalog and outcome checks pass. Report a
single comparison as preliminary evidence; repeat with held-out tasks before
claiming general routing or performance improvement. Keep raw machine paths
and any sensitive session content outside the public repository. Publish a
redacted result summary with evidence references when results exist.
