import numpy as np


class Quantizer:
    quantize_step = 0.0584

    @staticmethod
    def Quantize(input_vector: np.ndarray) -> np.ndarray:
        return np.round(input_vector / Quantizer.quantize_step) * Quantizer.quantize_step
