from typing import Tuple
from math import ceil


def aspect_ratio(x: int, y: int) -> Tuple[int, int]:
    return (ceil(16 * y / 9), y)
