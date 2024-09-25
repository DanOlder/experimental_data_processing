"""Data modeling."""

import numpy as np

from src.data_utils import DataType, PlotDataSequence, DataPoint, DataSequence


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
