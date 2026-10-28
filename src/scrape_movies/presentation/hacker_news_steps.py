"""@brief Text output of each "Scraping Hacker News" lecture step."""

from scrape_movies.application import use_cases
from scrape_movies.application.ports import HtmlFetcher
from scrape_movies.constants import (
    HACKER_NEWS_FIXTURE_PATH,
    HACKER_NEWS_LIVE_URL,
    HACKER_NEWS_URL,
)
from scrape_movies.infrastructure import hacker_news, http_client, soup_basics

## Where a step reads the page: the course mirror, the live site or the saved copy.
SOURCES: tuple[str, ...] = ("mirror", "live", "fixture")
_URLS: dict[str, str] = {
    "mirror": HACKER_NEWS_URL,
    "live": HACKER_NEWS_LIVE_URL,
    "fixture": str(HACKER_NEWS_FIXTURE_PATH),
}


def _fetcher(source: str) -> HtmlFetcher:
    if source == "fixture":
        return lambda path: soup_basics.load_html(HACKER_NEWS_FIXTURE_PATH)
    return http_client.fetch_html


def _numbered(lines: list[str]) -> str:
    return "\n".join(f"{number}. {line}" for number, line in enumerate(lines, 1))


def _run(source: str, step: str) -> str:
    fetch, url = _fetcher(source), _URLS[source]
    if step == "markup":
        return hacker_news.first_story_markup(fetch(url)).rstrip()
    stories = use_cases.list_stories(fetch, hacker_news.parse_stories, url)
    if step == "titles":
        return _numbered([story.title for story in stories])
    if step == "links":
        return _numbered([story.link for story in stories])
    if step == "upvotes":
        return _numbered([str(story.upvotes) for story in stories])
    top = use_cases.find_top_story(fetch, hacker_news.parse_stories, url)
    if top is None:
        return "No stories found."
    return f"{top.title}\n{top.link}\n{top.upvotes} points"


## The lecture steps by command-line name, in lecture order.
STEPS: tuple[str, ...] = ("markup", "titles", "links", "upvotes", "top")


def render_step(step: str, source: str) -> str:
    """@brief Run one lecture step.

    @param step One of STEPS.
    @param source One of SOURCES.
    @return The text the step prints.
    @throws KeyError When the step or the source is unknown.
    """
    if step not in STEPS:
        raise KeyError(step)
    return _run(source, step)
