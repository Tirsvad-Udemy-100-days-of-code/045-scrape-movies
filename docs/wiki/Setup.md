**English** · [Dansk](Setup-da) · [Bahasa Melayu](Setup-ms)

# Setup

You need Python 3.13 or newer. Everything below is run from the repository root.

## Create the virtual environment

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

On Linux and macOS use `python3 -m venv .venv` and `source .venv/bin/activate`.

## Run a lecture step

```bash
python -m scrape_movies soup title
python -m scrape_movies hacker-news top
python -m scrape_movies movies write
```

## Run the tests

```bash
python -m pytest
```

The tests use saved pages from `tests/fixtures/` and never touch the network.

## What we gained

- A virtual environment keeps the project's packages apart from the system Python.
- `pyproject.toml` is the one place for the Python version, the dependencies and the tool settings.
- Tests that run offline give the same result on every machine.
