# Review of MIL-005 Python code

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-015 |
| CrossReference | [MIL-005], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Proposed | Jens Tirsvad Nielsen | S01 (AI as stand-in, autonomous mode) | Initial version | [8f6b0fc] |

---

## Artifact Under Review

- Instance reviewed: [MIL-005]
- Checklist used: [QC-PY-001]
- Scope: full review. Code reviewed: tests/unit/test_wiki.py and tools/make_screenshots.py (robots.txt step). The wiki pages are Markdown with no QC checklist; they are checked by test_wiki.py (page set, language line, screenshots, gains heading, code blocks, sidebar) and read by the stand-in reviewer.
- Language and domain: n/a (technical type)
- Language reviewer: none
- Mode: autonomous, not independent (reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | modules and functions are snake_case, classes PascalCase, constants UPPER_SNAKE. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | names state purpose; the lecture names (`find_all`, `select_one`) are kept in the helper names. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff check` and `ruff format --check` are clean with no `noqa`. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | every signature is annotated; `mypy --strict` passes, also in a venv without the third-party packages. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | N-A | no exception is raised or caught. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | no mutable defaults, no shadowed builtins. |
| 7 | Files, locks and connections are managed with context managers | Pass | `urllib.request.urlopen` is used in a `with` block in the screenshot tool. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | every public module, class and function has a Doxygen docstring saying what it does. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | N-A | no logging; the tool prints the path of each image it writes. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | no Design Class Diagram; all tasks are plain technical tasks (Needs Use Case: No). |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | tests are named for behaviour, offline and independent of order. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `mypy --strict` runs over `src`, `tests` and `tools`. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Fail | dependencies are declared with lower bounds, not pinned (see RC-009 action item); none is unused. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | each constant and format is defined once; the step texts are built in one place. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | `domain` imports nothing from other layers; `infrastructure` imports `domain` and `constants`; `presentation` composes them. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | no class hierarchy; the dataclass `Link` has one reason to change. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | the wiki test is in `tests/unit`; no source layer changed. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | all names are English lowercase with `_`, no space. |

## Overall Verdict

Go — no Mandatory criterion fails and none is Pending. Stand-in review in autonomous mode, not independent; S01 challenges it in the run summary.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Pin dependencies or accept lower bounds (open from RC-009, optional criterion 13) | S01 | 2026-11-14 |
| Ask a native Danish and Malay reader to review the translations (the translations are written by the AI) | S01 | 2026-11-14 |

---

[MIL-005]: ../../milestones/mil-005-wiki.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[8f6b0fc]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/045-scrape-movies/commit/8f6b0fc541ba26d5212d5cb8e6ef579ca14b32fe
