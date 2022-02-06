import numpy as np


class MetricsCalculator:
    @staticmethod
    def PSNR(original: np.ndarray, compressed: np.ndarray) -> float:
        mse = np.mean((original - compressed) ** 2)
        if mse == 0:
            return 100
        max_pixel = 255.0
        psnr = 20 * np.log10(max_pixel / np.sqrt(mse))
        return psnr
