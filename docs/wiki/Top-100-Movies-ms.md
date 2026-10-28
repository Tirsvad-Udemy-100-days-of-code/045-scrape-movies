[English](Top-100-Movies) · [Dansk](Top-100-Movies-da) · **Bahasa Melayu**

# 100 filem terbaik

Kuliah: *Projek 100 filem*. Matlamatnya ialah `movies.txt` dengan tajuk bernombor bermula dari `1)`. Kodnya ialah `empire_movies.py` (penghuraian), `movie.py` (terbalikkan dan nomborkan) dan `movie_file.py` (penulisan).

## Langkah 1: pilih halaman

Tugasan mengunci syot kilat Internet Archive bagi senarai Empire kerana laman langsung sentiasa berubah. Tangkapan skrin menunjukkan tajuk halaman yang disimpan.

![Langkah 1: halaman](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/045-scrape-movies/raw/branch/main/docs/images/movies-1-page.png)

**Apa yang kita pelajari:** syot kilat yang dikunci menjadikan pengikis boleh diulang.

## Langkah 2: periksa markup

Halaman 2020 mempunyai `<h3 class="title">`; halaman semasa mempunyai tajuk `<h2><strong>` yang bermula dengan kedudukan.

![Langkah 2: markup](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/045-scrape-movies/raw/branch/main/docs/images/movies-2-markup.png)

**Apa yang kita pelajari:** apabila laman mengubah markup, penghurai mesti berubah bersama, jadi kita menampung kedua-dua susunan.

## Langkah 3: tajuk mengikut susunan halaman

`select("h3.title")` dan list comprehension pada `get_text()`. Halaman mengira turun dari 100.

![Langkah 3: tajuk](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/045-scrape-movies/raw/branch/main/docs/images/movies-3-titles.png)

**Apa yang kita pelajari:** list comprehension ialah cara ringkas mengumpul teks daripada banyak tag.

## Langkah 4: terbalikkan senarai

`titles[::-1]` menjadikan senarai mengira naik dari 1.

![Langkah 4: terbalik](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/045-scrape-movies/raw/branch/main/docs/images/movies-4-reversed.png)

**Apa yang kita pelajari:** hirisan dengan langkah negatif membalikkan senarai dalam satu ungkapan.

## Langkah 5: tulis movies.txt

Blok `with open(...)` menulis satu tajuk setiap baris.

![Langkah 5: tulis](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/045-scrape-movies/raw/branch/main/docs/images/movies-5-write.png)

**Apa yang kita pelajari:** pengurus konteks menutup fail untuk kita, dan larian yang sama sentiasa menghasilkan fail yang sama.

## Langkah 6: hasilnya

![Langkah 6: movies.txt](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/045-scrape-movies/raw/branch/main/docs/images/movies-6-file.png)

**Apa yang kita pelajari:** senarai tontonan peribadi daripada sebuah laman web, sedia untuk memilih filem secara rawak.

## Nota tentang data

`movies.txt` dihasilkan daripada senarai Empire semasa pada 2026-10-28, jadi kedudukannya berbeza daripada senarai 2020 dalam kuliah. Internet Archive menjawab `429 Too Many Requests` semasa kami membina projek ini, jadi susunan syot kilat dilindungi oleh contoh tulisan tangan dalam ujian.

## Apa yang kita pelajari

Kita boleh mengikis senarai berkedudukan, menyusunnya mengikut keperluan dan menyimpannya dalam fail.
