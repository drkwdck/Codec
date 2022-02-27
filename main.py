from ArithmeticCoder import ArithmeticCoder
from ArithmeticDecoder import ArithmeticDecoder
from ImageReader import ImageReader
from WaveletTransform import WaveletTransform
from SignalStorage import SignalStorage
from Quantizer import Quantizer
import sys
import numpy as np
import matplotlib.pyplot as plt
import pywt
import cv2

image = ImageReader.ReadImage('C:\\Users\\EReshetnikov\\Codec\\Images\\lena_gray_512.tif')
# ArithmeticCoder.encode_subband(image)
#
# ArithmeticCoder.finish_encoding()
#
# a = SignalStorage.storage
#
# ArithmeticDecoder.decode_subband(np.zeros((256, 256))))
# ArithmeticDecoder.finish_decoding()

x = image
shape = x.shape
max_lev = 4 # how many levels of decomposition to draw
label_levels = 3 # how many levels to explicitly label on the plots
fig, axes = plt.subplots(2, 4, figsize=[14, 8])
for level in range(4, max_lev + 1):
    if level == 4:
        # show the original image before decomposition
        axes[0, 0].set_axis_off()
        axes[1, 0].imshow(x, cmap=plt.cm.gray)
        axes[1, 0].set_title('Image')
        axes[1, 0].set_axis_off()
        # continue
    # plot subband boundaries of a standard DWT basis
    # axes[0, level].set_title('{} level\ndecomposition'.format(level))
    # compute the 2D DWT
    c = pywt.wavedec2(x, 'db2', level=level)
    d = pywt.waverec2(c, 'db2')
    # cv2.imshow(d)
    # normalize each coefficient array independently for better visibility
    c[0] /= np.abs(c[0]).max()
    for detail_level in range(level):
        c[detail_level + 1] = [d/np.abs(d).max() for d in c[detail_level + 1]]
    # show the normalized coefficients
    arr, slices = pywt.coeffs_to_array(c)
    # axes[1, 0].imshow(c[0], cmap=plt.cm.gray)
    axes[1, 0].imshow(d, cmap=plt.cm.gray)
    axes[1, 0].set_title('Coefficients\n({} level)'.format(level))
    axes[1, 0].set_axis_off()
plt.tight_layout()
plt.show()

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

