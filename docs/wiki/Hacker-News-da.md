[English](Hacker-News) · **Dansk** · [Bahasa Melayu](Hacker-News-ms)

# Scraping af Hacker News

Forelæsning: *Scraping af et live-websted*. Koden er `hacker_news.py` (parsing) og `http_client.py` (ét `requests.get` med timeout og `User-Agent`). Kommandoerne læser kursets statiske kopi af siden; `--source live` læser det rigtige websted, og `--source fixture` læser den gemte kopi uden netværk.

## Trin 1: se på siden

Siden viser historier med en titel, et link og en score.

![Trin 1: siden](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/045-scrape-movies/raw/branch/main/docs/images/hn-1-page.png)

**Hvad vi lærte:** live-data er rigere end en lokal fil, men de kan ændre sig, så vi gemmer også en kopi til testene.

## Trin 2: undersøg markup

Browserens udviklerværktøjer viser tagsene: en række `tr.athing`, titellinket `.titleline > a` og en `span.score` i næste række.

![Trin 2: markup](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/045-scrape-movies/raw/branch/main/docs/images/hn-2-markup.png)

**Hvad vi lærte:** vi finder det rigtige tag ved at undersøge siden, før vi skriver kode.

## Trin 3: titler

`find_all` på titellinkene og `get_text()`.

![Trin 3: titler](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/045-scrape-movies/raw/branch/main/docs/images/hn-3-titles.png)

**Hvad vi lærte:** en list comprehension gør mange tags til en almindelig liste af strenge.

## Trin 4: links

`get("href")` på de samme links.

![Trin 4: links](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/045-scrape-movies/raw/branch/main/docs/images/hn-4-links.png)

**Hvad vi lærte:** det samme element giver både tekst og attributværdier.

## Trin 5: upvotes

Teksten `38 points` deles op og omdannes med `int()`.

![Trin 5: upvotes](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/045-scrape-movies/raw/branch/main/docs/images/hn-5-upvotes.png)

**Hvad vi lærte:** scrapet tekst skal omdannes til tal, før den kan sammenlignes.

## Trin 6: den øverste historie

`max` over upvotes finder den mest populære artikel.

![Trin 6: øverste historie](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/045-scrape-movies/raw/branch/main/docs/images/hn-6-top.png)

**Hvad vi lærte:** når data er rene, besvarer almindelig Python spørgsmål om dem.

## Hvad vi lærte

Vi kan hente en side med Requests, finde rækkerne, læse titler, links og scores, omdanne dem til brugbare typer og besvare et spørgsmål om data.
