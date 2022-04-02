import numpy as np

class SubbandsWalker:
    _vertical_walk_indexes = [2, 5, 8, 11]
    _horizontal_walk_indexes = [1, 4, 7, 10]
    _zig_zag_walk_indexes = [0, 3, 6, 9, 12]

    @staticmethod
    def tranlate_subbands(subbands: list) -> list:
        translated_subbands = []

        for k in range(len(subbands)):
            subband = subbands[k]
            if k in SubbandsWalker._vertical_walk_indexes:
                translated_subbands.extend(SubbandsWalker._vertical_walk(subband).tolist())
            elif k in SubbandsWalker._horizontal_walk_indexes:
                translated_subbands.extend(SubbandsWalker._horizontal_walk(subband).tolist())
            else:
                translated_subbands.extend(SubbandsWalker._zig_zag_walk(subband).tolist())
        return translated_subbands

    @staticmethod
    def i_tranlate_subbands(subbands: list) -> list:
        i_translated_subbands = []

        for k in range(len(subbands)):
            subband = subbands[k]
            if k in SubbandsWalker._vertical_walk_indexes:
                i_translated_subbands.append(SubbandsWalker._i_vertical_walk(subband))
            elif k in SubbandsWalker._horizontal_walk_indexes:
                i_translated_subbands.append(SubbandsWalker._i_horizontal_walk(subband))
            else:
                i_translated_subbands.append(SubbandsWalker._i_zig_zag_walk(subband))
        return i_translated_subbands

    @staticmethod
    def _horizontal_walk(matrix: np.ndarray) -> np.ndarray:
        rewalked = []

        for i in range(matrix.shape[0]):
            if i % 2 == 0:
                for j in range(matrix.shape[1]):
                    rewalked.append(matrix[i][j])
            else:
                for j in range(matrix.shape[1] - 1, -1, -1):
                    rewalked.append(matrix[i][j])

        return np.array(rewalked)

    @staticmethod
    def _vertical_walk(matrix: np.ndarray) -> np.ndarray:
        return SubbandsWalker._horizontal_walk(matrix.T)

    @staticmethod
    def _zig_zag_walk(matrix: np.ndarray) -> np.ndarray:
        return matrix.reshape(-1,)

    @staticmethod
    def _i_zig_zag_walk(vector: np.ndarray) -> np.ndarray:
        size = int(np.sqrt(vector.shape[0]))
        return vector.reshape(size, size)

    @staticmethod
    def _i_horizontal_walk(vector: np.ndarray) -> np.ndarray:
        n_columns = int(np.sqrt(len(vector)))
        row_num = 1
        column_num = 0
        rewalked_matrix = np.zeros((n_columns, n_columns))

        for i in range(len(vector)):
            if i == row_num * n_columns:
                row_num += 1
                column_num = 0
            j = column_num if row_num % 2 != 0 else n_columns - column_num - 1
            rewalked_matrix[row_num - 1][j] = vector[i]
            column_num += 1
        return np.array(rewalked_matrix)

    @staticmethod
    def _i_vertical_walk(vector: np.ndarray) -> np.ndarray:
        return SubbandsWalker._i_horizontal_walk(vector).T
