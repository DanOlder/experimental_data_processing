"""Main file."""

from in_out import InOut
from model import Model, DataType

if __name__ == '__main__':

    # 2) linear piecewise
    display_data = Model.trend(DataType.linear, 0, 2.5, 0.01, alpha=1)
    InOut.prepare_data_to_display(display_data)

    display_data = Model.trend(DataType.linear, 2.5, 5, 0.01, alpha=2)
    Model.shift(display_data, -2.5)
    InOut.prepare_data_to_display(display_data, new_fig=False)

    InOut.show()
