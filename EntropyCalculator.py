import numpy as np

from ArithmeticCoder import ArithmeticCoder


class EntropyCalculator:
    @staticmethod
    def calculate(symbol, cum_freq: np.ndarray):
        p = (cum_freq[symbol + 1] - cum_freq[symbol]) / cum_freq[ArithmeticCoder.NO_OF_SYMBOLS]
        return (-1) * np.log2(p)
