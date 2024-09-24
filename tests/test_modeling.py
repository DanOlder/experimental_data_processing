"""Data modeling tests."""
import unittest
from dataclasses import dataclass, asdict

from src.in_out import DataPoint
from src.model import Model, DataType


@dataclass
class ModelTrendInput(object):
    """Input values of trend-making function."""

    data_type: DataType
    data_a: float
    data_b: float
    delta: float
    alpha: float


class TestModeling(unittest.TestCase):
    """Testing data creation and editing."""

    def setUp(self):
        """Set up data for the tests."""
        self.data_seq_creator = Model()
        self.model_trend_input = ModelTrendInput(
            data_type=DataType.linear,
            data_a=5,
            data_b=10,
            delta=0.01,
            alpha=0.1,
        )

    def test_generation(self):
        """Test for creating data sequence."""
        data_seq = self.data_seq_creator.trend(**asdict(self.model_trend_input))
        len_to_compare = 500
        self.assertEqual(len(data_seq), len_to_compare)

    def test_data_shift(self):
        """Test for shifting data sequence."""
        data_seq = self.data_seq_creator.trend(**asdict(self.model_trend_input))
        shift_const = 10
        self.data_seq_creator.shift(data_seq, shift_const=shift_const)

        start_point_to_compare = DataPoint(t=5, y=10.5)
        end_point_to_compare = DataPoint(t=9.99, y=10.999)
        self.assertAlmostEqual(data_seq[0].t, start_point_to_compare.t)
        self.assertAlmostEqual(data_seq[-1].t, end_point_to_compare.t)
        self.assertAlmostEqual(data_seq[-0].y, start_point_to_compare.y)
        self.assertAlmostEqual(data_seq[-1].y, end_point_to_compare.y)

    def test_data_mult(self):
        """Test for multiplying data sequence."""
        data_seq = self.data_seq_creator.trend(**asdict(self.model_trend_input))
        mult_const = 10
        self.data_seq_creator.mult(data_seq, mult_const=mult_const)

        start_point_to_compare = DataPoint(t=5, y=5)
        end_point_to_compare = DataPoint(t=9.99, y=9.99)
        self.assertAlmostEqual(data_seq[0].t, start_point_to_compare.t)
        self.assertAlmostEqual(data_seq[-1].t, end_point_to_compare.t)
        self.assertAlmostEqual(data_seq[-0].y, start_point_to_compare.y)
        self.assertAlmostEqual(data_seq[-1].y, end_point_to_compare.y)
