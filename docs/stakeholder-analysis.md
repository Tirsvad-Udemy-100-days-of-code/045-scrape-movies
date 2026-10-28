# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in, autonomous mode) | Initial version | [dcef5e6] |

---

## Purpose

Identify the people the repository serves and what each needs, so that the Business Case objectives, milestones and documents can name an owner, reviewer and audience. Method: power/interest grid with a FURPS+ mapping of each concern.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant, Product Owner, developer and reviewer | Tirsvad | HIGH | HIGH | Manage Closely | Finish the Day 45 assignment with clean, documented and reviewed work |
| S02 | Udemy coursists | Fellow participants of the course | Udemy community | LOW | HIGH | Keep Informed | Readable, runnable code with the assignment's function names and README instructions to run it |
| S03 | GitHub viewers | Visitors browsing for ideas | Public | LOW | LOW | Monitor | A clear repository description, topics and README, and no runtime dependencies beyond the need |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** decides scope, accepts the plan, reviews the summary and owns every artifact.
- **Keep Informed (S02):** cannot change the project but depends on the quality of the code and README.
- **Monitor (S03):** casual audience; served by the repository front page only.

## Primary Concerns and FURPS+ Mapping

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | Every lecture step is reproduced and its learning documented | Functionality |
| CN-002 | S01 | Work is traceable: plan, branch and pull request per milestone | Supportability |
| CN-003 | S01 | Personal tokens never enter the project | Functionality (security) |
| CN-004 | S02 | Code is readable and keeps the assignment's function names | Usability |
| CN-005 | S02 | Instructions to create the `.venv`, install and run the tests work as written | Usability |
| CN-006 | S02 | Tests run offline and are deterministic | Reliability |
| CN-007 | S03 | Repository description, topics and README explain the purpose at a glance | Usability |
| CN-008 | S03 | No runtime dependencies beyond what scraping needs | Implementation |
| CN-009 | S01, S02 | Wiki in English, Danish and Bahasa Malaysia with a screenshot per lecture step | Usability |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| C1 | Chat with S01 | At plan acceptance and at the end of the autonomous run | Plan dry run, then run summary with RC verdicts | All |
| C2 | Pull request per milestone | Once per milestone | PR description with `Closes #N` lines | All |
| C3 | README and wiki | On each merge | Instructions, screenshots, lecture learnings | MIL-001 to MIL-005 |
| C4 | Repository description and topics | Once | Metadata on the git host | MIL-001 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S03 wants no dependencies; the assignment needs `requests` and `beautifulsoup4` | S03, S01 | Keep exactly those two runtime dependencies; development tools stay in an optional `dev` group |
| S02 wants assignment names; clean code wants descriptive names | S02, S01 | Keep the assignment names as public functions and add thin, documented helpers |
| Live scraping vs deterministic tests | S02, S01 | Parsing functions take HTML text; tests use saved fixtures |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | CN-001 | O1, O2 [BC-001] |
| S01 | CN-002, CN-003 | O6 [BC-001] |
| S02 | CN-004, CN-005, CN-006 | O1, O3, O4 [BC-001] |
| S03 | CN-007, CN-008 | O4, O6 [BC-001] |
| S01, S02 | CN-009 | O5 [BC-001] |

## Sign-Off

Reviewer: S01 (decision recorded in the RC record of this document).

---

[BC-001]: ./business-case.md
[dcef5e6]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/045-scrape-movies/commit/dcef5e6e6e7ec16162817d3ec0ce1b303e0a3a63
