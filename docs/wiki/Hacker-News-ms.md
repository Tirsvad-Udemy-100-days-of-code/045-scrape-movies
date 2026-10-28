[English](Hacker-News) · [Dansk](Hacker-News-da) · **Bahasa Melayu**

# Mengikis Hacker News

Kuliah: *Mengikis laman web langsung*. Kodnya ialah `hacker_news.py` (penghuraian) dan `http_client.py` (satu `requests.get` dengan had masa dan `User-Agent`). Arahan membaca salinan statik halaman daripada kursus; `--source live` membaca laman sebenar dan `--source fixture` membaca salinan tersimpan tanpa rangkaian.

## Langkah 1: lihat halaman

Halaman menyenaraikan berita dengan tajuk, pautan dan skor.

![Langkah 1: halaman](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/045-scrape-movies/raw/branch/main/docs/images/hn-1-page.png)

**Apa yang kita pelajari:** data langsung lebih kaya daripada fail tempatan, tetapi boleh berubah, jadi kita juga menyimpan salinan untuk ujian.

## Langkah 2: periksa markup

Alat pembangun pelayar menunjukkan tag: baris `tr.athing`, pautan tajuk `.titleline > a` dan `span.score` pada baris seterusnya.

![Langkah 2: markup](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/045-scrape-movies/raw/branch/main/docs/images/hn-2-markup.png)

**Apa yang kita pelajari:** kita menemui tag yang betul dengan memeriksa halaman sebelum menulis kod.

## Langkah 3: tajuk

`find_all` pada pautan tajuk dan `get_text()`.

![Langkah 3: tajuk](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/045-scrape-movies/raw/branch/main/docs/images/hn-3-titles.png)

**Apa yang kita pelajari:** list comprehension menukar banyak tag menjadi senarai rentetan biasa.

## Langkah 4: pautan

`get("href")` pada anchor yang sama.

![Langkah 4: pautan](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/045-scrape-movies/raw/branch/main/docs/images/hn-4-links.png)

**Apa yang kita pelajari:** elemen yang sama memberi teks dan nilai atribut.

## Langkah 5: undian

Teks `38 points` dipecahkan dan ditukar dengan `int()`.

![Langkah 5: undian](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/045-scrape-movies/raw/branch/main/docs/images/hn-5-upvotes.png)

**Apa yang kita pelajari:** teks yang dikikis mesti ditukar kepada nombor sebelum boleh dibandingkan.

## Langkah 6: berita teratas

`max` pada undian mencari artikel paling popular.

![Langkah 6: berita teratas](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/045-scrape-movies/raw/branch/main/docs/images/hn-6-top.png)

**Apa yang kita pelajari:** apabila data sudah bersih, Python biasa menjawab soalan tentangnya.

## Apa yang kita pelajari

Kita boleh mengambil halaman dengan Requests, menemui baris, membaca tajuk, pautan dan skor, menukarnya kepada jenis yang berguna dan menjawab soalan tentang data.
