# Contributing

Thanks for your interest in contributing.

## Development setup

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
python -m pip install mypy pytest pytest-cov ruff
```

## Before opening a PR

Run:

```bash
ruff check .
mypy src
pytest
```

## Commit guidelines

- Keep commits focused and atomic.
- Use clear commit messages.
- Update tests and docs for behavior changes.
