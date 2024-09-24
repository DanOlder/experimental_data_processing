"""Data modeling."""

import math
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


class DataType(Enum):
    """Math function types enum."""

    linear = 1
    exponential = 2

    def get_calc_fun(self, alpha: float) -> dict:
        """Getting function and str label for a specific math function type."""
        return {
            self.linear: (
                lambda x: lin_fun(x, alpha),
                f'f(t)={alpha}t',
            ),
            self.exponential: (
                lambda x: exp_fun(x, alpha),
                f'f(t)=exp^({-alpha}t)',
            ),
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
    ) -> DataSequence:
        """Data calculation."""
        calc_fun, label = DataType.get_calc_fun(data_type, alpha)[data_type]
        time_list = np.arange(data_a, data_b, delta)
        data_list = []
        for time_point in time_list:
            data_list.append(
                DataPoint(time_point, calc_fun(time_point)),
            )
        return DataSequence(proc_data=data_list, k_coef=alpha, data_type=data_type)

    @classmethod
    def shift(cls, data_seq: DataSequence, shift_const: float) -> DataSequence:
        """Data sequence shift."""
        for point in data_seq.proc_data:
            point.y += shift_const
        data_seq.m_coef += shift_const
        return data_seq

    @classmethod
    def mult(cls, data_seq: DataSequence, mult_const: float) -> DataSequence:
        """Data sequence multiplication."""
        for point in data_seq.proc_data:
            point.y *= mult_const
        data_seq.m_coef *= mult_const
        data_seq.k_coef *= mult_const
        return data_seq
