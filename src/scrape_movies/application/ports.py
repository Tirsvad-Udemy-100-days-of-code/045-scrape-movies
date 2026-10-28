"""@brief The ports (interfaces) the use cases need from the outside world."""

from collections.abc import Callable, Sequence
from pathlib import Path
from typing import TypeAlias

from scrape_movies.domain.story import Story

## Fetches the HTML text of a page address.
HtmlFetcher: TypeAlias = Callable[[str], str]
## Turns Hacker News HTML into stories.
StoryParser: TypeAlias = Callable[[str], list[Story]]
## Turns the Empire page HTML into the movie lines found on it, in page order.
MovieParser: TypeAlias = Callable[[str], list[str]]
## Writes lines to a file, one per line.
MovieWriter: TypeAlias = Callable[[Sequence[str], Path], None]
