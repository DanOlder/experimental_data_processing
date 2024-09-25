"""Noise example."""
from src.in_out import InOut
from src.model import Model, DataType

if __name__ == '__main__':
    # 1st piece
    display_data = Model.noise(-100,  100, 0.5, 5)
    InOut.prepare_data_to_display(display_data)

    # draw
    InOut.show()
