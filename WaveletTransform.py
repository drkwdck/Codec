import pywt
import numpy as np


class WaveletTransform:
    wavelet_transform_levels_count = 4

    @staticmethod
    def transform(image: np.ndarray) -> np.ndarray:
        wavelet_transform_result = pywt.wavedec2(image, 'bior4.4', level=WaveletTransform.wavelet_transform_levels_count)
        subbands = [wavelet_transform_result[0]]

        for i in range(1, WaveletTransform.wavelet_transform_levels_count + 1):
            for subband in wavelet_transform_result[i]:
                subbands.append(subband)
        return subbands

    @staticmethod
    def i_transform(subbands: list) -> np.ndarray:
        restored_image = [subbands[0]]
        inserted_subbands_count = 1
        subbands_batch = []
        for i in range(1, len(subbands)):
            if inserted_subbands_count == 3:
                subbands_batch.append(subbands[i])
                restored_image.append(tuple(subbands_batch))
                subbands_batch = []
                inserted_subbands_count = 1
            else:
                subbands_batch.append(np.array(subbands[i]))
                inserted_subbands_count += 1
        return (pywt.waverec2(restored_image, 'bior4.4') * 256).astype(np.uint8)
