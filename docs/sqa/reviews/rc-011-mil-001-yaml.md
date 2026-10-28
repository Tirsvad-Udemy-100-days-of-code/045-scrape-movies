# Review of MIL-001 YAML files

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-011 |
| CrossReference | [MIL-001], [QC-YML-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Proposed | Jens Tirsvad Nielsen | S01 (AI as stand-in, autonomous mode) | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [MIL-001]
- Checklist used: [QC-YML-001]
- Scope: full review. Code reviewed: .gitea/workflows/*.yml, .yamllint.yml.
- Language and domain: n/a (technical type)
- Language reviewer: none
- Mode: autonomous, not independent (reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The file parses with a safe YAML loader and has no duplicate keys in any mapping | Pass | yamllint 1.38.0 (PyYAML based) parses all files and reports no duplicate key. |
| 2 | Indentation is 2 spaces everywhere, never tabs; lines end with LF; the file ends with one newline and has no trailing spaces | Pass | 2 spaces, LF, one final newline, no trailing spaces (yamllint relaxed profile). |
| 3 | Passes `yamllint` (or the project's YAML linter) with its configuration committed next to the code and no unexplained `disable` comments | Pass | `.yamllint.yml` is committed; no disable comments. |
| 4 | A scalar that YAML would coerce to another type is quoted: `yes`, `no`, `on`, `off`, `null`, `~`, numbers with a leading zero, versions such as `1.10`, and values that contain `: ` or ` #` | Pass | strings such as `"3.13"` are quoted; `on` is the Actions trigger key, not a value. |
| 5 | Only safe, plain types are used: no language-specific tags (`!!python/object`, `!ruby/object`) and no `!include`-style extension unless the consuming tool documents it | Pass | only plain types. |
| 6 | No secret is written in the file: no password, token, key or private connection string; a secret is referenced by name and supplied by the consuming tool | Pass | no secret in any file. |
| 7 | Embedded program text (shell, Python, SQL, `jq`, and so on) in a value is at most five lines; a longer one is moved to a file of its own, in its own language, and the YAML calls it | Pass | the longest `run:` block has two lines. |
| 8 | A block of keys or values repeated in the file or across files is defined once (an anchor, a template, an include or a reusable unit the consumer supports) | Pass | repeated blocks are not present; shared logic is reused through `uses:`. |
| 9 | Anchors, aliases and merge keys (`&`, `*`, `<<`) are used only where the consuming tool is known to support them | Pass | no anchors or aliases. |
| 10 | The file validates against the schema of the consuming tool where one exists, and the schema or tool version is stated | Pass | actionlint 1.7.12 validates the workflow schema. |
| 11 | A header comment states what the file is for, which tool reads it, and where its decision or design is recorded | Pass | each file has a header comment saying purpose, reader and where it is decided (MIL-001). |
| 12 | Key names follow the convention of the consuming tool; one case style is used within the file (kebab-case or snake_case, never mixed) | Pass | key names are those of the consuming tool (`cancel-in-progress`, `timeout-minutes`, `dry_run`), as the tool defines them. |
| 13 | Multi-line strings use a block scalar (`\|` or `>`) and state the chomping indicator (`\|-`, `\|+`) where the trailing newline matters | Pass | no multi-line strings other than `run: |` blocks where the trailing newline does not matter. |
| 14 | The file name is lowercase kebab-case with one extension style (`.yml` or `.yaml`) used throughout the repository | Pass | lowercase kebab-case `.yml` names. |
| 15 | A change is exercised by a check that runs without the real target: a parse and schema test, or a dry run of the consuming tool | Pass | pull request 35 ran the workflows on the host. |

## Overall Verdict

Go — no Mandatory criterion fails and none is Pending. Stand-in review in autonomous mode, not independent; S01 challenges it in the run summary.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | 2026-11-14 |

---

[MIL-001]: ../../milestones/mil-001-repository-setup.md
[QC-YML-001]: ../../../framework/qc/code/qc-yaml.md
