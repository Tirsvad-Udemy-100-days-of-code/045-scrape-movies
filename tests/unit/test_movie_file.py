from pathlib import Path

from scrape_movies.infrastructure.movie_file import write_movies


def test_write_movies_when_lines_given_writes_one_per_line(tmp_path: Path) -> None:
    target = tmp_path / "movies.txt"
    write_movies(["1) One", "2) Zoë"], target)
    assert target.read_bytes() == "1) One\n2) Zoë\n".encode()


def test_write_movies_when_file_exists_replaces_it(tmp_path: Path) -> None:
    target = tmp_path / "movies.txt"
    target.write_text("old\n", encoding="utf-8")
    write_movies(["1) New"], target)
    assert target.read_text(encoding="utf-8") == "1) New\n"
