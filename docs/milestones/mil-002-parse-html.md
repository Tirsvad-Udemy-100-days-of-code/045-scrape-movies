# Parsing HTML and Making Soup

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in, autonomous mode) | Initial version | [dcef5e6] |

---

## Purpose

Decide whether the first lecture steps (parsing HTML and making soup, finding and selecting elements) are reproduced, tested and documented.

## Deliverable

Module `soup_basics` with functions that parse `website.html` (title, prettify, find_all, find, select_one, select), the sample page as a fixture, tests, and screenshots of each step.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Every lecture operation (title, string, prettify, find_all, getText, get, find by id and class, select_one, select) has a function and a test | Met | Not met |
| 2 | Tests run offline against `tests/fixtures/website.html` | Met | Not met |
| 3 | All public functions carry Doxygen comments | Met | Not met |
| 4 | One screenshot per lecture step exists under `docs/images/` | Met | Not met |
| 5 | README has a section for this step with its screenshots | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-001 (project configuration and test scaffold) | Builds on it |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O1, O3, O5; criteria 1, 4 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-03 — no hard deadline in the Business Case; dates follow the order of the milestones.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add website.html fixture | Copy the sample page from the course archive to `tests/fixtures/website.html` and expose its path in `constants.py`. | No | |
| 2 | Implement soup creation and tag access | Functions `make_soup`, `get_title`, `prettify_html` using `html.parser`, matching the lecture on creating a soup object, `soup.title` and `prettify`. | No | |
| 3 | Implement find and select helpers | Functions for `find_all` over anchors with text and `href`, `find` by id and by class (using `class_`), and CSS selectors with `select_one` and `select`. | No | |
| 4 | Write tests for the parsing steps | pytest tests for each function against the fixture, covering text, attributes and nested selectors. | No | |
| 5 | Capture screenshots of the parsing steps | Run each step and save a terminal-output screenshot per lecture step in `docs/images/` for README and wiki. GUI-free: images are rendered from the command output, no desktop capture. | No | |
| 6 | Document the parsing steps in README | Add a README section per step with code, expected output and its screenshot. | No | |

---

[BC-001]: ../business-case.md
[dcef5e6]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/045-scrape-movies/commit/dcef5e6e6e7ec16162817d3ec0ce1b303e0a3a63
