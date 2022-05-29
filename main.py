import numpy as np
import os
from OptimalModelSearcher import OptimalModelSearcher
from WaveletTransform import WaveletTransform
from ArithmeticCoderFacade import ArithmeticCoderFacade
from ArithmeticCoder import ArithmeticCoder
from ArithmeticDecoder import ArithmeticDecoder
from ImageProvider import ImageProvider
from Quantizer import Quantizer
from SignalStorage import SignalStorage


def set_sample():
    # чтение изображения
    image_directory = 'TestImages'
    ArithmeticCoder.cum_freqs = [np.loadtxt('cum_freqs_0.txt', delimiter=',', dtype=np.uint64),
                                 np.loadtxt('cum_freqs_1.txt', delimiter=',', dtype=np.uint64),
                                 np.loadtxt('cum_freqs_2.txt', delimiter=',', dtype=np.uint64),
                                 np.loadtxt('cum_freqs_3.txt', delimiter=',', dtype=np.uint64),
                                 np.loadtxt('cum_freqs_4.txt', delimiter=',', dtype=np.uint64),
                                 np.loadtxt('cum_freqs_5.txt', delimiter=',', dtype=np.uint64),
                                 np.loadtxt('cum_freqs_6.txt', delimiter=',', dtype=np.uint64),
                                 np.loadtxt('cum_freqs_7.txt', delimiter=',', dtype=np.uint64)]

    ArithmeticDecoder.cum_freqs = [np.loadtxt('cum_freqs_0.txt', delimiter=',', dtype=np.uint64),
                                 np.loadtxt('cum_freqs_1.txt', delimiter=',', dtype=np.uint64),
                                 np.loadtxt('cum_freqs_2.txt', delimiter=',', dtype=np.uint64),
                                 np.loadtxt('cum_freqs_3.txt', delimiter=',', dtype=np.uint64),
                                 np.loadtxt('cum_freqs_4.txt', delimiter=',', dtype=np.uint64),
                                 np.loadtxt('cum_freqs_5.txt', delimiter=',', dtype=np.uint64),
                                 np.loadtxt('cum_freqs_6.txt', delimiter=',', dtype=np.uint64),
                                 np.loadtxt('cum_freqs_7.txt', delimiter=',', dtype=np.uint64)]

    for image_name in ['Lena.tif']:
        print(image_name)
        image = ImageProvider.read_with_norm(os.path.join(image_directory, image_name)).astype(np.float32)
        # вейвлет-преобрзование
        subbands = WaveletTransform.transform(image)

        # квантование
        subbands = Quantizer.quantize(subbands)

        coder = ArithmeticCoderFacade()
        optimal_model_searcher = OptimalModelSearcher()
        coder.encode_subbands(subbands, optimal_model_searcher)
        coded_image_len = len(SignalStorage.storage)
        restored_subbands = coder.decode_subbands()

        restored_subbands = Quantizer.dequantize(restored_subbands)

        image_r = WaveletTransform.i_transform(restored_subbands)

        square_error = np.sum(np.sum((image_r - image) ** 2))
        psnr = 10 * np.log10((512 * 512 / square_error))
        bpp = 8 * coded_image_len / 512 / 512
        # np.savetxt("OptimalModelSearcher_{0}.txt".format(image_name), optimal_model_searcher.get_sample(),
        #            delimiter=',', fmt="%i")
        print("PSNR = {0} bpp = {1}".format(psnr, bpp))

def set_models():
    ArithmeticCoder.cum_freqs = [np.loadtxt('cum_freqs_0.txt', delimiter=',', dtype=np.uint64),
                                 np.loadtxt('cum_freqs_1.txt', delimiter=',', dtype=np.uint64),
                                 np.loadtxt('cum_freqs_2.txt', delimiter=',', dtype=np.uint64),
                                 np.loadtxt('cum_freqs_3.txt', delimiter=',', dtype=np.uint64),
                                 np.loadtxt('cum_freqs_4.txt', delimiter=',', dtype=np.uint64),
                                 np.loadtxt('cum_freqs_5.txt', delimiter=',', dtype=np.uint64),
                                 np.loadtxt('cum_freqs_6.txt', delimiter=',', dtype=np.uint64),
                                 np.loadtxt('cum_freqs_7.txt', delimiter=',', dtype=np.uint64)]
    ArithmeticDecoder.cum_freqs = [np.loadtxt('cum_freqs_0.txt', delimiter=',', dtype=np.uint64),
                                 np.loadtxt('cum_freqs_1.txt', delimiter=',', dtype=np.uint64),
                                 np.loadtxt('cum_freqs_2.txt', delimiter=',', dtype=np.uint64),
                                 np.loadtxt('cum_freqs_3.txt', delimiter=',', dtype=np.uint64),
                                 np.loadtxt('cum_freqs_4.txt', delimiter=',', dtype=np.uint64),
                                 np.loadtxt('cum_freqs_5.txt', delimiter=',', dtype=np.uint64),
                                 np.loadtxt('cum_freqs_6.txt', delimiter=',', dtype=np.uint64),
                                 np.loadtxt('cum_freqs_7.txt', delimiter=',', dtype=np.uint64)]

    train_image_directory = 'TrainImages'
    images = [os.path.join(train_image_directory, img) for img in os.listdir(train_image_directory)]
    for image_name in ['TrainImages/17.png']:
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

        # restored_subbands = Quantizer.dequantize(restored_subbands)

        # image = WaveletTransform.i_transform(restored_subbands)
        # ImageProvider.WriteImage('123.png', (image * 256).astype(np.uint8))

    np.savetxt('cum_freqs_0.txt', ArithmeticCoder.cum_freqs[0], delimiter=',', fmt="%i")
    np.savetxt('cum_freqs_1.txt', ArithmeticCoder.cum_freqs[1], delimiter=',', fmt="%i")
    np.savetxt('cum_freqs_2.txt', ArithmeticCoder.cum_freqs[2], delimiter=',', fmt="%i")
    np.savetxt('cum_freqs_3.txt', ArithmeticCoder.cum_freqs[3], delimiter=',', fmt="%i")
    np.savetxt('cum_freqs_4.txt', ArithmeticCoder.cum_freqs[4], delimiter=',', fmt="%i")
    np.savetxt('cum_freqs_5.txt', ArithmeticCoder.cum_freqs[5], delimiter=',', fmt="%i")
    np.savetxt('cum_freqs_6.txt', ArithmeticCoder.cum_freqs[6], delimiter=',', fmt="%i")
    np.savetxt('cum_freqs_7.txt', ArithmeticCoder.cum_freqs[7], delimiter=',', fmt="%i")

set_sample()
