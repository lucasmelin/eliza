# ELIZA

![eliza](eliza.jpg)

A clone of Joseph Weizenbaum's [ELIZA](https://en.wikipedia.org/wiki/ELIZA), one of the first natural language processing computer progams.

# Demo

[![asciicast](https://asciinema.org/a/459592.svg)](https://asciinema.org/a/459592)

# Setup and usage

With [poetry](https://python-poetry.org/) installed:

```bash
poetry install
poetry shell

# Lint a file
past file_you_want_to_lint.py

# Run the unit tests
pytest -vvv
```