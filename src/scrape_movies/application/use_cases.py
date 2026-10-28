"""@brief Use cases of the scraping exercises."""

from collections.abc import Sequence
from pathlib import Path

from scrape_movies.application.ports import (
    HtmlFetcher,
    MovieParser,
    MovieWriter,
    StoryParser,
)
from scrape_movies.domain.movie import format_titles
from scrape_movies.domain.story import Story, top_story


def list_stories(fetch: HtmlFetcher, parse: StoryParser, url: str) -> list[Story]:
    """@brief Fetch a Hacker News page and read its stories.

    @param fetch Fetches the HTML of the page.
    @param parse Reads the stories from the HTML.
    @param url The page address.
    @return The stories in page order.
    """
    return parse(fetch(url))


def find_top_story(fetch: HtmlFetcher, parse: StoryParser, url: str) -> Story | None:
    """@brief Find the story with the most upvotes on a Hacker News page.

    @param fetch Fetches the HTML of the page.
    @param parse Reads the stories from the HTML.
    @param url The page address.
    @return The top story, or None when the page has no stories.
    """
    return top_story(list_stories(fetch, parse, url))


def scrape_movie_titles(fetch: HtmlFetcher, parse: MovieParser, url: str) -> list[str]:
    """@brief Fetch the Empire page and read the titles in page order.

    @param fetch Fetches the HTML of the page.
    @param parse Reads the titles from the HTML.
    @param url The page address.
    @return The titles in page order (100 down to 1).
    """
    return parse(fetch(url))


def save_movie_list(
    fetch: HtmlFetcher,
    parse: MovieParser,
    write: MovieWriter,
    url: str,
    path: Path,
) -> Sequence[str]:
    """@brief Scrape the list and write it, ascending and numbered, to a file.

    @param fetch Fetches the HTML of the page.
    @param parse Reads the titles from the HTML.
    @param write Writes the lines to the file.
    @param url The page address.
    @param path The file to write, for example `movies.txt`.
    @return The lines that were written.
    """
    lines = format_titles(scrape_movie_titles(fetch, parse, url))
    write(lines, path)
    return lines
