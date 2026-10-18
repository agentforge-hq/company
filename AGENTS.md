# Working in this company repository

The founder is Pierre Brunelle (`pierrebrunelle`). Treat the current
[vision](vision.md) and [roadmap](product/roadmap.md) as versioned working
documents. Read the function brief for the current task; do not load all
function folders into every agent's context.

- Product work: `product/README.md`.
- Engineering or worker code: `engineering/README.md`.
- Experience and design work: `design/README.md`.
- Positioning or distribution: `marketing/README.md`.
- Document health or coordination: `operations/README.md`.

Use `.company/work-items.json` to identify the owner, dependencies and observable
completion criterion. Separate measured evidence from inference. Claims from
the source brief are hypotheses unless the evidence register establishes them.
Replace or remove obsolete text when updating a document. Do not accumulate
exceptions merely to preserve previous prose.

Documents under the function folders and `vision.md` carry `owner`, `status`,
`reviewed` and `review_after` frontmatter. Update dates only after checking the
document's substance. A review date does not make a statement true.

Both the skill and company repositories are public. Write company documents and
operating experiments so people can follow and learn from the work. Keep claims
grounded in evidence. Credentials, personal information, customer data and
confidential third-party material must stay outside Git history, logs and
artifacts. Check worker inputs and outputs before publishing them.

All original company code, scripts, tests and documents are proprietary, with
all rights reserved under [LICENSE](LICENSE). Apache-2.0 applies only to the
separate skill repository. Keep this distinction explicit in public copy. Do
not add an open-source license, Apache headers or broader reuse permissions to
company material without explicit founder authorization to change its license.

Workers produce proposals within their role's declared write roots. They may
request another role's review through structured handoffs. A handoff is a new
work item that still needs assignment; it does not authorize arbitrary actions
or recursive spawning. Human review controls merges and changes to the vision,
budgets, credentials, publication, access and worker policy. A model cannot
promote its own authority by editing an instruction file.

For code changes, run the focused tests and then the standard-library suite:
`python3.11 -S -m unittest discover -s tests -v`. For document changes, run
`python3.11 -S scripts/company.py status` and check local links. Do not enable
recurring work until manual runs demonstrate its necessity and value.
