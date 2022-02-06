import numpy as np
import string
import cv2


class SignalReader:
    @staticmethod
    def ReadImage(self, file_path: string) -> np.ndarray:
        image = cv2.imread('images/lena.png', 0)
        rows, cols = image.shape

        for i in range(rows):
            for j in range(cols):
                print(image[i, j])
        # Convert to float for more resolution for use with pywt
        image = np.float32(image)
        image /= 255
        return image
