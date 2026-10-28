from typing import Any

import pytest
import requests

from scrape_movies.constants import REQUEST_TIMEOUT_SECONDS, USER_AGENT
from scrape_movies.domain.errors import FetchError
from scrape_movies.infrastructure import http_client


class _Response:
    def __init__(self, text: str, error: Exception | None = None) -> None:
        self.text = text
        self._error = error

    def raise_for_status(self) -> None:
        if self._error is not None:
            raise self._error


def test_fetch_html_when_request_succeeds_sends_user_agent_and_timeout(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    calls: list[dict[str, Any]] = []

    def fake_get(url: str, **kwargs: Any) -> _Response:
        calls.append({"url": url, **kwargs})
        return _Response("<html></html>")

    monkeypatch.setattr(requests, "get", fake_get)
    assert http_client.fetch_html("http://example.test") == "<html></html>"
    assert calls == [
        {
            "url": "http://example.test",
            "headers": {"User-Agent": USER_AGENT},
            "timeout": REQUEST_TIMEOUT_SECONDS,
        }
    ]


def test_fetch_html_when_server_errors_raises_fetch_error(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    error = requests.HTTPError("500")
    monkeypatch.setattr(requests, "get", lambda *a, **k: _Response("", error))
    with pytest.raises(FetchError) as caught:
        http_client.fetch_html("http://example.test")
    assert caught.value.__cause__ is error


def test_fetch_html_when_connection_fails_raises_fetch_error(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def fail(*args: Any, **kwargs: Any) -> _Response:
        raise requests.ConnectionError("down")

    monkeypatch.setattr(requests, "get", fail)
    with pytest.raises(FetchError):
        http_client.fetch_html("http://example.test")
