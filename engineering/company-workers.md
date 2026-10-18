---
owner: engineering
status: draft
reviewed: 2026-10-18
review_after: 2026-10-25
---
# Function worker prototype

Each role receives the company operating instructions, vision, its own mandate
and an explicit small set of evidence documents from `.company/config.json`.
One invocation produces one proposal and optional handoff requests. Shared
work-item IDs provide continuity; full chat transcripts are not copied between
roles.

## Implemented boundary

`scripts/company.py status` checks document metadata and due dates.
`brief` builds a bounded request offline. `propose` accepts a saved provider
response for offline validation or, with `--send`, performs a single configured
xAI request after the runtime policy has been enabled. The result is a JSON
proposal and a unified diff in `.company/runs/`.

The model receives no executable tools and cannot call GitHub, run shell code,
change credentials or merge a pull request. Only owned Markdown paths can be
proposed, and every replacement must match the original content fingerprint.
Vision, access, budgets, CI configuration and worker code are outside model
write scope. A stale proposal is rejected before it is rendered.

The [xAI Responses API](https://docs.x.ai/developers/rest-api-reference/inference/responses)
is the documented provider interface. A consumer Grok desktop app is not assumed
to expose an organization-worker API. Model availability is configuration, not
a hard-coded claim. `store: false` is requested; review the provider's current
data terms before sending company content.

## Activation requires an explicit operating decision

1. Approve the exact company documents that may be sent to xAI and select a
   supported model; set `XAI_MODEL` in the runtime environment.
2. Approve a provider budget and configure provider-side spend controls.
   The prototype bounds input, output and request count, not dollars billed.
3. Configure `XAI_API_KEY` as an Actions secret or local environment
   variable. Do not put it in a file committed to Git.
4. Change `runtime.enabled` to `true` and set a positive
   `approved_monthly_usd` through a founder-reviewed change.
5. Run a bounded pilot through the manual Company worker workflow, or:
   `python3.11 -S scripts/company.py propose --role product --task 'Review milestone M1' --send`.
6. Review the proposal and diff. A human prepares the actual document change
   in a branch; record accepted handoffs in the work queue.

No recurring schedule, self-merging, email, social publishing or customer access
is enabled. The manual workflow has read-only repository permissions and uploads
review artifacts. This repository and its workflow logs are public; keep
credentials, personal data and confidential material out of requests and outputs.
A later PR-writing service needs a separately reviewed
permission model and evidence that it improves this workflow.

## Stop and observe

Stop a pilot after one request, malformed output, unsupported provider behavior,
missing evidence or a policy boundary failure. No automatic network retry is
performed. Record provider response ID, usage when returned, role, input hashes
and review outcome. Do not confuse a generated proposal with accepted work.
