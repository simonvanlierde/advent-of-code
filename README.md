# Advent of Code

My answers to the annual <https://adventofcode.com/> challenge

I'm using the [advent-of-code-data](https://pypi.org/project/advent-of-code-data/) python package to help with fetching inputs and submitting answers.

## Quickstart

1. Clone the repository

   ```bash
   git clone https://github.com/simonvanlierde/advent-of-code.git
   cd advent-of-code
   ```

1. Fill in your advent of code session cookie in an `.env` file, based on the `.env.example` file.

1. Set up a virtual environment with [uv](https://docs.astral.sh/uv/):

   ```bash
   uv sync
   ```

1. You can open the notebooks in [VS code](https://code.visualstudio.com/) with the [Jupyter extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter), or run Jupyter Lab:

   ```bash
   uv run jupyter lab
   ```
