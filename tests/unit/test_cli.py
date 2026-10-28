import pytest

from scrape_movies.presentation import cli, soup_steps


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
