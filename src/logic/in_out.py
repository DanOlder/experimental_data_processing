"""Input and Output processing."""

from typing import Optional

from matplotlib import pyplot as plt

from src.logic.model import DataSequence, DataType, PlotDataSequence


def label_constructor(data_seq: [DataSequence, PlotDataSequence]) -> str:
    """Extract label from DataSequence class."""
    if data_seq.data_type.value == DataType.linear.value:
        k_coef = data_seq.k_coef if data_seq.k_coef != 1 else ''
        label = f'f(t)={k_coef}t'
    elif data_seq.data_type.value == DataType.exponential.value:
        label = f'f(t)=exp^({-data_seq.k_coef}t)'
    elif data_seq.data_type.value == DataType.exponential.value:
        return 'Noise'
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
        t_values = [p_d.t for p_d in proc_data]
        y_values = [p_d.y for p_d in proc_data]

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
