"""Common utilities for the Advent of Code solutions.

The package is organized into focused submodules:

- `dict_grid`: parse 2D text grids into ``dict[complex, str]`` using complex-number coordinates.
- `numpy_grid`: parse 2D text grids into NumPy arrays, with shift and kernel helpers.
- `perf_check`: check solutions against AoC examples and benchmark their runtime.
"""

from aoc_utils import dict_grid, numpy_grid, perf_check
from aoc_utils.dict_grid import text_to_grid_dict
from aoc_utils.numpy_grid import text_to_array_grid
from aoc_utils.perf_check import TimeUnit, check_example, time_solution

__all__ = [
    "TimeUnit",
    "check_example",
    "dict_grid",
    "numpy_grid",
    "perf_check",
    "text_to_array_grid",
    "text_to_grid_dict",
    "time_solution",
]
