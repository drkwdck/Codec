import numpy as np

from ArithmeticCoder import ArithmeticCoder


class EntropyCalculator:
    @staticmethod
    def calculate(symbol, cum_freq: np.ndarray):
        p = (cum_freq[symbol] - symbol) / (cum_freq[ArithmeticCoder.NO_OF_SYMBOLS] - 256)
        return (-1) * p
