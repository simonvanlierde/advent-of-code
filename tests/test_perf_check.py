"""Tests for the correctness-check and benchmarking utilities."""

import pytest
from aocd.examples import Example

from aoc_utils.perf_check import TimeUnit, check_example, time_solution


def _example() -> Example:
    """An aocd Example whose answers check_example compares against."""
    return Example(input_data="ignored", answer_a="6", answer_b="9")


def test_check_example_passes_on_correct_answer() -> None:
    # No exception means the answer matched.
    check_example(lambda _data: 6, _example(), "a")


def test_check_example_raises_on_wrong_answer() -> None:
    with pytest.raises(AssertionError, match="expected 6"):
        check_example(lambda _data: 7, _example(), "a")


def test_check_example_checks_part_b() -> None:
    check_example(lambda _data: 9, _example(), "b")


def test_time_solution_returns_float() -> None:
    result = time_solution(lambda _data: 42, "input", iterations=1, runs=1, print_result=False)
    assert isinstance(result, float)
    assert result >= 0


def test_time_solution_accepts_string_unit() -> None:
    result = time_solution(lambda _data: 42, "input", iterations=1, runs=1, time_unit="us", print_result=False)
    assert isinstance(result, float)


def test_time_unit_multipliers() -> None:
    assert TimeUnit.SECONDS.get_multiplier() == 1.0
    assert TimeUnit.MILLISECONDS.get_multiplier() == 1_000.0
    assert TimeUnit.MICROSECONDS.get_multiplier() == 1_000_000.0


def test_time_unit_str() -> None:
    assert str(TimeUnit.SECONDS) == "s"
    assert str(TimeUnit.MILLISECONDS) == "ms"
    assert str(TimeUnit.MICROSECONDS) == "μs"
