"""@brief Run the lecture steps and save one terminal screenshot per step.

Usage: python tools/make_screenshots.py [name-prefix]
The images are written to docs/images/ and used by the README and the wiki.
"""

import os
import subprocess
import sys
import urllib.request
from pathlib import Path

from capture_page import capture_page
from render_terminal_png import render

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

ROOT = Path(__file__).resolve().parents[1]
IMAGES = ROOT / "docs" / "images"

## File name (without .png) and the arguments given to `python -m scrape_movies`.
STEPS: dict[str, list[str]] = {
    "soup-1-title": ["soup", "title"],
    "soup-2-prettify": ["soup", "prettify"],
    "soup-3-find-all": ["soup", "find-all"],
    "soup-4-find": ["soup", "find"],
    "soup-5-select": ["soup", "select"],
    "hn-2-markup": ["hacker-news", "markup"],
    "hn-3-titles": ["hacker-news", "titles"],
    "hn-4-links": ["hacker-news", "links"],
    "hn-5-upvotes": ["hacker-news", "upvotes"],
    "hn-6-top": ["hacker-news", "top"],
    "movies-2-markup": ["movies", "markup", "--source", "fixture"],
    "movies-3-titles": ["movies", "titles", "--source", "fixture"],
    "movies-4-reversed": ["movies", "reversed", "--source", "fixture"],
    "movies-5-write": ["movies", "write", "--source", "fixture"],
}
## Screenshots of a file's first lines: image name, file and number of lines.
FILES: dict[str, tuple[str, int]] = {"movies-6-file": ("movies.txt", 15)}
## Screenshots of a small text page: image name and the address of the page.
ROBOTS: dict[str, str] = {"ethics-1-robots": "https://news.ycombinator.com/robots.txt"}
## Screenshots of real web pages: image name and the address of the page.
PAGES: dict[str, str] = {
    "hn-1-page": "https://appbrewery.github.io/news.ycombinator.com/",
    # The live page opens a consent wall, so the saved headings are drawn instead.
    "movies-1-page": (
        ROOT / "tests" / "fixtures" / "empire_live_excerpt.html"
    ).as_uri(),
}


def capture(name: str, args: list[str]) -> Path:
    """@brief Run one step and write its screenshot.

    @param name The image name without extension.
    @param args The arguments for `python -m scrape_movies`.
    @return The path of the PNG.
    """
    result = subprocess.run(
        [sys.executable, "-m", "scrape_movies", *args],
        cwd=ROOT,
        env={**os.environ, "PYTHONIOENCODING": "utf-8"},
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=True,
    )
    target = IMAGES / f"{name}.png"
    render("python -m scrape_movies " + " ".join(args), result.stdout, target)
    return target


def capture_text(name: str, url: str) -> Path:
    """@brief Download a small text file once and draw it like `curl` output.

    Reading `robots.txt` is the first thing a polite scraper does.

    @param name The image name without extension.
    @param url The address of the text file.
    @return The path of the PNG.
    """
    from scrape_movies.constants import USER_AGENT

    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=30) as response:  # noqa: S310
        text = response.read().decode("utf-8")
    target = IMAGES / f"{name}.png"
    render(f"curl {url}", text, target)
    return target


def main() -> None:
    """@brief Capture every step whose name starts with the given prefix."""
    prefix = sys.argv[1] if len(sys.argv) > 1 else ""
    for name, args in STEPS.items():
        if name.startswith(prefix):
            print(capture(name, args))
    for name, (file_name, count) in FILES.items():
        if name.startswith(prefix):
            text = (ROOT / file_name).read_text(encoding="utf-8")
            target = IMAGES / f"{name}.png"
            shown = os.linesep.join(text.splitlines()[:count])
            render(f"head -n {count} {file_name}", shown, target)
            print(target)
    for name, url in ROBOTS.items():
        if name.startswith(prefix):
            print(capture_text(name, url))
    for name, url in PAGES.items():
        if name.startswith(prefix):
            print(capture_page(url, IMAGES / f"{name}.png"))


if __name__ == "__main__":
    main()
