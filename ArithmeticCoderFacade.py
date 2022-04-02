import numpy as np
from ArithmeticCoder import ArithmeticCoder
from ArithmeticDecoder import ArithmeticDecoder
from SubbandsWalker import SubbandsWalker


class ArithmeticCoderFacade:
    def __init__(self):
        self.subband_shapes = []

    def encode_subbands(self, subbands: list):
        for subband in subbands:
            self.subband_shapes.append((subband.shape[0] * subband.shape[0]))

        subbands = SubbandsWalker.tranlate_subbands(subbands)
        ArithmeticCoder.encode_subband(subbands, self.subband_shapes)
        ArithmeticCoder.finish_encoding()

    def decode_subbands(self) -> list:
        decoded_subbands = []

        decoded_syms = []
        for subband_shape in self.subband_shapes:
            decoded_subband = np.zeros(subband_shape)
            ArithmeticDecoder.decode_subband(decoded_subband, decoded_syms)
            decoded_subbands.append(decoded_subband)
        return SubbandsWalker.i_tranlate_subbands(decoded_subbands)
