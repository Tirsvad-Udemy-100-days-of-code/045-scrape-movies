"""@brief Reading titles, links and upvotes from a Hacker News page."""

from bs4 import BeautifulSoup, Tag

from scrape_movies.domain.story import Story
from scrape_movies.infrastructure.soup_basics import make_soup

STORY_ROW = "tr.athing"
TITLE_LINK = ".titleline > a"
SCORE = ".score"


def _upvotes(row: Tag) -> int:
    """@brief Read the score shown in the row after a story, 0 when it has none."""
    following = row.find_next_sibling("tr")
    score = following.select_one(SCORE) if isinstance(following, Tag) else None
    if score is None:
        return 0
    return int(score.get_text().split()[0])


def _story_rows(soup: BeautifulSoup) -> list[Tag]:
    return [row for row in soup.select(STORY_ROW) if row.select_one(TITLE_LINK)]


def parse_stories(html: str) -> list[Story]:
    """@brief Read every story of a front page.

    @param html The HTML of the page.
    @return The stories in page order.
    """
    stories: list[Story] = []
    for row in _story_rows(make_soup(html)):
        anchor = row.select_one(TITLE_LINK)
        href = anchor.get("href") if anchor is not None else None
        if anchor is not None and isinstance(href, str):
            stories.append(
                Story(title=anchor.get_text(), link=href, upvotes=_upvotes(row))
            )
    return stories


def get_titles(html: str) -> list[str]:
    """@brief Return the headlines of a front page.

    @param html The HTML of the page.
    @return The titles in page order.
    """
    return [story.title for story in parse_stories(html)]


def get_links(html: str) -> list[str]:
    """@brief Return the addresses the headlines point to.

    @param html The HTML of the page.
    @return The links in page order.
    """
    return [story.link for story in parse_stories(html)]


def get_upvotes(html: str) -> list[int]:
    """@brief Return the scores as numbers, not text such as "38 points".

    @param html The HTML of the page.
    @return The upvotes in page order.
    """
    return [story.upvotes for story in parse_stories(html)]


def first_story_markup(html: str) -> str:
    """@brief Show the markup of the first story, as seen with "Inspect" in a browser.

    @param html The HTML of the page.
    @return The indented HTML of its title row and score row, or "" when none.
    """
    rows = _story_rows(make_soup(html))
    if not rows:
        return ""
    following = rows[0].find_next_sibling("tr")
    parts = [rows[0], following] if isinstance(following, Tag) else [rows[0]]
    return "\n".join(str(part.prettify()) for part in parts)
