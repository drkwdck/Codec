from ArithmeticCoder import ArithmeticCoder
from SignalReader import SignalReader
from WaveletTransform import WaveletTransform
from Quantizer import Quantizer
import sys
import numpy as np

ArithmeticCoder.encode_subband(np.array([[1,2],[3,4]]))
image_file_path = sys.argv[1]
print("Чтение исходного файла")
image = SignalReader.ReadImage(image_file_path)
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

