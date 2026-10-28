**English** · [Dansk](Scraping-Ethics-da) · [Bahasa Melayu](Scraping-Ethics-ms)

# Is web scraping legal and ethical?

Lecture: *The legal and ethical side of web scraping*. This is a summary in our own words, not legal advice.

## Step 1: read robots.txt first

A site's `robots.txt` says what it allows. Hacker News disallows some paths and asks for a crawl delay of 30 seconds.

![Step 1: robots.txt](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/045-scrape-movies/raw/branch/main/docs/images/ethics-1-robots.png)

**What we gained:** we check the rules before we scrape, and we keep our requests rare: this project fetches one page per run.

## The rules we follow

- Public data that is not copyrighted is generally fine to read. The cases Genius v. Google and hiQ v. LinkedIn show that the line is not simple.
- Copyrighted content, such as videos or blog posts, must not be copied. Data behind a login is covered by the site's user agreement.
- Commercial use of scraped data can lead to costly disputes even when the scraping itself was allowed.
- Prefer an official API, respect `robots.txt`, send a `User-Agent` and do not send more than one request a minute.

## What we gained

Scraping is a technical skill with legal and ethical limits. Knowing the limits is part of doing it well.
