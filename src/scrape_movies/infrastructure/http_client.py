"""@brief Fetching web pages with Requests."""

import requests

from scrape_movies.constants import REQUEST_TIMEOUT_SECONDS, USER_AGENT
from scrape_movies.domain.errors import FetchError


def fetch_html(url: str) -> str:
    """@brief Download a page with one GET request.

    Sends a User-Agent and gives up after a timeout. Call it once per run:
    scraping more often than once a minute is not polite.

    @param url The address of the page.
    @return The HTML text of the response.
    @throws FetchError When the request fails or the server answers with an error.
    """
    try:
        response = requests.get(
            url,
            headers={"User-Agent": USER_AGENT},
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
        response.raise_for_status()
    except requests.RequestException as error:
        raise FetchError(f"Could not fetch {url}: {error}") from error
    return str(response.text)
