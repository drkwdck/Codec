import numpy as np


class Quantizer:
    quantize_step = 0.0826

    @staticmethod
    def Quantize(input_vector: np.ndarray) -> np.ndarray:
        quantize_matrix = np.ones(input_vector.shape) * Quantizer.quantize_step
        return (np.sign(input_vector) * np.fix(np.abs(input_vector) / quantize_matrix)).astype(np.int64)

    @staticmethod
    def quantize(subbands: list) -> list:
        quantized_subbands = []
        for i in range(len(subbands)):
            quantize_matrix = np.ones(subbands[i].shape) * Quantizer.quantize_step
            quantized_subband = (np.sign(subbands[i]) * np.fix(np.abs(subbands[i]) / quantize_matrix)).astype(np.int64)

            if i != 0:
                quantized_subband = quantized_subband + 128

            quantized_subbands.append(quantized_subband)
        return quantized_subbands

    @staticmethod
    def dequantize(subbands: list) -> list:
        dequantized_subbands = []
        for i in range(len(subbands)):
            if i != 0:
                subbands[i] -= 128
            quantize_matrix = np.ones(subbands[i].shape) * Quantizer.quantize_step
            dequantized_subband = (subbands[i] + np.sign(subbands[i]) * 0.5) * quantize_matrix
            dequantized_subbands.append(dequantized_subband)
        return dequantized_subbands
