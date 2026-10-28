"""@brief BeautifulSoup basics from the "Parsing HTML and Making Soup" lectures."""

from pathlib import Path

from bs4 import BeautifulSoup, Tag

from scrape_movies.constants import HTML_PARSER
from scrape_movies.domain.link import Link


def load_html(path: Path) -> str:
    """@brief Read an HTML file as text.

    @param path The file to read.
    @return The content of the file.
    """
    return path.read_text(encoding="utf-8")


def make_soup(html: str) -> BeautifulSoup:
    """@brief Parse HTML text into a soup object.

    @param html The HTML document as text.
    @return The parsed document.
    """
    return BeautifulSoup(html, HTML_PARSER)


def get_title(soup: BeautifulSoup) -> str | None:
    """@brief Return the text of the `title` tag.

    @param soup The parsed document.
    @return The title text, or None when the page has no title.
    """
    if soup.title is None or soup.title.string is None:
        return None
    return str(soup.title.string)


def prettify_html(soup: BeautifulSoup) -> str:
    """@brief Return the document indented one tag per line.

    @param soup The parsed document.
    @return The indented HTML.
    """
    return str(soup.prettify())


def find_all_anchors(soup: BeautifulSoup) -> list[Link]:
    """@brief Find every anchor tag with its text and address (`find_all`).

    @param soup The parsed document.
    @return One Link per anchor that has an `href` attribute.
    """
    links: list[Link] = []
    for anchor in soup.find_all("a"):
        url = anchor.get("href")
        if isinstance(url, str):
            links.append(Link(text=str(anchor.get_text()), url=url))
    return links


def find_text_by_id(soup: BeautifulSoup, element_id: str) -> str | None:
    """@brief Return the text of the first tag with the given id (`find`).

    @param soup The parsed document.
    @param element_id The value of the `id` attribute.
    @return The text, or None when no tag has that id.
    """
    tag = soup.find(id=element_id)
    return str(tag.get_text()) if isinstance(tag, Tag) else None


def find_all_texts_by_class(
    soup: BeautifulSoup, tag_name: str, class_name: str
) -> list[str]:
    """@brief Return the text of every tag with the given class (`find_all`).

    The keyword is `class_` because `class` is a reserved word in Python.

    @param soup The parsed document.
    @param tag_name The tag to look for, for example `h3`.
    @param class_name The CSS class the tag must have.
    @return The texts in page order.
    """
    return [str(tag.get_text()) for tag in soup.find_all(tag_name, class_=class_name)]


def select_one_text(soup: BeautifulSoup, selector: str) -> str | None:
    """@brief Return the text of the first tag matching a CSS selector.

    @param soup The parsed document.
    @param selector A CSS selector such as `p a` or `#name`.
    @return The text, or None when nothing matches.
    """
    tag = soup.select_one(selector)
    return str(tag.get_text()) if tag is not None else None


def select_texts(soup: BeautifulSoup, selector: str) -> list[str]:
    """@brief Return the text of every tag matching a CSS selector.

    @param soup The parsed document.
    @param selector A CSS selector such as `.heading`.
    @return The texts in page order.
    """
    return [str(tag.get_text()) for tag in soup.select(selector)]
