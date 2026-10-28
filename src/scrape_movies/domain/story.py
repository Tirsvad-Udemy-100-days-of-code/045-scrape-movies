"""@brief The Story entity (a Hacker News article) and the top-story rule."""

from collections.abc import Sequence
from dataclasses import dataclass


@dataclass(frozen=True)
class Story:
    """@brief An article on the Hacker News front page.

    @param title The headline.
    @param link The address the headline points to.
    @param upvotes The number of points; 0 when the story shows none.
    """

    title: str
    link: str
    upvotes: int


def top_story(stories: Sequence[Story]) -> Story | None:
    """@brief Find the story with the most upvotes.

    @param stories The stories in page order.
    @return The first story with the highest score, or None when there are none.
    """
    best: Story | None = None
    for story in stories:
        if best is None or story.upvotes > best.upvotes:
            best = story
    return best
