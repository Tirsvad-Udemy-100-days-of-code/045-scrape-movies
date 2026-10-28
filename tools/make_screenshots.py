"""@brief Run the lecture steps and save one terminal screenshot per step.

Usage: python tools/make_screenshots.py [name-prefix]
The images are written to docs/images/ and used by the README and the wiki.
"""

import subprocess
import sys
from pathlib import Path

from render_terminal_png import render

ROOT = Path(__file__).resolve().parents[1]
IMAGES = ROOT / "docs" / "images"

## File name (without .png) and the arguments given to `python -m scrape_movies`.
STEPS: dict[str, list[str]] = {
    "soup-1-title": ["soup", "title"],
    "soup-2-prettify": ["soup", "prettify"],
    "soup-3-find-all": ["soup", "find-all"],
    "soup-4-find": ["soup", "find"],
    "soup-5-select": ["soup", "select"],
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
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=True,
    )
    target = IMAGES / f"{name}.png"
    render("python -m scrape_movies " + " ".join(args), result.stdout, target)
    return target


def main() -> None:
    """@brief Capture every step whose name starts with the given prefix."""
    prefix = sys.argv[1] if len(sys.argv) > 1 else ""
    for name, args in STEPS.items():
        if name.startswith(prefix):
            print(capture(name, args))


if __name__ == "__main__":
    main()
