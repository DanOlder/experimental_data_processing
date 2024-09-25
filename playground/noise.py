"""Noise example."""
from src.logic.in_out import InOut
from src.logic.model import Model

if __name__ == '__main__':
    display_data = Model.noise(-100,  100, 0.5, 5)
    InOut.prepare_data_to_display(display_data)

    # draw
    InOut.show()
