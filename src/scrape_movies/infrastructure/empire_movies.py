"""@brief Reading the movie titles from the Empire "100 Greatest Movies" page."""

import re

from bs4 import Tag

from scrape_movies.infrastructure.soup_basics import make_soup

## The 2020 page (the assignment's snapshot): `<h3 class="title">100) Title</h3>`.
SNAPSHOT_TITLE = "h3.title"
## The current page: `<h2><strong>100) Title (year)</strong></h2>`.
_RANKED_HEADING = re.compile(r"^\s*\d{1,3}\)")


def parse_titles(html: str) -> list[str]:
    """@brief Read the movie titles in page order.

    The assignment's snapshot is read through `h3.title`. When the page has no
    such tag, as on the current live page, the `h2` headings that start with a
    rank such as `100)` are used.

    @param html The HTML of the page.
    @return The titles in page order, each as the page shows it.
    """
    soup = make_soup(html)
    titles = [tag.get_text().strip() for tag in soup.select(SNAPSHOT_TITLE)]
    if titles:
        return titles
    headings = [tag for tag in soup.find_all("h2") if isinstance(tag, Tag)]
    return [
        text
        for text in (heading.get_text().strip() for heading in headings)
        if _RANKED_HEADING.match(text)
    ]


def first_title_markup(html: str) -> str:
    """@brief Show the markup of the first title, as seen with "Inspect".

    @param html The HTML of the page.
    @return The indented HTML of the first title tag, or "" when there is none.
    """
    soup = make_soup(html)
    tag = soup.select_one(SNAPSHOT_TITLE)
    if tag is None:
        tag = next(
            (
                heading
                for heading in soup.find_all("h2")
                if isinstance(heading, Tag)
                and _RANKED_HEADING.match(heading.get_text())
            ),
            None,
        )
    return str(tag.prettify()).rstrip() if tag is not None else ""
