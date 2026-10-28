"""@brief Use cases of the scraping exercises."""

from scrape_movies.application.ports import HtmlFetcher, StoryParser
from scrape_movies.domain.story import Story, top_story


def list_stories(fetch: HtmlFetcher, parse: StoryParser, url: str) -> list[Story]:
    """@brief Fetch a Hacker News page and read its stories.

    @param fetch Fetches the HTML of the page.
    @param parse Reads the stories from the HTML.
    @param url The page address.
    @return The stories in page order.
    """
    return parse(fetch(url))


def find_top_story(fetch: HtmlFetcher, parse: StoryParser, url: str) -> Story | None:
    """@brief Find the story with the most upvotes on a Hacker News page.

    @param fetch Fetches the HTML of the page.
    @param parse Reads the stories from the HTML.
    @param url The page address.
    @return The top story, or None when the page has no stories.
    """
    return top_story(list_stories(fetch, parse, url))
