"""Performance check utilities."""

from enum import StrEnum
from timeit import repeat
from typing import TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from collections.abc import Callable

    from aocd.examples import Example


### Correctness check
def check_example(
    func: Callable[..., object],
    example: Example,
    part: Literal["a", "b"] = "a",
    *args: object,
    **kwargs: object,
) -> None:
    """Check a solution function against example."""
    func_name = getattr(func, "__name__", type(func).__name__)
    func_answer = str(func(example.input_data, *args, **kwargs))
    example_answer = example.answer_a if part == "a" else example.answer_b
    if func_answer == example_answer:
        print(f"{func_name} found answer {example_answer}, which is the correct solution for part {part.capitalize()}!")

    else:
        msg = f"{func_name} returned {func_answer}, but expected {example_answer} for part {part.capitalize()}."
        raise AssertionError(msg)


### Performance timer
class TimeUnit(StrEnum):
    """Time units for performance measurement."""

    SECONDS = "s"
    MILLISECONDS = "ms"
    MICROSECONDS = "us"

    def get_multiplier(self) -> float:
        """Get multiplier to convert seconds to the specified unit."""
        match self:
            case TimeUnit.SECONDS:
                return 1.0
            case TimeUnit.MILLISECONDS:
                return 1_000.0
            case TimeUnit.MICROSECONDS:
                return 1_000_000.0
            case _:
                msg = f"Unknown time unit: {self}"
                raise ValueError(msg)

    def __str__(self) -> str:
        """Print microseconds with the proper symbol."""
        if self == TimeUnit.MICROSECONDS:
            return "μs"
        return self.value


def time_solution(
    func: Callable[..., object],
    *func_args: object,
    iterations: int = 100,
    runs: int = 5,
    time_unit: TimeUnit | str = TimeUnit.MILLISECONDS,
    print_result: bool = True,
    **func_kwargs: object,
) -> float:
    """Check average execution time of a solution function.

    Args:
        func: Solution function to time
        *func_args: Positional arguments to pass to the function
        iterations: Number of executions per timing run
        runs: Number of timing runs to perform
        time_unit: Time unit for the result ("s" for seconds, "ms" for milliseconds, "us" for microseconds)
        print_result: Whether to print the timing result
        **func_kwargs: Keyword arguments to pass to the function
    """
    if isinstance(time_unit, str):
        time_unit = TimeUnit(time_unit)

    func_name = getattr(func, "__name__", type(func).__name__)
    times = repeat(lambda: func(*func_args, **func_kwargs), repeat=runs, number=iterations)
    avg_time = min(times) / iterations * time_unit.get_multiplier()

    if print_result:
        print(f"{func_name} takes {avg_time:.2f} {time_unit}")

    return avg_time
