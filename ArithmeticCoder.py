import numpy as np
from SignalWriter import SignalWriter

# TODO избавиться от стремного функционального подхода
class ArithmeticCoder:
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
    bits_to_go = 16
    bits_to_follow = 0

    @staticmethod
    def encode_subband(subband: np.ndarray):
        for i in range(subband.shape[0]):
            for j in range(subband.shape[1]):
                symbol = subband[i][j] + 1 #что-то здесь не так#  # особенность индескации матлаба, + 1 - лишнее?

                if symbol > ArithmeticCoder.NO_OF_SYMBOLS:
                    print("Overflow! Decrease quality!")
                    return

                ArithmeticCoder.encode_symbol(symbol)
                ArithmeticCoder.update_model()

    @staticmethod
    def encode_symbol(symbol):
        ArithmeticCoder.range = ArithmeticCoder.high - ArithmeticCoder.low
        ArithmeticCoder.high = ArithmeticCoder.low \
                               + ArithmeticCoder.idivide_(ArithmeticCoder.cum_freq[symbol + 1] *
                                                          ArithmeticCoder.range,
                                                          ArithmeticCoder.cum_freq[
                                                              ArithmeticCoder.NO_OF_SYMBOLS]) - 1
        ArithmeticCoder.low = ArithmeticCoder.low +\
                              ArithmeticCoder.idivide_(ArithmeticCoder.cum_freq[symbol]
                                                       * ArithmeticCoder.range,
                                                       ArithmeticCoder.cum_freq[ArithmeticCoder.NO_OF_SYMBOLS])
        while True:
            if ArithmeticCoder.high < ArithmeticCoder.HALF:
                ArithmeticCoder.output_0_plus_follow()
            elif ArithmeticCoder.low >= ArithmeticCoder.HALF:
                ArithmeticCoder.output_1_plus_follow()
                ArithmeticCoder.low = ArithmeticCoder.low - ArithmeticCoder.HALF
                ArithmeticCoder.high = ArithmeticCoder.high - ArithmeticCoder.HALF
            else:
                if ArithmeticCoder.low >= ArithmeticCoder.FIRST_QTR and ArithmeticCoder.high < ArithmeticCoder.THIRD_QTR:
                    # Возможно зацикливание, выбрасываем второй по старшинству бит
                    ArithmeticCoder.high = ArithmeticCoder.high - ArithmeticCoder.FIRST_QTR
                    ArithmeticCoder.low = ArithmeticCoder.low - ArithmeticCoder.FIRST_QTR
                    ArithmeticCoder.bits_to_follow = ArithmeticCoder.bits_to_follow + 1
                else:
                    break
            # старший бит в low и high нулевой, втягиваем новый бит
            ArithmeticCoder.low = ArithmeticCoder.low + ArithmeticCoder.low
            ArithmeticCoder.high = ArithmeticCoder.high + ArithmeticCoder.high + 1


    @staticmethod
    def update_model():
        if ArithmeticCoder.cum_freq[ArithmeticCoder.NO_OF_SYMBOLS] == ArithmeticCoder.MAX_FREQUENCY:
            ArithmeticCoder.cum = 0

            for k in range(ArithmeticCoder.NO_OF_SYMBOLS - 1):
                fr = (ArithmeticCoder.cum_freq[k+1] - ArithmeticCoder.cum_freq[k] + 1) >> 1
                ArithmeticCoder.cum_freq[k] = ArithmeticCoder.cum
                ArithmeticCoder.cum = ArithmeticCoder.cum + fr

            ArithmeticCoder.cum_freq[ArithmeticCoder.NO_OF_SYMBOLS] = ArithmeticCoder.cum
        for i in range(ArithmeticCoder.symbol + 1, ArithmeticCoder.NO_OF_SYMBOLS):
            ArithmeticCoder.cum_freq[i] = ArithmeticCoder.cum_freq[i] + 1

    # TODO после отладки переимновать
    @staticmethod
    def idivide_(a, b):
        c=  a - np.remainder(a, b) / b
        return c

    @staticmethod
    def output_0_plus_follow():
        ArithmeticCoder.buffer = ArithmeticCoder.buffer >> 1
        ArithmeticCoder.bits_to_go = ArithmeticCoder.bits_to_go - 1

        if ArithmeticCoder.bits_to_go == 0:
            SignalWriter.write(ArithmeticCoder.buffer)
            ArithmeticCoder.bits_to_go = 16

        while ArithmeticCoder.bits_to_go > 0:
            ArithmeticCoder.buffer = (ArithmeticCoder.buffer >> 1) + 32768 # TODO магическая литера
            ArithmeticCoder.bits_to_go = ArithmeticCoder.bits_to_go - 1

            if ArithmeticCoder.bits_to_go == 0:
                SignalWriter.write(ArithmeticCoder.buffer)
                ArithmeticCoder.bits_to_go = 16

            ArithmeticCoder.bits_to_follow = ArithmeticCoder.bits_to_follow - 1

    @staticmethod
    def output_1_plus_follow():
        ArithmeticCoder.buffer = (ArithmeticCoder.buffer >> 1) + 32768 # TODO литера
        ArithmeticCoder.bits_to_go = ArithmeticCoder.bits_to_go - 1

        if ArithmeticCoder.bits_to_go == 0:
            SignalWriter.write(ArithmeticCoder.buffer)
            ArithmeticCoder.bits_to_go = 16

        while ArithmeticCoder.bits_to_go > 0:
            ArithmeticCoder.buffer = ArithmeticCoder.buffer >> 1
            ArithmeticCoder.bits_to_go = ArithmeticCoder.bits_to_go - 1

            if ArithmeticCoder.bits_to_go == 0:
                SignalWriter.write(ArithmeticCoder.buffer)
                ArithmeticCoder.bits_to_go = 16

            ArithmeticCoder.bits_to_follow = ArithmeticCoder.bits_to_follow - 1
