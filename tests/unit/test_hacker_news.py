from scrape_movies.constants import HACKER_NEWS_FIXTURE_PATH
from scrape_movies.domain.story import Story
from scrape_movies.infrastructure import hacker_news
from scrape_movies.infrastructure.soup_basics import load_html

PAGE = """
<table><tr class="athing" id="1"><td><span class="titleline">
<a href="https://example.com/one">One</a></span></td></tr>
<tr><td><span class="score">12 points</span></td></tr>
<tr class="athing" id="2"><td><span class="titleline">
<a href="https://example.com/job">A job ad</a></span></td></tr>
<tr><td>no score here</td></tr></table>
"""


def _fixture() -> str:
    return load_html(HACKER_NEWS_FIXTURE_PATH)


def test_parse_stories_when_page_has_score_reads_integer() -> None:
    assert hacker_news.parse_stories(PAGE)[0] == Story(
        "One", "https://example.com/one", 12
    )


def test_parse_stories_when_story_has_no_score_uses_zero() -> None:
    assert hacker_news.parse_stories(PAGE)[1].upvotes == 0


def test_parse_stories_when_page_has_no_stories_returns_empty() -> None:
    assert hacker_news.parse_stories("<p>nothing</p>") == []


def test_parse_stories_when_fixture_returns_thirty_stories() -> None:
    assert len(hacker_news.parse_stories(_fixture())) == 30


def test_get_titles_when_fixture_starts_with_first_headline() -> None:
    assert hacker_news.get_titles(_fixture())[0] == "Joan Feynman 1927-2020"


def test_get_links_when_fixture_returns_one_address_per_story() -> None:
    links = hacker_news.get_links(_fixture())
    assert len(links) == 30
    assert links[0].startswith("https://www.aps.org/")


def test_get_upvotes_when_fixture_returns_integers() -> None:
    upvotes = hacker_news.get_upvotes(_fixture())
    assert upvotes[:2] == [38, 205]
    assert all(isinstance(points, int) for points in upvotes)


def test_first_story_markup_when_page_has_story_shows_title_row() -> None:
    assert 'class="titleline"' in hacker_news.first_story_markup(PAGE)


def test_first_story_markup_when_page_has_no_story_returns_empty() -> None:
    assert hacker_news.first_story_markup("<p>x</p>") == ""
