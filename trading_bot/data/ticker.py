from collections import deque


class Ticker:

    def __init__(self, symbol: str, max_len: int = 1000):
        self._symbol = symbol

        self._data: deque[dict] = deque(maxlen=max_len)

    @property
    def symbol(self):
        return self._symbol.lower()

    @property
    def symbol_upper(self):
        return self._symbol.upper()

    @property
    def current_data(self):
        return self._data[-1]
