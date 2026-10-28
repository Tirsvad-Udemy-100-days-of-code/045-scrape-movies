# Scraping Hacker News

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in, autonomous mode) | Initial version | [dcef5e6] |

---

## Purpose

Decide whether scraping a live site is reproduced safely: Hacker News titles, links and upvotes are extracted, the top story found, and the ethics of scraping documented.

## Deliverable

Module `hacker_news` with fetch and parse functions, the saved front page as a fixture, tests, ethics note and screenshots of each step.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Parsing returns titles, links and integer upvotes from the fixture | Met | Not met |
| 2 | The article with the most upvotes is found with `max` | Met | Not met |
| 3 | Fetching sends one request with a `User-Agent` and a timeout; no loops of requests | Met | Not met |
| 4 | Tests run offline | Met | Not met |
| 5 | Ethics and legality notes from the lecture are in README and wiki source text | Met | Not met |
| 6 | One screenshot per lecture step exists under `docs/images/` | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-002 (soup helpers) | Builds on it |

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

2026-11-06 — no hard deadline in the Business Case; dates follow the order of the milestones.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add fetch function for Hacker News | `fetch_html(url)` using `requests` with a timeout, `User-Agent` and status check; URLs live in `constants.py`. The course mirror and the live site are both named. | No | |
| 2 | Add Hacker News fixture | Save the course mirror page `appbrewery.github.io/news.ycombinator.com` as `tests/fixtures/hacker_news.html` so tests never touch the network. | No | |
| 3 | Extract titles, links and upvotes | Functions returning lists of titles, links and integer scores from the title links and score spans, as in the lecture. | No | |
| 4 | Find the top story by upvotes | `top_story()` using `max` over the scraped rows and a test for ties and an empty page. | No | |
| 5 | Write tests for Hacker News parsing | pytest tests against the fixture, with `requests` patched for fetch tests. | No | |
| 6 | Document ethics and legality of scraping | Summarise the lecture: robots.txt, copyrighted and authenticated data, commercial risk, request frequency. Written in the README in our own words. | No | |
| 7 | Capture screenshots of the Hacker News steps | Save a screenshot per lecture step (page, inspected markup, extracted output, top story) in `docs/images/`. The live pages are opened in the built-in browser pane, not the host desktop. | No | |

---

[BC-001]: ../business-case.md
[dcef5e6]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/045-scrape-movies/commit/dcef5e6e6e7ec16162817d3ec0ce1b303e0a3a63
