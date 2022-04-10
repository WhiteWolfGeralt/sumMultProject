from typing import Tuple

from src.sum_mult.mult_config.mult_config import mult_config
from src.sum_mult.sum_config.sum_config import sum_config


def sum_mult_config(x: int) -> Tuple[int, int]:
    return sum_config(x), mult_config(x)
