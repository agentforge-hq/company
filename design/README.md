---
owner: design
status: draft
reviewed: 2026-10-18
review_after: 2026-10-25
---
# Design

Design owns whether a person can understand the current skill state, decide what
to change and recover from an unwanted result.

The first experience is an agent conversation supported by local reports.
Start with [the product roadmap](../product/roadmap.md) and the actual script
outputs. A future dashboard is an option to test, not an assumed requirement.

For the audit → proposal → review → apply → verify job, investigate:

- Can the user distinguish a measured fact, a proxy score and an inference?
- Can they see exactly which paths and harnesses a change affects?
- Are divergent versions and permission losses visible before application?
- Can they recover a selected cold-storage operation without guessing?

Design proposals should quote observed product behavior, describe a specific
failure and include a small interaction example. Request engineering feasibility
and product acceptance criteria through handoffs. Prioritize clarity of the
decision and rollback over decorative interface work.

The design worker proposes changes inside `design/`. It does not claim to have
tested a flow when it has only read a document. A useful initial deliverable is
one verified maintenance journey with its confusion points and a proposed fix.
