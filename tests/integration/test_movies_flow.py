from pathlib import Path

import pytest

from scrape_movies.presentation import cli


def _run(target: Path, capsys: pytest.CaptureFixture[str]) -> str:
    argv = ["movies", "write", "--source", "fixture", "--output", str(target)]
    assert cli.main(argv) == 0
    capsys.readouterr()
    return target.read_text(encoding="utf-8")


def test_write_when_run_from_fixture_creates_100_ascending_lines(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    lines = _run(tmp_path / "movies.txt", capsys).splitlines()
    assert len(lines) == 100
    assert [int(line.split(")")[0]) for line in lines] == list(range(1, 101))


def test_write_when_run_twice_produces_identical_files(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    first = _run(tmp_path / "a.txt", capsys)
    assert _run(tmp_path / "b.txt", capsys) == first
