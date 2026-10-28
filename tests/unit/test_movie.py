from scrape_movies.domain.movie import format_titles


def test_format_titles_when_titles_are_ranked_reverses_to_ascending() -> None:
    page = ["3) Three", "2) Two", "1) One"]
    assert format_titles(page) == ["1) One", "2) Two", "3) Three"]


def test_format_titles_when_titles_have_no_rank_numbers_them() -> None:
    assert format_titles(["Third", "Second", "First"]) == [
        "1) First",
        "2) Second",
        "3) Third",
    ]


def test_format_titles_when_list_is_empty_returns_empty() -> None:
    assert format_titles([]) == []
