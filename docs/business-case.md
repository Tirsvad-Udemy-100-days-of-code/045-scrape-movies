# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in, autonomous mode) | Initial version | pending |

---

## Executive Summary

Day 45 of the Udemy course "100 Days of Code: The Complete Python Pro Bootcamp" teaches web scraping with Requests and BeautifulSoup. This project turns the day's assignment into a small, readable and tested Python repository: parsing a local HTML file, scraping the Hacker News front page, and scraping Empire's "100 Greatest Movies" list into a numbered `movies.txt`. The repository is documented with a README and a three-language wiki (English, Danish, Bahasa Malaysia) that shows a screenshot per lecture step and explains what each step taught.

## Methodological and Standards Foundation

The project follows the SQA and QC framework mounted at `framework/` (plan-first gate, one reviewed artifact per step) and Larman's *Applying UML and Patterns* where a model is needed. Product quality is described with ISO/IEC 25010:2023 characteristics. Source code follows the `coding-conventions` (Python) and `clean-architecture` skills, with Doxygen comments in the source.

## Problem Statement

- The course assignment ships only a stub (`main.py`) and a sample HTML file, so every participant ends with a throw-away script that is hard to run, test or compare.
- A solution that only works against a live site breaks when the site changes; the assignment therefore pins an Internet Archive snapshot.
- Course lessons give no written record of what each step taught, which makes later review difficult.

## Business Opportunity

A clean reference repository lets the course participant revisit the lessons, lets other coursists compare solutions, and lets GitHub visitors find a small, dependency-light scraping example with tests and multi-language documentation.

## Objectives

1. O1: Deliver the three lecture exercises (parse HTML, Hacker News, 100 movies) as importable Python functions that keep the assignment's names.
2. O2: Generate `movies.txt` with the movies numbered `1) Title` in ascending order from the Wayback Machine snapshot (alternative: the live Empire URL).
3. O3: Provide tests with pytest that run offline against saved fixtures.
4. O4: Provide a README with set-up of a local `.venv`, how to run the project and the tests.
5. O5: Provide a wiki in English, Danish and Bahasa Malaysia with one screenshot and one "what we gained" explanation per lecture step.
6. O6: Set the repository description and topics, and install the shared CI workflows of `TirSystem/github-action`.

## Scope

### In Scope

- Python package under `src/`, tests under `tests/`, documents under `docs/`.
- `pyproject.toml`, `constants.py`, Python `.gitignore`, `Doxyfile`, Doxygen comments.
- Lecture steps: parsing HTML and making soup, finding and selecting elements, scraping Hacker News, scraping ethics note, 100 movies.
- README from the framework template; wiki pages in en, da and ms; screenshots per step.
- Repository description and topics on the git host; workflows for quality checks, English comments, code metrics, wiki publishing and milestone publishing.

### Out of Scope

- Scraping behind authentication or of copyrighted content beyond the course list titles.
- A graphical or web interface.
- Any use of the credentials in `.env` inside the project (personal use only, never imported, tested or committed).
- Runtime dependencies other than those the assignment needs (`requests`, `beautifulsoup4`).

## Expected Benefits

### Tangible Benefits

- A runnable, tested repository with a generated `movies.txt`.
- A wiki in three languages that documents every lecture step with screenshots.
- CI evidence (lint, type check, tests) on every pull request.

### Intangible Benefits

- Faster revision of the Day 45 material.
- A reusable pattern for later "100 Days" projects.

## Strategic Alignment

The project supports the participant's goal of completing the bootcamp with documented, reviewable work, and the framework's goal of exercising the SQA and QC process on a real, small project.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Tests pass offline | 100 % of pytest tests green | `python -m pytest` in CI and locally |
| 2 | `movies.txt` complete | 100 numbered lines, ascending | test on the generated file |
| 3 | Wiki completeness | every page exists in en, da and ms | `check-languages` style page-set comparison |
| 4 | Screenshot coverage | one screenshot per lecture step in README and each wiki language | review count |
| 5 | Runtime dependencies | only `requests` and `beautifulsoup4` | `pyproject.toml` review |
| 6 | Repository metadata | description and at least 5 topics set | host API read-back |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Live sites change markup (Hacker News, Empire) | Scrapers return nothing | Parse functions take HTML text; tests use saved fixtures; Wayback URL pinned |
| Wayback Machine unavailable | Cannot fetch the list | Fall back to the live Empire URL named in the request |
| Scraping too often loads a server | Unethical use | One request per run, a `User-Agent`, respect `robots.txt`, no loops |
| Token in `.env` leaks | Account compromise | `.env` is git-ignored, never imported; tokens are only read by shell commands for the git host API |
| Translations drift from English | Inconsistent wiki | English is authoritative; same page set checked per pull request |
| Git host repository name differs from the remote (`Tirsvad-Udemy-100_days_of_code` vs `Tirsvad-Udemy-100-days-of-code/045-scrape-movies`) | Metadata set on the wrong repository | Confirm the target before the API call (see Open Issues in the Project Plan) |

## Assumptions

- Python 3.13 or newer is installed; `venv` is available.
- The git host `git.tirsystem.com` is reachable and the token in `.env` is valid.
- S01 is Product Owner, developer and reviewer; in autonomous mode the AI acts as the stand-in reviewer and records it.
- The runners of `git.tirsystem.com` are available for the workflows.

## Constraints

- Python greater than 3.13 (3.13 or newer), `venv`, `pytest`, `pyproject.toml`, constants in `constants.py`.
- Folder structure `src/`, `tests/`, `docs/`.
- One branch and one pull request per milestone.
- No attribution lines in commit messages or pull request descriptions.
- Do not edit `framework/`.

## Cost–Benefit Assessment

| Costs | Benefits |
| --- | --- |
| Author time of S01 for plan acceptance and review of the summary | Reusable, tested reference repository |
| Runner minutes for CI | Automatic quality evidence |
| Translation effort for da and ms | Documentation readable by more coursists |

The assessment is qualitative: the project is a learning exercise with no revenue.

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Completes and reviews the assignment; owns the product |
| S02 | Reads, runs and compares the code |
| S03 | Finds the repository by description and topics and judges it by README |

## Recommendation

Proceed — the scope is small, the inputs are known, and the process is exercised end to end.

---

[SA-001]: ./stakeholder-analysis.md
