"""Utilities for parsing 2D text grids into Numpy arrays."""

import numpy as np


### Main parsing utilities
def text_to_array_grid(data: str) -> np.ndarray:
    """Convert grid-like text to 2D numpy array."""
    return np.array([list(line) for line in data.strip().splitlines()], dtype="U1")


def map_grid_values[T_in, T_out](arr: np.ndarray[tuple[int, int], np.dtype], mapping: dict[T_in, T_out]) -> np.ndarray:
    """Map values in a 2D array to integers using a provided mapping."""
    return np.vectorize(mapping.get)(arr)


def shift2d(arr: np.ndarray[tuple[int, int], np.dtype], dx: int = 0, dy: int = 0, *, fill_value: int = 0) -> np.ndarray:
    """Shift 2D array by (dx, dy) without wrapping."""
    h, w = arr.shape
    shifted = np.full_like(arr, fill_value)

    src_y0, src_y1 = max(0, dy), h + min(0, dy)
    src_x0, src_x1 = max(0, dx), w + min(0, dx)
    dst_y0, dst_y1 = max(0, -dy), h - max(0, dy)
    dst_x0, dst_x1 = max(0, -dx), w - max(0, dx)

    if src_y0 < src_y1 and src_x0 < src_x1:
        shifted[dst_y0:dst_y1, dst_x0:dst_x1] = arr[src_y0:src_y1, src_x0:src_x1]

    return shifted


### Directions
# Offset tuples for neighbor calculations
ORTHOGONAL_OFFSETS_TUPLE = [(-1, 0), (0, 1), (1, 0), (0, -1)]
OCTAGONAL_OFFSETS_TUPLE = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

# Kernels for convolution-based neighbor counting
ORTHOGONAL_KERNEL = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]], dtype=int)
OCTAGONAL_KERNEL = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]], dtype=int)
