from bs4 import BeautifulSoup

from scrape_movies.constants import WEBSITE_HTML_PATH
from scrape_movies.domain.link import Link
from scrape_movies.infrastructure import soup_basics


def _soup() -> BeautifulSoup:
    return soup_basics.make_soup(soup_basics.load_html(WEBSITE_HTML_PATH))


def test_get_title_when_page_has_title_returns_text() -> None:
    assert soup_basics.get_title(_soup()) == "Angela's Personal Site"


def test_get_title_when_page_has_no_title_returns_none() -> None:
    assert soup_basics.get_title(soup_basics.make_soup("<p>x</p>")) is None


def test_prettify_html_when_called_puts_tags_on_own_lines() -> None:
    pretty = soup_basics.prettify_html(soup_basics.make_soup("<p><b>x</b></p>"))
    assert pretty.splitlines()[:3] == ["<p>", " <b>", "  x"]


def test_find_all_anchors_when_page_has_links_returns_text_and_url() -> None:
    links = soup_basics.find_all_anchors(_soup())
    assert links[0] == Link("The App Brewery", "https://www.appbrewery.co/")
    assert [link.text for link in links] == [
        "The App Brewery",
        "My Hobbies",
        "Contact Me",
    ]


def test_find_all_anchors_when_anchor_has_no_href_skips_it() -> None:
    soup = soup_basics.make_soup("<a>no link</a><a href='/x'>x</a>")
    assert soup_basics.find_all_anchors(soup) == [Link("x", "/x")]


def test_find_text_by_id_when_id_exists_returns_text() -> None:
    assert soup_basics.find_text_by_id(_soup(), "name") == "Angela Yu"


def test_find_text_by_id_when_id_is_missing_returns_none() -> None:
    assert soup_basics.find_text_by_id(_soup(), "nobody") is None


def test_find_all_texts_by_class_when_class_matches_returns_texts() -> None:
    texts = soup_basics.find_all_texts_by_class(_soup(), "h3", "heading")
    assert texts == ["Books and Teaching", "Other Pages"]


def test_select_one_text_when_nested_selector_returns_first_match() -> None:
    assert soup_basics.select_one_text(_soup(), "p a") == "The App Brewery"


def test_select_one_text_when_nothing_matches_returns_none() -> None:
    assert soup_basics.select_one_text(_soup(), "table") is None


def test_select_texts_when_class_selector_returns_all_matches() -> None:
    assert soup_basics.select_texts(_soup(), ".heading") == [
        "Books and Teaching",
        "Other Pages",
    ]
