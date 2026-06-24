"""Tests for the complex-number dict grid utilities."""

import pytest

from aoc_utils.dict_grid import (
    OCTAGONAL_OFFSETS_COMPLEX,
    ORTHOGONAL_OFFSETS_COMPLEX,
    find_object_in_grid,
    find_objects_in_grid,
    get_grid_object,
    get_octagonal_neighbors,
    get_orthogonal_neighbors,
    map_grid_values,
    map_grid_values_to_int,
    text_to_grid_dict,
)

GRID_TEXT = "AB\nCD"


def test_text_to_grid_dict_reverses_y_axis() -> None:
    # Rows are reversed so the y-axis points upwards: the bottom row is y=0.
    grid = text_to_grid_dict(GRID_TEXT)
    assert grid == {0 + 0j: "C", 1 + 0j: "D", 0 + 1j: "A", 1 + 1j: "B"}


def test_map_grid_values_to_int() -> None:
    grid = text_to_grid_dict("12\n34")
    assert map_grid_values_to_int(grid) == {0 + 0j: 3, 1 + 0j: 4, 0 + 1j: 1, 1 + 1j: 2}


def test_map_grid_values_with_mapping() -> None:
    grid = text_to_grid_dict("AB")
    assert map_grid_values(grid, {"A": 1, "B": 2}) == {0 + 0j: 1, 1 + 0j: 2}


def test_get_grid_object_returns_allowed_object() -> None:
    grid = text_to_grid_dict("AB")
    assert get_grid_object(grid, 0 + 0j, ("A", "B")) == "A"


def test_get_grid_object_out_of_bounds_raises() -> None:
    grid = text_to_grid_dict("AB")
    with pytest.raises(ValueError, match="out of the grid bounds"):
        get_grid_object(grid, 9 + 9j, ("A", "B"))


def test_get_grid_object_disallowed_object_raises() -> None:
    grid = text_to_grid_dict("AB")
    with pytest.raises(ValueError, match="is invalid"):
        get_grid_object(grid, 0 + 0j, ("X",))


def test_find_object_in_grid_returns_first_position() -> None:
    grid = text_to_grid_dict("AB\nCA")
    # "A" appears twice; the first in insertion order (bottom row is built first) wins.
    assert find_object_in_grid(grid, "A") == 1 + 0j


def test_find_object_in_grid_missing_raises() -> None:
    grid = text_to_grid_dict("AB")
    with pytest.raises(ValueError, match="not found in grid"):
        find_object_in_grid(grid, "Z")


def test_find_objects_in_grid_returns_all_positions() -> None:
    grid = text_to_grid_dict("AA")
    assert sorted(find_objects_in_grid(grid, "A"), key=lambda p: p.real) == [0 + 0j, 1 + 0j]


def test_orthogonal_offsets_and_neighbors() -> None:
    assert ORTHOGONAL_OFFSETS_COMPLEX == [1, 1j, -1, -1j]
    assert get_orthogonal_neighbors(0) == [1, 1j, -1, -1j]


def test_octagonal_offsets_and_neighbors() -> None:
    assert len(OCTAGONAL_OFFSETS_COMPLEX) == 8
    neighbors = get_octagonal_neighbors(1 + 1j)
    assert len(neighbors) == 8
    assert (1 + 1j) not in neighbors
