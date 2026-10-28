# 🚀 scrape-movies

Day 45 of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp": web scraping with Requests and BeautifulSoup. It parses a local HTML page, scrapes the Hacker News front page and writes Empire's 100 greatest movies to `movies.txt`. It is for fellow coursists and anyone looking for a small, tested scraping example.

## 📚 Table of Contents

- [Overview](#-overview)
- [Requirements](#-requirements)
- [Setup](#-setup)
- [Run](#-run)
- [Tests](#-tests)
- [License](#-license)
- [Links](#-links)
- [Appendix: Project documents](#-appendix-project-documents)

## 🧭 Overview

| Part | What it is for |
| --- | --- |
| `src/scrape_movies/` | The code in clean-architecture layers (`domain`, `application`, `infrastructure`, `presentation`) plus `constants.py`; the lecture steps `soup_basics`, `hacker_news` and the movies scraper follow milestone by milestone |
| `tests/` | pytest tests that run offline against saved pages in `tests/fixtures/` |
| `docs/` | Project documents (business case, plan, milestones, reviews) and the wiki in English, Danish and Bahasa Malaysia |
| `Doxyfile` | Generates the API pages from the Doxygen comments in the source |

The only runtime dependencies are `requests` and `beautifulsoup4`.

## 📋 Requirements

- Python 3.13 or newer (the `venv` module comes with it).
- `requests` and `beautifulsoup4` (installed by the setup below).
- Optional: [Doxygen](https://www.doxygen.nl/) to build the API pages.

## 🛠️ Setup

Create a local virtual environment named `.venv`, update `pip`, then install the project with its test tools.

Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Linux and macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Leave out `[dev]` to install only the runtime dependencies. Personal tokens belong in a git-ignored `.env`; the project never reads it.

## ▶️ Run

Every lecture step is a command of the form `python -m scrape_movies <lecture> <step>`; without arguments the help is printed. Each step below shows the command, what it teaches and a screenshot of its output.

### Lecture: Parsing HTML and making soup

The sample page is `tests/fixtures/website.html`; the code is `src/scrape_movies/infrastructure/soup_basics.py`.

**1. Create a soup and read the title** (`BeautifulSoup(html, "html.parser")`, `soup.title.string`)

```bash
python -m scrape_movies soup title
```

![Step 1: soup title](docs/images/soup-1-title.png)

**2. Prettify** (`soup.prettify()` indents one tag per line)

```bash
python -m scrape_movies soup prettify
```

![Step 2: prettify](docs/images/soup-2-prettify.png)

**3. Find all tags** (`find_all("a")`, then `get_text()` and `get("href")` in a loop)

```bash
python -m scrape_movies soup find-all
```

![Step 3: find_all](docs/images/soup-3-find-all.png)

**4. Find by id and by class** (`find(id=...)`, `find_all("h3", class_=...)`; `class_` because `class` is a Python keyword)

```bash
python -m scrape_movies soup find
```

![Step 4: find by attribute](docs/images/soup-4-find.png)

**5. CSS selectors** (`select_one("p a")` and `select(".heading")`)

```bash
python -m scrape_movies soup select
```

![Step 5: select](docs/images/soup-5-select.png)

The screenshots are made by `python tools/make_screenshots.py`, which renders the command output as an image; no desktop is captured.

## 🧪 Tests

```bash
python -m pytest
```

The tests use saved pages and never touch the network. Lint and types: `ruff check .`, `ruff format --check .` and `mypy src tests`. API pages: `doxygen Doxyfile`.

## 📄 License

See [LICENSE](./LICENSE).

## 🔗 Links

- [Repository][repository]
- [Documentation][documentation]
- [Issue tracker][issues]

## 📎 Appendix: Project documents

| Document | What it tells you |
| --- | --- |
| [AGENTS.md][agents] | The rules AI agents follow in this repository |
| [Business Case][BC-001] | Why the project exists, its scope and success criteria |
| [Stakeholder Analysis][SA-001] | Who is involved; the stakeholder IDs used for owners and reviewers |
| [Project Plan][PP-001] | The gateways and their schedule |
| [Milestones][milestones] | One document per gateway: Go/No-Go criteria and tasks |
| [Artifact registry][registry] | Where each artifact type lives, the next version, the PO language and domain |
| [Framework README][framework-readme] | The framework this project uses |
| [Framework changelog][framework-changelog] | What changed in each framework release |

---

[repository]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/045-scrape-movies
[documentation]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/045-scrape-movies/wiki
[issues]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/045-scrape-movies/issues
[agents]: ./AGENTS.md
[BC-001]: ./docs/business-case.md
[SA-001]: ./docs/stakeholder-analysis.md
[PP-001]: ./docs/project-plan.md
[milestones]: ./docs/milestones/
[registry]: ./docs/artifact-registry.md
[framework-readme]: ./framework/README.md
[framework-changelog]: ./framework/CHANGELOG.md
