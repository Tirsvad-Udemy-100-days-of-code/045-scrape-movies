# Top 100 Movies Scraper

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in, autonomous mode) | Initial version | [dcef5e6] |

---

## Purpose

Decide whether the main assignment is met: the Empire list is scraped, reversed to ascending order and written to `movies.txt` as numbered lines.

## Deliverable

Module `movies` with `fetch`, `parse_titles`, `format_titles`, `write_movies`, a command-line entry `python -m scrape_movies`, a fixture of the Wayback page, tests, generated `movies.txt` and screenshots.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `movies.txt` has exactly 100 lines in the form `1) Title`, ascending | Met | Not met |
| 2 | The Wayback Machine snapshot is the default URL and the live Empire URL is the documented alternative | Met | Not met |
| 3 | Titles come from `h3` elements with class `title` | Met | Not met |
| 4 | Tests run offline against the fixture | Met | Not met |
| 5 | Running the module twice produces identical output | Met | Not met |
| 6 | One screenshot per lecture step exists under `docs/images/` | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-003 (fetch helper) | Builds on it |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O1, O2, O3, O5; criteria 1, 2, 4 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-10 — no hard deadline in the Business Case; dates follow the order of the milestones.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Fetch the Empire page | Use the shared `fetch_html` with the Wayback URL from the assignment as default and the live Empire URL as a selectable alternative, both in `constants.py`. | No | |
| 2 | Parse movie titles | `parse_titles(html)` selecting `h3.title` and returning the names in page order. | No | |
| 3 | Reverse and number the titles | `format_titles(titles)` reverses the descending page order and prefixes `1) ` to `100) ` as the assignment shows. | No | |
| 4 | Write movies.txt | `write_movies(lines, path)` writing UTF-8 with a trailing newline; a `__main__` entry runs fetch, parse, format, write. | No | |
| 5 | Add Wayback fixture and tests | Save the snapshot as `tests/fixtures/empire_best_movies.html` and test parse, format and write offline, including that 100 titles are found. | No | |
| 6 | Generate and commit movies.txt | Run the program once against the pinned snapshot and keep the produced `movies.txt` as the example result. | No | |
| 7 | Capture screenshots of the movie steps | Save screenshots of the source page, the inspected `h3.title`, the printed list and `movies.txt` in `docs/images/`. | No | |

---

[BC-001]: ../business-case.md
[dcef5e6]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/045-scrape-movies/commit/dcef5e6e6e7ec16162817d3ec0ce1b303e0a3a63
