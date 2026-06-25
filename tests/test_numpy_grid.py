"""Tests for the NumPy array grid utilities."""

import numpy as np

from aoc_utils.numpy_grid import (
    OCTAGONAL_KERNEL,
    OCTAGONAL_OFFSETS_TUPLE,
    ORTHOGONAL_KERNEL,
    ORTHOGONAL_OFFSETS_TUPLE,
    map_grid_values,
    shift2d,
    text_to_array_grid,
)


def test_text_to_array_grid_shape_and_dtype() -> None:
    arr = text_to_array_grid("AB\nCD")
    assert arr.shape == (2, 2)
    assert arr.dtype.kind == "U"
    assert arr.tolist() == [["A", "B"], ["C", "D"]]


def test_text_to_array_grid_strips_surrounding_whitespace() -> None:
    arr = text_to_array_grid("\nAB\nCD\n")
    assert arr.tolist() == [["A", "B"], ["C", "D"]]


def test_map_grid_values_applies_mapping() -> None:
    arr = text_to_array_grid("12\n34")
    mapped = map_grid_values(arr, {"1": 1, "2": 2, "3": 3, "4": 4})
    assert mapped.tolist() == [[1, 2], [3, 4]]


def test_shift2d_positive_dx() -> None:
    arr = np.array([[1, 2], [3, 4]])
    assert shift2d(arr, dx=1).tolist() == [[2, 0], [4, 0]]


def test_shift2d_negative_dx() -> None:
    arr = np.array([[1, 2], [3, 4]])
    assert shift2d(arr, dx=-1).tolist() == [[0, 1], [0, 3]]


def test_shift2d_positive_dy() -> None:
    arr = np.array([[1, 2], [3, 4]])
    assert shift2d(arr, dy=1).tolist() == [[3, 4], [0, 0]]


def test_shift2d_respects_fill_value() -> None:
    arr = np.array([[1, 2], [3, 4]])
    assert shift2d(arr, dx=1, fill_value=9).tolist() == [[2, 9], [4, 9]]


def test_shift2d_full_shift_has_no_overlap() -> None:
    arr = np.array([[1, 2], [3, 4]])
    assert shift2d(arr, dx=5).tolist() == [[0, 0], [0, 0]]


def test_kernels() -> None:
    assert int(ORTHOGONAL_KERNEL.sum()) == 4
    assert int(OCTAGONAL_KERNEL.sum()) == 8
    # Both kernels must exclude the centre cell.
    assert ORTHOGONAL_KERNEL[1, 1] == 0
    assert OCTAGONAL_KERNEL[1, 1] == 0


def test_offset_tuples() -> None:
    assert len(ORTHOGONAL_OFFSETS_TUPLE) == 4
    assert len(OCTAGONAL_OFFSETS_TUPLE) == 8
    assert (0, 0) not in OCTAGONAL_OFFSETS_TUPLE
