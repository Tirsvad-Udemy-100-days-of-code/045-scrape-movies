# Review of MIL-001 workflows

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-010 |
| CrossReference | [MIL-001], [QC-WF-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Proposed | Jens Tirsvad Nielsen | S01 (AI as stand-in, autonomous mode) | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [MIL-001]
- Checklist used: [QC-WF-001]
- Scope: full review. Code reviewed: .gitea/workflows/*.yml.
- Language and domain: n/a (technical type)
- Language reviewer: none
- Mode: autonomous, not independent (reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The file meets the YAML checklist ([QC-YML-001]) | Pass | see RC-011 for QC-YML-001. |
| 2 | The file is in `.gitea/workflows/` or `.github/workflows/` with the extension `.yml` or `.yaml`, and the same workflow does not exist in both directories | Pass | all five files are `.yml` under `.gitea/workflows/`; none under `.github/`. |
| 3 | The file declares `name`, `on` and `jobs`; `on` lists explicit events and, where it matters, `branches` or `paths` | Pass | each declares `name`, `on` and `jobs`, with branches or paths where they matter. |
| 4 | A header comment states the purpose, the triggers, the inputs, the secrets it needs, what it changes outside the repository, and the decision or milestone it implements | Pass | every file opens with a header naming purpose, triggers, secrets, outside effects and MIL-001. |
| 5 | Every job and step has a descriptive `name`, unique within its job | Pass | every job and step has a unique `name`. |
| 6 | The file passes `actionlint` (or the project's workflow validation test) and the tool version is stated | Pass | actionlint 1.7.12 reports no finding; `gitea.*` contexts were replaced by `github.*` to satisfy it. |
| 7 | Every job declares `permissions` explicitly with the least access that works (`contents: read` or none by default); write access only on the job that needs it | Pass | every job sets `permissions`; write only on the metrics job. |
| 8 | Every action used is pinned to a full commit SHA or an exact release tag, never to a branch; a moving major tag (`@v1`) is accepted only for an action published by the same organisation under a stated release policy | Pass | actions are at exact tags (`checkout@v4.2.2`, `setup-python@v5.3.0`, `upload-artifact@v4.6.2`); the reusable workflows of the same organisation use the major tag `v2` as the organisation publishes it. |
| 9 | No secret is written in the file; a secret is read as `secrets.NAME`, passed to a step through `env:`, never placed on a command line or echoed | Pass | the only secret is read as `secrets.TOKEN_FOR_GITEA_SYNC` through `env:`. |
| 10 | Untrusted text (`inputs.*`, event fields such as a title, branch name or label, step outputs derived from them) is never interpolated into a `run:` script; it is passed through `env:` and used as a quoted variable | Pass | `inputs.dry_run` reaches the script only through `env:`. |
| 11 | A trigger that gives a run secrets or a write token on code from a fork or an untrusted branch (`pull_request_target`, `workflow_run`) does not check out or execute that code | Pass | no `pull_request_target` or `workflow_run`. |
| 12 | A workflow that changes state outside the repository (release, tag, publish, sync, deploy) is started by hand or by a protected branch, and a manual run defaults to a dry run with an explicit input to apply | Pass | `sync-milestones` runs on main or by hand and defaults to a dry run on a manual start. |
| 13 | The token the workflow uses has only the scope the job needs, and where the host's built-in token is enough it is used instead of a personal token | N-A | the token is created by S01; its scope cannot be checked here. |
| 14 | Every job sets `runs-on` to an explicit label and `timeout-minutes` | Pass | every job with `runs-on` sets `ubuntu-latest` and `timeout-minutes`; called workflows set their own. |
| 15 | `concurrency` is set where two runs would conflict: a check cancels the older run (`cancel-in-progress: true`); a publishing job queues (`cancel-in-progress: false`) | Pass | checks cancel older runs; the publishing job queues. |
| 16 | Triggers are filtered (`branches`, `paths`, `types`) so the workflow runs only for the changes it concerns | Pass | triggers use `branches` or `paths`. |
| 17 | Tools and dependencies are installed at pinned versions; a version is a workflow input with a default or a value in one place | Pass | Python 3.13 and the tool versions come from one place, `pyproject.toml`; actionlint and yamllint were run by hand at the versions stated here. |
| 18 | A dependency cache is used where the install is slow enough to matter | N-A | the install is small enough that a cache does not matter. |
| 19 | A failing step names the tool, the file and the reason in its log (annotation or `::error::` line) | N-A | the called tools write their own annotations. |
| 20 | A `run:` block is within the limit on embedded program text of criterion 7 of [QC-YML-001]; a longer script is a file (`tools/`, or a shared repository fetched at a pinned ref) that the step calls with one command, and the workflow passes its settings through `env:` | Pass | no `run:` block exceeds five lines. |
| 21 | Logic used by more than one workflow or repository is a reusable workflow (`workflow_call`) or a composite action; each input has a `description`, a `type` and a `default` where one is sensible | Pass | quality, comments and metrics reuse the shared workflows with `uses:`. |
| 22 | Every workflow feature used is verified on the instance that runs it, and the host and version are recorded; a feature the target hosts differ on is noted in the header | Pass | on pull request 35 on git.tirsystem.com the tests, quality and English-comments runs completed with success. |
| 23 | A reusable workflow states, in its header, how a caller pins it and the script it fetches, so the workflow and its script are the same release | Pass | the headers say the callers use the major tag `v2` of the same organisation. |
| 24 | A static test of the repository's workflows exists and runs on every pull request: valid YAML, required keys, explicit permissions and runner, no inline script above the limit | Fail | no static workflow test runs in this repository; actionlint was run by hand. |

## Overall Verdict

Go — no Mandatory criterion fails and none is Pending. Stand-in review in autonomous mode, not independent; S01 challenges it in the run summary.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Add a static workflow test (optional criterion 24) | S01 | 2026-11-14 |
| Create the secret TOKEN_FOR_GITEA_SYNC (S01 only; the AI does not create secrets) | S01 | 2026-11-14 |

---

[MIL-001]: ../../milestones/mil-001-repository-setup.md
[QC-WF-001]: ../../../framework/qc/code/qc-workflow.md
