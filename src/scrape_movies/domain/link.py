"""@brief The Link value object: the text and the address of an anchor."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Link:
    """@brief A hyperlink found on a page.

    @param text The visible text of the anchor.
    @param url The value of its `href` attribute.
    """

    text: str
    url: str
