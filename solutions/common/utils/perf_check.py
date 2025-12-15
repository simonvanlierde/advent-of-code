"""Performance check utilities."""

from enum import Enum
from timeit import repeat
from typing import TYPE_CHECKING, Any, Literal

if TYPE_CHECKING:
    from collections.abc import Callable


class TimeUnit(str, Enum):
    """Time units for performance measurement."""

    SECONDS = "s"
    MILLISECONDS = "ms"
    MICROSECONDS = "us"

    def get_multiplier(self) -> float:
        """Get multiplier to convert seconds to the specified unit."""
        match self:
            case self.SECONDS:
                return 1.0
            case self.MILLISECONDS:
                return 1_000.0
            case self.MICROSECONDS:
                return 1_000_000.0
            case _:
                msg = f"Unsupported time unit: {self}"
                raise ValueError(msg)


def check_time(
    func: Callable, *args: Any, number: int = 100, repeat_times: int = 5, unit: TimeUnit = TimeUnit.MILLISECONDS
) -> float:
    """Check average execution time of a function over multiple runs.

    Args:
        func: Function to time
        *args: Arguments to pass to the function
        number: Number of executions per timing run
        repeat_times: Number of timing runs to perform
        unit: Time unit for the result ("s" for seconds, "ms" for milliseconds, "us" for microseconds)
    """
    times = repeat(lambda: func(*args), repeat=repeat_times, number=number)
    avg_time_s = min(times) / number
    return avg_time_s * unit.get_multiplier()
