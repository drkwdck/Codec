import numpy as np

from OptimalModelSearcher import OptimalModelSearcher
from WaveletTransform import WaveletTransform
from ArithmeticCoderFacade import ArithmeticCoderFacade
from ArithmeticCoder import ArithmeticCoder
from ImageProvider import ImageProvider
from Quantizer import Quantizer

# чтение изображения

images = ['Images\\goldhill2.tif', 'Images\\Barbara.png', 'Images\\Lena.tif']
ArithmeticCoder.cum_freqs = np.loadtxt('cum_freqs.txt', dtype=np.uint64, delimiter=',')
for image_name in images:
    print(image_name)
    image = ImageProvider.read_with_norm(image_name).astype(np.float32)
    # вейвлет-преобрзование
    subbands = WaveletTransform.transform(image)

    # квантование
    subbands = Quantizer.quantize(subbands)

    coder = ArithmeticCoderFacade()
    optimal_model_searcher = OptimalModelSearcher()
    coder.encode_subbands(subbands, optimal_model_searcher)
    # contexts = optimal_model_searcher.get_SymbolContext_on_optimal_model_map()
    # restored_subbands = coder.decode_subbands()
    #
    # restored_subbands = Quantizer.dequantize(restored_subbands)
    #
    # image = WaveletTransform.i_transform(restored_subbands)
