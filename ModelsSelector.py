class ModelsSelector:
    @staticmethod
    def get_neighbors(previous_symbols: list, current_symbol_ind: int, n_rows: int) -> list:
        neighbors = []

        if current_symbol_ind - n_rows * 2 >= 0:
            neighbors.append(previous_symbols[current_symbol_ind - n_rows * 2])
        else:
            neighbors.append(0)

        if current_symbol_ind - n_rows - 1 >= 0:
            neighbors.append(previous_symbols[current_symbol_ind - n_rows - 1])
        else:
            neighbors.append(0)

        if current_symbol_ind - n_rows >= 0:
            neighbors.append(previous_symbols[current_symbol_ind - n_rows])
        else:
            neighbors.append(0)

        if current_symbol_ind - 1 >= 0:
            neighbors.append(previous_symbols[current_symbol_ind - 1])
        else:
            neighbors.append(0)
        return neighbors

    @staticmethod
    def get_model_index(neighbors: list) -> int:
        normed_mean = sum(neighbors) / len(neighbors) / 256

        if normed_mean <= 0.5:
            return 3
        if normed_mean <= 0.7:
            return 2
        if normed_mean <= 0.9:
            return 1
        return 0
