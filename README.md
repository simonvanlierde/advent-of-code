# Advent of Code

[![CI](https://github.com/simonvanlierde/advent-of-code/actions/workflows/ci.yml/badge.svg)](https://github.com/simonvanlierde/advent-of-code/actions/workflows/ci.yml)
[![Python 3.14](https://img.shields.io/badge/python-3.14-blue.svg)](https://www.python.org/)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

My solutions to the annual [Advent of Code](https://adventofcode.com/) puzzles, written in
**Python**. I use them to practice writing clean, fully typed code that pays attention to
speed. Each day is a small problem that stands on its own, so it's a good place to try out
algorithms, libraries and tooling.

## What this repo demonstrates

- **Modern Python tooling.** [uv](https://docs.astral.sh/uv/) for packaging and reproducible
  environments, [Ruff](https://docs.astral.sh/ruff/) for linting and formatting (the full rule
  set), [ty](https://github.com/astral-sh/ty) for type checking. A
  [pre-commit](https://pre-commit.com/) pipeline runs these and also scans for secrets and
  checks spelling.
- **Typed, reusable utilities.** Shared logic lives in the installable
  [`aoc_utils`](src/aoc_utils) package, so I don't copy and paste it between notebooks.
- **Attention to speed.** I time solutions with `time_solution`, and where a problem invites
  it I compare approaches. See [2015 day 9](notebooks/2015/9.ipynb): it solves the
  traveling-salesman variant four ways (brute-force, recursive, `networkx`, and a Held–Karp
  dynamic program) and times each.
- **Correctness checks.** 36 of the 58 notebooks test their solution against the puzzle's
  worked example before submitting the real answer. 2015 (except day 16) does this through
  `check_example`, and 2023 and 2025 compare against `puzzle.examples` directly. The 2024
  notebooks do not check the example.

## Progress

| Year                   | Days solved | Notes                         |
| ---------------------- | ----------- | ----------------------------- |
| [2015](notebooks/2015) | 1–19        | Algorithm-heavy early puzzles |
| [2023](notebooks/2023) | 1–6         | Partial                       |
| [2024](notebooks/2024) | 1–21        | Most complete year            |
| [2025](notebooks/2025) | 1–12        | In progress                   |

## The `aoc_utils` package

A small, fully typed helper library that the notebooks share:

- [`dict_grid`](src/aoc_utils/dict_grid.py): parses 2D text grids into `dict[complex, str]`.
  It uses complex numbers as coordinates, so finding a neighbour is just addition.
- [`numpy_grid`](src/aoc_utils/numpy_grid.py): the NumPy version, with array shifting and
  convolution kernels for fast neighbour counting.
- [`perf_check`](src/aoc_utils/perf_check.py): `check_example` for correctness and
  `time_solution` for benchmarking.

Unit tests for the utilities are under [`tests/`](tests).

## Structure

```text
notebooks/
  <year>/<day>.ipynb   # one notebook per day
  templates/           # starting template for a new day
src/aoc_utils/         # shared, typed helper package
tests/                 # unit tests for aoc_utils
```

I solve each day in a Jupyter notebook. The
[advent-of-code-data](https://pypi.org/project/advent-of-code-data/) package fetches the
puzzle inputs and submits the answers. So no puzzle inputs are committed to this repository,
as the Advent of Code [guidelines](https://adventofcode.com/about#faq_copying) ask.

## Quickstart

1. Clone and enter the repo:

   ```bash
   git clone https://github.com/simonvanlierde/advent-of-code.git
   cd advent-of-code
   ```

1. Add your Advent of Code session cookie to a `.env` file (see `.env.example`).

1. Set up the environment with [uv](https://docs.astral.sh/uv/):

   ```bash
   uv sync
   ```

1. Open a notebook in VS Code (with the Jupyter extension) or run Jupyter Lab:

   ```bash
   uv run jupyter lab
   ```

Run the utility tests with:

```bash
uv run pytest
```
