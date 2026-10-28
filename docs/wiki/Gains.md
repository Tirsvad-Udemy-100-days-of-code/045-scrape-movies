**English** · [Dansk](Gains-da) · [Bahasa Melayu](Gains-ms)

# What we gained

| Lecture | What we can do now |
| --- | --- |
| [Parsing HTML](Parsing-HTML) | Make a soup, read its structure and select elements by tag, id, class or CSS selector |
| [Hacker News](Hacker-News) | Fetch a live page, read titles, links and scores, convert text to numbers, find the maximum |
| [Scraping ethics](Scraping-Ethics) | Check `robots.txt`, respect copyright and logins, keep requests rare |
| [Top 100 movies](Top-100-Movies) | Scrape a ranked list, reverse it and write it to a file |
| [Setup](Setup) | Work in a virtual environment with `pyproject.toml` and offline tests |

## Beyond the lectures

- **Parsing is separate from fetching.** The parsing functions take text, so the tests use saved pages and never need the network.
- **Layers keep rules apart.** The ranking rule has no knowledge of BeautifulSoup or Requests.
- **Screenshots are made by a script** (`tools/make_screenshots.py`), so they can be regenerated after a change.
