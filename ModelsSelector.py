import joblib
from sklearn.ensemble import RandomForestClassifier

class ModelsSelector:
    Model = joblib.load("model.joblib")

    @staticmethod
    def get_neighbors(previous_symbols: list, current_symbol_ind: int, n_rows: int, subband_shift: int) -> list:
        neighbors = []

        if current_symbol_ind - n_rows * 2 >= 0:
            neighbors.append(previous_symbols[subband_shift + current_symbol_ind - n_rows * 2])
        else:
            neighbors.append(0)

        if current_symbol_ind - n_rows - 1 >= 0:
            neighbors.append(previous_symbols[subband_shift + current_symbol_ind - n_rows - 1])
        else:
            neighbors.append(0)

        if current_symbol_ind - n_rows >= 0:
            neighbors.append(previous_symbols[subband_shift + current_symbol_ind - n_rows])
        else:
            neighbors.append(0)

        if current_symbol_ind - 1 >= 0:
            neighbors.append(previous_symbols[subband_shift + current_symbol_ind - 1])
        else:
            neighbors.append(0)
        return neighbors

    @staticmethod
    def get_model_index(neighbors: list, subband_number: int) -> int:
        model_index = 0

        # model_index = ModelsSelector.Model.predict([neighbors])[0]
        normed_mean = sum(neighbors) / len(neighbors) / 256

        if normed_mean <= 0.45:
            model_index = 3
        if normed_mean <= 0.47:
            model_index = 2
        if normed_mean <= 0.5:
            model_index = 1
        if normed_mean > 0.5:
            model_index = 0

        if subband_number in [0, 3, 6, 9, 12]:
            model_index += 4

        return model_index
