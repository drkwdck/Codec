import numpy as np
import string
import cv2


class ImageProvider:
    @staticmethod
    def ReadImage(file_path) -> np.ndarray:
        image = cv2.imread(file_path, 0)
        image = np.uint8(image)
        return image

    @staticmethod
    def read_with_norm(file_path) -> np.ndarray:
        if str(file_path).endswith('.gif'):
            cap = cv2.VideoCapture(file_path)
            ret, image = cap.read()
            cap.release()
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            image = cv2.imread(file_path, 0)
            image = np.uint8(image)
        return (image - np.min(image)) / (np.max(image) - np.min(image))

    @staticmethod
    def WriteImage(file_path: string, image_array: np.ndarray):
        cv2.imwrite(file_path, image_array * 256)
