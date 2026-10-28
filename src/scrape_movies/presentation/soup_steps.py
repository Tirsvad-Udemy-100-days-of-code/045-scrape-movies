"""@brief Text output of each "Parsing HTML and Making Soup" lecture step."""

from collections.abc import Callable

from bs4 import BeautifulSoup

from scrape_movies.constants import WEBSITE_HTML_PATH
from scrape_movies.infrastructure import soup_basics


def _title(soup: BeautifulSoup) -> str:
    return f"soup.title.string -> {soup_basics.get_title(soup)}"


def _prettify(soup: BeautifulSoup) -> str:
    return soup_basics.prettify_html(soup).rstrip()


def _find_all(soup: BeautifulSoup) -> str:
    return "\n".join(
        f"{link.text} -> {link.url}" for link in soup_basics.find_all_anchors(soup)
    )


def _find(soup: BeautifulSoup) -> str:
    by_id = soup_basics.find_text_by_id(soup, "name")
    by_class = soup_basics.find_all_texts_by_class(soup, "h3", "heading")
    return f'find(id="name") -> {by_id}\nfind_all("h3", class_="heading") -> {by_class}'


def _select(soup: BeautifulSoup) -> str:
    first = soup_basics.select_one_text(soup, "p a")
    every = soup_basics.select_texts(soup, ".heading")
    return f'select_one("p a") -> {first}\nselect(".heading") -> {every}'


## The lecture steps by command-line name, in lecture order.
STEPS: dict[str, Callable[[BeautifulSoup], str]] = {
    "title": _title,
    "prettify": _prettify,
    "find-all": _find_all,
    "find": _find,
    "select": _select,
}


def render_step(step: str) -> str:
    """@brief Run one lecture step against the sample page.

    @param step A key of STEPS.
    @return The text the step prints.
    @throws KeyError When the step name is unknown.
    """
    soup = soup_basics.make_soup(soup_basics.load_html(WEBSITE_HTML_PATH))
    return STEPS[step](soup)
