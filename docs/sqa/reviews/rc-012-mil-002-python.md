# Review of MIL-002 Python code

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-012 |
| CrossReference | [MIL-002], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Proposed | Jens Tirsvad Nielsen | S01 (AI as stand-in, autonomous mode) | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [MIL-002]
- Checklist used: [QC-PY-001]
- Scope: full review. Code reviewed: soup_basics, soup_steps, cli, Link, tools/, tests/unit.
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
| 7 | Files, locks and connections are managed with context managers | N-A | no file or connection is opened except through `Path.read_text`. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | every public module, class and function has a Doxygen docstring saying what it does. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | N-A | no logging; the command-line output is the product, written with `print` in the presentation layer. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | no Design Class Diagram; all tasks are plain technical tasks (Needs Use Case: No). |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | tests are named for behaviour, offline and independent of order. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `mypy --strict` runs over `src`, `tests` and `tools`. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Fail | dependencies are declared with lower bounds, not pinned (see RC-009 action item); none is unused. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | each constant and format is defined once; the step texts are built in one place. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | `domain` imports nothing from other layers; `infrastructure` imports `domain` and `constants`; `presentation` composes them. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | no class hierarchy; the dataclass `Link` has one reason to change. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | code is in `domain`, `infrastructure` and `presentation`; tests are in `tests/unit`. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | all names are English lowercase with `_`, no space. |

## Overall Verdict

Go — no Mandatory criterion fails and none is Pending. Stand-in review in autonomous mode, not independent; S01 challenges it in the run summary.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Pin dependencies or accept lower bounds (open from RC-009, optional criterion 13) | S01 | 2026-11-14 |

---

[MIL-002]: ../../milestones/mil-002-parse-html.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
