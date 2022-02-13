from ArithmeticCoder import ArithmeticCoder
from ImageReader import ImageReader
from WaveletTransform import WaveletTransform
from SignalStorage import SignalStorage
from Quantizer import Quantizer
import sys
import numpy as np


image = ImageReader.ReadImage('C:\\Users\\EReshetnikov\\Codec\\Images\\lena_gray_512.tif')
ArithmeticCoder.encode_subband(image)
a = SignalStorage.storage
image_file_path = sys.argv[1]
print("Чтение исходного файла")
image = ImageReader.ReadImage(image_file_path)
print("Чтение исходного файла завершено")

print("Запуск вейвлет-преобразования")
# (A, B, C, D) = WaveletTransform.Transform(image)
print("Вейвлет-преобразование завершено")

print("Квантование саббэндов")
A_quanted = Quantizer.Quantize(A)
B_quanted = Quantizer.Quantize(B)
C_quanted = Quantizer.Quantize(B)
D_quanted = Quantizer.Quantize(B)
print("Квантование саббэндов завершено")

