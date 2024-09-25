"""Piecewise linear function example."""
from src.logic.in_out import InOut
from src.logic.model import Model, DataType

if __name__ == '__main__':
    # 1st piece
    display_data = Model.trend(DataType.linear, 0, 2.5, 0.01, alpha=1)
    InOut.prepare_data_to_display(display_data)

    # 2nd piece
    display_data = Model.trend(DataType.linear, 2.5, 5, 0.01, alpha=2)
    Model.shift(display_data, -2.5)
    InOut.prepare_data_to_display(display_data, new_fig=False)

    # 3rd piece
    display_data = Model.trend(DataType.linear, 5, 7.5, 0.01, alpha=-2)
    Model.shift(display_data, 17.5)
    InOut.prepare_data_to_display(display_data, new_fig=False)

    # 4th piece
    display_data = Model.trend(DataType.linear, 7.5, 10, 0.01, alpha=10)
    Model.shift(display_data, -72.5)
    InOut.prepare_data_to_display(display_data, new_fig=False)

    # draw
    InOut.show()
