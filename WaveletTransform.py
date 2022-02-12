import pywt
import numpy as np

class WaveletTransform:
    @staticmethod
    def Transform(image_matrix: np.ndarray):
        transform_levels = 2
        return pywt.wavedec2(image_matrix, 'db2', mode='periodization', level=transform_levels)
