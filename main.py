from ArithmeticCoder import ArithmeticCoder
from ArithmeticDecoder import ArithmeticDecoder
from ImageProvider import ImageProvider
from WaveletTransform import WaveletTransform
from SignalStorage import SignalStorage
from Quantizer import Quantizer
import sys
import numpy as np
import matplotlib.pyplot as plt
import pywt
import cv2

wavelet_transform_levels_count = 4

image = ImageProvider.ReadImage('Images\\lena_gray_512.tif').astype(np.float32)

wavelet_transform_result = pywt.wavedec2(np.log(image), 'bior4.4', level=wavelet_transform_levels_count)
subbands = []
coefs_counts = []
subband_maxes = []

coefs_counts.append(wavelet_transform_result[0].shape)
subband_maxes.append(np.max(wavelet_transform_result[0]))
subbands.append(wavelet_transform_result[0] / 8)

for i in range(1, wavelet_transform_levels_count + 1):
    for subband in wavelet_transform_result[i]:
        subband = subband / 2
        coefs_counts.append(subband.shape)
        subband_maxes.append(np.max(subband))
        subbands.append(subband)

for i in range(len(subbands)):
    subbands[i] = Quantizer.Quantize(subbands[i])
    subbands[i] = subbands[i] + 100 if i != 0 else subbands[i]
    ArithmeticCoder.encode_subband(subbands[i])

ArithmeticCoder.finish_encoding()

restored_subbands = []
for i in range(len(coefs_counts)):
    restored_subband = subbands[i]
    ArithmeticDecoder.decode_subband(restored_subband)
    restored_subband = Quantizer.dequantize(restored_subband - 100 if i != 0 else restored_subband)
    restored_subband = restored_subband * 2

    if i == 0:
        restored_subband = restored_subband * 4

    restored_subbands.append(restored_subband)

# ImageProvider.WriteImage('C:\\Users\\EReshetnikov\\Codec\\Images\\lena_gray_resotred.tif', restored_image)

for_wave_rec = []
for_wave_rec.append(restored_subbands[0])

c = 1
batch = []
for i in range(1, len(restored_subbands)):
    if c == 3:
        batch.append(restored_subbands[i])
        for_wave_rec.append(batch)
        batch = []
        c = 1
    else:
        batch.append(restored_subbands[i])
        c += 1


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
    c = pywt.wavedec2(x, 'bior4.4', level=level)
    d = pywt.waverec2(c, 'bior4.4')
    # cv2.imshow(d)
    i = 0
    for item in c[2]:
        if i != 2:
            i = i + 1
            continue
        item[:] = 1
        break
    # normalize each coefficient array independently for better visibility
    c[0] /= np.abs(c[0]).max()
    for detail_level in range(level):
        c[detail_level + 1] = [d/np.abs(d).max() for d in c[detail_level + 1]]
    # show the normalized coefficients
    arr, slices = pywt.coeffs_to_array(c)
    # axes[1, 0].imshow(c[0], cmap=plt.cm.gray)
    axes[1, 0].imshow(arr, cmap=plt.cm.gray)
    axes[1, 0].set_title('Coefficients\n({} level)'.format(level))
    axes[1, 0].set_axis_off()
plt.tight_layout()
plt.show()

print("Чтение исходного файла")
image = ImageProvider.ReadImage('C:\\Users\\EReshetnikov\\Codec\\Images\\lena_gray_512.tif')
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

