"""Utilities for parsing 2D text grids into dictionaries with complex number keys."""

from typing import TypeVar

ObjectType = TypeVar("ObjectType")


### Main parsing utilities
def text_to_grid_dict(data: str) -> dict[complex, str]:
    """Parse grid data into a dictionary with complex coordinates."""
    return {
        x + y * 1j: char
        # The rows are reversed to make the y-axis positive upwards
        for y, line in enumerate(data.splitlines()[::-1])
        for x, char in enumerate(line)
    }


def map_grid_values_to_int(grid: dict[complex, str]) -> dict[complex, int]:
    """Map the values of a grid to integers."""
    return {k: int(v) for k, v in grid.items()}


def print_grid(grid: dict[complex, str] | dict[complex, int], *, reverse_y_axis: bool = True) -> None:
    """Print the grid, with the option to reverse the y-axis."""
    grid_height = int(max(p.imag for p in grid) - min(p.imag for p in grid) + 1)
    grid_width = int(max(p.real for p in grid) - min(p.real for p in grid) + 1)

    y_range = reversed(range(grid_height)) if reverse_y_axis else range(grid_height)

    for j in y_range:
        print(f"{j:<3}", "".join(str(grid.get(i + j * 1j, " ")) for i in range(grid_width)))


def get_grid_object(grid: dict[complex, str], position: complex, allowed_objects: tuple[str, ...]) -> str:
    """Find object at position in grid."""
    obj = grid.get(position)
    if not obj:
        err_msg = f"Position {position} is out of the grid bounds."
        raise ValueError(err_msg)
    if obj not in allowed_objects:
        err_msg = f"Object '{obj}' at position {position} is invalid, must be one of '{"','".join(allowed_objects)}'"
        raise ValueError(err_msg)
    return obj


def find_object_in_grid(grid: dict[complex, ObjectType], obj: ObjectType) -> complex:
    """Find object position in grid."""
    for position, value in grid.items():
        if value == obj:
            return position
    err_msg = f"Object '{obj}' not found in grid."
    raise ValueError(err_msg)


def find_objects_in_grid(grid: dict[complex, ObjectType], obj: ObjectType) -> list[complex]:
    """Find object positions in grid."""
    return [position for position, value in grid.items() if value == obj]


### Directions
ORTHOGONAL_OFFSETS_COMPLEX = [1, 1j, -1, -1j]
OCTAGONAL_OFFSETS_COMPLEX = [1, 1 + 1j, 1j, -1 + 1j, -1, -1 - 1j, -1j, 1 - 1j]


def get_orthogonal_neighbors(position: complex) -> list[complex]:
    """Return the 4 direct neighbors of a complex grid position."""
    return [position + d for d in ORTHOGONAL_OFFSETS_COMPLEX]


def get_octagonal_neighbors(position: complex) -> list[complex]:
    """Return the 8 neighbors of a complex grid position."""
    return [position + d for d in OCTAGONAL_OFFSETS_COMPLEX]
