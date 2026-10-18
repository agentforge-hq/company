---
owner: operations
status: active
reviewed: 2026-10-18
review_after: 2026-10-25
---
# Operations

Operations owns the health of the company work loop: owners, dependencies,
review dates, accepted outcomes and cost visibility.

Run `python3.11 -S scripts/company.py status` to identify overdue documents or
missing metadata. An overdue date creates a review candidate; it does not
authorize cosmetic rewrites or an automatic reset of the date.

Use `.company/work-items.json` for cross-function requests. Each item needs a
role owner, an observable acceptance criterion, evidence and dependency IDs.
Turn accepted worker handoffs into bounded work items after checking they are
necessary. Do not trigger an unbounded loop of agents responding to each other.

All substantive documents are living while active. A document can be marked
`superseded` when its replacement and rationale are clear. Preserve history in
Git; remove stale claims from the active view. Templates and source snapshots
are versioned artifacts and are not repeatedly rewritten merely to appear fresh.

The initial review cadence is a manual weekly operating review. Scheduling is a
later decision once the process produces useful accepted changes. Track stale
claims resolved, maintenance acceptance, regression outcomes and worker cost;
do not use the volume of generated documents as a success measure.

The operations worker proposes changes inside `operations/`. Changes to the
shared queue, budgets, provider access or authority require founder review.
