import numpy as np

from EntropyCalculator import EntropyCalculator
from ModelsSelector import ModelsSelector
from SymbolContext import SymbolContext


class OptimalModelSearcher:
    def __init__(self):
        self._context_on_optimal_model = dict()

    def init_SymbolContext_on_optimal_model_map(self, all_symbols: np.ndarray, subbands_shape, cum_freqs):
        current_shape = 0
        subband_i = 0
        subbands_shift = 0
        for i in range(len(all_symbols)):
            symbol = all_symbols[i]
            if subband_i == subbands_shape[current_shape]:
                current_shape += 1
                subband_i = 0
                subbands_shift = i - 1

            neighbors = ModelsSelector.get_neighbors(all_symbols, subband_i, int(np.sqrt(subbands_shape[current_shape])), subbands_shift)
            context = SymbolContext(symbol, neighbors)

            min_entropy = 2 ** 15
            optimal_model_index = 0
            for j in range(len(cum_freqs)):
                entropy = EntropyCalculator.calculate(symbol, cum_freqs[j])
                if entropy < min_entropy:
                    min_entropy = entropy
                    optimal_model_index = j
            self._context_on_optimal_model[context] = optimal_model_index
            subband_i += 1

    def get_SymbolContext_on_optimal_model_map(self):
        return self._context_on_optimal_model

    def get_sample(self):
        sample = []
        for context in self._context_on_optimal_model:
            row = context.get_neighbours()
            row.append(self._context_on_optimal_model[context])
            sample.append(row)
        return np.array(sample)
