"""@brief The movie list rule: ascending order, every line starting with its rank."""

import re
from collections.abc import Sequence

_RANK_PREFIX = re.compile(r"^\d+\) ")


def format_titles(titles: Sequence[str]) -> list[str]:
    """@brief Turn a descending page list into an ascending, numbered list.

    Empire lists the movies from 100 down to 1, so the page order is reversed.
    A title that already starts with its rank, such as `3) Jaws`, is kept as
    it is; any other title gets `<rank>) ` in front of it.

    @param titles The titles in page order.
    @return The lines `1) ...`, `2) ...` in ascending order.
    """
    lines: list[str] = []
    for rank, title in enumerate(reversed(titles), 1):
        lines.append(title if _RANK_PREFIX.match(title) else f"{rank}) {title}")
    return lines
