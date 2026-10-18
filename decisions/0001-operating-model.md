---
owner: founder
status: superseded
reviewed: 2026-10-18
review_after: 2026-11-01
---
# 0001: Separate the public skill from private company operations

The visibility boundary in this initial decision is superseded by
[0002: Build the company in public](0002-build-in-public.md). The new decision
retains the separate repositories, function roles and bounded worker model.

## Context

The founder requested a public skill, a private company repository organized by
function, living documents and a path toward cooperating Grok-powered workers.
The exact GitHub names `agentforge` and `agent-forge` were already registered.
The founder authorized choosing an alternative and selected Apache-2.0 for the
public skill. The initial alternative is `agentforge-hq`.

## Initial operating decision

- Publish the generated local skill in `agentforge-hq/agentforge`.
- Keep company documents and proprietary code in `agentforge-hq/company`.
- Start with five function mandates and an explicit shared queue.
- Use Git history and dated evidence to revise active documents.
- Prepare proposal-only, manually triggered xAI workers. Enable paid or
  recurring work after a reviewed budget, data scope and useful pilot.

## Tradeoff

Explicit review is slower than allowing agents to rewrite and merge everything.
It lets us distinguish useful maintenance from activity and retain a clear
reason for strategy changes. The first worker has no direct tool execution or
canonical-document write capability. A more capable service can be considered
when manual evidence identifies the binding constraint.

## Revisit when

Revisit the worker permission model after accepted manual proposals establish a
recurring job, or if the review process itself blocks demonstrated user value.
Record the evidence and a bounded change rather than granting general authority.
