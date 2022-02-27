import pywt
import numpy as np

class WaveletTransform:
    @staticmethod
    def Transform(image_matrix: np.ndarray):
        transform_levels = 2
        return pywt.wavedec2(image_matrix, 'bior4.4', level=transform_levels)
