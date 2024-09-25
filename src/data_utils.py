"""Data classes and utils."""

import math
import random
import time
from dataclasses import dataclass
from enum import Enum
from typing import Optional


def lin_fun(time_val: int, alpha: float):
    """Linear function."""
    return alpha * time_val


def exp_fun(time_val: int, alpha: float):
    """Exponential function."""
    return math.exp(-alpha * time_val)


def custom_rand(x_min, x_max) -> float:
    """Custom rand fun."""
    # Get the current time in seconds and use the fractional part as the seed
    seed = time.time() - int(time.time())
    seed %= 1000
    return x_min + seed * (x_max - x_min)


def noise_calc(rad, x_min, x_max, custom=False) -> float:
    """Noise calculation."""
    if custom:
        x_rand = custom_rand(x_min, x_max)
    else:
        x_rand = random.uniform(x_min, x_max)
    dist = (x_rand - x_min) / (x_max - x_min)
    return (dist - 0.5) * 2 * rad


class DataType(Enum):
    """Math function types enum."""

    linear = 1
    exponential = 2
    noise = 3

    def get_calc_fun(self, alpha: float = 5) -> dict:
        """Getting function and str label for a specific math function type."""
        return {
            self.linear: lambda t_val: lin_fun(t_val, alpha),
            self.exponential: lambda t_val: exp_fun(t_val, alpha),
            self.noise: noise_calc,
        }


@dataclass
class DataPoint(object):
    """Point class."""

    t: float
    y: float


@dataclass
class DataSequence(object):
    """Data sequence class."""

    proc_data: list[DataPoint]
    data_type: DataType


@dataclass
class PlotDataSequence(DataSequence):
    """Data sequence class."""

    k_coef: float
    m_coef: Optional[float] = 0
