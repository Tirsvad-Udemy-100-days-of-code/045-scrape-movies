# Repository Setup and Tooling

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in, autonomous mode) | Initial version | pending |

---

## Purpose

Decide whether the repository is ready to hold code: metadata, project configuration, documentation entry points and CI are in place so the lecture milestones can build on them.

## Deliverable

Repository with description and topics, `pyproject.toml`, `.gitignore`, `Doxyfile`, README, `src/` and `tests/` skeleton with `constants.py` and a passing smoke test, and installed workflows.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `python -m pytest` passes in a fresh `.venv` created as the README says | Met | Not met |
| 2 | `pyproject.toml` requires Python 3.13 or newer and lists only `requests` and `beautifulsoup4` as runtime dependencies | Met | Not met |
| 3 | Repository description and at least five topics are read back from the host | Met | Not met |
| 4 | README follows the framework template and passes `check-readme.sh` | Met | Not met |
| 5 | Workflows from `TirSystem/github-action` are installed and parse | Met | Not met |
| 6 | `.env` is git-ignored and nothing in the project reads it | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| None (first milestone) | Builds on it |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O3, O4, O6; criteria 1, 5, 6 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-30 — no hard deadline in the Business Case; dates follow the order of the milestones.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Set repository description and topics | Set a description and topics (python, web-scraping, beautifulsoup, requests, 100-days-of-code, udemy, pytest) through the Gitea API using the token from `.env` read by the shell only. Confirm the target repository first because the requested name differs from the origin remote. | No | |
| 2 | Add pyproject.toml, .gitignore and constants.py | Create `pyproject.toml` (Python >=3.13, `requests`, `beautifulsoup4`, optional `dev` group with pytest, ruff, mypy), a Python `.gitignore` that also ignores `.env`, and `src/scrape_movies/constants.py` for all constants. | No | |
| 3 | Add Doxyfile and Doxygen comment convention | Add a `Doxyfile` that reads `src/` and a short note on the Doxygen comment style used in the source so S02 can generate the API pages. | No | |
| 4 | Write README from the framework template | Start `README.md` from `framework/templates/README-template.md` with the `.venv` creation, `python -m pip install --upgrade pip`, install, run and test instructions. Lecture sections and screenshots are added by later milestones. | No | |
| 5 | Install workflows from TirSystem/github-action | Install quality checks, English comments, code metrics and milestone publishing as thin callers under `.gitea/workflows/`. Wiki publishing is scoped and needs no file; verify against the adoption rules and record the decision. | No | |
| 6 | Add test scaffold and smoke test | Add `tests/` with a pytest configuration in `pyproject.toml` and one smoke test that imports the package, so CI has a green baseline. | No | |
| 7 | Install git hooks and plan gate | Run `install-git-hooks.sh --enable-plan-gate` and record the AI prompts of the session in `docs/ai-prompts/session-001/` as the prompt-log process says. | No | |

---

[BC-001]: ../business-case.md
