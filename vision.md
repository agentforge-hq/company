---
owner: founder
status: draft
reviewed: 2026-10-18
review_after: 2026-11-01
---
# Vision

AgentForge should help people keep the instructions they give AI agents useful
as their code, tools and habits change.

The first product is a local meta-skill. The longer-term opportunity is a
maintenance system that can show whether a skill still helps, propose a smaller
or more accurate version, and verify the result before a person adopts it.

## Who benefits first

Our initial audience is developers who use multiple agent harnesses and maintain
their own skill collections. They need to see what is installed, where copies
conflict, what consumes context and which instructions no longer match their
work. This is an initial segment hypothesis; product interviews and dogfood
results can change it.

## Outcomes we want

- People can explain their active skill collection and undo a maintenance change.
- A proposed update includes source evidence and a before/after check.
- Skills remain compact while retaining the instructions that improve outcomes.
- Team maintenance becomes a repeatable process with visible ownership and cost.

An increase in skill count, document count or autonomous activity is not a
success metric by itself. We care about useful maintenance that survives
verification and reduces user effort.

## Company operating thesis

We will use the same maintenance loop on our own company. Each function has an
explicit job and a small context set. Shared work items carry handoffs. Agents
can inspect evidence and propose revisions; humans keep control of consequential
decisions. The company can evolve its strategy through versioned proposals
supported by new evidence, with a recorded explanation of what changed.

## Building in public

The local skill and its deterministic checks are public under Apache-2.0.
This company workspace is also public so people can see our organizational
design, workflow experiments, roadmap and verified results. We want the way we
work to become a useful part of how people discover and understand AgentForge.
Public visibility preserves the company's existing license. Confidential
material and credentials stay outside the public operating record.

The precise paid offering is still a hypothesis. We will test demand for team
maintenance, verified updates and recurring evaluation before building a
registry or hosted service merely because those are plausible extensions.

## What would change this vision

If controlled task tests show that maintained skills do not improve the target
jobs, or users do not value the maintenance enough to adopt it, we should reduce
or change the product. If a harness solves a problem natively, retire the
redundant mechanism. A proposal to change the target audience, business model or
company mission should name the conflicting evidence and require founder review.

The next decisions and their evidence gates are in [the roadmap](product/roadmap.md).
