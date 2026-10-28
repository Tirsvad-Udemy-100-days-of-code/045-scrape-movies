from collections.abc import Sequence
from pathlib import Path

from scrape_movies.application import use_cases
from scrape_movies.domain.story import Story


def _fetch(url: str) -> str:
    return f"html of {url}"


def _parse(html: str) -> list[Story]:
    return [Story(html, "/x", 3), Story("best", "/y", 99)]


def test_list_stories_when_called_passes_page_through_parser() -> None:
    stories = use_cases.list_stories(_fetch, _parse, "http://x")
    assert stories[0].title == "html of http://x"


def test_find_top_story_when_stories_exist_returns_highest() -> None:
    top = use_cases.find_top_story(_fetch, _parse, "http://x")
    assert top == Story("best", "/y", 99)


def test_find_top_story_when_page_is_empty_returns_none() -> None:
    assert use_cases.find_top_story(_fetch, lambda html: [], "http://x") is None


def test_save_movie_list_when_titles_are_descending_writes_ascending() -> None:
    written: list[tuple[list[str], Path]] = []

    def write(lines: Sequence[str], path: Path) -> None:
        written.append((list(lines), path))

    lines = use_cases.save_movie_list(
        _fetch, lambda html: ["2) Two", "1) One"], write, "http://x", Path("m.txt")
    )
    assert list(lines) == ["1) One", "2) Two"]
    assert written == [(["1) One", "2) Two"], Path("m.txt"))]


def test_scrape_movie_titles_when_called_keeps_page_order() -> None:
    titles = use_cases.scrape_movie_titles(_fetch, lambda html: ["b", "a"], "http://x")
    assert titles == ["b", "a"]
