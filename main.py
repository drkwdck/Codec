import numpy as np

from WaveletTransform import WaveletTransform
from ArithmeticCoderFacade import ArithmeticCoderFacade
from ImageProvider import ImageProvider
from Quantizer import Quantizer

coder = ArithmeticCoderFacade()
image = ImageProvider.read_with_norm('Images\\lena_gray_512.tif').astype(np.float32)

subbands = WaveletTransform.transform(image)
subbands = Quantizer.quantize(subbands)
coder.encode_subbands(subbands)

restored_subbands = coder.decode_subbands()
restored_subbands = Quantizer.dequantize(restored_subbands)
image = WaveletTransform.i_transform(restored_subbands)

ImageProvider.WriteImage('Images\\lena_gray_resotred.tif', image)

