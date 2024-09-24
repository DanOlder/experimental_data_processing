"""Input and Output processing."""

from dataclasses import dataclass
from typing import Optional

from matplotlib import pyplot as plt


@dataclass
class DataPoint(object):
    """Point class."""

    t: float
    y: float


class InOut(object):
    """In and Out processing."""

    @classmethod
    def prepare_data_to_display(cls, proc_data: list[DataPoint], n: Optional[int] = None):
        """Prepare graph."""
        t_values = [p.t for p in proc_data]
        y_values = [p.y for p in proc_data]

        if n and n < len(t_values):
            t_values = t_values[:n]
            y_values = y_values[:n]

        plt.figure()
        # draw
        plt.plot(t_values, y_values)

        return plt

    @classmethod
    def show(cls):
        """Show graphs."""
        plt.show()
