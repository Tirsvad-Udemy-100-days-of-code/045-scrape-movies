[English](Gains) · **Dansk** · [Bahasa Melayu](Gains-ms)

# Hvad vi lærte

| Forelæsning | Hvad vi kan nu |
| --- | --- |
| [Parsing af HTML](Parsing-HTML-da) | Lave en suppe, læse dens struktur og vælge elementer via tag, id, klasse eller CSS-selektor |
| [Hacker News](Hacker-News-da) | Hente en live-side, læse titler, links og scores, omdanne tekst til tal og finde maksimum |
| [Etik ved scraping](Scraping-Ethics-da) | Tjekke `robots.txt`, respektere ophavsret og logins og holde forespørgslerne sjældne |
| [Top 100 film](Top-100-Movies-da) | Scrape en rangeret liste, vende den om og skrive den til en fil |
| [Opsætning](Setup-da) | Arbejde i et virtuelt miljø med `pyproject.toml` og offline-tests |

## Ud over forelæsningerne

- **Parsing er adskilt fra hentning.** Parsing-funktionerne tager tekst, så testene bruger gemte sider og aldrig har brug for netværket.
- **Lag holder reglerne adskilt.** Rangeringsreglen kender hverken BeautifulSoup eller Requests.
- **Skærmbillederne laves af et script** (`tools/make_screenshots.py`), så de kan genskabes efter en ændring.
