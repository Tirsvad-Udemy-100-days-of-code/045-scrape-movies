"""@brief Writing the movie list to a text file."""

from collections.abc import Sequence
from pathlib import Path


def write_movies(lines: Sequence[str], path: Path) -> None:
    """@brief Write one line per movie, UTF-8, with a final newline.

    @param lines The lines to write.
    @param path The file to create or overwrite.
    """
    with path.open("w", encoding="utf-8", newline="\n") as file:
        for line in lines:
            file.write(f"{line}\n")
