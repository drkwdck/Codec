from ArithmeticCoder import ArithmeticCoder
from ArithmeticDecoder import ArithmeticDecoder
from ImageReader import ImageReader
from WaveletTransform import WaveletTransform
from SignalStorage import SignalStorage
from Quantizer import Quantizer
import sys
import numpy as np


# image = ImageReader.ReadImage('C:\\Users\\EReshetnikov\\Codec\\Images\\lena_gray_512.tif')
# ArithmeticCoder.encode_subband(image)
#
# ArithmeticCoder.finish_encoding()
#
# a = SignalStorage.storage
#
# ArithmeticDecoder.decode_subband(np.array(SignalStorage.storage))
# ArithmeticDecoder.finish_decoding()

print("Чтение исходного файла")
image = ImageReader.ReadImage('C:\\Users\\EReshetnikov\\Codec\\Images\\lena_gray_512.tif')
print("Чтение исходного файла завершено")

print("Запуск вейвлет-преобразования")
A = WaveletTransform.Transform(image)
print("Вейвлет-преобразование завершено")

print("Квантование саббэндов")
A_quanted = Quantizer.Quantize(A)
B_quanted = Quantizer.Quantize(B)
C_quanted = Quantizer.Quantize(B)
D_quanted = Quantizer.Quantize(B)
print("Квантование саббэндов завершено")

