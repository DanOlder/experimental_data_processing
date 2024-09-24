"""Input and Output processing."""

from typing import Optional

from matplotlib import pyplot as plt

from src.model import DataSequence, DataType


def label_constructor(data_seq: DataSequence):
    """Extract label from DataSequence class."""
    if data_seq.data_type == DataType.linear:
        label = f'f(t)={data_seq.k_coef}t'
    elif data_seq.data_type == DataType.exponential:
        label = f'f(t)=exp^({-data_seq.k_coef}t)'
    else:
        return ''

    if data_seq.m_coef:
        label += f'{data_seq.m_coef:+}'
    return label


class InOut(object):
    """In and Out processing."""

    @classmethod
    def prepare_data_to_display(
        cls,
        data_seq: DataSequence,
        max_n: Optional[int] = None,
        new_fig: bool = True,
    ):
        """Prepare graph."""
        proc_data = data_seq.proc_data
        t_values = [p.t for p in proc_data]
        y_values = [p.y for p in proc_data]

        if max_n and max_n < len(t_values):
            t_values = t_values[:max_n]
            y_values = y_values[:max_n]

        if new_fig:
            plt.figure()
            plt.grid(True)
            plt.xlabel('Time, sec')
            plt.ylabel('Value')

        label = label_constructor(data_seq)
        # draw
        plt.plot(t_values, y_values, label=label)
        plt.legend()

    @classmethod
    def show(cls):
        """Show graphs."""
        plt.show()
