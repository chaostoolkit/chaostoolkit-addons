import time


__all__ = ["idle_for"]


def idle_for(duration: float) -> None:
    """
    Pauses the experiment without blocking the process completely.
    """
    start = time.time()
    end = start + duration

    while time.time() < end:
        time.sleep(0.1)
