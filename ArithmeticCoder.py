import numpy as np

class ArithmeticCoder:
    BITS_IN_REGISTER = 48;
    TOP_VALUE = (BITS_IN_REGISTER << 1) - 1 # 1111...1
    FIRST_QTR = bitshift(TOP_VALUE, -2) + 1) # 0100...0
    HALF = (2 * FIRST_QTR) # 1000...0
    THIRD_QTR = (3 * FIRST_QTR) # 1100...0
    MAX_FREQUENCY = (bitshift(1, 15))
    NO_OF_CHARS = (256)
    EOF_SYMBOL = (NO_OF_CHARS) # char - коды: 0..NO_OF_CHARS - 1
    NO_OF_SYMBOLS = (NO_OF_CHARS + 1)

    # variables
    low = 0
    high = TOP_VALUE
    cum = 0
    range = high + 1
    symbol = 0
    buffer = 0
    c = 0

    # initialize
    model
    cum_freq = [for x in range(NO_OF_SYMBOLS)]

    def encode_symbol(input_vector: np.ndarray):

