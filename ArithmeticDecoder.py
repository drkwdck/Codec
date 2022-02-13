import numpy as np


class ArithmeticDecoder:
    BITS_IN_REGISTER = 48
    TOP_VALUE = (1 << BITS_IN_REGISTER) - 1  # 1111...1
    FIRST_QTR = (TOP_VALUE >> 2) + 1  # 0100...0
    HALF = (2 * FIRST_QTR)  # 1000...0
    THIRD_QTR = (3 * FIRST_QTR)  # 1100...0
    MAX_FREQUENCY = 1 << 15 # bitshift(1, 15)
    NO_OF_CHARS = 256
    EOF_SYMBOL = NO_OF_CHARS  # char - коды: 0..NO_OF_CHARS - 1
    NO_OF_SYMBOLS = NO_OF_CHARS + 1

    low = 0
    high = TOP_VALUE
    cum = 0
    range = high + 1
    symbol = 0
    buffer = 0
    c = 0

    cum_freq = [x for x in np.arange(0, NO_OF_SYMBOLS + 1, 1)]
    bits_to_go = 0
    garbage_bits = 0
    bit = 0
    value = 0
    initialezed = False

    @staticmethod
    def start_decoding():
        for i in range(ArithmeticDecoder.BITS_IN_REGISTER):
            ArithmeticDecoder.input_bit()
            ArithmeticDecoder.value = (ArithmeticDecoder.value << 1) + ArithmeticDecoder.bit

    @staticmethod
    def input_bit():
        if ArithmeticDecoder.bits_to_go == 0:
            pass