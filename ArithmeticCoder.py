import numpy as np
from SignalStorage import SignalStorage


class ArithmeticCoder:
    BITS_IN_REGISTER = np.uint8(48)
    TOP_VALUE = np.uint64((1 << 48) - 1)  # 1111...1
    FIRST_QTR = np.uint64((TOP_VALUE / 4) + 1)  # 0100...0
    HALF = np.uint64((2 * FIRST_QTR))  # 1000...0
    THIRD_QTR = np.uint64((3 * FIRST_QTR))  # 1100...0
    MAX_FREQUENCY = np.uint32(1 << 15)  # bitshift(1, 15)
    NO_OF_CHARS = np.uint16(256)
    EOF_SYMBOL = np.uint16(NO_OF_CHARS)  # char - коды: 0..NO_OF_CHARS - 1
    NO_OF_SYMBOLS = np.uint16(NO_OF_CHARS + 1)

    low = np.uint64(0)
    high = np.uint64(TOP_VALUE)
    cum = np.uint64(0)
    range = np.uint64(high + 1)
    symbol = np.uint16(0)
    buffer = np.uint16(0)
    c = np.uint16(0)

    cum_freq = [np.uint64(x) for x in np.arange(0, NO_OF_SYMBOLS + 1, 1)]
    bits_to_go = np.uint8(16)
    bits_to_follow = np.uint8(0)
    initialezed = False

    @staticmethod
    def encode_subband(subband: np.ndarray):
        if not ArithmeticCoder.initialezed:
            for i in range(129, ArithmeticCoder.NO_OF_SYMBOLS + 1):
                ArithmeticCoder.cum_freq[i] += np.uint64(10000)
            ArithmeticCoder.initialezed = True

        processed_count = 0
        for i in range(subband.shape[0]):
            for j in range(subband.shape[1]):
                symbol = np.uint16(subband[i][j])

                if symbol > ArithmeticCoder.NO_OF_SYMBOLS:
                    print("Overflow! Decrease quality!")
                    return

                ArithmeticCoder.encode_symbol(symbol)
                ArithmeticCoder.update_model(symbol)

                processed_count = processed_count + 1
                print(processed_count / (subband.shape[0] * subband.shape[1]))

    @staticmethod
    def encode_symbol(symbol):
        if len(SignalStorage.storage) == 10321:
            print('312')
        ArithmeticCoder.range = np.uint64((ArithmeticCoder.high - ArithmeticCoder.low + 1).round())
        ArithmeticCoder.high = np.uint64((ArithmeticCoder.low \
                                         + ArithmeticCoder.idivide_(ArithmeticCoder.cum_freq[symbol + 1] *
                                                                    ArithmeticCoder.range,
                                                                    ArithmeticCoder.cum_freq[
                                                                        ArithmeticCoder.NO_OF_SYMBOLS]) - 1).round())
        b = ArithmeticCoder.cum_freq[symbol]
        ArithmeticCoder.low = np.uint64((ArithmeticCoder.low + \
                              ArithmeticCoder.idivide_(ArithmeticCoder.cum_freq[symbol]
                                                       * ArithmeticCoder.range,
                                                       ArithmeticCoder.cum_freq[ArithmeticCoder.NO_OF_SYMBOLS])).round())
        a = ArithmeticCoder.cum_freq[symbol + 1]

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
                    ArithmeticCoder.bits_to_follow = ArithmeticCoder.bits_to_follow + np.uint64(1)
                else:
                    break

            ArithmeticCoder.low = ArithmeticCoder.low + ArithmeticCoder.low
            ArithmeticCoder.high = ArithmeticCoder.high + ArithmeticCoder.high + np.uint64(1)

    @staticmethod
    def update_model(symbol):
        if ArithmeticCoder.cum_freq[ArithmeticCoder.NO_OF_SYMBOLS] == ArithmeticCoder.MAX_FREQUENCY:
            ArithmeticCoder.cum = np.uint64(0)
            frs = []

            for k in range(ArithmeticCoder.NO_OF_SYMBOLS):
                fr = np.uint64(((ArithmeticCoder.cum_freq[k + 1] - ArithmeticCoder.cum_freq[k] + 1) / np.uint64(2)))
                frs.append(fr)
                ArithmeticCoder.cum_freq[k] = ArithmeticCoder.cum
                ArithmeticCoder.cum = np.uint64(ArithmeticCoder.cum + fr)

            ArithmeticCoder.cum_freq[ArithmeticCoder.NO_OF_SYMBOLS] = ArithmeticCoder.cum
        for i in range(symbol + 1, ArithmeticCoder.NO_OF_SYMBOLS + 1):
            ArithmeticCoder.cum_freq[i] = ArithmeticCoder.cum_freq[i] + np.uint64(1)

    # TODO после отладки переимновать
    @staticmethod
    def idivide_(a, b):
        t = np.remainder(a, b)
        f = (a - np.remainder(a, b))
        c = ((a - np.remainder(a, b)) / b).round()
        return np.uint64(((a - np.remainder(a, b)) / b).round())

    @staticmethod
    def output_0_plus_follow():
        ArithmeticCoder.buffer = ArithmeticCoder.buffer >> 1
        ArithmeticCoder.bits_to_go = ArithmeticCoder.bits_to_go - np.uint8(1)

        if ArithmeticCoder.bits_to_go == 0:
            SignalStorage.write(ArithmeticCoder.buffer)
            ArithmeticCoder.bits_to_go = np.uint8(16)

        while ArithmeticCoder.bits_to_follow > 0:
            ArithmeticCoder.buffer = np.uint16((ArithmeticCoder.buffer >> 1) + 32768)  # TODO магическая литера
            ArithmeticCoder.bits_to_go = np.uint8(ArithmeticCoder.bits_to_go - 1)

            if ArithmeticCoder.bits_to_go == 0:
                SignalStorage.write(ArithmeticCoder.buffer)
                ArithmeticCoder.bits_to_go = np.uint8(16)

            ArithmeticCoder.bits_to_follow = ArithmeticCoder.bits_to_follow - np.uint16(1)

    @staticmethod
    def output_1_plus_follow():
        ArithmeticCoder.buffer = (ArithmeticCoder.buffer >> 1) + 32768  # TODO литера
        ArithmeticCoder.bits_to_go = np.uint8(ArithmeticCoder.bits_to_go - 1)

        if ArithmeticCoder.bits_to_go == 0:
            SignalStorage.write(ArithmeticCoder.buffer)
            ArithmeticCoder.bits_to_go = np.uint8(16)

        while ArithmeticCoder.bits_to_follow > 0:
            ArithmeticCoder.buffer = np.uint16(ArithmeticCoder.buffer >> 1)
            ArithmeticCoder.bits_to_go = np.uint8(ArithmeticCoder.bits_to_go - 1)

            if ArithmeticCoder.bits_to_go == 0:
                SignalStorage.write(ArithmeticCoder.buffer)
                ArithmeticCoder.bits_to_go = np.uint8(16)

            ArithmeticCoder.bits_to_follow = np.uint8(ArithmeticCoder.bits_to_follow - 1)
