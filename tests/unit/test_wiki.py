import re

from scrape_movies.constants import PROJECT_ROOT

WIKI = PROJECT_ROOT / "docs" / "wiki"
IMAGES = PROJECT_ROOT / "docs" / "images"
LANGUAGES = {"": "**English**", "-da": "**Dansk**", "-ms": "**Bahasa Melayu**"}
STEP_PAGES = ("Parsing-HTML", "Hacker-News", "Scraping-Ethics", "Top-100-Movies")
GAINED = {"": "What we gained", "-da": "Hvad vi lærte", "-ms": "Apa yang kita pelajari"}
IMAGE = re.compile(r"!\[[^\]]*\]\(https://[^)]*/docs/images/([^)]+\.png)\)")
CODE_BLOCK = re.compile(r"```.*?```", re.DOTALL)


def _pages(suffix: str) -> set[str]:
    names = {path.stem for path in WIKI.glob("*.md") if not path.stem.startswith("_")}
    if suffix:
        return {name[: -len(suffix)] for name in names if name.endswith(suffix)}
    return {name for name in names if not name.endswith(("-da", "-ms"))}


def _read(page: str, suffix: str) -> str:
    return (WIKI / f"{page}{suffix}.md").read_text(encoding="utf-8")


def test_wiki_when_translated_has_same_page_set_in_every_language() -> None:
    english = _pages("")
    assert english
    for suffix in ("-da", "-ms"):
        assert _pages(suffix) == english, suffix


def test_wiki_when_page_opens_has_language_switch_line() -> None:
    for suffix, marker in LANGUAGES.items():
        for page in _pages(""):
            first_line = _read(page, suffix).splitlines()[0]
            assert marker in first_line, (page, suffix)
            assert first_line.count("](") == 2, (page, suffix)


def test_wiki_when_step_page_has_screenshots_and_gains_in_every_language() -> None:
    for page in STEP_PAGES:
        english_images = IMAGE.findall(_read(page, ""))
        assert english_images, page
        for suffix, gained in GAINED.items():
            text = _read(page, suffix)
            assert IMAGE.findall(text) == english_images, (page, suffix)
            assert f"## {gained}" in text, (page, suffix)


def test_wiki_when_images_are_linked_every_file_exists() -> None:
    for path in WIKI.glob("*.md"):
        for name in IMAGE.findall(path.read_text(encoding="utf-8")):
            assert (IMAGES / name).is_file(), (path.name, name)


def test_wiki_when_translated_keeps_code_blocks_in_english() -> None:
    for page in _pages(""):
        english = CODE_BLOCK.findall(_read(page, ""))
        for suffix in ("-da", "-ms"):
            assert CODE_BLOCK.findall(_read(page, suffix)) == english, (page, suffix)


def test_sidebar_when_read_lists_every_language_page() -> None:
    sidebar = (WIKI / "_Sidebar.md").read_text(encoding="utf-8")
    for suffix in LANGUAGES:
        for page in _pages(""):
            assert f"]({page}{suffix})" in sidebar, (page, suffix)
