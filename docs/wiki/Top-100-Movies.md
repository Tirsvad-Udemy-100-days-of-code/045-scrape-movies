**English** · [Dansk](Top-100-Movies-da) · [Bahasa Melayu](Top-100-Movies-ms)

# Top 100 movies

Lecture: *The 100 movies project*. The goal is `movies.txt` with the titles numbered from `1)` upwards. The code is `empire_movies.py` (parsing), `movie.py` (reverse and number) and `movie_file.py` (writing).

## Step 1: choose the page

The assignment pins an Internet Archive snapshot of Empire's list, because live sites change. The screenshot shows the saved headings of the page.

![Step 1: the page](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/045-scrape-movies/raw/branch/main/docs/images/movies-1-page.png)

**What we gained:** a pinned snapshot makes a scraper repeatable.

## Step 2: inspect the markup

The 2020 page has `<h3 class="title">`; the current page has `<h2><strong>` headings that start with a rank.

![Step 2: markup](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/045-scrape-movies/raw/branch/main/docs/images/movies-2-markup.png)

**What we gained:** when a site changes its markup, the parser must change with it, so we keep both layouts covered.

## Step 3: titles in page order

`select("h3.title")` and a list comprehension over `get_text()`. The page counts down from 100.

![Step 3: titles](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/045-scrape-movies/raw/branch/main/docs/images/movies-3-titles.png)

**What we gained:** a list comprehension is the compact way to collect text from many tags.

## Step 4: reverse the list

`titles[::-1]` makes the list count up from 1.

![Step 4: reversed](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/045-scrape-movies/raw/branch/main/docs/images/movies-4-reversed.png)

**What we gained:** slicing with a negative step reverses a list in one expression.

## Step 5: write movies.txt

A `with open(...)` block writes one title per line.

![Step 5: write](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/045-scrape-movies/raw/branch/main/docs/images/movies-5-write.png)

**What we gained:** the context manager closes the file for us, and the same run always gives the same file.

## Step 6: the result

![Step 6: movies.txt](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/045-scrape-movies/raw/branch/main/docs/images/movies-6-file.png)

**What we gained:** a personal watch list from a website, ready to pick a film from at random.

## Note on the data

`movies.txt` was produced from the current Empire list on 2026-10-28, so its ranking differs from the 2020 list in the lecture. The Internet Archive answered `429 Too Many Requests` while we built this, so the snapshot layout is covered by a hand-written sample in the tests.

## What we gained

We can scrape a ranked list, put it in the order we want and save it to a file.
