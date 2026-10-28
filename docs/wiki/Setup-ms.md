[English](Setup) · [Dansk](Setup-da) · **Bahasa Melayu**

# Persediaan

Anda memerlukan Python 3.13 atau lebih baharu. Semua arahan di bawah dijalankan dari akar repositori.

## Cipta persekitaran maya

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Di Linux dan macOS gunakan `python3 -m venv .venv` dan `source .venv/bin/activate`.

## Jalankan satu langkah kuliah

```bash
python -m scrape_movies soup title
python -m scrape_movies hacker-news top
python -m scrape_movies movies write
```

## Jalankan ujian

```bash
python -m pytest
```

Ujian menggunakan halaman tersimpan dalam `tests/fixtures/` dan tidak pernah menyentuh rangkaian.

## Apa yang kita pelajari

- Persekitaran maya mengasingkan pakej projek daripada Python sistem.
- `pyproject.toml` ialah satu tempat untuk versi Python, kebergantungan dan tetapan alat.
- Ujian yang berjalan tanpa talian memberi keputusan yang sama pada setiap mesin.
