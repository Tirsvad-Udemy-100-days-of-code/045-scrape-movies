"""@brief Text output of each "100 Movies to Watch" lecture step."""

from pathlib import Path

from scrape_movies.application import use_cases
from scrape_movies.application.ports import HtmlFetcher
from scrape_movies.constants import (
    EMPIRE_FIXTURE_PATH,
    EMPIRE_LIVE_URL,
    EMPIRE_WAYBACK_URL,
    MOVIES_OUTPUT_FILE,
)
from scrape_movies.infrastructure import empire_movies, http_client, soup_basics
from scrape_movies.infrastructure.movie_file import write_movies

## Where a step reads the page: the Wayback snapshot, the live site or the saved copy.
SOURCES: tuple[str, ...] = ("wayback", "live", "fixture")
_URLS: dict[str, str] = {
    "wayback": EMPIRE_WAYBACK_URL,
    "live": EMPIRE_LIVE_URL,
    "fixture": str(EMPIRE_FIXTURE_PATH),
}
## The lecture steps by command-line name, in lecture order.
STEPS: tuple[str, ...] = ("markup", "titles", "reversed", "write")
_SHOWN_LINES = 12


def _fetcher(source: str) -> HtmlFetcher:
    if source == "fixture":
        return lambda path: soup_basics.load_html(EMPIRE_FIXTURE_PATH)
    return http_client.fetch_html


def _head(lines: list[str]) -> str:
    shown = lines[:_SHOWN_LINES]
    more = len(lines) - len(shown)
    return "\n".join(shown + ([f"... and {more} more"] if more > 0 else []))


def render_step(step: str, source: str, output: Path | None = None) -> str:
    """@brief Run one lecture step.

    @param step One of STEPS.
    @param source One of SOURCES.
    @param output The file the `write` step creates; `movies.txt` when None.
    @return The text the step prints.
    @throws KeyError When the step or the source is unknown.
    """
    if step not in STEPS:
        raise KeyError(step)
    fetch, url = _fetcher(source), _URLS[source]
    if step == "markup":
        return empire_movies.first_title_markup(fetch(url))
    if step == "titles":
        titles = use_cases.scrape_movie_titles(fetch, empire_movies.parse_titles, url)
        return _head(titles)
    target = output or Path(MOVIES_OUTPUT_FILE)
    lines = use_cases.save_movie_list(
        fetch, empire_movies.parse_titles, write_movies, url, target
    )
    if step == "reversed":
        return _head(list(lines))
    return f"{_head(list(lines))}\nWrote {len(lines)} lines to {target}"
