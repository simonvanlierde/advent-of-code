"""Thread workers need to be in a python file to be picklable."""  # noqa: INP001 # Can't create packages whose name starts with a number

from hashlib import md5
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from threading import Event


def worker_b(
    input_data: str,
    stop_event: Event,
    *,
    num_zeroes: int = 5,
    start: int = 1,
    step: int = 1,
    check_interval: int = 10_000,
) -> int | None:
    """Worker function to find the lowest integer `i` > 0 such that md5("input_data"+"i") starts with n zeroes.

    Args:
        input_data: The base input string to hash with integers
        stop_event: Event to signal early stopping when another worker finds a solution
        num_zeroes: Number of leading zeroes required in the hash
        start: Starting integer for this worker
        step: Step size for this worker (to avoid overlap with other workers)
        check_interval: How often to check the stop_event
    """
    target = "0" * num_zeroes

    for i in range(start, int(1e9), step):
        # Check for stop event every N iterations
        if i % check_interval == 0 and stop_event.is_set():
            return None

        h = md5(f"{input_data}{i}".encode())  # noqa: S324
        if h.hexdigest().startswith(target):
            stop_event.set()
            return i

    msg = "No solution found within the first 1 billion integers."
    raise RuntimeError(msg)
