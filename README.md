# Advent of Code

[![CI](https://github.com/simonvanlierde/advent-of-code/actions/workflows/ci.yml/badge.svg)](https://github.com/simonvanlierde/advent-of-code/actions/workflows/ci.yml)
[![Python 3.14](https://img.shields.io/badge/python-3.14-blue.svg)](https://www.python.org/)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

My solutions to the annual [Advent of Code](https://adventofcode.com/) puzzles, one Jupyter
notebook per day, in fully typed **Python**. I use them to practice writing clean code that pays
attention to speed. For an example, [2015 day 9](notebooks/2015/9.ipynb) solves the
traveling-salesman variant four ways and times each.

| Year                   | Days solved |
| ---------------------- | ----------- |
| [2015](notebooks/2015) | 1–19        |
| [2023](notebooks/2023) | 1–6         |
| [2024](notebooks/2024) | 1–21        |
| [2025](notebooks/2025) | 1–12        |

36 of the 58 notebooks test their solution against the puzzle's worked example: 2015 (except
day 16) through `check_example`, 2023 and 2025 against `puzzle.examples` directly. The 2024
notebooks do not check the example.

Shared helpers (grid parsing, `check_example`, `time_solution`) live in the typed
[`aoc_utils`](src/aoc_utils) package, with unit tests under [`tests/`](tests).

No puzzle inputs are committed, as the Advent of Code
[guidelines](https://adventofcode.com/about#faq_copying) ask.
[advent-of-code-data](https://pypi.org/project/advent-of-code-data/) fetches them and submits
the answers.

## Quickstart

Add your Advent of Code session cookie to a `.env` file (see `.env.example`), then:

```bash
uv sync
uv run jupyter lab
uv run pytest   # aoc_utils tests
```
