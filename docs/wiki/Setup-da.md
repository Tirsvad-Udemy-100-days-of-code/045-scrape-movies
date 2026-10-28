[English](Setup) · **Dansk** · [Bahasa Melayu](Setup-ms)

# Opsætning

Du skal bruge Python 3.13 eller nyere. Alt nedenfor køres fra repositoryets rodmappe.

## Opret det virtuelle miljø

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

På Linux og macOS bruges `python3 -m venv .venv` og `source .venv/bin/activate`.

## Kør et trin fra forelæsningen

```bash
python -m scrape_movies soup title
python -m scrape_movies hacker-news top
python -m scrape_movies movies write
```

## Kør testene

```bash
python -m pytest
```

Testene bruger gemte sider fra `tests/fixtures/` og rører aldrig netværket.

## Hvad vi lærte

- Et virtuelt miljø holder projektets pakker adskilt fra systemets Python.
- `pyproject.toml` er det ene sted for Python-versionen, afhængighederne og værktøjsindstillingerne.
- Tests, der kører offline, giver det samme resultat på alle maskiner.
