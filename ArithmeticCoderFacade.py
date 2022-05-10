import numpy as np
from ArithmeticCoder import ArithmeticCoder
from ArithmeticDecoder import ArithmeticDecoder
from SubbandsWalker import SubbandsWalker
from OptimalModelSearcher import OptimalModelSearcher

class ArithmeticCoderFacade:
    def __init__(self):
        self.subband_shapes = []

    def encode_subbands(self, subbands: list, model_searcher: OptimalModelSearcher):
        for subband in subbands:
            self.subband_shapes.append((subband.shape[0] * subband.shape[0]))

        subbands = SubbandsWalker.tranlate_subbands(subbands)
        ArithmeticCoder.encode_subband(subbands, self.subband_shapes)
        ArithmeticCoder.finish_encoding()
        model_searcher.init_SymbolContext_on_optimal_model_map(subbands, self.subband_shapes, ArithmeticCoder.cum_freqs)

    def decode_subbands(self) -> list:
        decoded_subbands = []

        decoded_syms = []
        subband_shift = 0
        for subband_shape in self.subband_shapes:
            decoded_subband = np.zeros(subband_shape)
            ArithmeticDecoder.decode_subband(decoded_subband, decoded_syms, subband_shift)
            decoded_subbands.append(decoded_subband)
            subband_shift = len(decoded_syms) - 1
        return SubbandsWalker.i_tranlate_subbands(decoded_subbands)
