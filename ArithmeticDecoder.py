import numpy as np

from ModelsSelector import ModelsSelector
from SignalStorage import SignalStorage

class ArithmeticDecoder:
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

    cum_freqs = [[np.uint64(x) for x in np.arange(0, NO_OF_SYMBOLS + 1, 1)],
                 [np.uint64(x) for x in np.arange(0, NO_OF_SYMBOLS + 1, 1)],
                 [np.uint64(x) for x in np.arange(0, NO_OF_SYMBOLS + 1, 1)],
                 [np.uint64(x) for x in np.arange(0, NO_OF_SYMBOLS + 1, 1)]]
    bits_to_go = np.uint8(16)
    bit = np.uint64(0)
    garbage_bits = np.uint8(0)
    value = np.uint64(0)
    initialezed = False

    @staticmethod
    def start_decoding():
        ArithmeticDecoder.bits_to_go = np.uint8(0)
        ArithmeticDecoder.garbage_bits = np.uint8(0)
        ArithmeticDecoder.bit = np.uint64(0)
        ArithmeticDecoder.value = np.uint64(0)
        for i in range(ArithmeticDecoder.BITS_IN_REGISTER):
            ArithmeticDecoder.input_bit()
            ArithmeticDecoder.value = np.uint64((ArithmeticDecoder.value << np.uint64(1)) + ArithmeticDecoder.bit)

        for cum_freq in ArithmeticDecoder.cum_freqs:
            for i in range(129, ArithmeticDecoder.NO_OF_SYMBOLS + 1):
                cum_freq[i] += np.uint64(10000)

    @staticmethod
    def decode_subband(subband: np.ndarray, decoded_symbols, subband_shift: int):
        if not ArithmeticDecoder.initialezed:
            ArithmeticDecoder.start_decoding()
            ArithmeticDecoder.initialezed = True

        for i in range(subband.shape[0]):
            model = ArithmeticDecoder.get_model(decoded_symbols, i, int(np.sqrt(subband.shape[0])), subband_shift)
            symbol = ArithmeticDecoder.decode_symbol(model)
            ArithmeticDecoder.update_model(symbol, model)
            subband[i] = symbol
            decoded_symbols.append(symbol)

    @staticmethod
    def decode_symbol(cum_freq):
        ArithmeticDecoder.range = np.uint64((ArithmeticDecoder.high - ArithmeticDecoder.low + 1).round())
        ArithmeticDecoder.cum = np.uint64(ArithmeticDecoder.idivide_((ArithmeticDecoder.value - ArithmeticDecoder.low + 1) \
                                                           * cum_freq[ArithmeticDecoder.NO_OF_SYMBOLS] - 1,
                                                           ArithmeticDecoder.range).round())
        symbol = np.uint16(sum(cum_freq <= ArithmeticDecoder.cum)) - 1

        ArithmeticDecoder.high = np.uint64((ArithmeticDecoder.low \
                                          + ArithmeticDecoder.idivide_(cum_freq[symbol + 1] *
                                                                     ArithmeticDecoder.range,
                                                                     cum_freq[ArithmeticDecoder.NO_OF_SYMBOLS]) - 1).round())
        ArithmeticDecoder.low = np.uint64((ArithmeticDecoder.low + \
                                         ArithmeticDecoder.idivide_(cum_freq[symbol]
                                                                  * ArithmeticDecoder.range,
                                                                  cum_freq[ArithmeticDecoder.NO_OF_SYMBOLS])).round())

        while True:
            if ArithmeticDecoder.high < ArithmeticDecoder.HALF:
                pass
            elif ArithmeticDecoder.low >= ArithmeticDecoder.HALF:
                ArithmeticDecoder.value = ArithmeticDecoder.value - ArithmeticDecoder.HALF
                ArithmeticDecoder.low = ArithmeticDecoder.low - ArithmeticDecoder.HALF
                ArithmeticDecoder.high = ArithmeticDecoder.high - ArithmeticDecoder.HALF
            else:
                if ArithmeticDecoder.low >= ArithmeticDecoder.FIRST_QTR and ArithmeticDecoder.high < ArithmeticDecoder.THIRD_QTR:
                    ArithmeticDecoder.value = ArithmeticDecoder.value - ArithmeticDecoder.FIRST_QTR
                    ArithmeticDecoder.high = ArithmeticDecoder.high - ArithmeticDecoder.FIRST_QTR
                    ArithmeticDecoder.low = ArithmeticDecoder.low - ArithmeticDecoder.FIRST_QTR
                else:
                    break

            ArithmeticDecoder.low = ArithmeticDecoder.low + ArithmeticDecoder.low
            ArithmeticDecoder.high = ArithmeticDecoder.high + ArithmeticDecoder.high + np.uint64(1)
            ArithmeticDecoder.input_bit()
            ArithmeticDecoder.value = ArithmeticDecoder.value + ArithmeticDecoder.value + ArithmeticDecoder.bit
        return symbol

    @staticmethod
    def input_bit():
        if ArithmeticDecoder.bits_to_go == np.uint8(0):

            if len(SignalStorage.storage) == 0:
                ArithmeticDecoder.garbage_bits = np.uint8(ArithmeticDecoder.garbage_bits + 1)

                if ArithmeticDecoder.garbage_bits > ArithmeticDecoder.BITS_IN_REGISTER - 2:
                    print('Error in compressed file')
                    return

                ArithmeticDecoder.bits_to_go = np.uint8(1)
                ArithmeticDecoder.buffer = np.uint16(0)
            else:
                ArithmeticDecoder.buffer = np.uint16(SignalStorage.storage.pop(0))
                ArithmeticDecoder.bits_to_go = np.uint8(16)

        ArithmeticDecoder.bit = np.uint64(ArithmeticDecoder.get_first_bit(ArithmeticDecoder.buffer))
        ArithmeticDecoder.buffer = np.uint16(ArithmeticDecoder.buffer >> 1)
        ArithmeticDecoder.bits_to_go = np.uint8(ArithmeticDecoder.bits_to_go - 1)

    @staticmethod
    def update_model(symbol, cum_freq):
        if cum_freq[ArithmeticDecoder.NO_OF_SYMBOLS] == ArithmeticDecoder.MAX_FREQUENCY:
            ArithmeticDecoder.cum = np.uint64(0)

            for k in range(ArithmeticDecoder.NO_OF_SYMBOLS):
                fr = np.uint64(((cum_freq[k + 1] - cum_freq[k] + 1) / np.uint64(2)))
                cum_freq[k] = ArithmeticDecoder.cum
                ArithmeticDecoder.cum = np.uint64(ArithmeticDecoder.cum + fr)

            cum_freq[ArithmeticDecoder.NO_OF_SYMBOLS] = ArithmeticDecoder.cum
        for i in range(symbol + 1, ArithmeticDecoder.NO_OF_SYMBOLS + 1):
            cum_freq[i] = cum_freq[i] + np.uint64(1)

    @staticmethod
    def get_first_bit(value):
        return value & 0b1

    # TODO после отладки переимновать
    @staticmethod
    def idivide_(a, b):
        return np.uint64(((a - np.remainder(a, b)) / b).round())

    @staticmethod
    def get_model(decoded_symbols: list, current_symbol_ind: int, n_rows: int, subband_shift: int):
        neighbors = ModelsSelector.get_neighbors(decoded_symbols, current_symbol_ind, n_rows, subband_shift)
        model_index = ModelsSelector.get_model_index(neighbors)
        return ArithmeticDecoder.cum_freqs[model_index]
