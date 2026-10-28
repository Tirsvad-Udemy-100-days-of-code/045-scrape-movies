# Wiki in Three Languages

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-005 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in, autonomous mode) | Initial version | [dcef5e6] |

---

## Purpose

Decide whether the wiki is complete: every page exists in English, Danish and Bahasa Malaysia with a screenshot and a "what we gained" explanation for each lecture step.

## Deliverable

Pages under `docs/wiki/` in `en`, `da` and `ms`, a sidebar listing the three languages, README screenshot sections, and the wiki publication setup.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Every English page has a `-da` and a `-ms` page (same page set) | Met | Not met |
| 2 | Each lecture step page has a screenshot and a "What we gained" section in all three languages | Met | Not met |
| 3 | Each page starts with the language switch line and `_Sidebar.md` lists all languages | Met | Not met |
| 4 | README shows a screenshot for every lecture step | Met | Not met |
| 5 | Code blocks, commands, file names and IDs stay in English | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-004 (all screenshots exist) | Builds on it |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O4, O5; criteria 3, 4 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-14 — no hard deadline in the Business Case; dates follow the order of the milestones.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Write English wiki pages | Home, Setup, one page per lecture step (parse HTML, find and select, Hacker News, ethics, 100 movies) and Gains, each with its screenshot and a "What we gained" section. English is authoritative. | No | |
| 2 | Translate the wiki to Danish | Page for page `-da` versions of every English page, following `framework/process/wiki.md`. | No | |
| 3 | Translate the wiki to Bahasa Malaysia | Page for page `-ms` versions of every English page. The wiki process names BCP 47 codes, so `ms` is used. | No | |
| 4 | Add wiki sidebar and footer | `_Sidebar.md` and `_Footer.md` listing English, Dansk and Bahasa Melayu pages. | No | |
| 5 | Complete README screenshots and wiki links | Make sure every lecture step in README has its screenshot and a link to its wiki page in all three languages. | No | |
| 6 | Check wiki page set and publication | Add a test that compares the page sets of the three languages, and confirm the wiki publishes through the scoped workflow after merge. | No | |

---

[BC-001]: ../business-case.md
[dcef5e6]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/045-scrape-movies/commit/dcef5e6e6e7ec16162817d3ec0ce1b303e0a3a63
