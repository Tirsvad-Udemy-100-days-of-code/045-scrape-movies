"""@brief The ports (interfaces) the use cases need from the outside world."""

from collections.abc import Callable

from scrape_movies.domain.story import Story

## Fetches the HTML text of a page address.
type HtmlFetcher = Callable[[str], str]
## Turns Hacker News HTML into stories.
type StoryParser = Callable[[str], list[Story]]
