class SymbolContext:
    def __init__(self, symbol, neighbours: list):
        self._symbol = symbol
        self._neighbours = neighbours

    def get_symbol(self):
        return self._symbol

    def get_neighbours(self):
        return self._neighbours