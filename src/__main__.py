"""Main file."""

from in_out import InOut
from model import Model, DataType


def function_type_choice() -> DataType:
    """Math fun choice."""
    while True:
        data_type_choice = input('Choose function type:\n1) Linear\n2) Exponential\n')
        if data_type_choice not in {'1', '2'}:
            print('Error. Please, enter a valid number\n')
            continue
        if data_type_choice == '1':
            return DataType.linear
        return DataType.exponential


def end_input_choice() -> bool:
    """Stop entering data and show graphs or continue."""
    while True:
        choice = input('1) Continue entering data\n2) Draw entered data\n')
        if choice not in {'1', '2'}:
            print('Error. Please, enter a valid number\n')
            continue
        return choice == '2'


if __name__ == '__main__':
    # entering plots one by one
    while True:
        data_type = function_type_choice()

        data_a = float(input('Input starting point (a)\n'))
        data_b = float(input('Input ending point (b)\n'))
        delta = float(input('Input time points distance (delta)\n'))
        alpha = float(input('Input k coefficient of function (alpha)\n'))

        display_data = Model.trend(
            data_type,
            data_a,
            data_b,
            delta,
            alpha=2,
        )

        shift = float(input('Input shifting coefficient\n'))
        mult = float(input('Input multiplication coefficient\n'))

        Model.shift(display_data, shift)
        Model.mult(display_data, mult)

        InOut.prepare_data_to_display(display_data, new_fig=True)

        stop = end_input_choice()
        if stop:
            break

    InOut.show()
