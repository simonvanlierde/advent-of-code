"""Performance check utilities."""

from enum import Enum
from timeit import repeat
from typing import TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from collections.abc import Callable

    from aocd.examples import Example


### Correctness check
def check_example(
    func: Callable, example: Example, part: Literal["a", "b"] = "a", *args: object, **kwargs: object
) -> None:
    """Check a solution function against example."""
    func_answer = str(func(example.input_data, *args, **kwargs))
    example_answer = example.answer_a if part == "a" else example.answer_b
    if func_answer == example_answer:
        print(
            f"{func.__name__} found answer {example_answer},"
            f" which is the correct solution for part {part.capitalize()}!"
        )

    else:
        msg = f"{func.__name__} returned {func_answer}, but expected {example_answer} for part {part.capitalize()}."
        raise AssertionError(msg)


### Performance timer
class TimeUnit(str, Enum):
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
    func: Callable,
    input_data: str,
    *args: object,
    iterations: int = 100,
    runs: int = 5,
    time_unit: TimeUnit | str = TimeUnit.MILLISECONDS,
    print_result: bool = True,
    **kwargs: object,
) -> float:
    """Check average execution time of a solution function.

    Args:
        func: Solution function to time
        input_data: Main input data to pass to the function
        *args: Optional positional arguments to pass to the function
        iterations: Number of executions per timing run
        runs: Number of timing runs to perform
        time_unit: Time unit for the result ("s" for seconds, "ms" for milliseconds, "us" for microseconds)
        print_result: Whether to print the timing result
        **kwargs: Optional keyword arguments to pass to the function
    """
    if isinstance(time_unit, str):
        time_unit = TimeUnit(time_unit)

    times = repeat(lambda: func(input_data, *args, **kwargs), repeat=runs, number=iterations)
    avg_time = min(times) / iterations * time_unit.get_multiplier()

    if print_result:
        print(f"{func.__name__} takes {avg_time:.2f} {time_unit}")

    return avg_time
