import numpy as np
import string
import cv2


class ImageReader:
    @staticmethod
    def ReadImage(file_path) -> np.ndarray:
        image = cv2.imread(file_path, 0)
        rows, cols = image.shape
        # Convert to float for more resolution for use with pywt
        image = np.uint8(image)
        return image
