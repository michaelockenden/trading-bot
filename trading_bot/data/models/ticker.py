from collections import deque

from trading_bot.data.models.market_data import MarketData


class Ticker:

    def __init__(self, symbol: str, max_len: int = 1000):
        self._symbol = symbol
        self._data: deque[MarketData] = deque(maxlen=max_len)

    def add_data(self, data_entry: MarketData):
        self._data.append(data_entry)

    @property
    def symbol(self):
        return self._symbol.lower()

    @property
    def symbol_upper(self):
        return self._symbol.upper()

    @property
    def latest_market_data(self):
        return self._data[-1]
