---
owner: product
status: source-snapshot
reviewed: 2026-10-18
review_after: 2026-11-01
---

Supplied founder brief. This snapshot preserves source material; research claims remain unverified.

# Brief for an LLM: Build AgentForge v0.1 (Local-First Meta-Skill for Managing Agent Skills)

## 0. Your role
You are a senior engineer building `agentforge` v0.1. It is a portable skill made of a `SKILL.md` plus Python scripts that use only the standard library. It manages, audits, deduplicates, evaluates and fixes skills across many AI coding agents and assistants ("harnesses"). Build everything listed in §6, run the self-checks in §8, and report results. Ask before any destructive file operation on the user's machine.

## 1. Product thesis (why this exists)
Agent skills today work like World of Warcraft addons in 2006: you install them by hand, they're scattered across folders, they're hard to configure, and they break after updates. AgentForge aims to be "CurseForge for agent skills." The user installs **one** meta-skill that:
- finds the skills that are already installed, scores them, and cleans them up;
- suggests or installs missing skills safely;
- keeps skills up to date as the user's repo and habits change, always asking the user before applying a change.

The long-term moat is **continuous evaluation and maintenance** across every harness, not discovery. Discovery on its own is already crowded (skills.sh, Smithery, Glama).

## 2. What the field audits found (10 harnesses)
We asked Claude (chat), ChatGPT, Grok, Muse, Devin, Antigravity, and researched Hermes, Pi, DeepSeek Deep Code and OpenCode. Findings:
1. **Progressive disclosure is universal.** At startup a harness loads only the skill index (`name` + `description` + path). The full skill body is read when the model decides to read it. Don't reinvent this; build on the native `SKILL.md` format.
2. **Routing means the LLM matching your request against `description` text.** No harness has a separate pre-model router. Once you have more than ~20 skills, descriptions collide. Skill authors already hand-write "use X instead of Y unless Z" to work around this.
3. **Reference files are read only when `SKILL.md` explicitly points to them.** No harness reads sub-files recursively on its own.
4. **No harness can unload a single skill.** Once a skill is read, it stays in the transcript until the whole conversation is compacted. The only way to isolate a skill is a subagent: Claude Code `context: fork`, Devin `subagent: true`, OpenCode `mode: subagent`, Antigravity `invoke_subagent`, Pi `autoloadSkills`. Muse subagents inherit the parent's context, so they don't isolate anything.
5. **Discovery stops at what's installed locally.** No harness searches an open, cross-platform skill marketplace. Hermes and Muse can suggest saving a workflow as a skill.
6. **No harness fixes skills automatically.** Plugin and cloud skills are often read-only (`/mnt/skills`, plugin caches). Muse (Friday self-score job) and Grok (monthly PR check) propose edits that a human approves, and that's the experience users want. Hermes `skill_manage` can patch skills, but local edits silently override shared ones.
7. **Duplicate index bomb.** Harnesses that scan many folders (Devin, Pi, OpenCode) read `.claude/skills`, `.agents/skills`, `.cursor/skills` and their own folder all at once. Devin loaded `impeccable` 4× and `challenge-the-design` 2×. Pi is the only one that deduplicates (by realpath).
8. **Always-on rules cost tokens every turn.** `AGENTS.md`, `CLAUDE.md`, `.cursor/rules/*.mdc`, `GEMINI.md` and `global_rules.md` are loaded in full on turn 1. Step-by-step workflows stored there cost tokens on every prompt and should become lazy-loaded skills.

## 3. What others do, and lessons to adopt
- **Anthropic skill-creator v2:** create, eval, improve and benchmark modes, with positive/negative trigger tests. It's manual, local and Claude-only.
- **SkillsBench:** compares results with and without a skill ("skill lift") across harnesses. Reported lessons (not independently verified): compact skills beat long documentation, gains peak at 2–3 skills per task, and a bloated skill can make results *worse*.
- **Glama (MCP):** scans tools in a sandbox and scores their definitions (TDQS). MCP only.
- **OpenAgentSkill:** trust scores, but little real outcome data. **Vercel skills.sh:** huge distribution, no quality gate. It now has Skill Packs (`npx skills add/update`).
- **Lauren Tan's pstack (Cursor):** borrow these patterns:
  - one entry router that sends work to a few playbooks instead of a flat list of 51 skills;
  - **anti-skip rule:** copy the playbook's steps into the task list and mark any skipped step `skip: <reason>`;
  - when citing a principle, name the decision it changed;
  - `/automate-me`: turn transcripts into a personal `<user>-mode` skill;
  - **triaged drift fixes:** label each problem DOC_DRIFT (outdated skill text), HARNESS_GAP (broken helper script) or PRODUCT_BUG (the code itself is broken; never hide it by weakening the skill);
  - pass file pointers, not pasted context, to subagents.
  
  Community ports (open-pstack) track upstream commits by hand. AgentForge should automate that porting across harnesses.
- **Deephaven / SkillSV:** an LLM fixing its own skill tends to *add* rules, so skills keep growing. Pruning based on the skill's structure can cut many tokens without losing quality. → Enforce a token budget: every patch removes as much as it adds.

## 4. Product roadmap
- **v0.1 – Local meta-skill (build this now):** audit, deduplicate, sync, lint/score, safe discovery, drift proposals. No backend. Dogfood on Pixeltable skills (`pixeltable`, `review-footguns`, `pr-review-brief`, `walk-the-job`, `challenge-the-design`, `impeccable`).
- **v0.5 – Registry + CLI:** `npx agentforge init`. A nightly scrape of the top ~5k skills (skills.sh, GitHub `SKILL.md`/`.cursorrules`/`AGENTS.md`, MCP registries) with precomputed quality scores, generated trigger prompts, token cost and a permissions audit. Per-harness versions of each skill. A remote MCP bridge so read-only cloud harnesses (claude.ai, ChatGPT) can use the user's skill vault.
- **v1.0 – Team service:** a GitHub App ("Friday Skill Healer") that proposes skill patches based on PR reviews, each tested before/after with and without the change. Sandboxed microVM benchmarks. Regression tests when a new model ships, which flag skills as "obsolete / the base model already does this." Crowd-sourced health scores (reverts, Ctrl+C, user corrections).

User experience principles: no commands to memorize. Three modes:
1. **Suggest:** "I noticed X three times; skill Y (+lift, ~N tokens). Enable?"
2. **Auto-load** within a trust threshold the user sets.
3. **Weekly loadout report:** dormant skills moved to cold storage, drift diffs, deprecations.

## 5. v0.1 scope and non-goals
In scope: local files, Markdown and script skills, the 10 harness folders listed below, and drift proposals that a human approves.
Out of scope: running MCP servers, a cloud backend, sending usage data anywhere, and auto-applying skill edits.

## 6. Build spec
Install location: `~/.agents/skills/agentforge/` (the universal root).

```text
agentforge/
├── SKILL.md                # router, <1,000 tokens, <120 lines
├── config.default.json     # harness path map, token budgets, score weights
├── scripts/
│   ├── af_scanner.py       # discover skills + eager rules, token tiers, duplicates
│   ├── af_linter.py        # skill quality score (SDQS), collision matrix, script-flag check, eval generator
│   ├── af_sync.py          # vault, dedupe, freeze/thaw, transpile, overrides
│   ├── af_discover.py      # GitHub/skills.sh search → quarantine → security scan
│   └── af_drift.py         # git/PR/transcript mining, triaged drift, automate-me
└── references/
    ├── eval-rubric.md      # scoring rubric, pruning rules, trigger tests
    ├── harness-topology.md # paths, frontmatter, subagent flags per harness
    └── healing-playbooks.md# DOC_DRIFT / HARNESS_GAP / PRODUCT_BUG procedures
```

### A. SKILL.md
- Frontmatter: `name: agentforge`; `allowed-tools: Bash, Read, Write, Edit, Glob, Grep`. The description should say to use it for managing, auditing, deduplicating, evaluating, discovering, syncing or fixing skills and turn-1 rules; checking token cost; fixing trigger collisions; extracting habits from transcripts; or updating skills from PR reviews. It must also say **not** to use it for general app coding.
- Send every request to one of 5 playbooks: AUDIT, DEDUPE_AND_SYNC, DISCOVER_AND_INSTALL, HEAL_DRIFT, AUTOMATE_ME.
- Rules the agent must always follow: copy the playbook's steps into the task list verbatim (`skip: <reason>` for any skipped step); run `af_scanner.py --json` first; label every claim `[measured]` (script output) or `[inferred]` (LLM judgment); read a reference file only under its stated condition ("Read references/X.md ONLY when …").

### B. af_scanner.py
- **Skill folders (project + global):**
  - `.agents/skills`, `~/.agents/skills`, `.github/skills` (open standard/Codex/DeepSeek/Pi)
  - `.claude/skills`, `~/.claude/skills`
  - `.cursor/skills`, `~/.cursor/skills`
  - `~/.config/devin/skills`, `~/.local/share/devin/cli-next/plugins/cache`
  - `~/.gemini/config/skills`, `~/.gemini/antigravity/builtin/skills`
  - `~/.hermes/skills` (recursive)
  - `.opencode/skills`, `~/.config/opencode/skills`
  - `.deepcode/skills`, `~/.deepcode/skills`
  - `~/.omp/skills`
  - `~/workspace/custom-skills` (Muse)
  - `~/.agentforge/{vault,dormant}`
- **`--audit-rules`:** scan `AGENTS.md`, `CLAUDE.md`, `~/.claude/CLAUDE.md`, `GEMINI.md`, `.cursor/rules/*.mdc`, `~/.cursor/rules/*.mdc` and `~/.codeium/windsurf-next/memories/global_rules.md`. Report the turn-1 token cost and flag step-by-step blocks longer than 30 lines as candidates to extract into skills.
- Parse frontmatter (`name`, `description`, `when_to_use`, `allowed-tools`, `paths`). Estimate tokens as chars/4 at three tiers:
  - index cost (`name` + `description`);
  - activation cost (root body; flag BLOATED above 1,500);
  - reference cost (`references/`, `scripts/`, `examples/`).
- Detect duplicates by name and content hash across folders, and compute the duplication cost for harnesses that scan many folders.
- Output: JSON plus a Markdown table.

### C. af_linter.py: SDQS (Skill Definition Quality Score), 0–100
- Trigger specificity (25): description is 15–60 words, says "Use when…", and includes negative or disambiguation clauses.
- Compactness (25): root body ≤1,500 tokens; no inline code blocks longer than 40 lines.
- Reference hygiene (25): every reference or script file is cited with a load condition; no dead links or orphan files.
- Script/Markdown consistency (25): extract CLI flags with `ast` (argparse/sys.argv) and regex (getopts), then check that every flag documented in `SKILL.md` exists.
- `--collisions`: compare all descriptions pairwise for keyword overlap and TF-IDF cosine similarity. List risky pairs and suggest a disambiguation clause for each.
- Flag skills whose tier 2 + tier 3 cost exceeds 2,500 tokens and that have no subagent isolation.
- `--generate-eval-suite`: generate positive and near-miss negative prompts as JSON, for the host agent to grade routing accuracy.

### D. af_sync.py
- `~/.agentforge/vault/<skill>/` is the single writable source of truth.
- `--dedupe`: merge duplicates into the vault and expose **one** copy in `~/.agents/skills`. Don't copy the same skill into several folders that one harness scans, and use ignore settings where they exist (Pi `ignoredSkills`, OpenCode autoinvoke false). Always run a dry run and show a diff before moving anything.
- `--freeze/--thaw <skill>`: move a skill to or from `dormant/` so its description stops loading every session.
- `--transpile <skill> --target <harness>`: adjust the frontmatter for each harness (remove keys the target doesn't support) and wrap heavy skills in subagent isolation: `context: fork` (Claude Code), `subagent: true` (Devin), `mode: subagent` (OpenCode), or a written delegation directive for other harnesses.
- **Override layer:** for read-only plugin skills, create a writable shadow skill or override instead of editing the original.

### E. af_discover.py
- Search the GitHub API (`filename:SKILL.md`, topic `agent-skills`) and skills.sh. Download only into `~/.agentforge/quarantine/<skill>/`.
- Security gate: hidden Unicode, `curl | sh`, reads of `~/.ssh`, `.env` or the keychain, prompt-override phrases, unexpected network calls.
- Run the linter. If SDQS is below 75 or the root file is above 1,800 tokens, compact the skill (prune repetitive text, split into reference files) before promoting it to the vault, and only with the user's approval.

### F. af_drift.py
- `--mine-drift`: read `git log -n 30` (reverts and fixups), recent diffs, and `gh pr list/view` review comments if `gh` is logged in. Match recurring corrections to installed custom skills. Label each one DOC_DRIFT, HARNESS_GAP or PRODUCT_BUG. Propose a minimal diff and apply it **only after the user confirms**.
- Token budget rule: for any skill over 1,000 tokens, a patch must remove at least as many tokens as it adds.
- `--automate-me`: find tasks the user repeated 3 or more times in session logs or commits, and write a draft `SKILL.md` for approval.

## 7. Implementation rules
- Python 3.11+ standard library only (os, sys, json, re, ast, pathlib, shutil, hashlib, urllib.request, subprocess, difflib, math, collections).
- Every write operation supports `--dry-run`, shows a diff, and is reversible (back up to `~/.agentforge/backups/`).
- Never edit read-only mounts or plugin caches. Never send data off the machine except for explicit discover queries.

## 8. Acceptance criteria
1. `af_linter.py` scores agentforge itself 100/100; `SKILL.md` is under 1,000 tokens.
2. `af_scanner.py --audit-rules` and `af_linter.py --collisions` produce a full report on the host machine.
3. The audit catches known duplicates (e.g., `impeccable` ×4, `challenge-the-design` ×2) and measures the turn-1 rule cost.
4. `af_drift.py --mine-drift` on a real repo produces at least one triaged, budget-compliant proposed diff.

## 9. Launch checklist
**Phase 1 – Dogfood (days 1–3):** build → pass the self-lint → run a machine-wide audit → dedupe into the vault → run the drift healer on Pixeltable PRs.
**Phase 2 – Open source (week 2):** publish a "10-Harness Skill Audit" post with the comparison table → ship a one-command loadout health check → release pre-transpiled, deduplicated packs for popular stacks (e.g., impeccable, pstack).
**Phase 3 – Service (weeks 3–6):** a scraper with an SDQS leaderboard for the top 1,000 skills → an MCP bridge for read-only cloud harnesses → a GitHub App "Friday Skill Healer."

## 10. Caveat
The market numbers and research claims cited above (install stats, lift percentages, pruning ratios, paper IDs, model versions) came from an unverified LLM conversation. Treat them as hypotheses and don't hard-code them as facts.