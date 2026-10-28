"""@brief All constants of the project (URLs, limits, paths, parser name)."""

from pathlib import Path

## Root folder of the repository (two levels above this file's package folder).
PROJECT_ROOT: Path = Path(__file__).resolve().parents[2]
## Folder with the saved pages the tests and the lecture steps read.
FIXTURES_DIR: Path = PROJECT_ROOT / "tests" / "fixtures"
## The sample page from the "Parsing HTML and Making Soup" lecture.
WEBSITE_HTML_PATH: Path = FIXTURES_DIR / "website.html"

## Parser handed to BeautifulSoup; it is part of the standard library.
HTML_PARSER: str = "html.parser"

## Seconds to wait for a web server before giving up.
REQUEST_TIMEOUT_SECONDS: int = 10
## Sent with every request so a site owner can see who asks.
USER_AGENT: str = "scrape-movies/0.1 (Udemy 100 Days of Code, Day 45)"

## The course's static copy of the Hacker News front page.
HACKER_NEWS_URL: str = "https://appbrewery.github.io/news.ycombinator.com/"
## The live Hacker News front page (scrape it at most once a minute).
HACKER_NEWS_LIVE_URL: str = "https://news.ycombinator.com/news"

## Internet Archive snapshot of the Empire list, as the assignment requires.
EMPIRE_WAYBACK_URL: str = (
    "https://web.archive.org/web/20200518073855/"
    "https://www.empireonline.com/movies/features/best-movies-2/"
)
## The live Empire page, an alternative that may have changed its markup.
EMPIRE_LIVE_URL: str = "https://www.empireonline.com/movies/features/best-movies-2/"

## File the movie list is written to.
MOVIES_OUTPUT_FILE: str = "movies.txt"

## The saved copy of the course's Hacker News page, used offline.
HACKER_NEWS_FIXTURE_PATH: Path = FIXTURES_DIR / "hacker_news.html"
