"""@brief The ports (interfaces) the use cases need from the outside world."""

from collections.abc import Callable
from typing import TypeAlias

from scrape_movies.domain.story import Story

## Fetches the HTML text of a page address.
HtmlFetcher: TypeAlias = Callable[[str], str]
## Turns Hacker News HTML into stories.
StoryParser: TypeAlias = Callable[[str], list[Story]]
