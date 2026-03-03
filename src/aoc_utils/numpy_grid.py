"""Utilities for parsing 2D text grids into Numpy arrays."""

import numpy as np


### Main parsing utilities
def text_to_array_grid(data: str) -> np.ndarray:
    """Convert raw text data directly to 2D numpy array."""
    # Parse lines
    lines = data.strip().splitlines()

    # Get array dimensions
    height = len(lines)
    width = max(len(line) for line in lines)

    # Create array of single characters (dtype 'U1') and fill it
    arr = np.full((height, width), fill_value=" ", dtype="U1")
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            arr[i, j] = char

    return arr


def shift2d(arr: np.ndarray[tuple[int, int], np.dtype], dx: int = 0, dy: int = 0, *, fill_value: int = 0) -> np.ndarray:
    """Shift 2D array by (dx, dy) without wrapping."""
    # Initialize output array
    shifted = np.zeros(arr.shape, dtype=arr.dtype)

    # Fill with fill_value if needed
    if fill_value != 0:
        shifted.fill(fill_value)

    # Determine slices for the original and shifted arrays
    orig_y = slice(max(0, dy), None if dy >= 0 else dy)
    orig_x = slice(max(0, dx), None if dx >= 0 else dx)

    shifted_y = slice(max(0, -dy), None if dy <= 0 else -dy)
    shifted_x = slice(max(0, -dx), None if dx <= 0 else -dx)

    # Fill the shifted array with values from the original array
    shifted[shifted_y, shifted_x] = arr[orig_y, orig_x]
    return shifted


### Directions
# Offset tuples for neighbor calculations
ORTHOGONAL_OFFSETS_TUPLE = [(-1, 0), (0, 1), (1, 0), (0, -1)]
OCTAGONAL_OFFSETS_TUPLE = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

# Kernels for convolution-based neighbor counting
ORTHOGONAL_KERNEL = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]], dtype=int)
OCTAGONAL_KERNEL = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]], dtype=int)
