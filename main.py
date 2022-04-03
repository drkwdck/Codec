import numpy as np

from OptimalModelSearcher import OptimalModelSearcher
from WaveletTransform import WaveletTransform
from ArithmeticCoderFacade import ArithmeticCoderFacade
from ImageProvider import ImageProvider
from Quantizer import Quantizer

# чтение изображения
image = ImageProvider.read_with_norm('Images\\lena_gray_512.tif').astype(np.float32)

# вейвлет-преобрзование
subbands = WaveletTransform.transform(image)

# квантование
subbands = Quantizer.quantize(subbands)

coder = ArithmeticCoderFacade()
optimal_model_searcher = OptimalModelSearcher()
coder.encode_subbands(subbands, optimal_model_searcher)
contexts = optimal_model_searcher.get_SymbolContext_on_optimal_model_map()
restored_subbands = coder.decode_subbands()

restored_subbands = Quantizer.dequantize(restored_subbands)

image = WaveletTransform.i_transform(restored_subbands)

ImageProvider.WriteImage('Images\\lena_gray_resotred.tif', image)

