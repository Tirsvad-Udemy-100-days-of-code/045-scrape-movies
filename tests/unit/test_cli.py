import pytest

from scrape_movies.presentation import cli, hacker_news_steps, soup_steps


def test_main_when_soup_step_is_given_prints_output(
    capsys: pytest.CaptureFixture[str],
) -> None:
    for step in soup_steps.STEPS:
        assert cli.main(["soup", step]) == 0
        assert capsys.readouterr().out.strip(), step


def test_main_when_no_command_prints_help(
    capsys: pytest.CaptureFixture[str],
) -> None:
    assert cli.main([]) == 0
    assert "usage:" in capsys.readouterr().out


def test_render_step_when_title_returns_page_title() -> None:
    assert soup_steps.render_step("title") == (
        "soup.title.string -> Angela's Personal Site"
    )


def test_main_when_hacker_news_top_from_fixture_prints_top_story(
    capsys: pytest.CaptureFixture[str],
) -> None:
    assert cli.main(["hacker-news", "top", "--source", "fixture"]) == 0
    out = capsys.readouterr().out
    assert "Mozilla lays off 250 employees" in out
    assert "1312 points" in out


def test_main_when_every_hacker_news_step_runs_from_fixture_prints_output(
    capsys: pytest.CaptureFixture[str],
) -> None:
    for step in hacker_news_steps.STEPS:
        assert cli.main(["hacker-news", step, "--source", "fixture"]) == 0
        assert capsys.readouterr().out.strip(), step


def test_main_when_movies_markup_from_fixture_prints_heading(
    capsys: pytest.CaptureFixture[str],
) -> None:
    assert cli.main(["movies", "markup", "--source", "fixture"]) == 0
    assert "<h2>" in capsys.readouterr().out
