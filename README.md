---
owner: founder
status: active
reviewed: 2026-10-18
review_after: 2026-11-01
---
# AgentForge company workspace

We are building AgentForge in public. This repository contains our company
strategy, operating documents, organizational design and worker prototype.
The public skill lives separately in
[agentforge-hq/agentforge](https://github.com/agentforge-hq/agentforge).

Follow how we turn a vision into scoped work, coordinate functions, evaluate
agent proposals and simplify the organization as we learn. The roadmap,
decision records and verification results show both progress and open questions.

The working thesis is that agent skills need continuous evaluation and
maintenance as their environment changes. Our own documents should meet the
same standard: a named owner, evidence, a next review date and a clear next
decision. A document is maintained while it remains useful; obsolete content
is replaced or retired, with its history preserved in Git.

Start with [the vision](vision.md), then [the product roadmap](product/roadmap.md).
The [work queue](.company/work-items.json) connects work across functions.

| Function | Responsibility | Starting point |
| --- | --- | --- |
| Product | Problem, scope, acceptance evidence and roadmap | [Product](product/README.md) |
| Engineering | Product code, worker architecture and verification | [Engineering](engineering/README.md) |
| Design | Understandable workflows, permissions and review experience | [Design](design/README.md) |
| Marketing | Positioning, distribution and substantiated claims | [Marketing](marketing/README.md) |
| Operations | Document health, work handoffs and operating cadence | [Operations](operations/README.md) |

## Working loop

1. Select a work item and its acceptance criterion.
2. Read the relevant function brief and the smallest necessary evidence set.
3. Propose a focused change; identify obsolete material to remove.
4. Verify the claim or behavior. Record uncertainty when evidence is missing.
5. Review and merge the change, then update the work item and document review date.

Git history records revisions; [decision records](decisions/0002-build-in-public.md)
explain material choices. Use [the evidence register](evidence/claims.json) before
making public claims. Customer and competitor assumptions remain hypotheses
until checked against source evidence.

## Company workers

The initial worker is a manually triggered, proposal-only prototype. It can
prepare a scoped brief offline and, when explicitly enabled with a budget and
credentials, ask the xAI API for a bounded proposal. It cannot execute model
commands, edit the company vision, merge changes, publish marketing or grant
access. Handoffs are structured requests for another role, not an endless
conversation among bots.

```sh
python3.11 -S scripts/company.py status
python3.11 -S scripts/company.py brief --role product --task 'Review the next roadmap milestone'
python3.11 -S -m unittest discover -s tests -v
```

See [the worker design and activation steps](engineering/company-workers.md).
No paid calls or recurring jobs are enabled initially. The first commercial
service is a planned milestone, not implemented product code.

## Building in public

We share the operating model, experiments, accepted changes and lessons from
running an agent-assisted company. Marketing can use these source-linked
artifacts to explain how we work. Proposed work, accepted work and verified
outcomes remain distinguishable; a generated document alone is not a result.

Repository contents, commit history and workflow logs are public. Credentials,
personal information, customer data and confidential third-party material belong
outside this repository and its review artifacts. Provider transmission and
paid work still follow the configured approval and budget controls.

Public visibility does not change the existing [company license](LICENSE).
The separate skill is licensed under Apache-2.0.
