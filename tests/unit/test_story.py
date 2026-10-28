from scrape_movies.domain.story import Story, top_story


def test_top_story_when_scores_differ_returns_highest() -> None:
    stories = [Story("a", "/a", 5), Story("b", "/b", 50), Story("c", "/c", 7)]
    assert top_story(stories) == Story("b", "/b", 50)


def test_top_story_when_scores_tie_returns_first() -> None:
    stories = [Story("a", "/a", 9), Story("b", "/b", 9)]
    assert top_story(stories) == Story("a", "/a", 9)


def test_top_story_when_no_stories_returns_none() -> None:
    assert top_story([]) is None
