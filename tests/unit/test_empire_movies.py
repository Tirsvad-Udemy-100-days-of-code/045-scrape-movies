from scrape_movies.constants import EMPIRE_FIXTURE_PATH
from scrape_movies.infrastructure import empire_movies
from scrape_movies.infrastructure.soup_basics import load_html

SNAPSHOT_LAYOUT = """
<h3 class="title">4) The Shawshank Redemption</h3>
<h3 class="title">3) The Dark Knight</h3>
<h3 class="other">not a title</h3>
<h3 class="title">2) The Empire Strikes Back</h3>
"""


def test_parse_titles_when_snapshot_layout_reads_h3_title_in_page_order() -> None:
    assert empire_movies.parse_titles(SNAPSHOT_LAYOUT) == [
        "4) The Shawshank Redemption",
        "3) The Dark Knight",
        "2) The Empire Strikes Back",
    ]


def test_parse_titles_when_live_layout_reads_ranked_h2_headings() -> None:
    titles = empire_movies.parse_titles(load_html(EMPIRE_FIXTURE_PATH))
    assert len(titles) == 100
    assert titles[0].startswith("100) ")
    assert titles[-1].startswith("1) ")


def test_parse_titles_when_h2_has_no_rank_ignores_it() -> None:
    assert empire_movies.parse_titles("<h2>Jump to</h2><h2>2) Two</h2>") == ["2) Two"]


def test_parse_titles_when_page_has_no_titles_returns_empty() -> None:
    assert empire_movies.parse_titles("<p>nothing</p>") == []


def test_first_title_markup_when_snapshot_layout_shows_h3() -> None:
    assert empire_movies.first_title_markup(SNAPSHOT_LAYOUT).startswith(
        '<h3 class="title">'
    )


def test_first_title_markup_when_live_layout_shows_h2() -> None:
    markup = empire_movies.first_title_markup(load_html(EMPIRE_FIXTURE_PATH))
    assert markup.startswith("<h2>")


def test_first_title_markup_when_nothing_found_returns_empty() -> None:
    assert empire_movies.first_title_markup("<p>x</p>") == ""
