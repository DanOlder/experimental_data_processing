"""Data modeling."""

import math
import random
import time
from dataclasses import dataclass
from enum import Enum
from typing import Optional

import numpy as np


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


class Model(object):
    """Model class for data calculating."""

    @classmethod
    def trend(
        cls,
        data_type: DataType,
        data_a: float,  # start
        data_b: float,  # end
        delta: float,  # distance
        alpha: float = 5,  # k coefficient
    ) -> PlotDataSequence:
        """Data calculation."""
        calc_fun = DataType.get_calc_fun(data_type, alpha)[data_type]
        time_list = np.arange(data_a, data_b, delta)
        data_list = []
        for time_point in time_list:
            data_list.append(
                DataPoint(time_point, calc_fun(time_point)),
            )
        return PlotDataSequence(proc_data=data_list, k_coef=alpha, data_type=data_type)

    @classmethod
    def shift(cls, data_seq: PlotDataSequence, shift_const: float) -> PlotDataSequence:
        """Data sequence shift."""
        for point in data_seq.proc_data:
            point.y += shift_const
        data_seq.m_coef += shift_const
        return data_seq

    @classmethod
    def mult(cls, data_seq: PlotDataSequence, mult_const: float) -> PlotDataSequence:
        """Data sequence multiplication."""
        for point in data_seq.proc_data:
            point.y *= mult_const
        data_seq.m_coef *= mult_const
        data_seq.k_coef *= mult_const
        return data_seq

    @classmethod
    def noise(
        cls,
        data_a: float,  # start
        data_b: float,  # end
        delta: float,  # distance
        rad: float,  # radius (max abs of noise)
        x_min: float = 0,
        x_max: float = 100,
    ):
        """Generate noise."""
        time_list = np.arange(data_a, data_b, delta)
        calc_fun = DataType.get_calc_fun(DataType.noise)[DataType.noise]
        data_list = []
        for time_point in time_list:
            data_list.append(DataPoint(time_point, calc_fun(rad, x_min, x_max, custom=False)))
        return DataSequence(proc_data=data_list, data_type=DataType.noise)
