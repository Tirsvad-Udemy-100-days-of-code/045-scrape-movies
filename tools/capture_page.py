"""@brief Save a screenshot of a web page with a headless Chromium browser.

A headless browser draws into memory, so no desktop window is opened and no
mouse or keyboard is used. It needs Edge, Chrome or Chromium on the machine.
"""

import shutil
import subprocess
from pathlib import Path

CANDIDATES = (
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "google-chrome",
    "chromium",
    "chromium-browser",
)
WINDOW = "1280,1000"


def find_browser() -> str:
    """@brief Locate a Chromium-based browser.

    @return The path or command name of the browser.
    @throws FileNotFoundError When none is installed.
    """
    for candidate in CANDIDATES:
        if Path(candidate).exists() or shutil.which(candidate):
            return candidate
    raise FileNotFoundError("Install Edge, Chrome or Chromium to capture pages.")


def capture_page(url: str, target: Path) -> Path:
    """@brief Render a page and save it as a PNG.

    @param url The page address.
    @param target The PNG file to write.
    @return The path of the PNG.
    """
    target.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            find_browser(),
            "--headless=new",
            "--disable-gpu",
            "--hide-scrollbars",
            f"--window-size={WINDOW}",
            f"--screenshot={target}",
            url,
        ],
        check=True,
        capture_output=True,
        timeout=120,
    )
    return target
