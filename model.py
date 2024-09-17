"""."""
import math
from enum import Enum

import numpy as np

from in_out import DataPoint


def lin_fun(time_val: int, alpha: float):
    """Linear function."""
    return alpha * time_val


def exp_fun(time_val: int, alpha: float):
    """Exponential function."""
    return math.exp(-alpha * time_val)


class DataType(Enum):
    """."""

    linear = 1
    exponential = 2

    def get_calc_fun(self, alpha: float) -> dict:
        return {
            self.linear: lambda x: lin_fun(x, alpha),
            self.exponential: lambda x: exp_fun(x, alpha),
        }


class Model(object):
    """Model class for data calculating."""

    def __init__(self):
        """."""
        ...

    @classmethod
    def trend(
            cls,
            data_type: DataType,
            a: float,  # start
            b: float,  # end
            delta: float,  # distance
            alpha: float = 5,  # for graphs
            # n: int = 1000,  # points number // не уверен, зачем оно нужно здесь, лучше передавать сразу в отрисовку
    ) -> list[DataPoint]:
        """Data calculation."""
        calc_fun = DataType.get_calc_fun(data_type, alpha)[data_type]
        time_list = np.arange(a, b, delta)
        data_list = []
        for time_point in time_list:
            data_list.append(
                DataPoint(time_point, calc_fun(time_point)),
            )
        return data_list

    @classmethod
    def shift(cls, data_list: list[DataPoint], shift_const: float):
        """Data shift."""
        for point in data_list:
            point.y += shift_const
        return data_list

    @classmethod
    def mult(cls, data_list: list[DataPoint], mult_const: float):
        """Data multiplication."""
        for point in data_list:
            point.y *= mult_const
        return data_list
