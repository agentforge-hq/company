---
owner: operations
status: active
reviewed: 2026-10-18
review_after: 2026-11-01
---
# Sources and evidence rules

The [claim register](claims.json) records whether a statement is measured,
documented, inferred or an unverified hypothesis. Add a source and check date
when promoting a claim; a confident model answer is not independent evidence.

Primary technical sources checked for this setup:

- [GitHub organization creation](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/creating-a-new-organization-from-scratch)
- [GitHub repository transfers](https://docs.github.com/en/repositories/creating-and-managing-repositories/transferring-a-repository)
- [xAI Responses API](https://docs.x.ai/developers/rest-api-reference/inference/responses)
- [xAI function calling](https://docs.x.ai/developers/tools/function-calling)
- [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)

The supplied product brief explicitly labels market numbers, claimed routing
limits, lift percentages, model versions and some harness behavior as unverified.
Preserve that uncertainty when deriving roadmap work. Verify the specific
installed harness/version before changing a path or isolation mapping.

Local test results establish the tested invariants in their fixtures. They do
not establish every external harness behavior, commercial demand or benchmark
lift. Public reports should provide a reproduction and redact machine-specific
inventories, private paths and company information.
