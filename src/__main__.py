"""Main file."""

from in_out import InOut
from model import Model, DataType

if __name__ == '__main__':
    display_data = Model.trend(DataType.linear, 0, 1000, 1, alpha=1)
    # Model.shift(display_data, 200)
    # Model.mult(display_data, -1)
    InOut.prepare_data_to_display(display_data)

    # display_data = Model.trend(DataType.linear, 0, 1000, 1)
    # InOut.display_data(display_data)
    #
    # display_data = Model.trend(DataType.exponential, 0, 1000, 1)
    # InOut.display_data(display_data)

    display_data = Model.trend(DataType.exponential, 0, 1000, 1, alpha=0.06)
    InOut.prepare_data_to_display(display_data)

    InOut.show()

# кусочно-нелинейную соединить
