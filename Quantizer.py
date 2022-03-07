import numpy as np


class Quantizer:
    quantize_step = 0.0584

    @staticmethod
    def Quantize(input_vector: np.ndarray) -> np.ndarray:
        quantize_matrix = np.ones(input_vector.shape) * Quantizer.quantize_step
        return np.sign(input_vector) * np.fix(np.abs(input_vector) / quantize_matrix)

    @staticmethod
    def dequantize(input_vector: np.ndarray) -> np.ndarray:
        quantize_matrix = np.ones(input_vector.shape) * Quantizer.quantize_step
        return (input_vector + np.sign(input_vector) * 0.5) * quantize_matrix
