# vishuzz

`vishuzz` is a complete Python project template that includes:

- a reusable package (`src/vishuzz`)
- a CLI entrypoint (`vishuzz`)
- tests with `pytest`
- linting (`ruff`) and static type checking (`mypy`)
- CI via GitHub Actions

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e .[dev]
```

Analyze a text file:

```bash
vishuzz README.md
```

## Development

```bash
make check
```

## Project layout

```text
.
├── .github/workflows/ci.yml
├── src/vishuzz/
│   ├── __init__.py
│   ├── analysis.py
│   └── cli.py
├── tests/
├── pyproject.toml
└── README.md
```
